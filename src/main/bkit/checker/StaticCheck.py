"""
 * @author nhphung
"""
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import * 
from Visitor import *
from StaticError import *
from functools import *
import copy

class Type(ABC):
    __metaclass__ = ABCMeta
    @staticmethod
    def getTypeFromLiteral(literal):
        if type(literal) == IntLiteral:
            return IntType()
        elif type(literal) == FloatLiteral:
            return FloatType()
        elif type(literal) == StringLiteral:
            return StringType()
        elif type(literal) == BooleanLiteral:
            return BoolType()
        elif type(literal) == ArrayLiteral:
            if not all(isinstance(x, (StringType, BoolType, IntType, FloatType, ArrayType)) for x in [Type.getTypeFromLiteral(i) for i in literal.value]):
                raise TypeMismatchInExpression(literal)

            dimen1 = len(literal.value)
            dimen2 = 0
            dimen3 = 0
            for x in literal.value:
                varType = varType1 = Type.getTypeFromLiteral(x)
                if type(varType1) == ArrayType:
                    dimen2 = len(x.value) if dimen2 < len(x.value) else dimen2
                    for y in x.value:
                        varType = varType2 = Type.getTypeFromLiteral(y)
                        if type(varType2) == ArrayType:
                            dimen3 = len(y.value) if dimen3 < len(y.value) else dimen3
            dimen = [dimen1, dimen2, dimen3] if dimen3 > 0 else [dimen1, dimen2] if dimen2 > 0 else [dimen1]
            return ArrayType(dimen,varType)
        else:
            return Unknown()

class Prim(Type):
    __metaclass__ = ABCMeta
    pass
class IntType(Prim):
    def __str__(self):
        return "IntType"
class FloatType(Prim):
    def __str__(self):
        return "FloatType"
class StringType(Prim):
    def __str__(self):
        return "StringType"
class BoolType(Prim):
    def __str__(self):
        return "BoolType"
class VoidType(Type):
    def __str__(self):
        return "VoidType"
class Unknown(Type):
    def __str__(self):
        return "Unknown"

@dataclass
class ArrayType(Type):
    dimen:List[int]
    eletype: Type
    def __str__(self):
        return "ArrayType(" + printlist(self.dimen) + "," + str(self.eletype) + ")"


class Kind(ABC):
    __metaclass__ = ABCMeta
    pass
class Variable(Kind):
    def __str__(self):
        return "Variable"
class Function(Kind):
    def __str__(self):
        return "Function"
class Parameter(Kind):
    def __str__(self):
        return "Parameter"
class Identifier(Kind):
    def __str__(self):
        return "Identifier"

def printlist(lst,f=str,start="[",sepa=",",ending="]"):
	return start + sepa.join(f(i) for i in lst) + ending

@dataclass
class  MType:
    intype:List[Type] # Type of parameters
    restype:Type # Type return

    def __str__(self):
        return "MType(" + printlist(self.intype) + ',' + str(self.restype) + ')'

@dataclass
class Symbol:
    name: str
    mtype:Type
    kind: Kind
    isGlobal: bool
    visited: bool

    def __init__(self, name, mtype, kind = Function(), isGlobal = False, visited = False):
        self.name = name
        self.mtype = mtype
        self.kind = kind
        self.isGlobal = isGlobal
        self.visited = visited

    def __str__(self):
        return "Symbol(" + (self.name.name if type(self.name) == Id else self.name) + ',' + str(self.mtype) + ("" if self.kind == None else ("," + str(self.kind))) + (",global" if self.isGlobal == True else ",local") + (",visited" if self.visited == True else ",not visited") + ')'

    def toGlobal(self):
        self.isGlobal = True
        return self

    def makeVisit(self):
        self.visited = True
        return self

    def toParam(self):
        self.kind = Parameter()
        return self

    def toVar(self):
        self.kind = Variable()
        return self
    
    def updateMember(self, mtype = None, kind = None, isGlobal = None, visited = None):
        if mtype != None:
            self.mtype = mtype
        if kind != None:
            self.kind = kind
        if isGlobal != None:
            self.isGlobal = isGlobal
        if visited != None:
            self.visited = visited
        return self

    def update(self, newSymbol):
        self.updateMember(mtype = newSymbol.mtype, kind = newSymbol.kind, isGlobal = newSymbol.isGlobal, visited = newSymbol.visited)
        return self

    @staticmethod
    def fromVarDecl(var):
        name = var.variable.name
        if len(var.varDimen) > 0:
            if not all(isinstance(x, int) for x in var.varDimen):
                raise TypeMismatchInExpression(var)
            varType = ArrayType(var.varDimen, Type.getTypeFromLiteral(var.varInit))
        else:
            varType = Type.getTypeFromLiteral(var.varInit)
        kind = Variable()
        return Symbol(name, varType, kind)

    @staticmethod
    def fromFuncDecl(func):
        name = func.name.name
        kind = Function()

        param = [Symbol.fromVarDecl(x).toParam() for x in func.param]
        paramType = [x.mtype for x in param]
        varType = MType(paramType, Unknown())

        return Symbol(name, varType, kind)

    @staticmethod
    def fromDecl(decl):
        return Symbol.fromVarDecl(decl).makeVisit() if type(decl) is VarDecl else Symbol.fromFuncDecl(decl)

    @staticmethod
    def getSymbol(name, listSymbol):
        for x in listSymbol:
            if name == x.name:
                return x
        Checker.checkUndeclared(listSymbol, name, Function())
        

class Checker:
    @staticmethod
    def mergedEnvi(globalEnvi, localEnvi):
        newEnvi = copy.deepcopy(globalEnvi)
        envi = [x.name for x in newEnvi]
        for x in localEnvi:
            if x.name in envi:
                symbol = Symbol.getSymbol(x.name, newEnvi)
                symbol.update(x)
            else:
                envi.append(x.name)
                newEnvi.append(x)
        return newEnvi

    @staticmethod
    def updateGlobalEnvi(globalEnvi, localEnvi):
        envi = [x for x in localEnvi if x.isGlobal == True]
        for x in envi:
            symbol = Symbol.getSymbol(x.name, globalEnvi)
            symbol.update(x)

    # Check Redeclared Variable/Function/Parameter and return merged two environment
    @staticmethod
    def checkRedeclared(currentEnvi, listNewSymbols):
        newEnvi = copy.deepcopy(currentEnvi)
        envi = [x.name for x in newEnvi]
        for x in listNewSymbols:
            if x.name in envi:
                raise Redeclared(x.kind, x.name)
            envi.append(x.name)
            newEnvi.append(x)
        return newEnvi

    @staticmethod
    def checkUndeclared(currentEnvi, name, kind):
        envi = {x.name: Identifier() if type(x.kind) in [Variable, Parameter] else x.kind for x in currentEnvi}
        if name not in list(envi.keys()) or type(envi[name]) != type(kind):
            raise Undeclared(kind, name)
        return Symbol.getSymbol(name, currentEnvi)
        
    @staticmethod
    def updateSideType(side, sideType, ast, envi):
        if side == "left":
            if type(ast) == BinaryOp:
                name = ast.left.name
            elif type(ast) == ArrayCell:
                name = ast.lhs.arr.name
            elif type(ast) == CallExpr:
                name = ast.method.name
            elif type(ast) == Id:
                name = ast.name
            else:
                name = ast.lhs.name
        elif side == "right":
            if type(ast) == BinaryOp:
                name = ast.right.name
            elif type(ast) == ArrayCell:
                name = ast.rhs.arr.name
            elif type(ast) == CallExpr:
                name = ast.method.name
            elif type(ast) == Id:
                name = ast.name
            else:
                name = ast.rhs.name

        symbol = Symbol.getSymbol(name, envi)
        if type(symbol.kind) == Function:
            varType = MType(symbol.mtype.intype, sideType)
        else:
            varType = sideType
        
        symbol.updateMember(mtype = varType)

        return sideType

    @staticmethod
    def checkTwoSideType(left, right, ast, envi, opType = None, targetType = None):
        if type(ast) == BinaryOp: # Binary operator
            if type(left) == Unknown:
                left = Checker.updateSideType("left", targetType, ast.left, envi)
            if type(right) == Unknown:
                right = Checker.updateSideType("right", targetType, ast.right, envi)
            if type(left) == opType and type(right) == opType:
                typeReturn = targetType
            else:
                raise TypeMismatchInExpression(ast)
        elif type(ast) == Assign:
            if type(left) == Unknown and type(right) == Unknown:
                raise TypeCannotBeInferred(ast)
            elif type(left) == Unknown and type(right) != Unknown:
                left = right
                typeReturn = Checker.updateSideType("left", right, ast, envi)
            elif type(left) != Unknown and type(right) == Unknown:
                right = left
                typeReturn = Checker.updateSideType("right", left, ast, envi)
            elif type(left) != type(right):
                raise TypeCannotBeInferred(ast)
        elif type(ast) == CallExpr:
            for i in range(len(left)):
                if type(left[i]) == Unknown and type(right[i]) == Unknown:
                    raise TypeCannotBeInferred(ast)
                elif type(left[i]) == Unknown and type(right[i]) != Unknown:
                    left[i] = right[i]
                elif type(left[i]) != Unknown and type(right[i]) == Unknown:
                    right[i] = left[i]
                    typeReturn = Checker.updateSideType("right", left[i], ast.param[i], envi)
                elif type(left[i]) != type(right[i]):
                    raise TypeCannotBeInferred(ast)
            typeReturn = Checker.updateSideType("left", left, ast.method, envi)
            return left, right

        return typeReturn

    @staticmethod
    def checkOneSideType(body, ast, envi, opType, targetType):
        if type(ast.body) == CallExpr:
            body = targetType
            name = ast.body.method.name
            symbol = Symbol.getSymbol(name, envi)
            varType = MType(symbol.mtype.intype, body)
            symbol.updateMember(mtype = varType)
        elif type(ast.body) == Id:
            body = targetType
            name = ast.body.name
            symbol = Symbol.getSymbol(name, envi).updateMember(mtype = body)
        elif type(body) != opType:
            raise TypeMismatchInExpression(ast)

        return targetType

    @staticmethod
    def checkMatchType(left, right, ast, envi):
        # Handle Array Type
        if type(left) == ArrayType and type(right) == ArrayType:
            if left.dimen != right.dimen:
                raise TypeCannotBeInferred(ast)
            typeReturn = Checker.checkTwoSideType(left.eletype, right.eletype, ast, envi)
        else:
            typeReturn = Checker.checkTwoSideType(left, right, ast, envi)
            
        return typeReturn
    
    @staticmethod
    def checkParamType(actualParameters, formaParameters, ast, envi):
        if len(actualParameters) != len(formaParameters):
            return False
        formaParameters, actualParameters = Checker.checkTwoSideType(formaParameters, actualParameters, ast, envi)
        for a, b in zip(formaParameters, actualParameters):
            if Unknown not in [type(a), type(b)] and type(a) != type(b):
                return False
            if ArrayType in [type(a), type(b)]:
                if a.dimen != b.dimen or type(a.eletype) != type(b.eletype):
                    return False
        return True

    @staticmethod
    def checkCall(ast, envi, actualParameters):
        symbol = Checker.checkUndeclared(envi, ast.method.name, Function())

        if type(ast) == CallStmt:
            if type(symbol.mtype.restype) in [Unknown, VoidType]:
                typeReturn = VoidType()
            else:
                raise TypeMismatchInStatement(ast)
        else:
            typeReturn = symbol.mtype.restype
        
        formaParameters = symbol.mtype.intype

        if not Checker.checkParamType(actualParameters, formaParameters, ast, envi):
            if type(ast) == CallStmt:
                raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInExpression(ast)
        
        varType = MType(formaParameters, typeReturn)
        symbol.updateMember(mtype = varType)

        return typeReturn
        

class StaticChecker(BaseVisitor):    
    def __init__(self,ast):
        self.ast = ast
        # global_envi: built-in function names
        self.global_envi = [
Symbol("int_of_float",MType([FloatType()],IntType())),
Symbol("float_of_int",MType([IntType()],FloatType())),
Symbol("int_of_string",MType([StringType()],IntType())),
Symbol("string_of_int",MType([IntType()],StringType())),
Symbol("float_of_string",MType([StringType()],FloatType())),
Symbol("string_of_float",MType([FloatType()],StringType())),
Symbol("bool_of_string",MType([StringType()],BoolType())),
Symbol("string_of_bool",MType([BoolType()],StringType())),
Symbol("read",MType([],StringType())),
Symbol("printLn",MType([],VoidType())),
Symbol("printStr",MType([StringType()],VoidType())),
Symbol("printStrLn",MType([StringType()],VoidType()))]
   
    def check(self):
        return self.visit(self.ast,self.global_envi)

    # globalEnvi: global variables, built-in function names and other function names
    def visitProgram(self, ast: Program, globalEnvi):
        for x in globalEnvi:
            x.toGlobal()
            x.makeVisit()

        # Visit all global variables, function names from input
        symbols = [Symbol.fromDecl(x).toGlobal() for x in ast.decl]
        
        # Check Redeclared Variable/Function and update globalEnvi
        globalEnvi = Checker.checkRedeclared(globalEnvi, symbols)

        # Check no entry function "main"
        symbolList = {x.name: x.kind for x in symbols}
        if 'main' not in list(symbolList.keys()) or type(symbolList['main']) != Function:
            raise NoEntryPoint()

        # Visit all function except function "main"
        [self.visit(x, globalEnvi) for x in ast.decl if type(x) == FuncDecl and x.name.name != 'main']

        # for x in globalEnvi:
        #     print(x)

        # Get error function with attribute 'not visited'
        errorFunction = [x.name for x in globalEnvi if x.visited == False and x.name != 'main']

        # Visit again all error function except function "main"
        [self.visit(x, globalEnvi) for x in ast.decl if type(x) == FuncDecl and x.name.name in errorFunction]

        # Visit function "main"
        [self.visit(x, globalEnvi) for x in ast.decl if type(x) == FuncDecl and x.name.name == 'main']

        # for x in globalEnvi:
        #     print(x)


    # Visit declaration
    def visitVarDecl(self, ast, c):
        return Symbol.fromVarDecl(ast)

    def visitFuncDecl(self, ast: FuncDecl, globalEnvi):
        # Visit all local variables, parameter of function from input
        listParams = [self.visit(x, globalEnvi).toParam() for x in ast.param]
        listLocalVar = [self.visit(x, globalEnvi).toVar() for x in ast.body[0]]

        # Check Redeclared Variable/Parameter and update localEnvi
        localEnvi = Checker.checkRedeclared(listParams, listLocalVar)

        # Merge local with global environment
        localEnvi = Checker.mergedEnvi(globalEnvi, localEnvi)

        # Visit statements
        stmts = [self.visit(x, localEnvi) for x in ast.body[1]]

        if "Error" not in stmts:
            # Update parameter type
            paramType = [x.update(y).mtype for x in listParams for y in localEnvi if x.name == y.name]
            typeReturn = Unknown()
            varType = MType(paramType, typeReturn)

            Symbol.getSymbol(ast.name.name, localEnvi).updateMember(mtype = varType, visited = True)

            # print(ast.name.name)
            # for x in localEnvi:
            #     print(x)
            # print("==================")

            # Update global environment
            Checker.updateGlobalEnvi(globalEnvi, localEnvi)



    # Visit expression
    # Return Type of expression
    def visitBinaryOp(self, ast: BinaryOp, param):
        leftType = self.visit(ast.left, param)
        rightType = self.visit(ast.right, param)
        
        if "Error" not in [leftType, rightType]:
            if ast.op in ['+', '-', '*', '\\', '%']:
                typeReturn = Checker.checkTwoSideType(leftType, rightType, ast, param, IntType, IntType())
            elif ast.op in ['+.', '-.', '*.', '\\.']:
                typeReturn = Checker.checkTwoSideType(leftType, rightType, ast, param, FloatType, FloatType())
            elif ast.op in ['==', '!=', '<', '>', '<=', '>=']:
                typeReturn = Checker.checkTwoSideType(leftType, rightType, ast, param, IntType, BoolType())
            elif ast.op in ['=/=', '<.', '>.', '<=.', '>=.']:
                typeReturn = Checker.checkTwoSideType(leftType, rightType, ast, param, FloatType, BoolType())
            elif ast.op in ['&&', '||']:
                typeReturn = Checker.checkTwoSideType(leftType, rightType, ast, param, BoolType, BoolType())
            return typeReturn
        else:
            return "Error"

    
    def visitUnaryOp(self, ast: UnaryOp, param):
        bodyType = self.visit(ast.body, param)

        if "Error" == bodyType:
            return "Error"
        else:
            if ast.op == '-':
                typeReturn = Checker.checkOneSideType(bodyType, ast, param, IntType, IntType())
            elif ast.op == '-.':
                typeReturn = Checker.checkOneSideType(bodyType, ast, param, FloatType, FloatType())
            elif ast.op == '!':
                typeReturn = Checker.checkOneSideType(bodyType, ast, param, BoolType, BoolType())
            return typeReturn
    
    # Visit statement
    # Function call, no semi
    def visitCallExpr(self, ast: CallExpr, globalEnvi):
        symbol = Symbol.getSymbol(ast.method.name, globalEnvi)
        
        if symbol.visited == False:
            return "Error"

        paramType = [self.visit(x, globalEnvi) for x in ast.param]
        typeReturn = Checker.checkCall(ast, globalEnvi, paramType)

        return typeReturn
    
    def visitId(self, ast: Id, envi):
        symbol = Checker.checkUndeclared(envi, ast.name, Identifier())
        return symbol.mtype

    def visitArrayCell(self, ast: ArrayCell, envi):
        arrType = self.visit(ast.arr, envi)
        if not all(isinstance(x, IntType) for x in [Type.getTypeFromLiteral(i) for i in ast.idx]):
            raise TypeMismatchInExpression(ast)

        return arrType
    

    def visitAssign(self, ast: Assign, envi):
        rhsType = self.visit(ast.rhs, envi)
        lhsType = self.visit(ast.lhs, envi)
        
        if "Error" not in [lhsType, rhsType]:
            if type(lhsType) in [VoidType]: # StringType
                raise TypeMismatchInStatement(ast)
            
            typeReturn = Checker.checkMatchType(lhsType, rhsType, ast, envi)
            return typeReturn
        else:
            return "Error"

    def visitIf(self, ast, param):
        return None
    
    def visitFor(self, ast, param):
        return None
    
    def visitContinue(self, ast, param):
        return None
    
    def visitBreak(self, ast, param):
        return None
    
    def visitReturn(self, ast, param):
        return None
    
    def visitDowhile(self, ast, param):
        return None

    def visitWhile(self, ast, param):
        return None

    # Call stmt return VoidType, have semi
    def visitCallStmt(self, ast: CallStmt, globalEnvi):
        symbol = Symbol.getSymbol(ast.method.name, globalEnvi)
        if symbol.visited == False:
            return "Error"

        paramType = [self.visit(x, globalEnvi) for x in ast.param]
        typeReturn = Checker.checkCall(ast, globalEnvi, paramType)

        return typeReturn


    # Return type
    def visitIntLiteral(self, ast, param):
        return IntType()
    
    def visitFloatLiteral(self, ast, param):
        return FloatType()
    
    def visitBooleanLiteral(self, ast, param):
        return BoolType()
    
    def visitStringLiteral(self, ast, param):
        return StringType()
        
    def visitArrayLiteral(self, ast, param):
        if not all(isinstance(x, (StringType, BoolType, IntType, FloatType, ArrayType)) for x in [Type.getTypeFromLiteral(i) for i in ast.value]):
            raise TypeMismatchInExpression(ast)

        dimen1 = len(ast.value)
        dimen2 = 0
        dimen3 = 0
        for x in ast.value:
            varType = varType1 = Type.getTypeFromLiteral(x)
            if type(varType1) == ArrayType:
                dimen2 = len(x.value) if dimen2 < len(x.value) else dimen2
                for y in x.value:
                    varType = varType2 = Type.getTypeFromLiteral(y)
                    if type(varType2) == ArrayType:
                        dimen3 = len(y.value) if dimen3 < len(y.value) else dimen3
        dimen = [dimen1, dimen2, dimen3] if dimen3 > 0 else [dimen1, dimen2] if dimen2 > 0 else [dimen1]
        return ArrayType(dimen, varType)
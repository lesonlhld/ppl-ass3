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
            if dimen1 == 0:
                return ArrayType([0],Unknown())
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
    inHere: bool

    def __init__(self, name, mtype, kind = Function(), isGlobal = False, visited = False, inHere = False):
        self.name = name
        self.mtype = mtype
        self.kind = kind
        self.isGlobal = isGlobal
        self.visited = visited
        self.inHere = inHere

    def __str__(self):
        return "Symbol(" + (self.name.name if type(self.name) == Id else self.name) + ',' + str(self.mtype) + ("" if self.kind == None else ("," + str(self.kind))) + (",global" if self.isGlobal == True else ",local") + (",visited" if self.visited == True else ",not visited") + (",in here" if self.inHere == True else ",not here") + ')'

    def toGlobal(self):
        self.isGlobal = True
        return self

    def makeHere(self):
        self.inHere = True
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
    
    def updateMember(self, mtype = None, kind = None, isGlobal = None, visited = None, inHere = None):
        if mtype != None:
            self.mtype = mtype
        if kind != None:
            self.kind = kind
        if isGlobal != None:
            self.isGlobal = isGlobal
        if visited != None:
            self.visited = visited
        if inHere != None:
            self.inHere = inHere
        return self

    def update(self, newSymbol):
        self.updateMember(mtype = newSymbol.mtype, kind = newSymbol.kind, isGlobal = newSymbol.isGlobal, visited = newSymbol.visited, inHere= newSymbol.inHere)
        return self

    @staticmethod
    def fromVarDecl(var):
        name = var.variable.name
        if len(var.varDimen) > 0:
            if not all(isinstance(x, int) for x in var.varDimen):
                raise TypeMismatchInExpression(var)
            
            init = Type.getTypeFromLiteral(var.varInit)
            if type(init) == ArrayType:
                # if var.varDimen != init.dimen:
                #     raise TypeCannotBeInferred(var)
                varType = ArrayType(var.varDimen, init.eletype)
            elif type(init) == Unknown:
                varType = ArrayType(var.varDimen, init)
            else:
                raise TypeMismatchInExpression(var)
            
        else:
            varType = Type.getTypeFromLiteral(var.varInit)
        kind = Variable()
        return Symbol(name, varType, kind)

    @staticmethod
    def fromFuncDecl(func):
        name = func.name.name
        kind = Function()

        param = [Symbol.fromVarDecl(x).toParam() for x in func.param]
        listParams = Checker.checkRedeclared([], param)
        paramType = [x.mtype for x in listParams]
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

    @staticmethod
    def getNowSymbol(listSymbol):
        for x in listSymbol:
            if x.inHere == True:
                return x
        Checker.checkUndeclared(listSymbol, name, Function())

    @staticmethod
    def updateParamAndReturnType(stmtList, envi, ast):
        symbol = Symbol.getNowSymbol(envi)

        paramType = [x.mtype for x in envi if type(x.kind) == Parameter]
        if Return in list(stmtList.keys()):
            if type(symbol.mtype.restype) == Unknown or type(symbol.mtype.restype) == type(stmtList[Return]):
                typeReturn = stmtList[Return]
            else:
                raise TypeMismatchInStatement(ast)
        else:
            typeReturn = symbol.mtype.restype

        varType = MType(paramType, typeReturn)

        symbol.updateMember(mtype = varType, visited = True)
        return typeReturn
        
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
    def updateEnvi(globalEnvi, localEnvi, exceptList = None):
        if exceptList == None:
            envi = [x for x in localEnvi if x.isGlobal == True]
            for x in envi:
                symbol = Symbol.getSymbol(x.name, globalEnvi)
                symbol.update(x)
        else:
            envi = [x for x in localEnvi]
            noUpdateList = [x.name for x in exceptList]
            for x in localEnvi:
                if x.name not in noUpdateList:
                    symbol = Symbol.getSymbol(x.name, globalEnvi).update(x)

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
        if type(ast) == ArrayCell:
            name = ast.arr.name
        elif type(ast) == CallExpr:
            name = ast.method.name
        elif type(ast) == Id:
            name = ast.name
        elif type(ast) == BinaryOp:
            name = ast.left.name if side == "left" else ast.right.name
        else:
            name = ast.lhs.name if side == "left" else ast.rhs.name

        symbol = Symbol.getSymbol(name, envi)
        if type(symbol.kind) == Function:
            varType = MType(symbol.mtype.intype, sideType)
        elif type(symbol.mtype) == ArrayType:
            varType = ArrayType(symbol.mtype.dimen, sideType)
        else:
            varType = sideType
        symbol.updateMember(mtype = varType)

        return sideType

    @staticmethod
    def checkTwoSideType(left, right, ast, envi, opType = None, targetType = None):
        if type(ast) == BinaryOp: # Binary operator
            if type(left) == Unknown:
                left = Checker.updateSideType("left", opType, ast.left, envi)
            elif type(left) == ArrayType and type(left.eletype) == Unknown:
                left = Checker.updateSideType("left", opType, ast.left, envi)
            elif type(left) == ArrayType and type(left.eletype) != Unknown:
                left = left.eletype
                
            if type(right) == Unknown:
                right = Checker.updateSideType("right", opType, ast.right, envi)
            elif type(right) == ArrayType and type(right.eletype) == Unknown:
                right = Checker.updateSideType("right", opType, ast.right, envi)
            elif type(right) == ArrayType and type(right.eletype) != Unknown:
                right = right.eletype

            if type(left) == type(opType) and type(right) == type(opType):
                typeReturn = targetType
            else:
                raise TypeMismatchInExpression(ast)
        elif type(ast) == Assign:
            if type(ast.lhs) == Id:
                leftName = ast.lhs.name
            elif type(ast.lhs) in [CallExpr, CallStmt]:
                leftName = ast.lhs.method.name
            if type(ast.rhs) == Id:
                rightName = ast.rhs.name
            elif type(ast.rhs) in [CallExpr, CallStmt]:
                rightName = ast.rhs.method.name

            if type(left) == Unknown and type(right) == Unknown:
                return "TypeCannotBeInferred"
            elif type(left) == Unknown and type(right) != Unknown and type(right) != ArrayType:
                left = right
                typeReturn = Checker.updateSideType("left", right, ast.lhs, envi)
            elif type(left) != Unknown and type(left) != ArrayType and type(right) == Unknown:
                right = left
                typeReturn = Checker.updateSideType("right", left, ast.rhs, envi)
            elif type(left) != type(right):
                raise TypeMismatchInStatement(ast)
            else:
                typeReturn = left
        elif type(ast) in [CallExpr, CallStmt]:
            for i in range(len(left)):
                if type(left[i]) == Unknown and type(right[i]) == Unknown:
                    return "TypeCannotBeInferred"
                elif type(left[i]) == Unknown and type(right[i]) != Unknown and type(right[i]) != ArrayType:
                    left[i] = right[i]
                elif type(left[i]) == Unknown and type(right[i]) == ArrayType and type(right[i].eletype) != Unknown:
                    left[i] = right[i].eletype
                elif type(left[i]) != Unknown and type(left[i]) != ArrayType and type(right[i]) == Unknown:
                    right[i] = left[i]
                    typeReturn = Checker.updateSideType("right", left[i], ast.param[i], envi)
                elif type(left[i]) != Unknown and type(left[i]) != ArrayType and type(right[i]) == ArrayType and type(right[i].eletype) != Unknown and type(left[i]) != type(right[i].eletype):
                    if type(ast) == CallExpr:
                        raise TypeMismatchInExpression(ast)
                    else:
                        raise TypeMismatchInStatement(ast)
                elif (type(left[i]) != Unknown and type(left[i]) != ArrayType and type(right[i]) == ArrayType and type(right[i].eletype) != Unknown and type(left[i]) == type(right[i].eletype)):
                    pass
                elif type(left[i]) != type(right[i]):
                    if type(ast) == CallExpr:
                        raise TypeMismatchInExpression(ast)
                    else:
                        raise TypeMismatchInStatement(ast)
            typeReturn = Checker.updateSideType("left", left, ast.method, envi)
            return left, right
        return typeReturn

    @staticmethod
    def checkOneSideType(body, ast, envi, opType, targetType):
        if type(body) == Unknown:
            body = Checker.updateSideType("left", opType, ast.body, envi)
        elif type(body) == ArrayType and type(body.eletype) == Unknown:
            body = Checker.updateSideType("left", opType, ast.body, envi)
        elif type(body) == ArrayType and type(body.eletype) != Unknown:
            body = body.eletype
        if type(body) == type(opType):
            typeReturn = targetType
        else:
            raise TypeMismatchInExpression(ast)

        return typeReturn

    @staticmethod
    def checkMatchType(left, right, ast, envi):
        # Handle Array Type
        if type(left) == ArrayType and type(right) == ArrayType:
            lhs = left.eletype
            rhs = right.eletype
            typeReturn = Checker.checkTwoSideType(lhs, rhs, ast, envi)
        elif ArrayType in [type(left), type(right)] and Unknown in [type(left), type(right)]:
            return "TypeCannotBeInferred"
        elif ArrayType in [type(left), type(right)]:
            lhs = left.eletype if type(left) == ArrayType else left
            rhs = right.eletype if type(right) == ArrayType else right
            typeReturn = Checker.checkTwoSideType(lhs, rhs, ast, envi)
        else:
            typeReturn = Checker.checkTwoSideType(left, right, ast, envi)
            
        return typeReturn
    
    @staticmethod
    def checkParamType(actualParameters, formaParameters, ast, envi):
        if len(actualParameters) != len(formaParameters):
            return False
        returnVal = Checker.checkTwoSideType(formaParameters, actualParameters, ast, envi)
        if "TypeCannotBeInferred" == returnVal:
            return "TypeCannotBeInferred"
        formaParameters, actualParameters = returnVal
        
        for a, b in zip(formaParameters, actualParameters):
            if Unknown not in [type(a), type(b)] and type(a) != type(b) and type(a) != ArrayType and type(b) == ArrayType and type(b.eletype) != Unknown and type(a) != type(b.eletype):
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
        checkParam = Checker.checkParamType(actualParameters, formaParameters, ast, envi)
        if not checkParam:
            if type(ast) == CallStmt:
                raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInExpression(ast)
        
        if "TypeCannotBeInferred" == checkParam:
            return "TypeCannotBeInferred"
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

        # Visit all function
        [self.visit(x, globalEnvi) for x in ast.decl if type(x) == FuncDecl]

    # Visit declaration
    def visitVarDecl(self, ast, c):
        return Symbol.fromVarDecl(ast)

    def visitFuncDecl(self, ast: FuncDecl, globalEnvi):
        symbol = Symbol.getSymbol(ast.name.name, globalEnvi).makeHere()
        formaParameters = symbol.mtype.intype

        # Visit all local variables, parameter of function from input
        listParams = [self.visit(x, globalEnvi).toParam() for x in ast.param]
        
        # Check Redeclared Parameter and update localEnvi
        localEnvi = Checker.checkRedeclared([], listParams)
        for a, b in zip(localEnvi, formaParameters):
            a.updateMember(mtype = b)

        listLocalVar = [self.visit(x, globalEnvi).toVar() for x in ast.body[0]]

        # Check Redeclared Variable and update localEnvi
        localEnvi = Checker.checkRedeclared(localEnvi, listLocalVar)

        # Merge local with global environment
        localEnvi = Checker.mergedEnvi(globalEnvi, localEnvi)

        # Visit statements
        stmts = {type(x): self.visit(x, localEnvi) for x in ast.body[1]}

        Symbol.updateParamAndReturnType(stmts, localEnvi, ast)

        # Update global environment
        Checker.updateEnvi(globalEnvi, localEnvi)

        Symbol.getSymbol(ast.name.name, globalEnvi).updateMember(inHere = False)

    # Visit expression
    # Return Type of expression
    def visitBinaryOp(self, ast: BinaryOp, param):
        leftType = self.visit(ast.left, param)
        if "TypeCannotBeInferred" == leftType:
            return "TypeCannotBeInferred"
        rightType = self.visit(ast.right, param)
        if "TypeCannotBeInferred" == rightType:
            return "TypeCannotBeInferred"

        if ast.op in ['+', '-', '*', '\\', '%']:
            typeReturn = Checker.checkTwoSideType(leftType, rightType, ast, param, IntType(), IntType())
        elif ast.op in ['+.', '-.', '*.', '\\.']:
            typeReturn = Checker.checkTwoSideType(leftType, rightType, ast, param, FloatType(), FloatType())
        elif ast.op in ['==', '!=', '<', '>', '<=', '>=']:
            typeReturn = Checker.checkTwoSideType(leftType, rightType, ast, param, IntType(), BoolType())
        elif ast.op in ['=/=', '<.', '>.', '<=.', '>=.']:
            typeReturn = Checker.checkTwoSideType(leftType, rightType, ast, param, FloatType(), BoolType())
        elif ast.op in ['&&', '||']:
            typeReturn = Checker.checkTwoSideType(leftType, rightType, ast, param, BoolType(), BoolType())
        return typeReturn
    
    def visitUnaryOp(self, ast: UnaryOp, param):
        bodyType = self.visit(ast.body, param)

        if ast.op == '-':
            typeReturn = Checker.checkOneSideType(bodyType, ast, param, IntType(), IntType())
        elif ast.op == '-.':
            typeReturn = Checker.checkOneSideType(bodyType, ast, param, FloatType(), FloatType())
        elif ast.op == '!':
            typeReturn = Checker.checkOneSideType(bodyType, ast, param, BoolType(), BoolType())
        return typeReturn
    
    def visitId(self, ast: Id, envi):
        symbol = Checker.checkUndeclared(envi, ast.name, Identifier())
        return symbol.mtype
    
    # Function call, no semi
    def visitCallExpr(self, ast: CallExpr, globalEnvi):
        symbol = Symbol.getSymbol(ast.method.name, globalEnvi)
        paramType = [self.visit(x, globalEnvi) for x in ast.param]
        typeReturn = Checker.checkCall(ast, globalEnvi, paramType)
        if "TypeCannotBeInferred" == typeReturn:
            return "TypeCannotBeInferred"

        return typeReturn

    def visitArrayCell(self, ast: ArrayCell, envi):
        arrType = self.visit(ast.arr, envi)
        idxType = [self.visit(i, envi) for i in ast.idx]
        
        # if (type(ast.arr) == CallExpr and type(Symbol.getSymbol(ast.arr.method.name, envi).mtype.restype) in [ArrayType, Unknown]):
        #     pass
        # elif (type(ast.arr) == CallExpr and type(Symbol.getSymbol(ast.arr.method.name, envi).mtype.restype) not in [ArrayType, Unknown]) or type(arrType) != ArrayType:
        if type(arrType) != ArrayType:
            raise TypeMismatchInExpression(ast)
        for x in range(len(idxType)):
            if type(idxType[x]) == Unknown:
                idxType[x] = Checker.updateSideType("left", IntType(), ast.idx[x], envi)
            elif type(idxType[x]) == ArrayType:
                if type(idxType[x].eletype) == Unknown:
                    idxType[x] = ArrayType(idxType[x].dimen, Checker.updateSideType("left", IntType(), ast.idx[x], envi))

        if not all((isinstance(x, IntType) if type(x) != ArrayType else isinstance(x.eletype, IntType)) for x in idxType):
            raise TypeMismatchInExpression(ast)
        return arrType
    

    # Visit statement
    def visitAssign(self, ast: Assign, envi):
        lhsType = self.visit(ast.lhs, envi)
        rhsType = self.visit(ast.rhs, envi)
        if "TypeCannotBeInferred" in [lhsType, rhsType]:
            raise TypeCannotBeInferred(ast)
        if type(lhsType) == VoidType or (type(ast.lhs) == CallExpr and type(lhsType) == Unknown): # StringType
            raise TypeMismatchInStatement(ast)
        
        typeReturn = Checker.checkMatchType(lhsType, rhsType, ast, envi)
        if typeReturn == "TypeCannotBeInferred":
            raise TypeCannotBeInferred(ast)
        
        return typeReturn

    def visitIf(self, ast: If, envi):
        listReturn = []
        for x in ast.ifthenStmt:
            conditionalExprIf = self.visit(x[0], envi)
            if type(conditionalExprIf) != BoolType:
                raise TypeMismatchInStatement(ast)

            varDeclIf = [self.visit(y, envi) for y in x[1]]
            localEnvi = Checker.checkRedeclared([], varDeclIf)
            localEnvi = Checker.mergedEnvi(envi, localEnvi)
            
            stmtIf = {type(y): self.visit(y, localEnvi) for y in x[2]}
            
            listReturn.append(Symbol.updateParamAndReturnType(stmtIf, localEnvi, ast))
            Checker.updateEnvi(envi, localEnvi, varDeclIf)
        
        varDeclElse = [self.visit(y, envi) for y in ast.elseStmt[0]]
        localEnvi = Checker.checkRedeclared([], varDeclElse)
        localEnvi = Checker.mergedEnvi(envi, localEnvi)
        stmtElse = {type(y): self.visit(y, localEnvi) for y in ast.elseStmt[1]}
        listReturn.append(Symbol.updateParamAndReturnType(stmtElse, localEnvi, ast))
        Checker.updateEnvi(envi, localEnvi, varDeclElse)
        
        if not all(isinstance(x, (StringType, BoolType, IntType, FloatType, ArrayType, Unknown, VoidType)) for x in listReturn):
            raise TypeMismatchInStatement(ast)
        
        return listReturn[0]
    
    def visitFor(self, ast: For, envi):
        indexVar = self.visit(ast.idx1, envi)
        expr1 = self.visit(ast.expr1, envi)
        if type(expr1) != IntType:
            raise TypeMismatchInStatement(ast)
        if type(indexVar) != IntType:
            if type(indexVar) == Unknown:
                Checker.checkTwoSideType(indexVar, expr1, Assign(ast.idx1, ast.expr1), envi)
            else:
                raise TypeMismatchInStatement(ast)
        expr2 = self.visit(ast.expr2, envi)
        if type(expr2) != BoolType:
            raise TypeMismatchInStatement(ast)
        expr3 = self.visit(ast.expr3, envi)
        if type(expr3) != IntType:
            raise TypeMismatchInStatement(ast)
        
        varDecl = [self.visit(y, envi) for y in ast.loop[0]]
        localEnvi = Checker.checkRedeclared([], varDecl)
        localEnvi = Checker.mergedEnvi(envi, localEnvi)
        stmt = {type(y): self.visit(y, localEnvi) for y in ast.loop[1]}

        typeReturn = Symbol.updateParamAndReturnType(stmt, localEnvi, ast)
        Checker.updateEnvi(envi, localEnvi, varDecl)
        
        return typeReturn
    
    def visitContinue(self, ast, param):
        return None
    
    def visitBreak(self, ast, param):
        return None
    
    def visitReturn(self, ast: Return, envi):
        symbol = Symbol.getNowSymbol(envi)
        if ast.expr == None:
            typeReturn = VoidType()
        else:
            typeReturn = self.visit(ast.expr, envi)
        if type(typeReturn) != type(symbol.mtype.restype) and type(symbol.mtype.restype) != Unknown:
            raise TypeMismatchInStatement(ast)
        return typeReturn
    
    def visitDowhile(self, ast: Dowhile, envi):        
        varDecl = [self.visit(y, envi) for y in ast.sl[0]]
        localEnvi = Checker.checkRedeclared([], varDecl)
        localEnvi = Checker.mergedEnvi(envi, localEnvi)
        stmt = {type(y): self.visit(y, localEnvi) for y in ast.sl[1]}

        exp = self.visit(ast.exp, envi)
        if type(exp) != BoolType:
            raise TypeMismatchInStatement(ast)

        typeReturn = Symbol.updateParamAndReturnType(stmt, localEnvi, ast)
        Checker.updateEnvi(envi, localEnvi, varDecl)
        return typeReturn

    def visitWhile(self, ast: While, envi):
        exp = self.visit(ast.exp, envi)
        if type(exp) != BoolType:
            raise TypeMismatchInStatement(ast)
        
        varDecl = [self.visit(y, envi) for y in ast.sl[0]]
        localEnvi = Checker.checkRedeclared([], varDecl)
        localEnvi = Checker.mergedEnvi(envi, localEnvi)
        stmt = {type(y): self.visit(y, localEnvi) for y in ast.sl[1]}

        typeReturn = Symbol.updateParamAndReturnType(stmt, localEnvi, ast)
        Checker.updateEnvi(envi, localEnvi, varDecl)
        return typeReturn

    # Call stmt return VoidType, have semi
    def visitCallStmt(self, ast: CallStmt, globalEnvi):
        symbol = Symbol.getSymbol(ast.method.name, globalEnvi)

        paramType = [self.visit(x, globalEnvi) for x in ast.param]
        
        typeReturn = Checker.checkCall(ast, globalEnvi, paramType)
        
        if typeReturn == "TypeCannotBeInferred":
            raise TypeCannotBeInferred(ast)
        return typeReturn

    # Visit literal
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
        valueType = [self.visit(x, param) for x in ast.value]
        if not all(isinstance(x, (StringType, BoolType, IntType, FloatType, ArrayType)) for x in valueType):
            raise TypeMismatchInExpression(ast)

        dimen1 = len(valueType)
        dimen2 = 0
        dimen3 = 0
        for x in ast.value:
            varType = varType1 = self.visit(x, param)
            if type(varType1) == ArrayType:
                dimen2 = len(x.value) if dimen2 < len(x.value) else dimen2
                for y in x.value:
                    varType = varType2 = self.visit(y, param)
                    if type(varType2) == ArrayType:
                        dimen3 = len(y.value) if dimen3 < len(y.value) else dimen3
        dimen = [dimen1, dimen2, dimen3] if dimen3 > 0 else [dimen1, dimen2] if dimen2 > 0 else [dimen1]
        return ArrayType(dimen, varType)
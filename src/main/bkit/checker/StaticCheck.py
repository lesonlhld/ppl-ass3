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
                varType = ArrayType(var.varDimen, init.eletype)
            elif type(init) == Unknown:
                varType = ArrayType(var.varDimen, init)
            else:
                raise TypeMismatchInExpression(var)
            
        else:
            init = Type.getTypeFromLiteral(var.varInit)
            if type(init) == ArrayType:
                raise TypeMismatchInExpression(var)
            else:
                varType = init
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
                #Checker.checkUndeclared(listSymbol, x.name, Function())
                return x
        

    @staticmethod
    def updateParamType(envi, ast):
        symbol = Symbol.getNowSymbol(envi)

        actualParam = [x for x in envi if type(x.kind) == Parameter]
        actualParamType = [x.mtype for x in actualParam]

        formaParamType = symbol.mtype.intype
        
        paramType = []
        if len(formaParamType) == len(actualParamType):
            for i in range(len(formaParamType)):
                if type(formaParamType[i]) == Unknown and type(actualParamType[i]) != Unknown and type(actualParamType[i]) != ArrayType:
                    paramType.append(actualParamType[i])
                elif type(formaParamType[i]) == Unknown and type(actualParamType[i]) == ArrayType and type(actualParamType[i].eletype) != Unknown:
                    paramType.append(actualParamType[i].eletype)
                elif type(formaParamType[i]) != Unknown and type(formaParamType[i]) != ArrayType and type(actualParamType[i]) == Unknown:
                    paramType.append(formaParamType[i])
                    actualParam[i].updateMember(mtype = formaParamType[i])
                elif type(formaParamType[i]) == ArrayType and type(formaParamType[i].eletype) != Unknown and type(actualParamType[i]) == Unknown:
                    paramType.append(formaParamType[i].eletype)
                    actualParam[i].updateMember(mtype = formaParamType[i].eletype)
                elif type(formaParamType[i]) == ArrayType and type(formaParamType[i].eletype) != Unknown and type(actualParamType[i]) == ArrayType and type(actualParamType[i].eletype) == Unknown:
                    paramType.append(formaParamType[i].eletype)
                    actualParam[i].updateMember(mtype = formaParamType[i])
                elif type(formaParamType[i]) == ArrayType and type(formaParamType[i].eletype) == Unknown and type(actualParamType[i]) == ArrayType and type(actualParamType[i].eletype) != Unknown:
                    paramType.append(actualParamType[i])
                else:
                    paramType.append(formaParamType[i])
                    actualParam[i].updateMember(mtype = formaParamType[i])
        else:
            paramType = formaParamType
        typeReturn = symbol.mtype.restype

        varType = MType(paramType, typeReturn)
        symbol.updateMember(mtype = varType)

    @staticmethod
    def updateReturnType(listReturn, envi, ast):
        symbol = Symbol.getNowSymbol(envi)

        actualParamType = [x.mtype for x in envi if type(x.kind) == Parameter]
        formaParamType = symbol.mtype.intype
        paramType = formaParamType if len(formaParamType) != len(actualParamType) or Unknown not in [type(x) for x in formaParamType] else actualParamType

        if len(listReturn) > 0:
            if not all(isinstance(x, (StringType, BoolType, IntType, FloatType, ArrayType, Unknown, VoidType)) for x in listReturn):
                raise TypeMismatchInStatement(ast)
            
            if type(symbol.mtype.restype) == Unknown or type(symbol.mtype.restype) in [type(x) for x in listReturn]:
                typeReturn = listReturn[0]
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
        curFunction = Symbol.getNowSymbol(globalEnvi)
        redeclareFunctionName = False
        newEnvi = copy.deepcopy(globalEnvi)
        envi = [x.name for x in newEnvi]
        for x in localEnvi:
            if x.name in envi:
                symbol = Symbol.getSymbol(x.name, newEnvi)
                symbol.update(x)
            else:
                envi.append(x.name)
                newEnvi.append(x)
            if x.name == curFunction.name and type(x.kind) != Function:
                redeclareFunctionName = True
        if redeclareFunctionName == True:
            newEnvi.append(curFunction)
        return newEnvi

    @staticmethod
    def updateEnvi(globalEnvi, localEnvi, exceptList = None):
        if exceptList == None:
            envi = [x for x in localEnvi if x.isGlobal == True]
            for x in envi:
                symbol = Symbol.getSymbol(x.name, globalEnvi)
                symbol.update(x)
        else:
            curFunction = Symbol.getNowSymbol(globalEnvi)
            envi = [x for x in localEnvi]
            noUpdateList = [x.name for x in exceptList]
            
            for x in localEnvi:
                if x.name not in noUpdateList:
                    if x.name == curFunction.name:
                        if type(x.kind) == Function:
                            symbol = curFunction.update(x)
                    else:
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
        checkRedeclareFunction = Symbol.getSymbol(currentEnvi[-1].name, currentEnvi)
        if type(checkRedeclareFunction.kind) != type(currentEnvi[-1].kind):
            newCurrentEnvi = copy.deepcopy(currentEnvi[:-1])
        else:
            newCurrentEnvi = currentEnvi
        envi = {x.name: Identifier() if type(x.kind) in [Variable, Parameter] else x.kind for x in newCurrentEnvi}
        
        if name not in list(envi.keys()) or type(envi[name]) != type(kind):
            raise Undeclared(kind, name)
        
        return Symbol.getSymbol(name, newCurrentEnvi)
        
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
            if (type(symbol.mtype.restype) == Unknown or type(symbol.mtype.restype) == type(sideType)) and side == "right":
                varType = MType(symbol.mtype.intype, sideType)
                symbol.updateMember(mtype = varType)
        elif type(symbol.mtype) == ArrayType:
            if type(symbol.mtype.eletype) == Unknown or type(symbol.mtype.eletype) == type(sideType):
                varType = ArrayType(symbol.mtype.dimen, sideType)
                symbol.updateMember(mtype = varType)
        else:
            varType = sideType
            symbol.updateMember(mtype = varType)
        return sideType

    @staticmethod
    def checkTwoSideType(left, right, ast, envi, opType = None, targetType = None):
        if type(ast) == Assign:
            if type(left) == Unknown and type(right) == Unknown:
                raise TypeCannotBeInferred(ast)
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
            for i in range(len(right)):
                if (type(left[i]) == Unknown and type(right[i]) == Unknown) or (type(left[i]) == ArrayType and type(left[i].eletype) == Unknown and type(right[i]) == ArrayType and type(right[i].eletype) == Unknown):
                    raise TypeCannotBeInferred(ast)
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
                elif type(left[i]) != type(right[i]) or (type(left[i]) == ArrayType and type(right[i]) == ArrayType and type(left[i].eletype) != Unknown and type(right[i].eletype) != Unknown and type(left[i].eletype) != type(right[i].eletype)):
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
            body = Checker.updateSideType("right", opType, ast, envi)
        elif type(body) == ArrayType and type(body.eletype) == Unknown:
            body = Checker.updateSideType("right", opType, ast, envi)
        elif type(body) == ArrayType and type(body.eletype) != Unknown:
            body = body.eletype
        if type(body) == type(opType):
            typeReturn = targetType
        else:
            raise TypeMismatchInExpression(ast)

        Symbol.updateParamType(envi, ast)
        return typeReturn

    @staticmethod
    def checkMatchType(left, right, ast, envi):
        # Handle Array Type
        if type(left) == ArrayType and type(right) == ArrayType:
            lhs = left.eletype
            rhs = right.eletype
            typeReturn = Checker.checkTwoSideType(lhs, rhs, ast, envi)
        elif ArrayType in [type(left), type(right)] and Unknown in [type(left), type(right)]:
            raise TypeCannotBeInferred(ast)
        elif ArrayType in [type(left), type(right)]:
            lhs = left.eletype if type(left) == ArrayType else left
            rhs = right.eletype if type(right) == ArrayType else right
            typeReturn = Checker.checkTwoSideType(lhs, rhs, ast, envi)
        else:
            typeReturn = Checker.checkTwoSideType(left, right, ast, envi)
            
        return typeReturn
    
    @staticmethod
    def checkParamType(actualParameters, formaParameters, ast, envi, final):
        if len(formaParameters) < len(actualParameters):
            return False        
            
        formaParameters, actualParameters = Checker.checkTwoSideType(formaParameters, actualParameters, ast, envi)

        if len(formaParameters) > len(actualParameters) and final == True:
            return False        

        for a, b in zip(formaParameters, actualParameters):
            if Unknown not in [type(a), type(b)] and type(a) != type(b) and type(a) != ArrayType and type(b) == ArrayType and type(b.eletype) != Unknown and type(a) != type(b.eletype):
                return False
            
        return True

    @staticmethod
    def checkCall(ast, envi, actualParameters, final = False):
        symbol = Checker.checkUndeclared(envi, ast.method.name, Function())

        formaParameters = symbol.mtype.intype
        
        checkParam = Checker.checkParamType(actualParameters, formaParameters, ast, envi, final)
        if type(ast) == CallStmt:
            if type(symbol.mtype.restype) in [Unknown, VoidType]:
                typeReturn = VoidType()
            else:
                raise TypeMismatchInStatement(ast)
        else:
            typeReturn = symbol.mtype.restype
        if not checkParam:
            if type(ast) == CallStmt:
                raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInExpression(ast)
        varType = MType(formaParameters, typeReturn)
        symbol.updateMember(mtype = varType)
        
        return typeReturn
        
    
class StaticChecker(BaseVisitor):
    def checkUnOp(self, ast, param, inType, outType):
        bodyType = self.visit(ast.body, param)
        if ArrayType == type(bodyType):
            raise TypeMismatchInExpression(ast)
        try:
            typeReturn = Checker.checkOneSideType(bodyType, ast.body, param, inType, outType)
        except TypeMismatchInExpression:
            raise TypeMismatchInExpression(ast)
        return typeReturn

    def checkLeftBinOp(self, ast, param, inType, outType):
        leftType = self.visit(ast.left, param)
        if ArrayType == type(leftType):
            raise TypeMismatchInExpression(ast)
        try:
            typeReturn = Checker.checkOneSideType(leftType, ast.left, param, inType, outType)
        except TypeMismatchInExpression:
            raise TypeMismatchInExpression(ast)

    def checkRightBinOp(self, ast, param, inType, outType):
        rightType = self.visit(ast.right, param)
        if ArrayType == type(rightType):
            raise TypeMismatchInExpression(ast)
        try:
            typeReturn = Checker.checkOneSideType(rightType, ast.right, param, inType, outType)
        except TypeMismatchInExpression:
            raise TypeMismatchInExpression(ast)

    def __init__(self,ast):
        self.ast = ast
        # global_envi: built-in function names
        self.global_envi = [
Symbol("int_of_float",MType([FloatType()],IntType())),
Symbol("float_to_int",MType([IntType()],FloatType())),
Symbol("int_of_string",MType([StringType()],IntType())),
Symbol("string_of_int",MType([IntType()],StringType())),
Symbol("float_of_string",MType([StringType()],FloatType())),
Symbol("string_of_float",MType([FloatType()],StringType())),
Symbol("bool_of_string",MType([StringType()],BoolType())),
Symbol("string_of_bool",MType([BoolType()],StringType())),
Symbol("read",MType([],StringType())),
Symbol("printLn",MType([],VoidType())),
Symbol("print",MType([StringType()],VoidType())),
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
        listReturn = []
        for y in ast.body[1]:
            z = self.visit(y, localEnvi)
            if type(y) == Return:
                listReturn.append(z)
        # Update global environment
        Checker.updateEnvi(globalEnvi, localEnvi)
        Symbol.updateReturnType(listReturn, globalEnvi, ast)

        symbol.updateMember(inHere = False)

    # Visit expression
    # Return Type of expression
    def visitBinaryOp(self, ast: BinaryOp, param):
        if ast.op in ['+', '-', '*', '\\', '%']:
            self.checkLeftBinOp(ast, param, IntType(), IntType())
            self.checkRightBinOp(ast, param, IntType(), IntType())

            typeReturn = IntType()
        elif ast.op in ['+.', '-.', '*.', '\\.']:
            self.checkLeftBinOp(ast, param, FloatType(), FloatType())
            self.checkRightBinOp(ast, param, FloatType(), FloatType())

            typeReturn = FloatType()
        elif ast.op in ['==', '!=', '<', '>', '<=', '>=']:
            self.checkLeftBinOp(ast, param, IntType(), BoolType())
            self.checkRightBinOp(ast, param, IntType(), BoolType())

            typeReturn = BoolType()
        elif ast.op in ['=/=', '<.', '>.', '<=.', '>=.']:
            self.checkLeftBinOp(ast, param, FloatType(), BoolType())
            self.checkRightBinOp(ast, param, FloatType(), BoolType())

            typeReturn = BoolType()
        elif ast.op in ['&&', '||']:
            self.checkLeftBinOp(ast, param, BoolType(), BoolType())
            self.checkRightBinOp(ast, param, BoolType(), BoolType())

            typeReturn = BoolType()
        return typeReturn
    
    def visitUnaryOp(self, ast: UnaryOp, param):
        if ast.op == '-':
            typeReturn = self.checkUnOp(ast, param, IntType(), IntType())
        elif ast.op == '-.':
            typeReturn = self.checkUnOp(ast, param, FloatType(), FloatType())
        elif ast.op == '!':
            typeReturn = self.checkUnOp(ast, param, BoolType(), BoolType())
        return typeReturn
    
    def visitId(self, ast: Id, envi):
        symbol = Checker.checkUndeclared(envi, ast.name, Identifier())
        return symbol.mtype
    
    # Function call, no semi
    def visitCallExpr(self, ast: CallExpr, globalEnvi):
        typeReturn = self.visitCall(ast, globalEnvi)
        
        return typeReturn

    def visitArrayCell(self, ast: ArrayCell, envi):
        arrType = self.visit(ast.arr, envi)
        idxType = []
        for i in ast.idx:
            y = self.visit(i, envi)
            if type(y) == Unknown:
                y = Checker.updateSideType("left", IntType(), i, envi)
            Symbol.updateParamType(envi, ast)
            idxType.append(y)
        
        if type(arrType) != ArrayType and type(ast.arr) == CallExpr:
            raise TypeCannotBeInferred(ast)
        elif type(arrType) != ArrayType:
            raise TypeMismatchInExpression(ast)

        if len(arrType.dimen) != len(idxType):
            raise TypeMismatchInExpression(ast)

        if not all(isinstance(x, IntType) for x in idxType):
            raise TypeMismatchInExpression(ast)

        Symbol.updateParamType(envi, ast)
        return self.visit(ast.arr, envi).eletype
    

    # Visit statement
    def visitAssign(self, ast: Assign, envi):
        try:
            lhsType = self.visit(ast.lhs, envi)
        except TypeCannotBeInferred:
            raise TypeCannotBeInferred(ast)
        try:
            rhsType = self.visit(ast.rhs, envi)
        except TypeCannotBeInferred:
            raise TypeCannotBeInferred(ast)
        if type(lhsType) == Unknown:
            lhsType = self.visit(ast.lhs, envi)
        
        if ArrayType == type(lhsType) and ArrayType == type(rhsType):
            if len(lhsType.dimen) != len(rhsType.dimen):
                raise TypeMismatchInStatement(ast)
            for x in range(len(lhsType.dimen)):
                if lhsType.dimen[x] != rhsType.dimen[x]:
                    raise TypeMismatchInStatement(ast)
        elif (ArrayType == type(lhsType) and ArrayType != type(rhsType)) or (ArrayType != type(lhsType) and ArrayType == type(rhsType)):
            raise TypeMismatchInStatement(ast)
        if type(lhsType) == VoidType or type(rhsType) == VoidType or (type(ast.lhs) == CallExpr and (type(lhsType) == Unknown or type(lhsType) == ArrayType)) or (type(ast.lhs) == ArrayCell and type(ast.lhs.arr) == CallExpr and type(ast.rhs) == Id and type(rhsType) == ArrayType): # StringType
            raise TypeMismatchInStatement(ast)
        typeReturn = Checker.checkMatchType(lhsType, rhsType, ast, envi)
        Symbol.updateParamType(envi, ast)
        return typeReturn

    def visitIf(self, ast: If, envi):
        listReturn = []
        for x in ast.ifthenStmt:
            try:
                conditionalExprIf = self.visit(x[0], envi)
            except TypeCannotBeInferred:
                raise TypeCannotBeInferred(ast)
            if type(conditionalExprIf) == Unknown:
                Checker.checkOneSideType(conditionalExprIf, x[0], envi, BoolType(), BoolType())
            elif type(conditionalExprIf) != BoolType:
                raise TypeMismatchInStatement(ast)
            varDeclIf = [self.visit(y, envi) for y in x[1]]
            localEnvi = Checker.checkRedeclared([], varDeclIf)
            localEnvi = Checker.mergedEnvi(envi, localEnvi)
            for y in x[2]:
                z = self.visit(y, localEnvi)
                if type(y) == Return:
                    listReturn.append(z)
            listReturn.append(Symbol.updateReturnType(listReturn, localEnvi, ast))
                
            Checker.updateEnvi(envi, localEnvi, varDeclIf)
            
        varDeclElse = [self.visit(y, envi) for y in ast.elseStmt[0]]
        localEnvi = Checker.checkRedeclared([], varDeclElse)
        localEnvi = Checker.mergedEnvi(envi, localEnvi)
        for y in ast.elseStmt[1]:
            z = self.visit(y, localEnvi)
            if type(y) == Return:
                listReturn.append(z)
        typeReturn = Symbol.updateReturnType(listReturn, localEnvi, ast)

        Checker.updateEnvi(envi, localEnvi, varDeclElse)
        
        Symbol.updateParamType(envi, ast)
        return typeReturn
    
    def visitFor(self, ast: For, envi):
        indexVar = self.visit(ast.idx1, envi)
        expr1 = self.visit(ast.expr1, envi)
        if type(expr1) != IntType:
            if type(expr1) == Unknown:
                Checker.checkOneSideType(indexVar, ast.expr1, envi, IntType(), IntType())
            else:
                raise TypeMismatchInStatement(ast)
        if type(indexVar) != IntType:
            if type(indexVar) == Unknown:
                Checker.checkTwoSideType(indexVar, expr1, Assign(ast.idx1, ast.expr1), envi)
            else:
                raise TypeMismatchInStatement(ast)
        expr2 = self.visit(ast.expr2, envi)
        if type(expr2) != BoolType:
            if type(expr2) == Unknown:
                Checker.checkOneSideType(indexVar, ast.expr2, envi, BoolType(), BoolType())
            else:
                raise TypeMismatchInStatement(ast)
        expr3 = self.visit(ast.expr3, envi)
        if type(expr3) != IntType:
            if type(expr3) == Unknown:
                Checker.checkOneSideType(indexVar, ast.expr3, envi, IntType(), IntType())
            else:
                raise TypeMismatchInStatement(ast)
        
        varDecl = [self.visit(y, envi) for y in ast.loop[0]]
        localEnvi = Checker.checkRedeclared([], varDecl)
        localEnvi = Checker.mergedEnvi(envi, localEnvi)
        
        listReturn = []
        for y in ast.loop[1]:
            z = self.visit(y, localEnvi)
            if type(y) == Return:
                listReturn.append(z)

        typeReturn = Symbol.updateReturnType(listReturn, localEnvi, ast)

        Checker.updateEnvi(envi, localEnvi, varDecl)
        
        Symbol.updateParamType(envi, ast)
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
            try:
                typeReturn = self.visit(ast.expr, envi)
            except TypeCannotBeInferred:
                raise TypeCannotBeInferred(ast)
            if type(typeReturn) == VoidType:
                raise TypeMismatchInStatement(ast)
        if type(typeReturn) != type(symbol.mtype.restype) and type(symbol.mtype.restype) != Unknown:
            raise TypeMismatchInStatement(ast)
        elif type(typeReturn) == Unknown or (type(typeReturn) == ArrayType and type(typeReturn.eletype) == Unknown):
            raise TypeCannotBeInferred(ast)
        return typeReturn
    
    def visitDowhile(self, ast: Dowhile, envi):        
        varDecl = [self.visit(y, envi) for y in ast.sl[0]]
        localEnvi = Checker.checkRedeclared([], varDecl)
        localEnvi = Checker.mergedEnvi(envi, localEnvi)
        
        listReturn = []
        for y in ast.sl[1]:
            z = self.visit(y, localEnvi)
            if type(y) == Return:
                listReturn.append(z)

        Checker.updateEnvi(envi, localEnvi, varDecl)
    
        try:
            exp = self.visit(ast.exp, envi)
        except TypeCannotBeInferred:
            raise TypeCannotBeInferred(ast)
        if type(exp) == Unknown:
            Checker.checkOneSideType(exp, ast.exp, envi, BoolType(), BoolType())
        elif type(exp) != BoolType:
            raise TypeMismatchInStatement(ast)
        
        typeReturn = Symbol.updateReturnType(listReturn, envi, ast)
        Symbol.updateParamType(envi, ast)
        return typeReturn

    def visitWhile(self, ast: While, envi):
        try:
            exp = self.visit(ast.exp, envi)
        except TypeCannotBeInferred:
            raise TypeCannotBeInferred(ast)
        if type(exp) == Unknown:
            Checker.checkOneSideType(exp, ast.exp, envi, BoolType(), BoolType())
        elif type(exp) != BoolType:
            raise TypeMismatchInStatement(ast)
        
        varDecl = [self.visit(y, envi) for y in ast.sl[0]]
        localEnvi = Checker.checkRedeclared([], varDecl)
        localEnvi = Checker.mergedEnvi(envi, localEnvi)
        listReturn = []
        for y in ast.sl[1]:
            z = self.visit(y, localEnvi)
            if type(y) == Return:
                listReturn.append(z)

        typeReturn = Symbol.updateReturnType(listReturn, localEnvi, ast)
        Checker.updateEnvi(envi, localEnvi, varDecl)
        Symbol.updateParamType(envi, ast)
        return typeReturn

    def visitCall(self, ast, globalEnvi):
        symbol = Symbol.getSymbol(ast.method.name, globalEnvi)

        paramType = []
        for i in ast.param:
            y = self.visit(i, globalEnvi)
            paramType.append(y)
            Checker.checkCall(ast, globalEnvi, paramType)
            Symbol.updateParamType(globalEnvi, ast)

        try:
            typeReturn = Checker.checkCall(ast, globalEnvi, paramType, True)
        except TypeCannotBeInferred:
            raise TypeCannotBeInferred(ast)
        Symbol.updateParamType(globalEnvi, ast)
        return typeReturn
        
    # Call stmt return VoidType, have semi
    def visitCallStmt(self, ast: CallStmt, globalEnvi):
        try:
            typeReturn = self.visitCall(ast, globalEnvi)
        except TypeCannotBeInferred:
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
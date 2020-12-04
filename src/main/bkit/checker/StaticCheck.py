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
            for x in literal.value:
                varType = Type.getTypeFromLiteral(x)
            return varType
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

    # @staticmethod
    # def getListName(listSymbol):
    #     name = [x.name for x in listSymbol]
    #     return name

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
        envi = [x.name for x in currentEnvi]
        if name not in envi:
            raise Undeclared(kind, name)
        return Symbol.getSymbol(name, currentEnvi)
        
    @staticmethod
    def checkMatchType(lhs, rhs, ast, envi):
        # Handle Array Type
        if ArrayType in [type(lhs), type(rhs)]:
            if type(patternType) != type(paramType): return False
            return Checker.matchArrayType(patternType, paramType)
        else:
            if type(lhs) == Unknown and type(rhs) == Unknown:
                raise TypeCannotBeInferred(ast)
            elif type(rhs) != Unknown and type(lhs) == Unknown:
                lhs = rhs
                symbol = Symbol.getSymbol(ast.lhs.name, envi).updateMember(mtype = rhs)
            elif type(lhs) != Unknown and type(rhs) == Unknown:
                rhs = lhs
                symbol = Symbol.getSymbol(ast.rhs.name, envi).updateMember(mtype = lhs)
            elif not type(lhs) == type(rhs):
                raise TypeCannotBeInferred(ast)
        

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

        # Visit all function expect function "main"
        [self.visit(x, globalEnvi) for x in ast.decl if type(x) == FuncDecl]

        # # Visit all functions and update its type
        # for x in globalEnvi:
        #     if type(x.kind) == Function and x.name != 'main':
        #         a = self.visit(x)
        #         x.updateType()
        #         x.makeVisit()



    # Visit declaration
    def visitVarDecl(self, ast, c):
        return Symbol.fromVarDecl(ast)

    def visitFuncDecl(self, ast: FuncDecl, globalEnvi):
        symbol = Symbol.getSymbol(ast.name.name, globalEnvi)

        # Visit all local variables, parameter of function from input
        listParams = [self.visit(x, globalEnvi).toParam() for x in ast.param]
        listLocalVar = [self.visit(x, globalEnvi).toVar() for x in ast.body[0]]

        # Check Redeclared Variable/Parameter and update localEnvi
        localEnvi = Checker.checkRedeclared(listParams, listLocalVar)

        # Merge local with global environment
        localEnvi = Checker.mergedEnvi(globalEnvi, localEnvi)

        # Visit statements
        stmts = [self.visit(x, localEnvi) for x in ast.body[1]]

        # for x in globalEnvi:
        #    print(x)
        # print("====================")
        # for x in localEnvi:
        #    print(x)
        # print("====================")
        # Checker.updateGlobalEnvi(globalEnvi, localEnvi)
        # for x in globalEnvi:
        #    print(x)
        # print("====================")

        symbol.updateMember(mtype = None,visited = True)


    # Visit statement
    def visitBinaryOp(self, ast, param):
        return None
    
    def visitUnaryOp(self, ast, param):
        return None
    
    def visitCallExpr(self, ast, param):
        return None
    
    def visitId(self, ast: Id, envi):
        symbol = Checker.checkUndeclared(envi, ast.name, Identifier())
        return symbol.mtype

    def visitArrayCell(self, ast, envi):
        print(envi)
        return None
    

    def visitAssign(self, ast: Assign, envi):
        rhs = self.visit(ast.rhs, envi)
        lhs = self.visit(ast.lhs, envi)

        print(type(ast.lhs))
        print("======*********=======")
        Checker.checkMatchType(lhs, rhs, ast, envi)
        # # Return None Type
        # scope, retType, inLoop, funcName = params
        # lhsType = self.visit(ast.lhs, (scope, funcName))
        # expType = self.visit(ast.exp, (scope, funcName))
        # if type(lhsType) in [ArrayType, VoidType, StringType] or not Checker.matchType(lhsType, expType):
        #     raise TypeMismatchInStatement(ast)
        # Scope.end()
        # return (ast, None)

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

    def visitCallStmt(self, ast, param):
        return None
    




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
        print("***********************")
        for x in ast.value:
            varType = Type.getTypeFromLiteral(x)
        return varType
import sys,os
from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener,ErrorListener
if not './main/bkit/parser/' in sys.path:
    sys.path.append('./main/bkit/parser/')
if os.path.isdir('../target/main/bkit/parser') and not '../target/main/bkit/parser/' in sys.path:
    sys.path.append('../target/main/bkit/parser/')

from BKITLexer import BKITLexer
from BKITParser import BKITParser
from lexererr import *
from ASTGeneration import ASTGeneration
from StaticCheck import StaticChecker
from StaticError import *
import json


testcase = "./test/CheckSuite.txt"
testfile = open(testcase,"a")
testfile.write("""import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):""")
testfile.close()


class TestUtil:
    @staticmethod
    def makeSource(inputStr,num):
        filename = "./test/testcases/" + str(num) + ".txt"
        file = open(filename,"w")
        """tmp = repr(inputStr)
        file.write(tmp[1:-1])"""
        file.write(inputStr)
        file.close()
        return FileStream(filename)


class TestLexer:
    @staticmethod
    def checkLexeme(input,expect,num):
        inputfile = TestUtil.makeSource(input,num)
        dest = open("./test/solutions/" + str(num) + ".txt","w")
        lexer = BKITLexer(inputfile)
        try:
            TestLexer.printLexeme(dest,lexer)
        except (ErrorToken,UncloseString,IllegalEscape) as err:
            dest.write(err.message)
        finally:
            dest.close() 
        dest = open("./test/solutions/" + str(num) + ".txt","r")
        line = dest.read()
        return line == expect

    @staticmethod    
    def printLexeme(dest,lexer):
        tok = lexer.nextToken()
        if tok.type != Token.EOF:
            dest.write(tok.text+",")
            TestLexer.printLexeme(dest,lexer)
        else:
            dest.write("<EOF>")
class NewErrorListener(ConsoleErrorListener):
    INSTANCE = None
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxException("Error on line "+ str(line) + " col " + str(column)+ ": " + offendingSymbol.text)
NewErrorListener.INSTANCE = NewErrorListener()

class SyntaxException(Exception):
    def __init__(self,msg):
        self.message = msg

class TestParser:
    @staticmethod
    def createErrorListener():
         return NewErrorListener.INSTANCE

    @staticmethod
    def checkParser(input,expect,num):
        inputfile = TestUtil.makeSource(input,num)
        dest = open("./test/solutions/" + str(num) + ".txt","w")
        lexer = BKITLexer(inputfile)
        listener = TestParser.createErrorListener()

        tokens = CommonTokenStream(lexer)

        parser = BKITParser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(listener)
        try:
            parser.program()
            dest.write("successful")
        except SyntaxException as f:
            dest.write(f.message)
        except Exception as e:
            dest.write(str(e))
        finally:
            dest.close()
        dest = open("./test/solutions/" + str(num) + ".txt","r")
        line = dest.read()
        return line == expect

class TestAST:
    @staticmethod
    def checkASTGen(input,expect,num):
        inputfile = TestUtil.makeSource(input,num)
        dest = open("./test/solutions/" + str(num) + ".txt","w")
        lexer = BKITLexer(inputfile)
        tokens = CommonTokenStream(lexer)
        parser = BKITParser(tokens)
        tree = parser.program()
        asttree = ASTGeneration().visit(tree)
        dest.write(str(asttree))
        dest.close()
        dest = open("./test/solutions/" + str(num) + ".txt","r")
        line = dest.read()
        return line == expect
    @staticmethod
    def test(inputdir,outputdir,num):
        #print("inutdir = "+inputdir)
        #print("outputdir = "+outputdir)
        dest = open(outputdir + "/" + str(num) + ".txt","w")
        lexer = BKITLexer(FileStream(inputdir + "/" + str(num) + ".txt"))
        tokens = CommonTokenStream(lexer)
        parser = BKITParser(tokens)
        tree = parser.program()
        asttree = ASTGeneration().visit(tree)
        dest.write(str(asttree))
        dest.close()
        dest1 = open(outputdir + "/" + str(num) + ".json","w")
        dest1.write(asttree.to_json())
        dest1.close()

class TestChecker:
    __count = 401
    @staticmethod
    def test(input,expect,num):
        return TestChecker.checkStatic(input,expect,num)
    @staticmethod
    def checkStatic(input,expect,num):
        testcase = "./test/CheckSuite.txt"
        testfile = open(testcase,"a")
        testfile.write("""
    def test_""" + str(TestChecker._TestChecker__count)+"""(self):
        \"\"\"Created automatically\"\"\"""" + (("""
        input = r\"\"\"""" + input + """\"\"\"""") if type(input) is str else ("""
        input = """ + str(input))) + """
        expect = str(""")


        dest = open("./test/solutions/" + str(num) + ".txt","w")
        
        if type(input) is str:
            inputfile = TestUtil.makeSource(input,num)
            lexer = BKITLexer(inputfile)
            tokens = CommonTokenStream(lexer)
            parser = BKITParser(tokens)
            tree = parser.program()
            asttree = ASTGeneration().visit(tree)
        else:
            inputfile = TestUtil.makeSource(str(input),num)
            asttree = input
        
        
        checker = StaticChecker(asttree)
        try:
            res = checker.check()
            #dest.write(str(list(res)))
        except StaticError as e:
            dest.write(str(e))
        finally:
            dest.close()
        dest = open("./test/solutions/" + str(num) + ".txt","r")
        line = dest.read()


        output = line if len(line) > 0 else ""
        testfile.write(line + """)
        self.assertTrue(TestChecker.test(input,expect,"""+str(TestChecker._TestChecker__count)+"""))
        """)
        testfile.close()
        TestChecker.__count += 1


        return line == expect

    @staticmethod
    def test1(inputdir,outputdir,num):
        
        dest = open(outputdir + "/" + str(num) + ".txt","w")
        
        try:
            lexer = BKITLexer(FileStream(inputdir + "/" + str(num) + ".txt"))
            tokens = CommonTokenStream(lexer)
            parser = BKITParser(tokens)
            tree = parser.program()
            asttree = ASTGeneration().visit(tree)

            checker = StaticChecker(asttree)
            res = checker.check()
            
        except StaticError as e:
            dest.write(str(e)+'\n')
        except:
            trace = traceback.format_exc()
            print ("Test " + str(num) + " catches unexpected error:" + trace + "\n")
        finally:
            dest.close()

        

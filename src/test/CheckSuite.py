import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):

    def test430(self):
        input = """
        Var: x;
        Function: main
            Body:
                foo(1);
                x = foo(1) + 2;
                Return;
            EndBody.
        Function: foo
            Parameter: x
            Body:
                Return;
            EndBody.
                   """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(CallExpr(Id('bar'),[Id('a')]),[Id('e'),Id('f')]),FloatLiteral(3.0))))
        self.assertTrue(TestChecker.test(input,expect,430))

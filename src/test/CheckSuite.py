import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):
    def test_418(self):
        """Created automatically"""
        input = r"""
        Var: x[10], y;
        Function: main
        Body:
            Var: k;
            k = -x[foo(x[0])];
            x = f();
        EndBody.
        Function: foo
        Parameter: y
        Body:
            Return y;
        EndBody.
        Function: f
        Body:
            Var: k[10];
            If k[2] Then
                Return k;
            EndIf.
            Return x;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id("z"),CallExpr(Id("main"),[IntLiteral(1),CallExpr(Id("main"),[Id("x"),BooleanLiteral(True)])]))))
        self.assertTrue(TestChecker.test(input,expect,418))
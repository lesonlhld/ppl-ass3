import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):
    def test_418(self):
        """Created automatically"""
        input = r"""
        Function: main
        Parameter: x, y
        Body:
            Var: z;
            While (True) Do
                z = main(1, main(x, True));
            EndWhile.
            Return y && z;
        EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id("z"),CallExpr(Id("main"),[IntLiteral(1),CallExpr(Id("main"),[Id("x"),BooleanLiteral(True)])]))))
        self.assertTrue(TestChecker.test(input,expect,418))
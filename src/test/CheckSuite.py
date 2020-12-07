import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):
    def test_401(self):
        """Created automatically"""
        input = r"""
        Var: a;
        Function: foo
            Body:
                a = 1.5;
                bar(a);
            EndBody.
                   
        Function: main
            Body:
            a =2.5;
            foo();
            EndBody.

        Function: bar
            Parameter: a
            Body:
                a = 3.0;

            EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,401))
        
import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):
    def test_401(self):
        """Created automatically"""
        input = r"""
        **Var: x[1] = {{{1,2},{3,4}},{{5,6},{7,8}},{9,10}};**
        Var: x;
Function: fact
Parameter: m[1][2],n[1],a**,y,x**
Body:
**n = !True;**
**m[1] ={1};**
**y = a + foo(x,2.5);**
**m[1][2] = {{2,2}};**
n[1] = 1;
a[3 + foo(2)] = a[n[1]] + 4;
**x = 1.5+ foo(3);**
Return 3.5;
EndBody.
Function: foo
Parameter: a
Body:
a=3;
Return 2;
EndBody.
Function: main
Body:
x = -10;
EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,401))
        
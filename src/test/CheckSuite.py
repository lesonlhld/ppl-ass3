import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):

    def test_undeclared_function(self):
        """Simple program: main"""
        input = """Function: main
        Parameter: n
                   Body: 
                        foo();
                   EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_diff_numofparam_stmt(self):
        """Complex program"""
        input = """Function: main  
                   Body:
                        printStrLn();
                    EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_diff_numofparam_expr(self):
        """More complex program"""
        input = """Function: main 
                    Body:
                        printStrLn(read(4));
                    EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([FuncDecl(Id("main"),[],([],[
            CallExpr(Id("foo"),[])]))])
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[
                        CallExpr(Id("read"),[IntLiteral(4)])
                        ])]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_diff_numofparam_stmt_use_ast(self):
        """Complex program"""
        input = Program([
                FuncDecl(Id("main"),[VarDecl(Id("x"),[],None)],([],[
                    CallStmt(Id("printStrLn"),[])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_var_decl(self):
        input = Program([VarDecl(Id("main"),[],IntLiteral(5)),VarDecl(Id("b"),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[],IntLiteral(6)),VarDecl(Id("e"),[],None),VarDecl(Id("f"),[],None),VarDecl(Id("m"),[],None),VarDecl(Id("n"),[10],None)])
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,406))
        
    def test_multi_func(self):
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
        self.assertTrue(TestChecker.test(input,expect,407))

        def test_12fcefe3(self):
            input = r"""
                Function: main
                Body:
                EndBody.

                Function: foo
                Parameter: a[1]
                Body:
                    Var: b[2];
                    a[1] = 2;
                    b[2] = {4.4,3.5};
                EndBody.
                """
            expect = str()
            self.assertTrue(TestChecker.test(input,expect,408))


    def test_1(self):
        """Simple program: main"""
        input = """
                Var: abc[5];
                Function: foo
                Parameter: x[2]
                Body:
                    x[1] = 1;
                    abc[1] = 2;
                EndBody.
                Function: main
                Body:
                    Var: z[2] = {1,2};
                    Var: w[2] = {3,4};
                    Var: x;
                    abc[1] = 1.5;
                EndBody.
            """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id("abc"),[IntLiteral(1)]),FloatLiteral(1.5))))
        self.assertTrue(TestChecker.test(input,expect,409))
    
    def test_3(self):
        """Simple program: main"""
        input = """
            Var: abc[5];
                Function: foo
                Parameter: x[2]
                Body:
                    x[1] = 1;
                    abc[1] = 2;
                EndBody.
                Function: main
                Body:
                    Var: z[2] = {1,2};
                    Var: w[2] = {3.,4.};
                    Var: x;
                    abc[1] = 1;
                    foo(z);
                    foo(w);
                EndBody.    
            """
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[Id("w")])))
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_4(self):
        """Simple program: main"""
        input = """
                Var: abc[2][3][4];
                Function: foo
                Parameter: x[2]
                Body:
                    x[1] = 1;
                    abc[1] = 2.;
                EndBody.
                Function: main
                Body:
                    Var: z[2][3][4] = {1.,2.};
                    Var: w[2] = {3.,4.};
                    Var: x;
                    abc = z;
                    foo(x);
                EndBody.
            """
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[Id("x")])))
        self.assertTrue(TestChecker.test(input,expect,411))
    
    def test_5(self):
        """Simple program: main"""
        input = """
                Function: foo
                Parameter: x
                Body:
                EndBody.
                Function: main
                Body:
                    Var: x, y = 0.5;
                    x = 1. +. foo(1);
                    y = foo(2.5) -. 1.;
                EndBody.
            """
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[FloatLiteral(2.5)])))
        self.assertTrue(TestChecker.test(input,expect,412))        
    
    def test_6(self):
        """Simple program: main"""
        input = """
                Function: foo
                Parameter: x
                Body:
                EndBody.
                Function: main
                Body:
                    Var: x, y = 0.5;
                    foo(x);
                    y = foo(x);
                EndBody.
            """
        expect = str(TypeCannotBeInferred(CallStmt(Id("foo"),[Id("x")])))
        self.assertTrue(TestChecker.test(input,expect,413))      
    
    def test_7(self):
        """Simple program: main"""
        input = """
                Function: foo
                Parameter: x
                Body:
                    Var: a[5]={1,2,3,4};
                    Return a;
                EndBody.
                Function: main
                Body:
                    Var: a[5]={1,2,3,4};
                    Var: b[4];
                    Var: c;
                    a[5]=b;
                EndBody.
            """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,414))  

    def test_8(self):
        """Simple program: main"""
        input = """
                Function: foo
                Parameter: x
                Body:
                    Var: a[5]={1,2,3,4};
                    Return a;
                EndBody.
                Function: main
                Body:
                    Var: a[5]={1,2,3,4};
                    Var: b[4];
                    Var: c;
                    a=b;
                EndBody.
            """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,415))   

    def test_9(self):
        """Simple program: main"""
        input = """
                Function: foo
                Parameter: x
                Body:
                    Var: a[5]={1,2,3,4};
                    Return a;
                EndBody.
                Function: main
                Body:
                    Var: a[5]={1,2,3,4};
                    Var: b[4];
                    Var: c;
                    a=c;
                EndBody.
                
            """
        expect = str(TypeCannotBeInferred(Assign(Id("a"),Id("c"))))
        self.assertTrue(TestChecker.test(input,expect,416))   

    def test_10(self):
        """Simple program: main"""
        input = """
                Function: foo
                Parameter: x
                Body:
                    Var: a[5]={1,2,3,4};
                    Return a;
                EndBody.
                Function: main
                Body:
                    Var: a[5]={1,2,3,4};
                    Var: b[4];
                    Var: c;
                    foo(3)[5] = a[1];
                    foo(3)[5]=b;
                EndBody.
            """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_11(self):
        input =r"""
        Var: a;

        Function: bar
            Parameter: n[10], int_of_string
            Body:
                b = 3.0;

            EndBody.

        Function: main
            Body:
                a = 1;
            EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("a"),IntLiteral(1))))
        expect = str(Undeclared(Identifier(),"b"))
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_310(self):
        """Created automatically"""
        input = r"""
        Var: x;
Function: fact
Parameter: n
Body:
If n == 0 Then
Return 2;
Else
Return n * fact (n - 1);
EndIf.
EndBody.
Function: main
Parameter: n
Body:
x = 10;
n = fact (x);
EndBody.""" 
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_24547643524(self):
        input = r"""Function: main
Parameter: a[5], b
Body:
Var: i = 0;
While (i < 5) Do
a[i] = b +. 1.0;
i = i + 1;
EndWhile.
EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_345(self):
        input = r"""
        Function: foroke
        Body:
            Var: i;
            For (i = 0, i < 10, 2) Do
                i =i + 1;
            EndFor.
            Return;
        EndBody.
        Function: main
        Body:
        EndBody.""" 
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,421))

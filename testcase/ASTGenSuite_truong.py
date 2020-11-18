import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_301(self):
        """Created automatically"""
        input = r"""
        Var: a = 5, b[2][3] = {123.123, True, {23.23, -23}};
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),VarDecl(Id("b"),[2,3],ArrayLiteral([FloatLiteral(123.123),BooleanLiteral(True),ArrayLiteral([FloatLiteral(23.23),UnaryOp("-",IntLiteral(23))])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
        
    def test_302(self):
        """Created automatically"""
        input = r"""Var: a;""" 
        expect = Program([VarDecl(Id("a"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
        
    def test_303(self):
        """Created automatically"""
        input = r"""Var: a = 5;""" 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5))])
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
        
    def test_304(self):
        """Created automatically"""
        input = r"""Var: a = 5 , b;""" 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),VarDecl(Id("b"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
        
    def test_305(self):
        """Created automatically"""
        input = r"""Var: a = "Truong";""" 
        expect = Program([VarDecl(Id("a"),[],StringLiteral("Truong"))])
        self.assertTrue(TestAST.checkASTGen(input,expect,305))
        
    def test_306(self):
        """Created automatically"""
        input = r"""Var: a = 4.0;""" 
        expect = Program([VarDecl(Id("a"),[],FloatLiteral(4.0))])
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
        
    def test_307(self):
        """Created automatically"""
        input = r"""Var: a = -1;""" 
        expect = Program([VarDecl(Id("a"),[],UnaryOp("-",IntLiteral(1)))])
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
        
    def test_308(self):
        """Created automatically"""
        input = r"""Var: a = -0.5;""" 
        expect = Program([VarDecl(Id("a"),[],UnaryOp("-",FloatLiteral(0.5)))])
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
        
    def test_309(self):
        """Created automatically"""
        input = r"""Var: a = True;""" 
        expect = Program([VarDecl(Id("a"),[],BooleanLiteral(True))])
        self.assertTrue(TestAST.checkASTGen(input,expect,309))
        
    def test_310(self):
        """Created automatically"""
        input = r"""Var: a = False;""" 
        expect = Program([VarDecl(Id("a"),[],BooleanLiteral(False))])
        self.assertTrue(TestAST.checkASTGen(input,expect,310))
        
    def test_311(self):
        """Created automatically"""
        input = r"""Var: a[2];""" 
        expect = Program([VarDecl(Id("a"),[2],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,311))
        
    def test_312(self):
        """Created automatically"""
        input = r"""Var: a[2] = {2};""" 
        expect = Program([VarDecl(Id("a"),[2],ArrayLiteral([IntLiteral(2)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,312))
        
    def test_313(self):
        """Created automatically"""
        input = r"""Var: a[2][3] = {True,{2,3}};""" 
        expect = Program([VarDecl(Id("a"),[2,3],ArrayLiteral([BooleanLiteral(True),ArrayLiteral([IntLiteral(2),IntLiteral(3)])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,313))
        
    def test_314(self):
        """Created automatically"""
        input = r"""Var: a, b = 4 , c = 6;""" 
        expect = Program([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],IntLiteral(4)),VarDecl(Id("c"),[],IntLiteral(6))])
        self.assertTrue(TestAST.checkASTGen(input,expect,314))
        
    def test_315(self):
        """Created automatically"""
        input = r"""""" 
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input,expect,315))
        
    def test_316(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;
        Function: main
        Parameter: a,b,c,d
        Body:
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,316))
        
    def test_317(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;
        Function: main
        Parameter: a
        Body:
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[VarDecl(Id("a"),[],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,317))
        
    def test_318(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;
        Function: main
        Body:
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,318))
        
    def test_319(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;
        Function: main
        Body:
        a = a + 2;
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(2)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,319))
        
    def test_320(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;
        Function: main
        Body:
        Var: a = 4;
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],IntLiteral(4))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,320))
        
    def test_321(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;
        Function: main
        Body:
        Var: a = 4;
        a = 3 + 1;
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],IntLiteral(4))],[Assign(Id("a"),BinaryOp("+",IntLiteral(3),IntLiteral(1)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,321))
        
    def test_322(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;
        Function: main
        Body:
        Var: a = 4;
        a = 3 + 1;
        foo();
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],IntLiteral(4))],[Assign(Id("a"),BinaryOp("+",IntLiteral(3),IntLiteral(1))),CallStmt(Id("foo"),[])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,322))
        
    def test_323(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;
        Function: main
        Body:
        Var: a = 4;
        a = 3 + 1;
        a = a + foo(a);
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],IntLiteral(4))],[Assign(Id("a"),BinaryOp("+",IntLiteral(3),IntLiteral(1))),Assign(Id("a"),BinaryOp("+",Id("a"),CallExpr(Id("foo"),[Id("a")])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,323))
        
    def test_324(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;
        Function: main
        Body:
        Var: a = 4;
        If a == 5 Then
            a = 2;
        EndIf.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],IntLiteral(4))],[If([(BinaryOp("==",Id("a"),IntLiteral(5)),[],[Assign(Id("a"),IntLiteral(2))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
        
    def test_325(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;
        Function: main
        Body:
        Var: a = 4;
        If a == 5 Then
            a = 2;
        Else Return 2;
        EndIf.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],IntLiteral(4))],[If([(BinaryOp("==",Id("a"),IntLiteral(5)),[],[Assign(Id("a"),IntLiteral(2))])],([],[Return(IntLiteral(2))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
        
    def test_326(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;
        Function: main
        Body:
        Var: a = 4;
        If a == 5 Then
            a = 2;
        Else
            Var: a = 3; 
            Return a;
        EndIf.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],IntLiteral(4))],[If([(BinaryOp("==",Id("a"),IntLiteral(5)),[],[Assign(Id("a"),IntLiteral(2))])],([VarDecl(Id("a"),[],IntLiteral(3))],[Return(Id("a"))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,326))
        
    def test_327(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;
        Function: main
        Body:
        Var: a = 4;
        If a == 5 Then
            a = 2;
        ElseIf True Then
            Var: a = 2;
            Break;
        Else
            Var: a = 3; 
            Return a;
        EndIf.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],IntLiteral(4))],[If([(BinaryOp("==",Id("a"),IntLiteral(5)),[],[Assign(Id("a"),IntLiteral(2))]),(BooleanLiteral(True),[VarDecl(Id("a"),[],IntLiteral(2))],[Break()])],([VarDecl(Id("a"),[],IntLiteral(3))],[Return(Id("a"))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,327))
        
    def test_328(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;
        Function: main
        Body:
        Var: a = 4;
        While a >. 2 Do
            a = 2 * 2;
        EndWhile.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],IntLiteral(4))],[While(BinaryOp(">.",Id("a"),IntLiteral(2)),([],[Assign(Id("a"),BinaryOp("*",IntLiteral(2),IntLiteral(2)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,328))
        
    def test_329(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;
        Function: main
        Body:
        Var: a = 4;
        While (a >. 2) || (a != 2) Do
            a = 2 * 2;
        EndWhile.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],IntLiteral(4))],[While(BinaryOp("||",BinaryOp(">.",Id("a"),IntLiteral(2)),BinaryOp("!=",Id("a"),IntLiteral(2))),([],[Assign(Id("a"),BinaryOp("*",IntLiteral(2),IntLiteral(2)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,329))
        
    def test_330(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;
        Function: main
        Body:
        Var: a = 4;
        While (a >. 2) || (a != 2) Do
            Var: a = -2;
            a = 2 * 2;
        EndWhile.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],IntLiteral(4))],[While(BinaryOp("||",BinaryOp(">.",Id("a"),IntLiteral(2)),BinaryOp("!=",Id("a"),IntLiteral(2))),([VarDecl(Id("a"),[],UnaryOp("-",IntLiteral(2)))],[Assign(Id("a"),BinaryOp("*",IntLiteral(2),IntLiteral(2)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,330))
        
    def test_331(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;
        Function: main
        Body:
        Var: a = 4;
        Do
            If a == 2 Then
                Return x + foo(2 + x);
            Else Break;
            EndIf.
        While a == 2
        EndDo.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],IntLiteral(4))],[Dowhile(([],[If([(BinaryOp("==",Id("a"),IntLiteral(2)),[],[Return(BinaryOp("+",Id("x"),CallExpr(Id("foo"),[BinaryOp("+",IntLiteral(2),Id("x"))])))])],([],[Break()]))]),BinaryOp("==",Id("a"),IntLiteral(2)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,331))
        
    def test_332(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;
        Function: main
        Body:
        Var: a = 4;
        Do
            If a == 2 Then
                Return x + foo(2 + x);
            Else Break;
            EndIf.

            While i == 2 Do
                Continue;
            EndWhile.
        While a == 2
        EndDo.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],IntLiteral(4))],[Dowhile(([],[If([(BinaryOp("==",Id("a"),IntLiteral(2)),[],[Return(BinaryOp("+",Id("x"),CallExpr(Id("foo"),[BinaryOp("+",IntLiteral(2),Id("x"))])))])],([],[Break()])),While(BinaryOp("==",Id("i"),IntLiteral(2)),([],[Continue()]))]),BinaryOp("==",Id("a"),IntLiteral(2)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,332))
        
    def test_333(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;
        Function: foo
        Body:
        Var: a = 4;
        Do
            If a == 2 Then
                Return x + foo(2 + x);
            Else Break;
            EndIf.

            While i == 2 Do
                Continue;
            EndWhile.
        While a == 2
        EndDo.
        EndBody.

        Function: main
        Parameter: a,b[2]
        Body:
            Return;
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("foo"),[],([VarDecl(Id("a"),[],IntLiteral(4))],[Dowhile(([],[If([(BinaryOp("==",Id("a"),IntLiteral(2)),[],[Return(BinaryOp("+",Id("x"),CallExpr(Id("foo"),[BinaryOp("+",IntLiteral(2),Id("x"))])))])],([],[Break()])),While(BinaryOp("==",Id("i"),IntLiteral(2)),([],[Continue()]))]),BinaryOp("==",Id("a"),IntLiteral(2)))])),FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2],None)],([],[Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,333))
        
    def test_334(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;

        Function: main
        Parameter: a,b[2]
        Body:
            x = x + 2 + 3*x + 6;
            Return a + foo(2 + a);
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2],None)],([],[Assign(Id("x"),BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("x"),IntLiteral(2)),BinaryOp("*",IntLiteral(3),Id("x"))),IntLiteral(6))),Return(BinaryOp("+",Id("a"),CallExpr(Id("foo"),[BinaryOp("+",IntLiteral(2),Id("a"))])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,334))
        
    def test_335(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;

        Function: main
        Parameter: a,b[2]
        Body:
            If bool_of_string ("True") Then
                a = int_of_string (read ());
                b = float_of_int (a) +. 2.0;
            ElseIf a == 5 Then
                a = a + main(123);
                Return a;
            ElseIf a == 6 Then
                a = a *. 2;
                Break;
            Else Continue;
            EndIf.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2],None)],([],[If([(CallExpr(Id("bool_of_string"),[StringLiteral("True")]),[],[Assign(Id("a"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),Assign(Id("b"),BinaryOp("+.",CallExpr(Id("float_of_int"),[Id("a")]),FloatLiteral(2.0)))]),(BinaryOp("==",Id("a"),IntLiteral(5)),[],[Assign(Id("a"),BinaryOp("+",Id("a"),CallExpr(Id("main"),[IntLiteral(123)]))),Return(Id("a"))]),(BinaryOp("==",Id("a"),IntLiteral(6)),[],[Assign(Id("a"),BinaryOp("*.",Id("a"),IntLiteral(2))),Break()])],([],[Continue()]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,335))
        
    def test_336(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;

        Function: main
        Parameter: a,b[2]
        Body:
            For (i = -2, i <= -10, -5) Do
                writeln(i);
            EndFor.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2],None)],([],[For(Id("i"),UnaryOp("-",2),BinaryOp("<=",Id("i"),UnaryOp("-",IntLiteral(10))),UnaryOp("-",IntLiteral(5)),([],[CallStmt(Id("writeln"),[Id("i")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,336))
        
    def test_337(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;

        Function: main
        Parameter: a,b[2]
        Body:
            For (i = -2, i <=. -10.2, -5) Do
                a = a + 2;
            EndFor.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2],None)],([],[For(Id("i"),UnaryOp("-",2),BinaryOp("<=.",Id("i"),UnaryOp("-",FloatLiteral(10.2))),UnaryOp("-",IntLiteral(5)),([],[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(2)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,337))
        
    def test_338(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;

        Function: main
        Parameter: a,b[2]
        Body:
            For (i = -2, i <=. -10.2, -5) Do
                If a == 2 Then
                    a[2 + foo(2)] = 3 + a*2*(2+3);
                    Return a + 2*foo(2 + a);
                EndIf.
            EndFor.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2],None)],([],[For(Id("i"),UnaryOp("-",2),BinaryOp("<=.",Id("i"),UnaryOp("-",FloatLiteral(10.2))),UnaryOp("-",IntLiteral(5)),([],[If([(BinaryOp("==",Id("a"),IntLiteral(2)),[],[Assign(ArrayCell(Id("a"),[BinaryOp("+",IntLiteral(2),CallExpr(Id("foo"),[IntLiteral(2)]))]),BinaryOp("+",IntLiteral(3),BinaryOp("*",BinaryOp("*",Id("a"),IntLiteral(2)),BinaryOp("+",IntLiteral(2),IntLiteral(3))))),Return(BinaryOp("+",Id("a"),BinaryOp("*",IntLiteral(2),CallExpr(Id("foo"),[BinaryOp("+",IntLiteral(2),Id("a"))]))))])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,338))
        
    def test_339(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;

        Function: main
        Parameter: a,b[2]
        Body:
            a = a + 2;
            writeln(i);
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2],None)],([],[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(2))),CallStmt(Id("writeln"),[Id("i")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,339))
        
    def test_340(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;

        Function: main
        Parameter: a,b[2]
        Body:
            a = foo(2);
            goo ();
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2],None)],([],[Assign(Id("a"),CallExpr(Id("foo"),[IntLiteral(2)])),CallStmt(Id("goo"),[])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,340))
        
    def test_341(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;

        Function: main
        Parameter: a,b[2]
        Body:
            a = foo("truong");
            goo ();
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2],None)],([],[Assign(Id("a"),CallExpr(Id("foo"),[StringLiteral("truong")])),CallStmt(Id("goo"),[])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,341))
        
    def test_342(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;

        Function: main
        Parameter: a,b[2]
        Body:
            a = foo(True);
            goo ();
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2],None)],([],[Assign(Id("a"),CallExpr(Id("foo"),[BooleanLiteral(True)])),CallStmt(Id("goo"),[])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,342))
        
    def test_343(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;

        Function: main
        Parameter: a,b[2]
        Body:
            printStrLn(arg);
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2],None)],([],[CallStmt(Id("printStrLn"),[Id("arg")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,343))
        
    def test_344(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;

        Function: main
        Parameter: a,b[2]
        Body:
            printLn();
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2],None)],([],[CallStmt(Id("printLn"),[])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,344))
        
    def test_345(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;

        Function: main
        Parameter: a,b[2]
        Body:
            print(arg);
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2],None)],([],[CallStmt(Id("print"),[Id("arg")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,345))
        
    def test_346(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;

        Function: main
        Parameter: a,b[2]
        Body:
            read();
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2],None)],([],[CallStmt(Id("read"),[])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,346))
        
    def test_347(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;

        Function: foo
        Parameter: a[5], b
        Body:
            Var: i = 0;
            While (i < 5) Do
                a[i] = b +. 1.0;
                i = i + 1;
            EndWhile.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("foo"),[VarDecl(Id("a"),[5],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("<",Id("i"),IntLiteral(5)),([],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,347))
        
    def test_348(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;
        Function: main
        Parameter: a,b[2]
        Body:
            If bool_of_string ("True") Then
                a = int_of_string (read ());
                b = float_of_int (a) +. 2.0;
            ElseIf a == 5 Then
                a = a + main(123);
                Return a;
            ElseIf a == 6 Then
                a = a *. 2;
                Break;
                writeln(a);
            Else Continue;
            EndIf.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2],None)],([],[If([(CallExpr(Id("bool_of_string"),[StringLiteral("True")]),[],[Assign(Id("a"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),Assign(Id("b"),BinaryOp("+.",CallExpr(Id("float_of_int"),[Id("a")]),FloatLiteral(2.0)))]),(BinaryOp("==",Id("a"),IntLiteral(5)),[],[Assign(Id("a"),BinaryOp("+",Id("a"),CallExpr(Id("main"),[IntLiteral(123)]))),Return(Id("a"))]),(BinaryOp("==",Id("a"),IntLiteral(6)),[],[Assign(Id("a"),BinaryOp("*.",Id("a"),IntLiteral(2))),Break(),CallStmt(Id("writeln"),[Id("a")])])],([],[Continue()]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,348))
        
    def test_349(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;
        Function: main
        Parameter: a,b[2],f
        Body:
            If bool_of_string ("True") Then
                a = int_of_string (read ());
                b = float_of_int (a) +. 2.0;
            ElseIf a == 5 Then
                a = a + main(123);
                Return a;
            ElseIf a == 6 Then
                a = a *. 2;
                Break;
                writeln(a);
            Else Continue;
            EndIf.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2],None),VarDecl(Id("f"),[],None)],([],[If([(CallExpr(Id("bool_of_string"),[StringLiteral("True")]),[],[Assign(Id("a"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),Assign(Id("b"),BinaryOp("+.",CallExpr(Id("float_of_int"),[Id("a")]),FloatLiteral(2.0)))]),(BinaryOp("==",Id("a"),IntLiteral(5)),[],[Assign(Id("a"),BinaryOp("+",Id("a"),CallExpr(Id("main"),[IntLiteral(123)]))),Return(Id("a"))]),(BinaryOp("==",Id("a"),IntLiteral(6)),[],[Assign(Id("a"),BinaryOp("*.",Id("a"),IntLiteral(2))),Break(),CallStmt(Id("writeln"),[Id("a")])])],([],[Continue()]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,349))
        
    def test_350(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;

        Function: foo
        Parameter: a[5], b
        Body:
            Var: i = 0;
            While (i < 5) Do
                a[i] = b +. 1.0;
                i = i + 1;
                Var: a = 5;
                If (a==2) && (a >. 5) Then
                    Var: x = "Truong";
                    a[2] = 2 + a;
                EndIf.
            EndWhile.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("foo"),[VarDecl(Id("a"),[5],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("<",Id("i"),IntLiteral(5)),([VarDecl(Id("a"),[],IntLiteral(5))],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),If([(BinaryOp("&&",BinaryOp("==",Id("a"),IntLiteral(2)),BinaryOp(">.",Id("a"),IntLiteral(5))),[VarDecl(Id("x"),[],StringLiteral("Truong"))],[Assign(ArrayCell(Id("a"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(2),Id("a")))])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,350))
        
    def test_351(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;
        Function: foo
        Parameter: a[5], b
        Body:
            Var: a[5] = {1,4,3,2,0};
            Var: b[2][3]={{1,2,3},{4,5,6}};
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("foo"),[VarDecl(Id("a"),[5],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("a"),[5],ArrayLiteral([IntLiteral(1),IntLiteral(4),IntLiteral(3),IntLiteral(2),IntLiteral(0)])),VarDecl(Id("b"),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])]))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,351))
        
    def test_352(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: fact
        Parameter: n
        Body:
            If n == 0 Then
                Return 1;
            Else
                Return n * fact (n - 1);
            EndIf.
        EndBody.
        Function: main
        Body:
            x = 10;
            fact (x);
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("fact"),[VarDecl(Id("n"),[],None)],([],[If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],[Return(IntLiteral(1))])],([],[Return(BinaryOp("*",Id("n"),CallExpr(Id("fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))]))])),FuncDecl(Id("main"),[],([],[Assign(Id("x"),IntLiteral(10)),CallStmt(Id("fact"),[Id("x")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,352))
        
    def test_353(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10];
        """ 
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],IntLiteral(5)),VarDecl(Id("b"),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[],IntLiteral(6)),VarDecl(Id("e"),[],None),VarDecl(Id("f"),[],None),VarDecl(Id("m"),[],None),VarDecl(Id("n"),[10],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,353))
        
    def test_354(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10];
        Function: foo
        Parameter: n
        Body:
        While a !=5 Do
            Return foo(2.2 + a*foo(2));
        EndWhile.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],IntLiteral(5)),VarDecl(Id("b"),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[],IntLiteral(6)),VarDecl(Id("e"),[],None),VarDecl(Id("f"),[],None),VarDecl(Id("m"),[],None),VarDecl(Id("n"),[10],None),FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[While(BinaryOp("!=",Id("a"),IntLiteral(5)),([],[Return(CallExpr(Id("foo"),[BinaryOp("+",FloatLiteral(2.2),BinaryOp("*",Id("a"),CallExpr(Id("foo"),[IntLiteral(2)])))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,354))
        
    def test_355(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10];
        Function: foo
        Parameter: n
        Body:
        While a !=5 Do
            Return foo(2.2 + a*foo(2));
        EndWhile.
        If (a == 2) || (a <. 5.5) Then
            x = 5;
            Return x;
        Else Break;
        EndIf.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],IntLiteral(5)),VarDecl(Id("b"),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[],IntLiteral(6)),VarDecl(Id("e"),[],None),VarDecl(Id("f"),[],None),VarDecl(Id("m"),[],None),VarDecl(Id("n"),[10],None),FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[While(BinaryOp("!=",Id("a"),IntLiteral(5)),([],[Return(CallExpr(Id("foo"),[BinaryOp("+",FloatLiteral(2.2),BinaryOp("*",Id("a"),CallExpr(Id("foo"),[IntLiteral(2)])))]))])),If([(BinaryOp("||",BinaryOp("==",Id("a"),IntLiteral(2)),BinaryOp("<.",Id("a"),FloatLiteral(5.5))),[],[Assign(Id("x"),IntLiteral(5)),Return(Id("x"))])],([],[Break()]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,355))
        
    def test_356(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10];
        Function: foo
        Parameter: n
        Body:
        While a !=5 Do
            Return foo(2.2 + a*foo(2));
        EndWhile.
        If (a == 2) || (a <. 5.5) Then
            x = 5;
            Return x;
        Else Break;
        EndIf.
        Var: a = 5;
        
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],IntLiteral(5)),VarDecl(Id("b"),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[],IntLiteral(6)),VarDecl(Id("e"),[],None),VarDecl(Id("f"),[],None),VarDecl(Id("m"),[],None),VarDecl(Id("n"),[10],None),FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([VarDecl(Id("a"),[],IntLiteral(5))],[While(BinaryOp("!=",Id("a"),IntLiteral(5)),([],[Return(CallExpr(Id("foo"),[BinaryOp("+",FloatLiteral(2.2),BinaryOp("*",Id("a"),CallExpr(Id("foo"),[IntLiteral(2)])))]))])),If([(BinaryOp("||",BinaryOp("==",Id("a"),IntLiteral(2)),BinaryOp("<.",Id("a"),FloatLiteral(5.5))),[],[Assign(Id("x"),IntLiteral(5)),Return(Id("x"))])],([],[Break()]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,356))
        
    def test_357(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10];
        Function: foo
        Parameter: n
        Body:
        While a !=5 Do
            Return foo(2.2 + a*foo(2));
        EndWhile.
        If (a == 2) || (a <. 5.5) Then
            x = 5;
            Return x;
        Else Break;
        EndIf.
        Var: a = 5;
        Break;
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],IntLiteral(5)),VarDecl(Id("b"),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[],IntLiteral(6)),VarDecl(Id("e"),[],None),VarDecl(Id("f"),[],None),VarDecl(Id("m"),[],None),VarDecl(Id("n"),[10],None),FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([VarDecl(Id("a"),[],IntLiteral(5))],[While(BinaryOp("!=",Id("a"),IntLiteral(5)),([],[Return(CallExpr(Id("foo"),[BinaryOp("+",FloatLiteral(2.2),BinaryOp("*",Id("a"),CallExpr(Id("foo"),[IntLiteral(2)])))]))])),If([(BinaryOp("||",BinaryOp("==",Id("a"),IntLiteral(2)),BinaryOp("<.",Id("a"),FloatLiteral(5.5))),[],[Assign(Id("x"),IntLiteral(5)),Return(Id("x"))])],([],[Break()])),Break()]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,357))
        
    def test_358(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10];
        Function: foo
        Parameter: n
        Body:
        While a !=5 Do
            Return foo(2.2 + a*foo(2));
        EndWhile.
        If (a == 2) || (a <. 5.5) Then
            x = 5;
            Return x;
        Else Break;
        EndIf.
        Var: a = 5;
        For(i = -2, i != 5, 100) Do
            writeln(a);
            If a == 2 Then
                Return 4;
            EndIf.
        EndFor.
        Return True;
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],IntLiteral(5)),VarDecl(Id("b"),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[],IntLiteral(6)),VarDecl(Id("e"),[],None),VarDecl(Id("f"),[],None),VarDecl(Id("m"),[],None),VarDecl(Id("n"),[10],None),FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([VarDecl(Id("a"),[],IntLiteral(5))],[While(BinaryOp("!=",Id("a"),IntLiteral(5)),([],[Return(CallExpr(Id("foo"),[BinaryOp("+",FloatLiteral(2.2),BinaryOp("*",Id("a"),CallExpr(Id("foo"),[IntLiteral(2)])))]))])),If([(BinaryOp("||",BinaryOp("==",Id("a"),IntLiteral(2)),BinaryOp("<.",Id("a"),FloatLiteral(5.5))),[],[Assign(Id("x"),IntLiteral(5)),Return(Id("x"))])],([],[Break()])),For(Id("i"),UnaryOp("-",2),BinaryOp("!=",Id("i"),IntLiteral(5)),IntLiteral(100),([],[CallStmt(Id("writeln"),[Id("a")]),If([(BinaryOp("==",Id("a"),IntLiteral(2)),[],[Return(IntLiteral(4))])],([],[]))])),Return(BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,358))
        
    def test_359(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10];
        Function: foo
        Parameter: n
        Body:
        Var: a,b,c,d,e,f;
        While a !=5 Do
            Return foo(2.2 + a*foo(2));
        EndWhile.
        If (a == 2) || (a <. 5.5) Then
            x = 5;
            Return x;
        Else Break;
        EndIf.
        Var: a = 5;
        For(i = -2, i != 5, 100) Do
            writeln(a);
            If a == 2 Then
                Return 4;
            EndIf.
        EndFor.
        Return True;
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],IntLiteral(5)),VarDecl(Id("b"),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[],IntLiteral(6)),VarDecl(Id("e"),[],None),VarDecl(Id("f"),[],None),VarDecl(Id("m"),[],None),VarDecl(Id("n"),[10],None),FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[],None),VarDecl(Id("e"),[],None),VarDecl(Id("f"),[],None),VarDecl(Id("a"),[],IntLiteral(5))],[While(BinaryOp("!=",Id("a"),IntLiteral(5)),([],[Return(CallExpr(Id("foo"),[BinaryOp("+",FloatLiteral(2.2),BinaryOp("*",Id("a"),CallExpr(Id("foo"),[IntLiteral(2)])))]))])),If([(BinaryOp("||",BinaryOp("==",Id("a"),IntLiteral(2)),BinaryOp("<.",Id("a"),FloatLiteral(5.5))),[],[Assign(Id("x"),IntLiteral(5)),Return(Id("x"))])],([],[Break()])),For(Id("i"),UnaryOp("-",2),BinaryOp("!=",Id("i"),IntLiteral(5)),IntLiteral(100),([],[CallStmt(Id("writeln"),[Id("a")]),If([(BinaryOp("==",Id("a"),IntLiteral(2)),[],[Return(IntLiteral(4))])],([],[]))])),Return(BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,359))
        
    def test_360(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10];
        Function: foo
        Parameter: t,r,u,o,n,g
        Body:
        Var: a,b,c,d,e,f;
        While a !=5 Do
            Return foo(2.2 + a*foo(2));
        EndWhile.
        If (a == 2) || (a <. 5.5) Then
            x = 5;
            Return x;
        Else Break;
        EndIf.
        Var: a = 5;
        For(i = -2, i != 5, 100) Do
            writeln(a);
            If a == 2 Then
                Return 4;
            EndIf.
        EndFor.
        Return True;
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],IntLiteral(5)),VarDecl(Id("b"),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[],IntLiteral(6)),VarDecl(Id("e"),[],None),VarDecl(Id("f"),[],None),VarDecl(Id("m"),[],None),VarDecl(Id("n"),[10],None),FuncDecl(Id("foo"),[VarDecl(Id("t"),[],None),VarDecl(Id("r"),[],None),VarDecl(Id("u"),[],None),VarDecl(Id("o"),[],None),VarDecl(Id("n"),[],None),VarDecl(Id("g"),[],None)],([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[],None),VarDecl(Id("e"),[],None),VarDecl(Id("f"),[],None),VarDecl(Id("a"),[],IntLiteral(5))],[While(BinaryOp("!=",Id("a"),IntLiteral(5)),([],[Return(CallExpr(Id("foo"),[BinaryOp("+",FloatLiteral(2.2),BinaryOp("*",Id("a"),CallExpr(Id("foo"),[IntLiteral(2)])))]))])),If([(BinaryOp("||",BinaryOp("==",Id("a"),IntLiteral(2)),BinaryOp("<.",Id("a"),FloatLiteral(5.5))),[],[Assign(Id("x"),IntLiteral(5)),Return(Id("x"))])],([],[Break()])),For(Id("i"),UnaryOp("-",2),BinaryOp("!=",Id("i"),IntLiteral(5)),IntLiteral(100),([],[CallStmt(Id("writeln"),[Id("a")]),If([(BinaryOp("==",Id("a"),IntLiteral(2)),[],[Return(IntLiteral(4))])],([],[]))])),Return(BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,360))
        
    def test_361(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10];
        
        Function: foo
        Parameter: t,r,u,o,n,g
        Body:
        Var: a,b,c,d,e,f;
        While a !=5 Do
            Return foo(2.2 + a*foo(2));
        EndWhile.
        If (a == 2) || (a <. 5.5) Then
            x = 5;
            Return x;
        Else 
            Break;
        EndIf.
        Var: a = 5;
        For(i = -2, i != 5, 100) Do
            writeln(a);
            If a == 2 Then
                Return 4;
            EndIf.
        EndFor.
        Return True;
        EndBody.
        Function: main
        Body:
        If a == 5 Then
            a = 2 + foo(3);
            Return;
        ElseIf (a == 6) && (a <=. 10) Then
            a = 2 + foo(3);
        EndIf.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],IntLiteral(5)),VarDecl(Id("b"),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[],IntLiteral(6)),VarDecl(Id("e"),[],None),VarDecl(Id("f"),[],None),VarDecl(Id("m"),[],None),VarDecl(Id("n"),[10],None),FuncDecl(Id("foo"),[VarDecl(Id("t"),[],None),VarDecl(Id("r"),[],None),VarDecl(Id("u"),[],None),VarDecl(Id("o"),[],None),VarDecl(Id("n"),[],None),VarDecl(Id("g"),[],None)],([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[],None),VarDecl(Id("e"),[],None),VarDecl(Id("f"),[],None),VarDecl(Id("a"),[],IntLiteral(5))],[While(BinaryOp("!=",Id("a"),IntLiteral(5)),([],[Return(CallExpr(Id("foo"),[BinaryOp("+",FloatLiteral(2.2),BinaryOp("*",Id("a"),CallExpr(Id("foo"),[IntLiteral(2)])))]))])),If([(BinaryOp("||",BinaryOp("==",Id("a"),IntLiteral(2)),BinaryOp("<.",Id("a"),FloatLiteral(5.5))),[],[Assign(Id("x"),IntLiteral(5)),Return(Id("x"))])],([],[Break()])),For(Id("i"),UnaryOp("-",2),BinaryOp("!=",Id("i"),IntLiteral(5)),IntLiteral(100),([],[CallStmt(Id("writeln"),[Id("a")]),If([(BinaryOp("==",Id("a"),IntLiteral(2)),[],[Return(IntLiteral(4))])],([],[]))])),Return(BooleanLiteral(True))])),FuncDecl(Id("main"),[],([],[If([(BinaryOp("==",Id("a"),IntLiteral(5)),[],[Assign(Id("a"),BinaryOp("+",IntLiteral(2),CallExpr(Id("foo"),[IntLiteral(3)]))),Return(None)]),(BinaryOp("&&",BinaryOp("==",Id("a"),IntLiteral(6)),BinaryOp("<=.",Id("a"),IntLiteral(10))),[],[Assign(Id("a"),BinaryOp("+",IntLiteral(2),CallExpr(Id("foo"),[IntLiteral(3)])))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,361))
        
    def test_362(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10];
        Function: foo
        Parameter: t,r,u,o,n,g
        Body:
        Var: a,b,c,d,e,f;
        While a !=5 Do
            Return foo(2.2 + a*foo(2));
        EndWhile.
        If (a == 2) || (a <. 5.5) Then
            x = 5;
            Return x;
        Else Break;
        EndIf.
        Var: a = 5;
        For(i = -2, i != 5, 100) Do
            writeln(a);
            If a == 2 Then
                Return 4;
            EndIf.
        EndFor.
        Return True;
        EndBody.
        Function: main
        Body:
        If a == 5 Then
            a = 2 + foo(3);
            Return;
        ElseIf (a == 6) && (a <=. 10) Then
            a = 2 + foo(3);
            For(i = -2, i >. 5, 1001) Do
                Var: a = 4;
                a = a -. 2;
            EndFor.
            Break;
        EndIf.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],IntLiteral(5)),VarDecl(Id("b"),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[],IntLiteral(6)),VarDecl(Id("e"),[],None),VarDecl(Id("f"),[],None),VarDecl(Id("m"),[],None),VarDecl(Id("n"),[10],None),FuncDecl(Id("foo"),[VarDecl(Id("t"),[],None),VarDecl(Id("r"),[],None),VarDecl(Id("u"),[],None),VarDecl(Id("o"),[],None),VarDecl(Id("n"),[],None),VarDecl(Id("g"),[],None)],([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[],None),VarDecl(Id("e"),[],None),VarDecl(Id("f"),[],None),VarDecl(Id("a"),[],IntLiteral(5))],[While(BinaryOp("!=",Id("a"),IntLiteral(5)),([],[Return(CallExpr(Id("foo"),[BinaryOp("+",FloatLiteral(2.2),BinaryOp("*",Id("a"),CallExpr(Id("foo"),[IntLiteral(2)])))]))])),If([(BinaryOp("||",BinaryOp("==",Id("a"),IntLiteral(2)),BinaryOp("<.",Id("a"),FloatLiteral(5.5))),[],[Assign(Id("x"),IntLiteral(5)),Return(Id("x"))])],([],[Break()])),For(Id("i"),UnaryOp("-",2),BinaryOp("!=",Id("i"),IntLiteral(5)),IntLiteral(100),([],[CallStmt(Id("writeln"),[Id("a")]),If([(BinaryOp("==",Id("a"),IntLiteral(2)),[],[Return(IntLiteral(4))])],([],[]))])),Return(BooleanLiteral(True))])),FuncDecl(Id("main"),[],([],[If([(BinaryOp("==",Id("a"),IntLiteral(5)),[],[Assign(Id("a"),BinaryOp("+",IntLiteral(2),CallExpr(Id("foo"),[IntLiteral(3)]))),Return(None)]),(BinaryOp("&&",BinaryOp("==",Id("a"),IntLiteral(6)),BinaryOp("<=.",Id("a"),IntLiteral(10))),[],[Assign(Id("a"),BinaryOp("+",IntLiteral(2),CallExpr(Id("foo"),[IntLiteral(3)]))),For(Id("i"),UnaryOp("-",2),BinaryOp(">.",Id("i"),IntLiteral(5)),IntLiteral(1001),([VarDecl(Id("a"),[],IntLiteral(4))],[Assign(Id("a"),BinaryOp("-.",Id("a"),IntLiteral(2)))])),Break()])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,362))
        
    def test_363(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: main
        Body:
        If a == 5 Then
            If a == 4 Then
                If a == 3 Then
                    If a == 2 Then
                        If a == 1 Then
                            print("Happy new year");
                        EndIf.
                    EndIf.
                EndIf.
            EndIf.
        EndIf.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],([],[If([(BinaryOp("==",Id("a"),IntLiteral(5)),[],[If([(BinaryOp("==",Id("a"),IntLiteral(4)),[],[If([(BinaryOp("==",Id("a"),IntLiteral(3)),[],[If([(BinaryOp("==",Id("a"),IntLiteral(2)),[],[If([(BinaryOp("==",Id("a"),IntLiteral(1)),[],[CallStmt(Id("print"),[StringLiteral("Happy new year")])])],([],[]))])],([],[]))])],([],[]))])],([],[]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,363))
        
    def test_364(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: main
        Body:
        If a == 5 Then
            While a < 5 Do
                Var: a = 2, b = 4, c = 5;
                Var: z = 0;
                z = a + b + c + foo(2);
                Return z;
            EndWhile.
        EndIf.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],([],[If([(BinaryOp("==",Id("a"),IntLiteral(5)),[],[While(BinaryOp("<",Id("a"),IntLiteral(5)),([VarDecl(Id("a"),[],IntLiteral(2)),VarDecl(Id("b"),[],IntLiteral(4)),VarDecl(Id("c"),[],IntLiteral(5)),VarDecl(Id("z"),[],IntLiteral(0))],[Assign(Id("z"),BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("a"),Id("b")),Id("c")),CallExpr(Id("foo"),[IntLiteral(2)]))),Return(Id("z"))]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,364))
        
    def test_365(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: main
        Body:
        If a == 5 Then
            While a < 5 Do
                Var: a = 2, b = 4, c = 5;
                Var: z = 0;
                z = a + b + c + foo(2);
                Return z;
            EndWhile.
            Var: q = 1, a[2][3] = {1, 2, {2,3}};
        EndIf.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],([],[If([(BinaryOp("==",Id("a"),IntLiteral(5)),[VarDecl(Id("q"),[],IntLiteral(1)),VarDecl(Id("a"),[2,3],ArrayLiteral([IntLiteral(1),IntLiteral(2),ArrayLiteral([IntLiteral(2),IntLiteral(3)])]))],[While(BinaryOp("<",Id("a"),IntLiteral(5)),([VarDecl(Id("a"),[],IntLiteral(2)),VarDecl(Id("b"),[],IntLiteral(4)),VarDecl(Id("c"),[],IntLiteral(5)),VarDecl(Id("z"),[],IntLiteral(0))],[Assign(Id("z"),BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("a"),Id("b")),Id("c")),CallExpr(Id("foo"),[IntLiteral(2)]))),Return(Id("z"))]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,365))
        
    def test_366(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: main
        Body:
        If a == 5 Then
            While a < 5 Do
                Var: a = 2, b = 4, c = 5;
                Var: z = 0;
                z = a + b + c + foo(2);
                Return z;
            EndWhile.
            Var: q = 1, a[2][3] = {1, 2, {2,3}};
            If q == 1 Then
                Continue;
            Else foo(2);
            EndIf.
        EndIf.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],([],[If([(BinaryOp("==",Id("a"),IntLiteral(5)),[VarDecl(Id("q"),[],IntLiteral(1)),VarDecl(Id("a"),[2,3],ArrayLiteral([IntLiteral(1),IntLiteral(2),ArrayLiteral([IntLiteral(2),IntLiteral(3)])]))],[While(BinaryOp("<",Id("a"),IntLiteral(5)),([VarDecl(Id("a"),[],IntLiteral(2)),VarDecl(Id("b"),[],IntLiteral(4)),VarDecl(Id("c"),[],IntLiteral(5)),VarDecl(Id("z"),[],IntLiteral(0))],[Assign(Id("z"),BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("a"),Id("b")),Id("c")),CallExpr(Id("foo"),[IntLiteral(2)]))),Return(Id("z"))])),If([(BinaryOp("==",Id("q"),IntLiteral(1)),[],[Continue()])],([],[CallStmt(Id("foo"),[IntLiteral(2)])]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,366))
        
    def test_367(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: main
        Body:
        If a == 5 Then
            While a < 5 Do
                Var: a = 2, b = 4, c = 5;
                Var: z = 0;
                z = a + b + c + foo(2);
                Return z;
            EndWhile.
            Var: q = 1, a[2][3] = {1, 2, {2,3}};
            If q == 1 Then
                Continue;
            Else foo(2);
            EndIf.
            Return True;
        EndIf.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],([],[If([(BinaryOp("==",Id("a"),IntLiteral(5)),[VarDecl(Id("q"),[],IntLiteral(1)),VarDecl(Id("a"),[2,3],ArrayLiteral([IntLiteral(1),IntLiteral(2),ArrayLiteral([IntLiteral(2),IntLiteral(3)])]))],[While(BinaryOp("<",Id("a"),IntLiteral(5)),([VarDecl(Id("a"),[],IntLiteral(2)),VarDecl(Id("b"),[],IntLiteral(4)),VarDecl(Id("c"),[],IntLiteral(5)),VarDecl(Id("z"),[],IntLiteral(0))],[Assign(Id("z"),BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("a"),Id("b")),Id("c")),CallExpr(Id("foo"),[IntLiteral(2)]))),Return(Id("z"))])),If([(BinaryOp("==",Id("q"),IntLiteral(1)),[],[Continue()])],([],[CallStmt(Id("foo"),[IntLiteral(2)])])),Return(BooleanLiteral(True))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,367))
        
    def test_368(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: main
        Body:
        If a == 5 Then
            While a < 5 Do
                Var: a = 2, b = 4, c = 5;
                Var: z = 0;
                z = a + b + c + foo(2);
                Return z;
            EndWhile.
            Var: q = 1, a[2][3] = {1, 2, {2,3}};
            If q == 1 Then
                Continue;
            Else foo(2);
            EndIf.
            Return False;
        EndIf.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],([],[If([(BinaryOp("==",Id("a"),IntLiteral(5)),[VarDecl(Id("q"),[],IntLiteral(1)),VarDecl(Id("a"),[2,3],ArrayLiteral([IntLiteral(1),IntLiteral(2),ArrayLiteral([IntLiteral(2),IntLiteral(3)])]))],[While(BinaryOp("<",Id("a"),IntLiteral(5)),([VarDecl(Id("a"),[],IntLiteral(2)),VarDecl(Id("b"),[],IntLiteral(4)),VarDecl(Id("c"),[],IntLiteral(5)),VarDecl(Id("z"),[],IntLiteral(0))],[Assign(Id("z"),BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("a"),Id("b")),Id("c")),CallExpr(Id("foo"),[IntLiteral(2)]))),Return(Id("z"))])),If([(BinaryOp("==",Id("q"),IntLiteral(1)),[],[Continue()])],([],[CallStmt(Id("foo"),[IntLiteral(2)])])),Return(BooleanLiteral(False))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,368))
        
    def test_369(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: main
        Body:
        If (a == 5) || (a >= 4) Then
            Break;
        EndIf.
        Do 
            Var: str = "TRUONG DEP TRAI"; **COMMENT ALL RIGHT**
            print(str);
        While True
        EndDo.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],([],[If([(BinaryOp("||",BinaryOp("==",Id("a"),IntLiteral(5)),BinaryOp(">=",Id("a"),IntLiteral(4))),[],[Break()])],([],[])),Dowhile(([VarDecl(Id("str"),[],StringLiteral("TRUONG DEP TRAI"))],[CallStmt(Id("print"),[Id("str")])]),BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,369))
        
    def test_370(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: main
        Body:
        If (a == 5) || (a >= 4) Then
            Break;
        EndIf.
        Do 
            Var: str = "TRUONG DEP TRAI"; **COMMENT ALL RIGHT**
            print(str);
            Var: a = True, b, c = False;
            Return a;
        While True
        EndDo.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],([],[If([(BinaryOp("||",BinaryOp("==",Id("a"),IntLiteral(5)),BinaryOp(">=",Id("a"),IntLiteral(4))),[],[Break()])],([],[])),Dowhile(([VarDecl(Id("str"),[],StringLiteral("TRUONG DEP TRAI")),VarDecl(Id("a"),[],BooleanLiteral(True)),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],BooleanLiteral(False))],[CallStmt(Id("print"),[Id("str")]),Return(Id("a"))]),BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,370))
        
    def test_371(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: main
        Body:
        EndBody.

        Function: main2
        Body:
        EndBody.

        Function: main3
        Body:
        EndBody.

        Function: main4
        Body:
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],([],[])),FuncDecl(Id("main2"),[],([],[])),FuncDecl(Id("main3"),[],([],[])),FuncDecl(Id("main4"),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,371))
        
    def test_372(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: main
        Body:
        Var: a = 3;
        EndBody.

        Function: main2
        Body:
        Return 0;
        EndBody.

        Function: main3
        Body:
        Break;
        EndBody.

        Function: main4
        Body:
            Continue;
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],IntLiteral(3))],[])),FuncDecl(Id("main2"),[],([],[Return(IntLiteral(0))])),FuncDecl(Id("main3"),[],([],[Break()])),FuncDecl(Id("main4"),[],([],[Continue()]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,372))
        
    def test_373(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: main
        Body:
        Var: a = 3;
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],IntLiteral(3))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,373))
        
    def test_374(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: main
        Body:
        Var: a = 3;
        x[2 + 3*.foor(2)] = a + foo(123)*a_2; 
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],IntLiteral(3))],[Assign(ArrayCell(Id("x"),[BinaryOp("+",IntLiteral(2),BinaryOp("*.",IntLiteral(3),CallExpr(Id("foor"),[IntLiteral(2)])))]),BinaryOp("+",Id("a"),BinaryOp("*",CallExpr(Id("foo"),[IntLiteral(123)]),Id("a_2"))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,374))
        
    def test_375(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: main
        Body:
        Var: a = 3;
        x[2 + 3*.foor(2)] = a + foo(123)*a_2; 
        Var: a = True;
        If a == 2 Then
            Do 
                a = foo(2);
            While a < 2
            EndDo.
        EndIf.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],IntLiteral(3)),VarDecl(Id("a"),[],BooleanLiteral(True))],[Assign(ArrayCell(Id("x"),[BinaryOp("+",IntLiteral(2),BinaryOp("*.",IntLiteral(3),CallExpr(Id("foor"),[IntLiteral(2)])))]),BinaryOp("+",Id("a"),BinaryOp("*",CallExpr(Id("foo"),[IntLiteral(123)]),Id("a_2")))),If([(BinaryOp("==",Id("a"),IntLiteral(2)),[],[Dowhile(([],[Assign(Id("a"),CallExpr(Id("foo"),[IntLiteral(2)]))]),BinaryOp("<",Id("a"),IntLiteral(2)))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,375))
        
    def test_376(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: main
        Body:
        Var: a = 3;
        x[2 + 3*.foor(2)] = a + foo(123)*a_2; 
        Var: a = True;
        If a == 2 Then
            Do 
                a = foo(2);
            While a < 2
            EndDo.
        Else Return aaaaa_123;
        EndIf.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],IntLiteral(3)),VarDecl(Id("a"),[],BooleanLiteral(True))],[Assign(ArrayCell(Id("x"),[BinaryOp("+",IntLiteral(2),BinaryOp("*.",IntLiteral(3),CallExpr(Id("foor"),[IntLiteral(2)])))]),BinaryOp("+",Id("a"),BinaryOp("*",CallExpr(Id("foo"),[IntLiteral(123)]),Id("a_2")))),If([(BinaryOp("==",Id("a"),IntLiteral(2)),[],[Dowhile(([],[Assign(Id("a"),CallExpr(Id("foo"),[IntLiteral(2)]))]),BinaryOp("<",Id("a"),IntLiteral(2)))])],([],[Return(Id("aaaaa_123"))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,376))
        
    def test_377(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: main
        Body:
        Var: a = 3;
        x[2 + 3*.foor(2)] = a + foo(123)*a_2; 
        Var: a = True;
        If a == 2 Then
            Do 
                a = foo(2);
            While a < 2
            EndDo.
        ElseIf a <. 3 Then
            While a != 4 Do
                For(i = 2, i <=. 5.5, 1) Do
                    a = a + 1;
                EndFor.
            EndWhile.
        Else Return aaaaa_123;
        EndIf.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],IntLiteral(3)),VarDecl(Id("a"),[],BooleanLiteral(True))],[Assign(ArrayCell(Id("x"),[BinaryOp("+",IntLiteral(2),BinaryOp("*.",IntLiteral(3),CallExpr(Id("foor"),[IntLiteral(2)])))]),BinaryOp("+",Id("a"),BinaryOp("*",CallExpr(Id("foo"),[IntLiteral(123)]),Id("a_2")))),If([(BinaryOp("==",Id("a"),IntLiteral(2)),[],[Dowhile(([],[Assign(Id("a"),CallExpr(Id("foo"),[IntLiteral(2)]))]),BinaryOp("<",Id("a"),IntLiteral(2)))]),(BinaryOp("<.",Id("a"),IntLiteral(3)),[],[While(BinaryOp("!=",Id("a"),IntLiteral(4)),([],[For(Id("i"),IntLiteral(2),BinaryOp("<=.",Id("i"),FloatLiteral(5.5)),IntLiteral(1),([],[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))]))]))])],([],[Return(Id("aaaaa_123"))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,377))
        
    def test_378(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: main
        Body:
        Var: a = 3;
        x[2 + 3*.foor(2)] = a + foo(123)*a_2; 
        Var: a = True;
        If a == 2 Then
            Do 
                a = foo(2);
            While a < 2
            EndDo.
        ElseIf a <. 3 Then
            While a != 4 Do
                For(i = 2, i <=. 5.5, 1) Do
                    a = a + 1;
                EndFor.
            EndWhile.
        Else
            Var: a = 5; 
            Return aaaaa_123;
        EndIf.
        Break;
        
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],IntLiteral(3)),VarDecl(Id("a"),[],BooleanLiteral(True))],[Assign(ArrayCell(Id("x"),[BinaryOp("+",IntLiteral(2),BinaryOp("*.",IntLiteral(3),CallExpr(Id("foor"),[IntLiteral(2)])))]),BinaryOp("+",Id("a"),BinaryOp("*",CallExpr(Id("foo"),[IntLiteral(123)]),Id("a_2")))),If([(BinaryOp("==",Id("a"),IntLiteral(2)),[],[Dowhile(([],[Assign(Id("a"),CallExpr(Id("foo"),[IntLiteral(2)]))]),BinaryOp("<",Id("a"),IntLiteral(2)))]),(BinaryOp("<.",Id("a"),IntLiteral(3)),[],[While(BinaryOp("!=",Id("a"),IntLiteral(4)),([],[For(Id("i"),IntLiteral(2),BinaryOp("<=.",Id("i"),FloatLiteral(5.5)),IntLiteral(1),([],[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))]))]))])],([VarDecl(Id("a"),[],IntLiteral(5))],[Return(Id("aaaaa_123"))])),Break()]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,378))
        
    def test_379(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: main
        Body:
            If a == "Truog" Then
                Return a;
            EndIf.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],([],[If([(BinaryOp("==",Id("a"),StringLiteral("Truog")),[],[Return(Id("a"))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,379))
        
    def test_380(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: main
        Body:
            If a == 123.123 Then
                Return a;
            EndIf.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],([],[If([(BinaryOp("==",Id("a"),FloatLiteral(123.123)),[],[Return(Id("a"))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,380))
        
    def test_381(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: main
        Body:
            If a == -123.123 Then
                Return a;
            EndIf.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],([],[If([(BinaryOp("==",Id("a"),UnaryOp("-",FloatLiteral(123.123))),[],[Return(Id("a"))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,381))
        
    def test_382(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: main
        Body:
            If a == int_of_string("12") Then
                Return a;
            EndIf.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],([],[If([(BinaryOp("==",Id("a"),CallExpr(Id("int_of_string"),[StringLiteral("12")])),[],[Return(Id("a"))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,382))
        
    def test_383(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: main
        Body:
            If a == int_of_string(read()) Then
                Return a;
            EndIf.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],([],[If([(BinaryOp("==",Id("a"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),[],[Return(Id("a"))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,383))
        
    def test_384(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: main
        Body:
            If a == int_of_string(read()) Then
                Return a;
            EndIf.
            Var: a = 2, b[2] = {2,3,4,55,12.3};
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],IntLiteral(2)),VarDecl(Id("b"),[2],ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(55),FloatLiteral(12.3)]))],[If([(BinaryOp("==",Id("a"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),[],[Return(Id("a"))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,384))
        
    def test_385(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: main
        Body:
            Var: x = -2;
            Var: a = 2, b[2] = {2,3,4,55,12.3, True, False, "Truong"};
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],UnaryOp("-",IntLiteral(2))),VarDecl(Id("a"),[],IntLiteral(2)),VarDecl(Id("b"),[2],ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(55),FloatLiteral(12.3),BooleanLiteral(True),BooleanLiteral(False),StringLiteral("Truong")]))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,385))
        
    def test_386(self):
        """Created automatically"""
        input = r"""
        Var: x = -2.3, u = True, u_123_ASS = 5;
        Function: main
        Body:
            Var: x = -2;
            Var: a = 2, b[2] = {2,3,4,55,12.3, True, False, "Truong"};
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],UnaryOp("-",FloatLiteral(2.3))),VarDecl(Id("u"),[],BooleanLiteral(True)),VarDecl(Id("u_123_ASS"),[],IntLiteral(5)),FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],UnaryOp("-",IntLiteral(2))),VarDecl(Id("a"),[],IntLiteral(2)),VarDecl(Id("b"),[2],ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(55),FloatLiteral(12.3),BooleanLiteral(True),BooleanLiteral(False),StringLiteral("Truong")]))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,386))
        
    def test_387(self):
        """Created automatically"""
        input = r"""
        Var: x = -2.3, u = True, u_123_ASS = 5;
        Var: a[2] = {2,4,{2,3}};
        Function: main
        Body:
            Var: x = -2;
            Var: a = 2, b[2] = {2,3,4,55,12.3, True, False, "Truong"};
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],UnaryOp("-",FloatLiteral(2.3))),VarDecl(Id("u"),[],BooleanLiteral(True)),VarDecl(Id("u_123_ASS"),[],IntLiteral(5)),VarDecl(Id("a"),[2],ArrayLiteral([IntLiteral(2),IntLiteral(4),ArrayLiteral([IntLiteral(2),IntLiteral(3)])])),FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],UnaryOp("-",IntLiteral(2))),VarDecl(Id("a"),[],IntLiteral(2)),VarDecl(Id("b"),[2],ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(55),FloatLiteral(12.3),BooleanLiteral(True),BooleanLiteral(False),StringLiteral("Truong")]))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,387))
        
    def test_388(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: main
        Parameter: a , b[2][2]
        Body:
            Var: x = -2;
            Var: a = 2, b[2] = {2,3,4,55,12.3, True, False, "Truong"};
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2,2],None)],([VarDecl(Id("x"),[],UnaryOp("-",IntLiteral(2))),VarDecl(Id("a"),[],IntLiteral(2)),VarDecl(Id("b"),[2],ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(55),FloatLiteral(12.3),BooleanLiteral(True),BooleanLiteral(False),StringLiteral("Truong")]))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,388))
        
    def test_389(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: main
        Parameter: a , b[2][2]
        Body:
            If a >= 5 Then
                Return;
            ElseIf a <=5 Then
                Var: a = 5;
                Break;
            Else
                While a >= 5 Do
                    Var: a = 5;
                    Return 5;
                EndWhile.
                Var: a = 5;
            EndIf.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2,2],None)],([],[If([(BinaryOp(">=",Id("a"),IntLiteral(5)),[],[Return(None)]),(BinaryOp("<=",Id("a"),IntLiteral(5)),[VarDecl(Id("a"),[],IntLiteral(5))],[Break()])],([VarDecl(Id("a"),[],IntLiteral(5))],[While(BinaryOp(">=",Id("a"),IntLiteral(5)),([VarDecl(Id("a"),[],IntLiteral(5))],[Return(IntLiteral(5))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,389))
        
    def test_390(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: main
        Parameter: a , b[2][2]
        Body:
            If a >= 5 Then
                Return;
            ElseIf a <=5 Then
                Var: a = 5;
                Break;
            Else
                While a >= 5 Do
                    Var: a = 5;
                    Return 5;
                EndWhile.
                Var: a = 5;
            EndIf.
            For (a = 5, a == 2, 10) Do
                print("Truong");
                Var: a[2][3] = {2, True, {2,"Truong"}};
                Return True;
            EndFor.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2,2],None)],([],[If([(BinaryOp(">=",Id("a"),IntLiteral(5)),[],[Return(None)]),(BinaryOp("<=",Id("a"),IntLiteral(5)),[VarDecl(Id("a"),[],IntLiteral(5))],[Break()])],([VarDecl(Id("a"),[],IntLiteral(5))],[While(BinaryOp(">=",Id("a"),IntLiteral(5)),([VarDecl(Id("a"),[],IntLiteral(5))],[Return(IntLiteral(5))]))])),For(Id("a"),IntLiteral(5),BinaryOp("==",Id("a"),IntLiteral(2)),IntLiteral(10),([VarDecl(Id("a"),[2,3],ArrayLiteral([IntLiteral(2),BooleanLiteral(True),ArrayLiteral([IntLiteral(2),StringLiteral("Truong")])]))],[CallStmt(Id("print"),[StringLiteral("Truong")]),Return(BooleanLiteral(True))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,390))
        
    def test_391(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: main
        Parameter: a , b[2][2]
        Body:
            If a >= 5 Then
                Return;
            ElseIf a <=5 Then
                Var: a = 5;
                Break;
            Else
                While a >= 5 Do
                    Var: a = 5;
                    Return 5;
                EndWhile.
                Var: a = 5;
            EndIf.
            For (a = 5, a == 2, 10) Do
                print("Truong");
                Var: a[2][3] = {2, True, {2,"Truong"}};
                Return True;
            EndFor.
            Var: a = 5;
            While a == 2 Do
                If (a != 2) || (a == 2) && (a <= 2) Then
                    print("Truong");
                    Return False;
                ElseIf a == 2 Then
                    Return x + foo(2);    
                EndIf.
            EndWhile.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2,2],None)],([VarDecl(Id("a"),[],IntLiteral(5))],[If([(BinaryOp(">=",Id("a"),IntLiteral(5)),[],[Return(None)]),(BinaryOp("<=",Id("a"),IntLiteral(5)),[VarDecl(Id("a"),[],IntLiteral(5))],[Break()])],([VarDecl(Id("a"),[],IntLiteral(5))],[While(BinaryOp(">=",Id("a"),IntLiteral(5)),([VarDecl(Id("a"),[],IntLiteral(5))],[Return(IntLiteral(5))]))])),For(Id("a"),IntLiteral(5),BinaryOp("==",Id("a"),IntLiteral(2)),IntLiteral(10),([VarDecl(Id("a"),[2,3],ArrayLiteral([IntLiteral(2),BooleanLiteral(True),ArrayLiteral([IntLiteral(2),StringLiteral("Truong")])]))],[CallStmt(Id("print"),[StringLiteral("Truong")]),Return(BooleanLiteral(True))])),While(BinaryOp("==",Id("a"),IntLiteral(2)),([],[If([(BinaryOp("&&",BinaryOp("||",BinaryOp("!=",Id("a"),IntLiteral(2)),BinaryOp("==",Id("a"),IntLiteral(2))),BinaryOp("<=",Id("a"),IntLiteral(2))),[],[CallStmt(Id("print"),[StringLiteral("Truong")]),Return(BooleanLiteral(False))]),(BinaryOp("==",Id("a"),IntLiteral(2)),[],[Return(BinaryOp("+",Id("x"),CallExpr(Id("foo"),[IntLiteral(2)])))])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,391))
        
    def test_392(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: foo
        Body:
            Var: a = 5;
            Var: b, c, d[2];
            Return a;
        EndBody.
        Function: main
        Parameter: a , b[2][2]
        Body:
            If a >= 5 Then
                Return;
            ElseIf a <=5 Then
                Var: a = 5;
                Break;
            Else
                While a >= 5 Do
                    Var: a = 5;
                    Return 5;
                EndWhile.
                Var: a = 5;
            EndIf.
            For (a = 5, a == 2, 10) Do
                print("Truong");
                Var: a[2][3] = {2, True, {2,"Truong"}};
                Return True;
            EndFor.
            Var: a = 5;
            While a == 2 Do
                If (a != 2) || (a == 2) && (a <= 2) Then
                    print("Truong");
                    Return False;
                ElseIf a == 2 Then
                    Return x + foo(2);    
                EndIf.
            EndWhile.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("foo"),[],([VarDecl(Id("a"),[],IntLiteral(5)),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[2],None)],[Return(Id("a"))])),FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2,2],None)],([VarDecl(Id("a"),[],IntLiteral(5))],[If([(BinaryOp(">=",Id("a"),IntLiteral(5)),[],[Return(None)]),(BinaryOp("<=",Id("a"),IntLiteral(5)),[VarDecl(Id("a"),[],IntLiteral(5))],[Break()])],([VarDecl(Id("a"),[],IntLiteral(5))],[While(BinaryOp(">=",Id("a"),IntLiteral(5)),([VarDecl(Id("a"),[],IntLiteral(5))],[Return(IntLiteral(5))]))])),For(Id("a"),IntLiteral(5),BinaryOp("==",Id("a"),IntLiteral(2)),IntLiteral(10),([VarDecl(Id("a"),[2,3],ArrayLiteral([IntLiteral(2),BooleanLiteral(True),ArrayLiteral([IntLiteral(2),StringLiteral("Truong")])]))],[CallStmt(Id("print"),[StringLiteral("Truong")]),Return(BooleanLiteral(True))])),While(BinaryOp("==",Id("a"),IntLiteral(2)),([],[If([(BinaryOp("&&",BinaryOp("||",BinaryOp("!=",Id("a"),IntLiteral(2)),BinaryOp("==",Id("a"),IntLiteral(2))),BinaryOp("<=",Id("a"),IntLiteral(2))),[],[CallStmt(Id("print"),[StringLiteral("Truong")]),Return(BooleanLiteral(False))]),(BinaryOp("==",Id("a"),IntLiteral(2)),[],[Return(BinaryOp("+",Id("x"),CallExpr(Id("foo"),[IntLiteral(2)])))])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,392))
        
    def test_393(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: foo
        Body:
            Var: a = 5;
            Var: b, c, d[2];
            If a =/= 5 Then
                Return True;
            EndIf.
            Return a;
        EndBody.
        Function: main
        Parameter: a , b[2][2]
        Body:
            If a >= 5 Then
                Return;
            ElseIf a <=5 Then
                Var: a = 5;
                Break;
            Else
                While a >= 5 Do
                    Var: a = 5;
                    Return 5;
                EndWhile.
                Var: a = 5;
            EndIf.
            For (a = 5, a == 2, 10) Do
                print("Truong");
                Var: a[2][3] = {2, True, {2,"Truong"}};
                Return True;
            EndFor.
            Var: a = 5;
            While a == 2 Do
                If (a != 2) || (a == 2) && (a <= 2) Then
                    print("Truong");
                    Return False;
                ElseIf a == 2 Then
                    Return x + foo(2);    
                EndIf.
            EndWhile.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("foo"),[],([VarDecl(Id("a"),[],IntLiteral(5)),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[2],None)],[If([(BinaryOp("=/=",Id("a"),IntLiteral(5)),[],[Return(BooleanLiteral(True))])],([],[])),Return(Id("a"))])),FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2,2],None)],([VarDecl(Id("a"),[],IntLiteral(5))],[If([(BinaryOp(">=",Id("a"),IntLiteral(5)),[],[Return(None)]),(BinaryOp("<=",Id("a"),IntLiteral(5)),[VarDecl(Id("a"),[],IntLiteral(5))],[Break()])],([VarDecl(Id("a"),[],IntLiteral(5))],[While(BinaryOp(">=",Id("a"),IntLiteral(5)),([VarDecl(Id("a"),[],IntLiteral(5))],[Return(IntLiteral(5))]))])),For(Id("a"),IntLiteral(5),BinaryOp("==",Id("a"),IntLiteral(2)),IntLiteral(10),([VarDecl(Id("a"),[2,3],ArrayLiteral([IntLiteral(2),BooleanLiteral(True),ArrayLiteral([IntLiteral(2),StringLiteral("Truong")])]))],[CallStmt(Id("print"),[StringLiteral("Truong")]),Return(BooleanLiteral(True))])),While(BinaryOp("==",Id("a"),IntLiteral(2)),([],[If([(BinaryOp("&&",BinaryOp("||",BinaryOp("!=",Id("a"),IntLiteral(2)),BinaryOp("==",Id("a"),IntLiteral(2))),BinaryOp("<=",Id("a"),IntLiteral(2))),[],[CallStmt(Id("print"),[StringLiteral("Truong")]),Return(BooleanLiteral(False))]),(BinaryOp("==",Id("a"),IntLiteral(2)),[],[Return(BinaryOp("+",Id("x"),CallExpr(Id("foo"),[IntLiteral(2)])))])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,393))
        
    def test_394(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: foo
        Body:
            Var: a = 5;
            Var: b, c, d[2];
            If a =/= 5 Then
                Var: a = 5;
                a = a *2 + 3 -. 4 + (2.2 + 1) + foo(x + 2*a);
                Return True;
            EndIf.
            Return a;
        EndBody.
        Function: main
        Parameter: a , b[2][2]
        Body:
            If a >= 5 Then
                Return;
            ElseIf a <=5 Then
                Var: a = 5;
                Break;
            Else
                While a >= 5 Do
                    Var: a = 5;
                    Return 5;
                EndWhile.
                Var: a = 5;
            EndIf.
            For (a = 5, a == 2, 10) Do
                print("Truong");
                Var: a[2][3] = {2, True, {2,"Truong"}};
                Return True;
            EndFor.
            Var: a = 5;
            While a == 2 Do
                If (a != 2) || (a == 2) && (a <= 2) Then
                    print("Truong");
                    Return False;
                ElseIf a == 2 Then
                    Return x + foo(2);    
                EndIf.
            EndWhile.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("foo"),[],([VarDecl(Id("a"),[],IntLiteral(5)),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[2],None)],[If([(BinaryOp("=/=",Id("a"),IntLiteral(5)),[VarDecl(Id("a"),[],IntLiteral(5))],[Assign(Id("a"),BinaryOp("+",BinaryOp("+",BinaryOp("-.",BinaryOp("+",BinaryOp("*",Id("a"),IntLiteral(2)),IntLiteral(3)),IntLiteral(4)),BinaryOp("+",FloatLiteral(2.2),IntLiteral(1))),CallExpr(Id("foo"),[BinaryOp("+",Id("x"),BinaryOp("*",IntLiteral(2),Id("a")))]))),Return(BooleanLiteral(True))])],([],[])),Return(Id("a"))])),FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2,2],None)],([VarDecl(Id("a"),[],IntLiteral(5))],[If([(BinaryOp(">=",Id("a"),IntLiteral(5)),[],[Return(None)]),(BinaryOp("<=",Id("a"),IntLiteral(5)),[VarDecl(Id("a"),[],IntLiteral(5))],[Break()])],([VarDecl(Id("a"),[],IntLiteral(5))],[While(BinaryOp(">=",Id("a"),IntLiteral(5)),([VarDecl(Id("a"),[],IntLiteral(5))],[Return(IntLiteral(5))]))])),For(Id("a"),IntLiteral(5),BinaryOp("==",Id("a"),IntLiteral(2)),IntLiteral(10),([VarDecl(Id("a"),[2,3],ArrayLiteral([IntLiteral(2),BooleanLiteral(True),ArrayLiteral([IntLiteral(2),StringLiteral("Truong")])]))],[CallStmt(Id("print"),[StringLiteral("Truong")]),Return(BooleanLiteral(True))])),While(BinaryOp("==",Id("a"),IntLiteral(2)),([],[If([(BinaryOp("&&",BinaryOp("||",BinaryOp("!=",Id("a"),IntLiteral(2)),BinaryOp("==",Id("a"),IntLiteral(2))),BinaryOp("<=",Id("a"),IntLiteral(2))),[],[CallStmt(Id("print"),[StringLiteral("Truong")]),Return(BooleanLiteral(False))]),(BinaryOp("==",Id("a"),IntLiteral(2)),[],[Return(BinaryOp("+",Id("x"),CallExpr(Id("foo"),[IntLiteral(2)])))])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,394))
        
    def test_395(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: foo
        Body:
            Var: a = 5;
            Var: b, c, d[2];
            If a =/= 5 Then
                Var: a = 5;
                a = a *2 + 3 -. 4 + (2.2 + 1) + foo(x + 2*a);
                Return True;
            ElseIf a == 4 Then
                a[2 + 3*foo(2)] = arr_123 + arr_456 + 12*.123.123;
            EndIf.
            Return a;
        EndBody.
        Function: main
        Parameter: a , b[2][2]
        Body:
            If a >= 5 Then
                Return;
            ElseIf a <=5 Then
                Var: a = 5;
                Break;
            Else
                While a >= 5 Do
                    Var: a = 5;
                    Return 5;
                EndWhile.
                Var: a = 5;
            EndIf.
            For (a = 5, a == 2, 10) Do
                print("Truong");
                Var: a[2][3] = {2, True, {2,"Truong"}};
                Return True;
            EndFor.
            Var: a = 5;
            While a == 2 Do
                If (a != 2) || (a == 2) && (a <= 2) Then
                    print("Truong");
                    Return False;
                ElseIf a == 2 Then
                    Return x + foo(2);    
                EndIf.
            EndWhile.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("foo"),[],([VarDecl(Id("a"),[],IntLiteral(5)),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[2],None)],[If([(BinaryOp("=/=",Id("a"),IntLiteral(5)),[VarDecl(Id("a"),[],IntLiteral(5))],[Assign(Id("a"),BinaryOp("+",BinaryOp("+",BinaryOp("-.",BinaryOp("+",BinaryOp("*",Id("a"),IntLiteral(2)),IntLiteral(3)),IntLiteral(4)),BinaryOp("+",FloatLiteral(2.2),IntLiteral(1))),CallExpr(Id("foo"),[BinaryOp("+",Id("x"),BinaryOp("*",IntLiteral(2),Id("a")))]))),Return(BooleanLiteral(True))]),(BinaryOp("==",Id("a"),IntLiteral(4)),[],[Assign(ArrayCell(Id("a"),[BinaryOp("+",IntLiteral(2),BinaryOp("*",IntLiteral(3),CallExpr(Id("foo"),[IntLiteral(2)])))]),BinaryOp("+",BinaryOp("+",Id("arr_123"),Id("arr_456")),BinaryOp("*.",IntLiteral(12),FloatLiteral(123.123))))])],([],[])),Return(Id("a"))])),FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2,2],None)],([VarDecl(Id("a"),[],IntLiteral(5))],[If([(BinaryOp(">=",Id("a"),IntLiteral(5)),[],[Return(None)]),(BinaryOp("<=",Id("a"),IntLiteral(5)),[VarDecl(Id("a"),[],IntLiteral(5))],[Break()])],([VarDecl(Id("a"),[],IntLiteral(5))],[While(BinaryOp(">=",Id("a"),IntLiteral(5)),([VarDecl(Id("a"),[],IntLiteral(5))],[Return(IntLiteral(5))]))])),For(Id("a"),IntLiteral(5),BinaryOp("==",Id("a"),IntLiteral(2)),IntLiteral(10),([VarDecl(Id("a"),[2,3],ArrayLiteral([IntLiteral(2),BooleanLiteral(True),ArrayLiteral([IntLiteral(2),StringLiteral("Truong")])]))],[CallStmt(Id("print"),[StringLiteral("Truong")]),Return(BooleanLiteral(True))])),While(BinaryOp("==",Id("a"),IntLiteral(2)),([],[If([(BinaryOp("&&",BinaryOp("||",BinaryOp("!=",Id("a"),IntLiteral(2)),BinaryOp("==",Id("a"),IntLiteral(2))),BinaryOp("<=",Id("a"),IntLiteral(2))),[],[CallStmt(Id("print"),[StringLiteral("Truong")]),Return(BooleanLiteral(False))]),(BinaryOp("==",Id("a"),IntLiteral(2)),[],[Return(BinaryOp("+",Id("x"),CallExpr(Id("foo"),[IntLiteral(2)])))])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,395))
        
    def test_396(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: foo
        Body:
            Var: a = 5;
            Var: b, c, d[2];
            If a =/= 5 Then
                Var: a = 5;
                a = a *2 + 3 -. 4 + (2.2 + 1) + foo(x + 2*a);
                Return True;
            ElseIf a == 4 Then
                a[2 + 3*foo(2)] = arr_123 + arr_456 + 12*.123.123;
            EndIf.
            Return a;
        EndBody.
        Function: main
        Parameter: a , b[2][2]
        Body:
            If a >= 5 Then
                Return;
            ElseIf a <=5 Then
                Var: a = 5;
                Break;
            Else
                While a >= 5 Do
                    Var: a = 5;
                    Return 5;
                EndWhile.
                Var: a = 5;
            EndIf.
            For (a = 5, a == 2, 10) Do
                print("Truong");
                Var: a[2][3] = {2, True, {2,"Truong"}};
                Return True;
            EndFor.
            Var: a = 5;
            While a == 2 Do
                If (a != 2) || (a == 2) && (a <= 2) Then
                    print("Truong");
                    Return False;
                ElseIf a == 2 Then
                    Return x + foo(2);
                EndIf.
            EndWhile.
        EndBody.
        Function: aaaaa_123
        Body:
            Var: a,b,c,d,e,a_123_123 = 123;
            Return a;
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("foo"),[],([VarDecl(Id("a"),[],IntLiteral(5)),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[2],None)],[If([(BinaryOp("=/=",Id("a"),IntLiteral(5)),[VarDecl(Id("a"),[],IntLiteral(5))],[Assign(Id("a"),BinaryOp("+",BinaryOp("+",BinaryOp("-.",BinaryOp("+",BinaryOp("*",Id("a"),IntLiteral(2)),IntLiteral(3)),IntLiteral(4)),BinaryOp("+",FloatLiteral(2.2),IntLiteral(1))),CallExpr(Id("foo"),[BinaryOp("+",Id("x"),BinaryOp("*",IntLiteral(2),Id("a")))]))),Return(BooleanLiteral(True))]),(BinaryOp("==",Id("a"),IntLiteral(4)),[],[Assign(ArrayCell(Id("a"),[BinaryOp("+",IntLiteral(2),BinaryOp("*",IntLiteral(3),CallExpr(Id("foo"),[IntLiteral(2)])))]),BinaryOp("+",BinaryOp("+",Id("arr_123"),Id("arr_456")),BinaryOp("*.",IntLiteral(12),FloatLiteral(123.123))))])],([],[])),Return(Id("a"))])),FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2,2],None)],([VarDecl(Id("a"),[],IntLiteral(5))],[If([(BinaryOp(">=",Id("a"),IntLiteral(5)),[],[Return(None)]),(BinaryOp("<=",Id("a"),IntLiteral(5)),[VarDecl(Id("a"),[],IntLiteral(5))],[Break()])],([VarDecl(Id("a"),[],IntLiteral(5))],[While(BinaryOp(">=",Id("a"),IntLiteral(5)),([VarDecl(Id("a"),[],IntLiteral(5))],[Return(IntLiteral(5))]))])),For(Id("a"),IntLiteral(5),BinaryOp("==",Id("a"),IntLiteral(2)),IntLiteral(10),([VarDecl(Id("a"),[2,3],ArrayLiteral([IntLiteral(2),BooleanLiteral(True),ArrayLiteral([IntLiteral(2),StringLiteral("Truong")])]))],[CallStmt(Id("print"),[StringLiteral("Truong")]),Return(BooleanLiteral(True))])),While(BinaryOp("==",Id("a"),IntLiteral(2)),([],[If([(BinaryOp("&&",BinaryOp("||",BinaryOp("!=",Id("a"),IntLiteral(2)),BinaryOp("==",Id("a"),IntLiteral(2))),BinaryOp("<=",Id("a"),IntLiteral(2))),[],[CallStmt(Id("print"),[StringLiteral("Truong")]),Return(BooleanLiteral(False))]),(BinaryOp("==",Id("a"),IntLiteral(2)),[],[Return(BinaryOp("+",Id("x"),CallExpr(Id("foo"),[IntLiteral(2)])))])],([],[]))]))])),FuncDecl(Id("aaaaa_123"),[],([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[],None),VarDecl(Id("e"),[],None),VarDecl(Id("a_123_123"),[],IntLiteral(123))],[Return(Id("a"))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,396))
        
    def test_397(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;
        Function: main
        Body:
            a[2][3] = (as + a*.123.123) + foo(2 + a);   
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[],([],[Assign(ArrayCell(ArrayCell(Id("a"),[IntLiteral(2)]),[IntLiteral(3)]),BinaryOp("+",BinaryOp("+",Id("as"),BinaryOp("*.",Id("a"),FloatLiteral(123.123))),CallExpr(Id("foo"),[BinaryOp("+",IntLiteral(2),Id("a"))])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,397))
        
    def test_398(self):
        """Created automatically"""
        input = r"""
        Var: a = 5;
        Function: main
        Body:
            a = (a == 2); 
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("==",Id("a"),IntLiteral(2)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,398))
        
    def test_399(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: main
        Body:
            foo1(2);
            foo2(x+ y);
            a = foo3(2);
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],([],[CallStmt(Id("foo1"),[IntLiteral(2)]),CallStmt(Id("foo2"),[BinaryOp("+",Id("x"),Id("y"))]),Assign(Id("a"),CallExpr(Id("foo3"),[IntLiteral(2)]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,399))
        
    def test_400(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: main
        Body:
            foo1(2);
            foo2(x + y);
            a = foo3(2);
            If (a == foo(2)) Then
                Return a;
            EndIf.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],([],[CallStmt(Id("foo1"),[IntLiteral(2)]),CallStmt(Id("foo2"),[BinaryOp("+",Id("x"),Id("y"))]),Assign(Id("a"),CallExpr(Id("foo3"),[IntLiteral(2)])),If([(BinaryOp("==",Id("a"),CallExpr(Id("foo"),[IntLiteral(2)])),[],[Return(Id("a"))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,400))
        
import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_301(self):
        input = """Var:x[2] = {3,2, {2, {2}}}, a = "b", b = True;"""
        expect = Program([VarDecl(Id("x"),[2],ArrayLiteral([IntLiteral(3),IntLiteral(2),ArrayLiteral([IntLiteral(2),ArrayLiteral([IntLiteral(2)])])])),VarDecl(Id("a"),[],StringLiteral("b")),VarDecl(Id("b"),[],BooleanLiteral(True))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test_302(self):
        input = """
        Var:x[2] = {3,2, {2, {2}}}, a = "b", b = True;
        Var:c="string";
        """
        expect = Program([VarDecl(Id("x"),[2],ArrayLiteral([IntLiteral(3),IntLiteral(2),ArrayLiteral([IntLiteral(2),ArrayLiteral([IntLiteral(2)])])])),VarDecl(Id("a"),[],StringLiteral("b")),VarDecl(Id("b"),[],BooleanLiteral(True)),VarDecl(Id("c"),[],StringLiteral("string"))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    def test_303(self):
        """Simple program: int main() {} """
        input = """Var: x;"""
        expect = Program([VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_304(self):
        """Miss variable"""
        input = """Var: a[2];"""
        expect = Program([VarDecl(Id("a"),[2],None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_305(self):
        input = """Var:x[2][2] = {3,2, {2, {2}}}, a = "b";"""
        expect = Program([VarDecl(Id("x"),[2,2],ArrayLiteral([IntLiteral(3),IntLiteral(2),ArrayLiteral([IntLiteral(2),ArrayLiteral([IntLiteral(2)])])])),VarDecl(Id("a"),[],StringLiteral("b"))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test_306(self):
        input = """
        Function: main
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
        expect = Program([FuncDecl(Id("main"),[],([],[If([(CallExpr(Id("bool_of_string"),[StringLiteral("True")]),[],[Assign(Id("a"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),Assign(Id("b"),BinaryOp("+.",CallExpr(Id("float_of_int"),[Id("a")]),FloatLiteral(2.0)))]),(BinaryOp("==",Id("a"),IntLiteral(5)),[],[Assign(Id("a"),BinaryOp("+",Id("a"),CallExpr(Id("main"),[IntLiteral(123)]))),Return(Id("a"))]),(BinaryOp("==",Id("a"),IntLiteral(6)),[],[Assign(Id("a"),BinaryOp("*.",Id("a"),IntLiteral(2))),Break()])],([],[Continue()]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    def test_307(self):
        input = """
        Function: main
        Body:
            If bool_of_string ("True") Then
                a = int_of_string (read ());
                b = float_of_int (a) % 2.0;
            ElseIf a == 5 Then
                a = a \\ main(123);
                Return a;
            ElseIf a == 6 Then
                a = a \\. 2;
                Break;
            Else Continue;
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[If([(CallExpr(Id("bool_of_string"),[StringLiteral("True")]),[],[Assign(Id("a"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),Assign(Id("b"),BinaryOp("%",CallExpr(Id("float_of_int"),[Id("a")]),FloatLiteral(2.0)))]),(BinaryOp("==",Id("a"),IntLiteral(5)),[],[Assign(Id("a"),BinaryOp("\\",Id("a"),CallExpr(Id("main"),[IntLiteral(123)]))),Return(Id("a"))]),(BinaryOp("==",Id("a"),IntLiteral(6)),[],[Assign(Id("a"),BinaryOp("\.",Id("a"),IntLiteral(2))),Break()])],([],[Continue()]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    def test_308(self):
        """function"""
        input = """
        Function: foo
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) Do
                a[i] = b +. 1.0;
                i = i + 1;
            EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("<",Id("i"),IntLiteral(5)),([],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    def test_309(self):
        """function"""
        input = """
        Function: foo
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) Do
                Var: j = 0;
                While (j % 5 == 2) Do
                    a[i] = b +. 1.0;
                    j = j + 1;
                EndWhile.
            EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("<",Id("i"),IntLiteral(5)),([VarDecl(Id("j"),[],IntLiteral(0))],[While(BinaryOp("==",BinaryOp("%",Id("j"),IntLiteral(5)),IntLiteral(2)),([],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("j"),BinaryOp("+",Id("j"),IntLiteral(1)))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    def test_310(self):
        """function"""
        input = """
        Function: foo
        Parameter: a, b
        Body:
            If a > 10 Then
                a = 2;
            EndIf.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([],[If([(BinaryOp(">",Id("a"),IntLiteral(10)),[],[Assign(Id("a"),IntLiteral(2))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    def test_311(self):
        """function"""
        input = """
        Function: foo
        Parameter: a, b
        Body:
            If !(a > 10) Then
                a = 2;
            EndIf.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([],[If([(UnaryOp("!",BinaryOp(">",Id("a"),IntLiteral(10))),[],[Assign(Id("a"),IntLiteral(2))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_312(self):
        """function"""
        input = """
        Function: foo
        Parameter: a, b
        Body:
            If a > 10 Then
                a = 2;
            Else
                a = 3;
            EndIf.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([],[If([(BinaryOp(">",Id("a"),IntLiteral(10)),[],[Assign(Id("a"),IntLiteral(2))])],([],[Assign(Id("a"),IntLiteral(3))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_313(self):
        """function"""
        input = """
        Function: foo
        Parameter: a, b
        Body:
            If a > 10 Then
                a = 2;
            ElseIf b < 10 Then
                a = 15;
            Else
                a = 3;
            EndIf.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([],[If([(BinaryOp(">",Id("a"),IntLiteral(10)),[],[Assign(Id("a"),IntLiteral(2))]),(BinaryOp("<",Id("b"),IntLiteral(10)),[],[Assign(Id("a"),IntLiteral(15))])],([],[Assign(Id("a"),IntLiteral(3))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_314(self):
        """function"""
        input = """
        Function: foo
        Parameter: a, b
        Body:
            If a > 10 Then
                a = 2;
            ElseIf b < 10 Then
                a = 15;
            ElseIf b < 10 Then
                a = 15;
            ElseIf b < 10 Then
                a = 15;
            Else
                a = 3;
            EndIf.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([],[If([(BinaryOp(">",Id("a"),IntLiteral(10)),[],[Assign(Id("a"),IntLiteral(2))]),(BinaryOp("<",Id("b"),IntLiteral(10)),[],[Assign(Id("a"),IntLiteral(15))]),(BinaryOp("<",Id("b"),IntLiteral(10)),[],[Assign(Id("a"),IntLiteral(15))]),(BinaryOp("<",Id("b"),IntLiteral(10)),[],[Assign(Id("a"),IntLiteral(15))])],([],[Assign(Id("a"),IntLiteral(3))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test_315(self):
        """function"""
        input = """
        Function: foo
        Parameter: a, b
        Body:
            If a > 10 Then
                If a > 10 Then
                    a = 2;
                ElseIf b < 10 Then
                    a = 15;
                ElseIf b < 10 Then
                    a = 15;
                ElseIf b < 10 Then
                    a = 15;
                Else
                    a = 3;
                EndIf.
            ElseIf b < 10 Then
                If a > 10 Then
                    a = 2;
                Else
                    a = 3;
                EndIf.
            ElseIf b < 10 Then
                If a > 10 Then
                    a = 2;
                ElseIf b < 10 Then
                    a = 15;
                ElseIf b < 10 Then
                    a = 15;
                ElseIf b < 10 Then
                    a = 15;
                EndIf.
            ElseIf abc > 345 Then
                If (foo(a[a_A[456]],b) == 3) Then a = a - e; EndIf.
            ElseIf b < 10 Then
                a = 15;
            Else
                a = 3;
            EndIf.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([],[If([(BinaryOp(">",Id("a"),IntLiteral(10)),[],[If([(BinaryOp(">",Id("a"),IntLiteral(10)),[],[Assign(Id("a"),IntLiteral(2))]),(BinaryOp("<",Id("b"),IntLiteral(10)),[],[Assign(Id("a"),IntLiteral(15))]),(BinaryOp("<",Id("b"),IntLiteral(10)),[],[Assign(Id("a"),IntLiteral(15))]),(BinaryOp("<",Id("b"),IntLiteral(10)),[],[Assign(Id("a"),IntLiteral(15))])],([],[Assign(Id("a"),IntLiteral(3))]))]),(BinaryOp("<",Id("b"),IntLiteral(10)),[],[If([(BinaryOp(">",Id("a"),IntLiteral(10)),[],[Assign(Id("a"),IntLiteral(2))])],([],[Assign(Id("a"),IntLiteral(3))]))]),(BinaryOp("<",Id("b"),IntLiteral(10)),[],[If([(BinaryOp(">",Id("a"),IntLiteral(10)),[],[Assign(Id("a"),IntLiteral(2))]),(BinaryOp("<",Id("b"),IntLiteral(10)),[],[Assign(Id("a"),IntLiteral(15))]),(BinaryOp("<",Id("b"),IntLiteral(10)),[],[Assign(Id("a"),IntLiteral(15))]),(BinaryOp("<",Id("b"),IntLiteral(10)),[],[Assign(Id("a"),IntLiteral(15))])],([],[]))]),(BinaryOp(">",Id("abc"),IntLiteral(345)),[],[If([(BinaryOp("==",CallExpr(Id("foo"),[ArrayCell(Id("a"),[ArrayCell(Id("a_A"),[IntLiteral(456)])]),Id("b")]),IntLiteral(3)),[],[Assign(Id("a"),BinaryOp("-",Id("a"),Id("e")))])],([],[]))]),(BinaryOp("<",Id("b"),IntLiteral(10)),[],[Assign(Id("a"),IntLiteral(15))])],([],[Assign(Id("a"),IntLiteral(3))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test_316(self):
        input = """
        Function: foo
        Parameter: a, b
        Body:
            Var: i = 0;
            For (i = 10, i >= 0, -1) Do
                a = a + b;
            EndFor.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0))],[For(Id("i"),IntLiteral(10),BinaryOp(">=",Id("i"),IntLiteral(0)),UnaryOp("-",IntLiteral(1)),([],[Assign(Id("a"),BinaryOp("+",Id("a"),Id("b")))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    def test_317(self):
        input = """
        Function: foo
        Parameter: a, b
        Body:
            Var: i = 0,j, a[3] = {1,2,3};
            For (i = 10, i >= 0, -1) Do
                For (j = 0, j < 3, 1) Do
                    a[j] = j*i;
                EndFor.
            EndFor.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0)),VarDecl(Id("j"),[],None),VarDecl(Id("a"),[3],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))],[For(Id("i"),IntLiteral(10),BinaryOp(">=",Id("i"),IntLiteral(0)),UnaryOp("-",IntLiteral(1)),([],[For(Id("j"),IntLiteral(0),BinaryOp("<",Id("j"),IntLiteral(3)),IntLiteral(1),([],[Assign(ArrayCell(Id("a"),[Id("j")]),BinaryOp("*",Id("j"),Id("i")))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test_318(self):
        input = """
        Function: foo
        Body:
            a = 6;
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(Id("a"),IntLiteral(6))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test_319(self):
        input = """
        Function: foo
        Body:
            While (x+y > x-y) Do
                If (x*y % 2) Then
                    Break;
                EndIf.
            EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[While(BinaryOp(">",BinaryOp("+",Id("x"),Id("y")),BinaryOp("-",Id("x"),Id("y"))),([],[If([(BinaryOp("%",BinaryOp("*",Id("x"),Id("y")),IntLiteral(2)),[],[Break()])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    def test_320(self):
        input = """
        Function: foo
        Parameter: a, b
        Body:
            Var: i = 0,j, a[3] = {1,2,3};
            For (i = 10, i >= 0, -1) Do
                For (j = 0, j < 3, 1) Do
                    If (i==j) Then Break; EndIf.
                    a[j] = j*i;
                EndFor.
            EndFor.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0)),VarDecl(Id("j"),[],None),VarDecl(Id("a"),[3],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))],[For(Id("i"),IntLiteral(10),BinaryOp(">=",Id("i"),IntLiteral(0)),UnaryOp("-",IntLiteral(1)),([],[For(Id("j"),IntLiteral(0),BinaryOp("<",Id("j"),IntLiteral(3)),IntLiteral(1),([],[If([(BinaryOp("==",Id("i"),Id("j")),[],[Break()])],([],[])),Assign(ArrayCell(Id("a"),[Id("j")]),BinaryOp("*",Id("j"),Id("i")))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test_321(self):
        input = """
        Function: foo
        Body:
            While (x+y > x-y) Do
                If (x*y % 2) Then
                    Continue;
                EndIf.
                x = x+1;
            EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[While(BinaryOp(">",BinaryOp("+",Id("x"),Id("y")),BinaryOp("-",Id("x"),Id("y"))),([],[If([(BinaryOp("%",BinaryOp("*",Id("x"),Id("y")),IntLiteral(2)),[],[Continue()])],([],[])),Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test_322(self):
        input = """
        Function: foo
        Parameter: a, b
        Body:
            Var: i = 0,j, a[3] = {1,2,3};
            For (i = 10, i >= 0, -1) Do
                For (j = 0, j < 3, 1) Do
                    If (i==j) Then Continue; EndIf.
                    a[j] = j*i;
                EndFor.
            EndFor.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0)),VarDecl(Id("j"),[],None),VarDecl(Id("a"),[3],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))],[For(Id("i"),IntLiteral(10),BinaryOp(">=",Id("i"),IntLiteral(0)),UnaryOp("-",IntLiteral(1)),([],[For(Id("j"),IntLiteral(0),BinaryOp("<",Id("j"),IntLiteral(3)),IntLiteral(1),([],[If([(BinaryOp("==",Id("i"),Id("j")),[],[Continue()])],([],[])),Assign(ArrayCell(Id("a"),[Id("j")]),BinaryOp("*",Id("j"),Id("i")))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test_323(self):
        input = """
        Function: foo
        Parameter: a, b
        Body:
            Var: i = 0,j, a[3] = {1,2,3};
            Do
                Var: i = 0,j, a[3] = {1,2,3};
                For (j = 0, j < 3, 1) Do
                    If (i==j) Then Continue; EndIf.
                    a[j] = j*i;
                EndFor.
                i= i+1;
            While i<10 EndDo.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0)),VarDecl(Id("j"),[],None),VarDecl(Id("a"),[3],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))],[Dowhile(([VarDecl(Id("i"),[],IntLiteral(0)),VarDecl(Id("j"),[],None),VarDecl(Id("a"),[3],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))],[For(Id("j"),IntLiteral(0),BinaryOp("<",Id("j"),IntLiteral(3)),IntLiteral(1),([],[If([(BinaryOp("==",Id("i"),Id("j")),[],[Continue()])],([],[])),Assign(ArrayCell(Id("a"),[Id("j")]),BinaryOp("*",Id("j"),Id("i")))])),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]),BinaryOp("<",Id("i"),IntLiteral(10)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_324(self):
        input = """
        Function: foo
        Parameter: a, b
        Body:
            Var: i = 0,j, a[3] = {1,2,3};
            Do
                While (x+y > x-y) Do
                    If (x*y % 2) Then
                        Continue;
                    EndIf.
                    x = x+1;
                EndWhile.
                i= i+1;
            While i<10 EndDo.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0)),VarDecl(Id("j"),[],None),VarDecl(Id("a"),[3],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))],[Dowhile(([],[While(BinaryOp(">",BinaryOp("+",Id("x"),Id("y")),BinaryOp("-",Id("x"),Id("y"))),([],[If([(BinaryOp("%",BinaryOp("*",Id("x"),Id("y")),IntLiteral(2)),[],[Continue()])],([],[])),Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))])),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]),BinaryOp("<",Id("i"),IntLiteral(10)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test_325(self):
        input = """
        Var: x,a=6,arr[3][4] = {1,2,3,4};
        Function: add
        Parameter: a, b
        Body:
            Return a+b;
        EndBody.
        Function: checkNeg
        Parameter: a
        Body:
            Return (a<0) || (a<.0);
        EndBody."""
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],IntLiteral(6)),VarDecl(Id("arr"),[3,4],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)])),FuncDecl(Id("add"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([],[Return(BinaryOp("+",Id("a"),Id("b")))])),FuncDecl(Id("checkNeg"),[VarDecl(Id("a"),[],None)],([],[Return(BinaryOp("||",BinaryOp("<",Id("a"),IntLiteral(0)),BinaryOp("<.",Id("a"),IntLiteral(0))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test_326(self):
        input = """
        Var: x,a=6,arr[3][4] = {1,2,3,4};
        Function: add
        Parameter: a, b
        Body:
            Var: a = 1;
        EndBody.
        Function: checkNeg
        Parameter: a
        Body:
            Return (a<0) || (a<.0);
        EndBody."""
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],IntLiteral(6)),VarDecl(Id("arr"),[3,4],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)])),FuncDecl(Id("add"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("a"),[],IntLiteral(1))],[])),FuncDecl(Id("checkNeg"),[VarDecl(Id("a"),[],None)],([],[Return(BinaryOp("||",BinaryOp("<",Id("a"),IntLiteral(0)),BinaryOp("<.",Id("a"),IntLiteral(0))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_327(self):
        input = """
        Var: x,a=6,arr[3][4] = {1,2,3,4};
        Function: add
        Parameter: a, b
        Body:
        EndBody.
        Function: checkNeg
        Parameter: a
        Body:
            Return (a<0) || (a<.0);
        EndBody."""
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],IntLiteral(6)),VarDecl(Id("arr"),[3,4],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)])),FuncDecl(Id("add"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([],[])),FuncDecl(Id("checkNeg"),[VarDecl(Id("a"),[],None)],([],[Return(BinaryOp("||",BinaryOp("<",Id("a"),IntLiteral(0)),BinaryOp("<.",Id("a"),IntLiteral(0))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test_328(self):
        """function"""
        input = """
        Function: foo
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) Do
                a[i] = b +. 1.0;
                i = i + 1;
            EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("<",Id("i"),IntLiteral(5)),([],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_329(self):
        input = """
        Function: foo
        Parameter: a, b
        Body:
            Var: i = 0,j, a[3] = {1,2,3};
            For (i = 10, i >= 0, -1) Do
                While (j % 5 == 2) Do
                    a[i] = b +. 1.0;
                    j = j + 1;
                EndWhile.
            EndFor.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0)),VarDecl(Id("j"),[],None),VarDecl(Id("a"),[3],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))],[For(Id("i"),IntLiteral(10),BinaryOp(">=",Id("i"),IntLiteral(0)),UnaryOp("-",IntLiteral(1)),([],[While(BinaryOp("==",BinaryOp("%",Id("j"),IntLiteral(5)),IntLiteral(2)),([],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("j"),BinaryOp("+",Id("j"),IntLiteral(1)))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    def test_330(self):
        """function"""
        input = """
        Function: foo
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) Do
                a[i] = b +. 1.0;
                i = i + 1;
                EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("<",Id("i"),IntLiteral(5)),([],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    def test_331(self):
        input = """
        Var: a[3] = {{1,2},{2,3}};
        Function: foo
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i + 1;
                EndWhile.
        EndBody."""
        expect = Program([VarDecl(Id("a"),[3],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)]),ArrayLiteral([IntLiteral(2),IntLiteral(3)])])),FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("||",BinaryOp("&&",BinaryOp("<",Id("i"),IntLiteral(5)),BinaryOp(">",Id("j"),IntLiteral(6))),BinaryOp("==",Id("k"),IntLiteral(7))),([],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_332(self):
        input = """
        Var: a[3] = {23,2,3};
        Function: func
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i + 1 + a + b + c + d;
            EndWhile.
        EndBody."""
        expect = Program([VarDecl(Id("a"),[3],ArrayLiteral([IntLiteral(23),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("func"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("||",BinaryOp("&&",BinaryOp("<",Id("i"),IntLiteral(5)),BinaryOp(">",Id("j"),IntLiteral(6))),BinaryOp("==",Id("k"),IntLiteral(7))),([],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("i"),IntLiteral(1)),Id("a")),Id("b")),Id("c")),Id("d")))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test_333(self):
        input = """
        Var: a[3] = {23,2,3};
        Function: func
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i - 1 + a -. b - c - -.d;
            EndWhile.
        EndBody."""
        expect = Program([VarDecl(Id("a"),[3],ArrayLiteral([IntLiteral(23),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("func"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("||",BinaryOp("&&",BinaryOp("<",Id("i"),IntLiteral(5)),BinaryOp(">",Id("j"),IntLiteral(6))),BinaryOp("==",Id("k"),IntLiteral(7))),([],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("-",BinaryOp("-",BinaryOp("-.",BinaryOp("+",BinaryOp("-",Id("i"),IntLiteral(1)),Id("a")),Id("b")),Id("c")),UnaryOp("-.",Id("d"))))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_334(self):
        input = """
        Var: a[3] = {23,2,3};
        Function: func
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
            EndWhile.
        EndBody."""
        expect = Program([VarDecl(Id("a"),[3],ArrayLiteral([IntLiteral(23),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("func"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("||",BinaryOp("&&",BinaryOp("<",Id("i"),IntLiteral(5)),BinaryOp(">",Id("j"),IntLiteral(6))),BinaryOp("==",Id("k"),IntLiteral(7))),([],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("-",BinaryOp("-.",BinaryOp("-",Id("i"),BinaryOp("*",Id("b"),Id("a"))),BinaryOp("\\",Id("b"),Id("c"))),UnaryOp("-.",Id("d"))))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    def test_335(self):
        input = """
        Var: a[3] = {23,2,3};
        Function: func
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
            EndWhile.
        EndBody."""
        expect = Program([VarDecl(Id("a"),[3],ArrayLiteral([IntLiteral(23),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("func"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("||",BinaryOp("&&",BinaryOp("<",Id("i"),IntLiteral(5)),BinaryOp(">",Id("j"),IntLiteral(6))),BinaryOp("==",Id("k"),IntLiteral(7))),([],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("-",BinaryOp("-.",BinaryOp("-",Id("i"),BinaryOp("*",Id("b"),Id("a"))),BinaryOp("\\",Id("b"),Id("c"))),UnaryOp("-.",Id("d"))))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test_336(self):
        input = """
        Var: a[3] = {True,2,3};
        Function: func
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
            EndWhile.
        EndBody."""
        expect = Program([VarDecl(Id("a"),[3],ArrayLiteral([BooleanLiteral(True),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("func"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("||",BinaryOp("&&",BinaryOp("<",Id("i"),IntLiteral(5)),BinaryOp(">",Id("j"),IntLiteral(6))),BinaryOp("==",Id("k"),IntLiteral(7))),([],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("-",BinaryOp("-.",BinaryOp("-",Id("i"),BinaryOp("*",Id("b"),Id("a"))),BinaryOp("\\",Id("b"),Id("c"))),UnaryOp("-.",Id("d"))))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test_337(self):
        input = """
        Var: a[3] = {True,2,3};
        Function: func
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
            EndWhile.
            Return 1;
        EndBody."""
        expect = Program([VarDecl(Id("a"),[3],ArrayLiteral([BooleanLiteral(True),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("func"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("||",BinaryOp("&&",BinaryOp("<",Id("i"),IntLiteral(5)),BinaryOp(">",Id("j"),IntLiteral(6))),BinaryOp("==",Id("k"),IntLiteral(7))),([],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("-",BinaryOp("-.",BinaryOp("-",Id("i"),BinaryOp("*",Id("b"),Id("a"))),BinaryOp("\\",Id("b"),Id("c"))),UnaryOp("-.",Id("d"))))])),Return(IntLiteral(1))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    def test_338(self):
        input = """
        Var: a[3] = {True,2,3};
        Function: func
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
            EndWhile.
            Return 1+3;
        EndBody."""
        expect = Program([VarDecl(Id("a"),[3],ArrayLiteral([BooleanLiteral(True),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("func"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("||",BinaryOp("&&",BinaryOp("<",Id("i"),IntLiteral(5)),BinaryOp(">",Id("j"),IntLiteral(6))),BinaryOp("==",Id("k"),IntLiteral(7))),([],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("-",BinaryOp("-.",BinaryOp("-",Id("i"),BinaryOp("*",Id("b"),Id("a"))),BinaryOp("\\",Id("b"),Id("c"))),UnaryOp("-.",Id("d"))))])),Return(BinaryOp("+",IntLiteral(1),IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    def test_339(self):
        input = """
        Var: a[3] = {True,2,3};
        Function: func
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
            EndWhile.
            Return !( True && abc || func(a) ) || !!!((a>b) || (a<c));
        EndBody."""
        expect = Program([VarDecl(Id("a"),[3],ArrayLiteral([BooleanLiteral(True),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("func"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("||",BinaryOp("&&",BinaryOp("<",Id("i"),IntLiteral(5)),BinaryOp(">",Id("j"),IntLiteral(6))),BinaryOp("==",Id("k"),IntLiteral(7))),([],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("-",BinaryOp("-.",BinaryOp("-",Id("i"),BinaryOp("*",Id("b"),Id("a"))),BinaryOp("\\",Id("b"),Id("c"))),UnaryOp("-.",Id("d"))))])),Return(BinaryOp("||",UnaryOp("!",BinaryOp("||",BinaryOp("&&",BooleanLiteral(True),Id("abc")),CallExpr(Id("func"),[Id("a")]))),UnaryOp("!",UnaryOp("!",UnaryOp("!",BinaryOp("||",BinaryOp(">",Id("a"),Id("b")),BinaryOp("<",Id("a"),Id("c"))))))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    def test_340(self):
        input = """
        Var: a[3] = {True,2,3};
        Function: func
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
            EndWhile.
            Return a[1];
        EndBody."""
        expect = Program([VarDecl(Id("a"),[3],ArrayLiteral([BooleanLiteral(True),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("func"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("||",BinaryOp("&&",BinaryOp("<",Id("i"),IntLiteral(5)),BinaryOp(">",Id("j"),IntLiteral(6))),BinaryOp("==",Id("k"),IntLiteral(7))),([],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("-",BinaryOp("-.",BinaryOp("-",Id("i"),BinaryOp("*",Id("b"),Id("a"))),BinaryOp("\\",Id("b"),Id("c"))),UnaryOp("-.",Id("d"))))])),Return(ArrayCell(Id("a"),[IntLiteral(1)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test_341(self):
        input = """
        Var: a[3] = {{"abc","123"},2,3};
        Function: func
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
            EndWhile.
        EndBody."""
        expect = Program([VarDecl(Id("a"),[3],ArrayLiteral([ArrayLiteral([StringLiteral("abc"),StringLiteral("123")]),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("func"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("||",BinaryOp("&&",BinaryOp("<",Id("i"),IntLiteral(5)),BinaryOp(">",Id("j"),IntLiteral(6))),BinaryOp("==",Id("k"),IntLiteral(7))),([],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("-",BinaryOp("-.",BinaryOp("-",Id("i"),BinaryOp("*",Id("b"),Id("a"))),BinaryOp("\\",Id("b"),Id("c"))),UnaryOp("-.",Id("d"))))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test_342(self):
        input = """
        Var: a[3] = {True,2,3};
        Function: func
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
            EndWhile.
            Return 1;
        EndBody."""
        expect = Program([VarDecl(Id("a"),[3],ArrayLiteral([BooleanLiteral(True),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("func"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("||",BinaryOp("&&",BinaryOp("<",Id("i"),IntLiteral(5)),BinaryOp(">",Id("j"),IntLiteral(6))),BinaryOp("==",Id("k"),IntLiteral(7))),([],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("-",BinaryOp("-.",BinaryOp("-",Id("i"),BinaryOp("*",Id("b"),Id("a"))),BinaryOp("\\",Id("b"),Id("c"))),UnaryOp("-.",Id("d"))))])),Return(IntLiteral(1))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    def test_343(self):
        input = """
        Var: a[3] = {True,2,3};
        Function: func
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
            EndWhile.
            Return;
        EndBody."""
        expect = Program([VarDecl(Id("a"),[3],ArrayLiteral([BooleanLiteral(True),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("func"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("||",BinaryOp("&&",BinaryOp("<",Id("i"),IntLiteral(5)),BinaryOp(">",Id("j"),IntLiteral(6))),BinaryOp("==",Id("k"),IntLiteral(7))),([],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("-",BinaryOp("-.",BinaryOp("-",Id("i"),BinaryOp("*",Id("b"),Id("a"))),BinaryOp("\\",Id("b"),Id("c"))),UnaryOp("-.",Id("d"))))])),Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    def test_344(self):
        input = """
        Var: a[3] = {True,2,3};
        Function: func
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
            EndWhile.
            Return;
        EndBody."""
        expect = Program([VarDecl(Id("a"),[3],ArrayLiteral([BooleanLiteral(True),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("func"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("||",BinaryOp("&&",BinaryOp("<",Id("i"),IntLiteral(5)),BinaryOp(">",Id("j"),IntLiteral(6))),BinaryOp("==",Id("k"),IntLiteral(7))),([],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("-",BinaryOp("-.",BinaryOp("-",Id("i"),BinaryOp("*",Id("b"),Id("a"))),BinaryOp("\\",Id("b"),Id("c"))),UnaryOp("-.",Id("d"))))])),Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    def test_345(self):
        input = """
        Var: a[3] = {True,2,3};
        Function: func
        Parameter: a[2], b
        Body:
            Var: i = 0;
            While (i < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
            EndWhile.
            Return;
        EndBody."""
        expect = Program([VarDecl(Id("a"),[3],ArrayLiteral([BooleanLiteral(True),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("func"),[VarDecl(Id("a"),[2],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("||",BinaryOp("&&",BinaryOp("<",Id("i"),IntLiteral(5)),BinaryOp(">",Id("j"),IntLiteral(6))),BinaryOp("==",Id("k"),IntLiteral(7))),([],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("-",BinaryOp("-.",BinaryOp("-",Id("i"),BinaryOp("*",Id("b"),Id("a"))),BinaryOp("\\",Id("b"),Id("c"))),UnaryOp("-.",Id("d"))))])),Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test_346(self):
        input = """
        Var: a[3] = {True,2,3};
        ** this is a comment **
        Function: func
        Body:
            While (a < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
            EndWhile.
        EndBody."""
        expect = Program([VarDecl(Id("a"),[3],ArrayLiteral([BooleanLiteral(True),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("func"),[],([],[While(BinaryOp("||",BinaryOp("&&",BinaryOp("<",Id("a"),IntLiteral(5)),BinaryOp(">",Id("j"),IntLiteral(6))),BinaryOp("==",Id("k"),IntLiteral(7))),([],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("-",BinaryOp("-.",BinaryOp("-",Id("i"),BinaryOp("*",Id("b"),Id("a"))),BinaryOp("\\",Id("b"),Id("c"))),UnaryOp("-.",Id("d"))))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test_347(self):
        input = """
        Var: a[3] = {True,2,3};
        ** this is a comment **
        ** this is another comment **
        Function: func
        Body:
            While (a < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
            EndWhile.
        EndBody."""
        expect = Program([VarDecl(Id("a"),[3],ArrayLiteral([BooleanLiteral(True),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("func"),[],([],[While(BinaryOp("||",BinaryOp("&&",BinaryOp("<",Id("a"),IntLiteral(5)),BinaryOp(">",Id("j"),IntLiteral(6))),BinaryOp("==",Id("k"),IntLiteral(7))),([],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("-",BinaryOp("-.",BinaryOp("-",Id("i"),BinaryOp("*",Id("b"),Id("a"))),BinaryOp("\\",Id("b"),Id("c"))),UnaryOp("-.",Id("d"))))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    def test_348(self):
        input = """
        ** this is a comment **
        Var: a[3] = {True,2,3};
        ** this is another comment **
        Function: func
        Body:
            While (a < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
            EndWhile.
        EndBody."""
        expect = Program([VarDecl(Id("a"),[3],ArrayLiteral([BooleanLiteral(True),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("func"),[],([],[While(BinaryOp("||",BinaryOp("&&",BinaryOp("<",Id("a"),IntLiteral(5)),BinaryOp(">",Id("j"),IntLiteral(6))),BinaryOp("==",Id("k"),IntLiteral(7))),([],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("-",BinaryOp("-.",BinaryOp("-",Id("i"),BinaryOp("*",Id("b"),Id("a"))),BinaryOp("\\",Id("b"),Id("c"))),UnaryOp("-.",Id("d"))))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    def test_349(self):
        input = """
        ** this is a comment **
        Var: a[3] = {True,2,3}, str = "string";
        ** this is another comment **
        Function: func
        Body:
            While (a < 5) && (j>6) || (k==7) Do
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
            EndWhile.
        EndBody."""
        expect = Program([VarDecl(Id("a"),[3],ArrayLiteral([BooleanLiteral(True),IntLiteral(2),IntLiteral(3)])),VarDecl(Id("str"),[],StringLiteral("string")),FuncDecl(Id("func"),[],([],[While(BinaryOp("||",BinaryOp("&&",BinaryOp("<",Id("a"),IntLiteral(5)),BinaryOp(">",Id("j"),IntLiteral(6))),BinaryOp("==",Id("k"),IntLiteral(7))),([],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("-",BinaryOp("-.",BinaryOp("-",Id("i"),BinaryOp("*",Id("b"),Id("a"))),BinaryOp("\\",Id("b"),Id("c"))),UnaryOp("-.",Id("d"))))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    def test_350(self):
        input = """Var: x = "string"; """
        expect = Program([VarDecl(Id("x"),[],StringLiteral("string"))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    def test_351(self):
        input = """
        ** this is a comment **
        Var: a[2] = {True,2,3}, str = "string'"";
        Function: func
        Body:
            If (a + 5) && (j-6) || (k*7) Then
                ** this is another comment **
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
            EndIf.
        EndBody.
        Function: main
        Body:
            func();
            Return 0;
        EndBody.
        """
        expect = Program([VarDecl(Id("a"),[2],ArrayLiteral([BooleanLiteral(True),IntLiteral(2),IntLiteral(3)])),VarDecl(Id("str"),[],StringLiteral("string\'\"")),FuncDecl(Id("func"),[],([],[If([(BinaryOp("||",BinaryOp("&&",BinaryOp("+",Id("a"),IntLiteral(5)),BinaryOp("-",Id("j"),IntLiteral(6))),BinaryOp("*",Id("k"),IntLiteral(7))),[],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("-",BinaryOp("-.",BinaryOp("-",Id("i"),BinaryOp("*",Id("b"),Id("a"))),BinaryOp("\\",Id("b"),Id("c"))),UnaryOp("-.",Id("d"))))])],([],[]))])),FuncDecl(Id("main"),[],([],[CallStmt(Id("func"),[]),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test_352(self):
        input = """
        ** this is a comment **
        Var: a[2] = {True,{2,3}}, str = "string";
        Function: func
        Body:
            If (a + 5) && (j-6) || (k*7) Then
                ** this is another comment **
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
            EndIf.
            Return a+func();
        EndBody.
        Function: main
        Body:
            func();
            Return 0;
        EndBody.
        """
        expect = Program([VarDecl(Id("a"),[2],ArrayLiteral([BooleanLiteral(True),ArrayLiteral([IntLiteral(2),IntLiteral(3)])])),VarDecl(Id("str"),[],StringLiteral("string")),FuncDecl(Id("func"),[],([],[If([(BinaryOp("||",BinaryOp("&&",BinaryOp("+",Id("a"),IntLiteral(5)),BinaryOp("-",Id("j"),IntLiteral(6))),BinaryOp("*",Id("k"),IntLiteral(7))),[],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("-",BinaryOp("-.",BinaryOp("-",Id("i"),BinaryOp("*",Id("b"),Id("a"))),BinaryOp("\\",Id("b"),Id("c"))),UnaryOp("-.",Id("d"))))])],([],[])),Return(BinaryOp("+",Id("a"),CallExpr(Id("func"),[])))])),FuncDecl(Id("main"),[],([],[CallStmt(Id("func"),[]),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test_353(self):
        input = """
        ** this is a comment **
        Var: a[2] = {True,{2,3}}, str = "string";
        Function: func
        Body:
            If (a + 5) && (j-6) || (k*7) Then
                ** this is another comment **
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
            EndIf.
            For (i = 10, i >= 0, -1) Do
                a = a + b;
            EndFor.
            Return a+func();
        EndBody.
        Function: main
        Body:
            func();
            Return 0;
        EndBody.
        """
        expect = Program([VarDecl(Id("a"),[2],ArrayLiteral([BooleanLiteral(True),ArrayLiteral([IntLiteral(2),IntLiteral(3)])])),VarDecl(Id("str"),[],StringLiteral("string")),FuncDecl(Id("func"),[],([],[If([(BinaryOp("||",BinaryOp("&&",BinaryOp("+",Id("a"),IntLiteral(5)),BinaryOp("-",Id("j"),IntLiteral(6))),BinaryOp("*",Id("k"),IntLiteral(7))),[],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("-",BinaryOp("-.",BinaryOp("-",Id("i"),BinaryOp("*",Id("b"),Id("a"))),BinaryOp("\\",Id("b"),Id("c"))),UnaryOp("-.",Id("d"))))])],([],[])),For(Id("i"),IntLiteral(10),BinaryOp(">=",Id("i"),IntLiteral(0)),UnaryOp("-",IntLiteral(1)),([],[Assign(Id("a"),BinaryOp("+",Id("a"),Id("b")))])),Return(BinaryOp("+",Id("a"),CallExpr(Id("func"),[])))])),FuncDecl(Id("main"),[],([],[CallStmt(Id("func"),[]),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test_354(self):
        input = """
        ** this is a comment **
        Var: a[2] = {True,{2,3}}, str = "string";
        Function: func
        Body:
            If (a + 5) && (j-6) || (k*7) Then
                ** this is another comment **
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
                For (i = 10, i >= 0, -1) Do
                a = a + b;
            EndFor.
            EndIf.
            Return a+func();
        EndBody.
        Function: main
        Body:
            func();
            Return 0;
        EndBody.
        """
        expect = Program([VarDecl(Id("a"),[2],ArrayLiteral([BooleanLiteral(True),ArrayLiteral([IntLiteral(2),IntLiteral(3)])])),VarDecl(Id("str"),[],StringLiteral("string")),FuncDecl(Id("func"),[],([],[If([(BinaryOp("||",BinaryOp("&&",BinaryOp("+",Id("a"),IntLiteral(5)),BinaryOp("-",Id("j"),IntLiteral(6))),BinaryOp("*",Id("k"),IntLiteral(7))),[],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("-",BinaryOp("-.",BinaryOp("-",Id("i"),BinaryOp("*",Id("b"),Id("a"))),BinaryOp("\\",Id("b"),Id("c"))),UnaryOp("-.",Id("d")))),For(Id("i"),IntLiteral(10),BinaryOp(">=",Id("i"),IntLiteral(0)),UnaryOp("-",IntLiteral(1)),([],[Assign(Id("a"),BinaryOp("+",Id("a"),Id("b")))]))])],([],[])),Return(BinaryOp("+",Id("a"),CallExpr(Id("func"),[])))])),FuncDecl(Id("main"),[],([],[CallStmt(Id("func"),[]),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test_355(self):
        input = """
        ** this is a comment **
        Var: a[2] = {True,{2,3}}, str = "string";
        Function: func
        Body:
            If (a + 5) && (j-6) || (k*7) Then
                ** this is another comment **
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
                For (i = 10, i >= 0, -1) Do
                a = a + b;
            EndFor.
            EndIf.
            Return a+func();
        EndBody.
        Function: main
        Body:
            func();
            Return 0;
        EndBody.
        """
        expect = Program([VarDecl(Id("a"),[2],ArrayLiteral([BooleanLiteral(True),ArrayLiteral([IntLiteral(2),IntLiteral(3)])])),VarDecl(Id("str"),[],StringLiteral("string")),FuncDecl(Id("func"),[],([],[If([(BinaryOp("||",BinaryOp("&&",BinaryOp("+",Id("a"),IntLiteral(5)),BinaryOp("-",Id("j"),IntLiteral(6))),BinaryOp("*",Id("k"),IntLiteral(7))),[],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("-",BinaryOp("-.",BinaryOp("-",Id("i"),BinaryOp("*",Id("b"),Id("a"))),BinaryOp("\\",Id("b"),Id("c"))),UnaryOp("-.",Id("d")))),For(Id("i"),IntLiteral(10),BinaryOp(">=",Id("i"),IntLiteral(0)),UnaryOp("-",IntLiteral(1)),([],[Assign(Id("a"),BinaryOp("+",Id("a"),Id("b")))]))])],([],[])),Return(BinaryOp("+",Id("a"),CallExpr(Id("func"),[])))])),FuncDecl(Id("main"),[],([],[CallStmt(Id("func"),[]),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test_356(self):
        input = """
        ** this is a comment **
        Var: a[2] = {True,{2,3}}, str = "string";
        Function: func
        Body:
            If (a + 5) && (j-6) || (k*7) Then
                ** this is another comment **
                a[i] = b +. 1.0;
                i = i - b * a -. b \\ c - -.d;
                For (i = 10, i >= 0, -1) Do
                    a = a + b;
                EndFor.
            EndIf.
            Return a+func();
        EndBody.
        Function: main
        Body:
            func();
            Return 0;
        EndBody.
        Function: boo
        Parameter: a, b
        Body:
            Var: i = 0,j, a[3] = {1,2,3};
            Do
                Var: i = 0,j, a[3] = {1,2,3};
                For (j = 0, j < 3, 1) Do
                    If (i==j) Then Continue; EndIf.
                    a[j] = j*i;
                EndFor.
                i= i+1;
            While i<10 EndDo.
        EndBody.
        """
        expect = Program([VarDecl(Id("a"),[2],ArrayLiteral([BooleanLiteral(True),ArrayLiteral([IntLiteral(2),IntLiteral(3)])])),VarDecl(Id("str"),[],StringLiteral("string")),FuncDecl(Id("func"),[],([],[If([(BinaryOp("||",BinaryOp("&&",BinaryOp("+",Id("a"),IntLiteral(5)),BinaryOp("-",Id("j"),IntLiteral(6))),BinaryOp("*",Id("k"),IntLiteral(7))),[],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("-",BinaryOp("-.",BinaryOp("-",Id("i"),BinaryOp("*",Id("b"),Id("a"))),BinaryOp("\\",Id("b"),Id("c"))),UnaryOp("-.",Id("d")))),For(Id("i"),IntLiteral(10),BinaryOp(">=",Id("i"),IntLiteral(0)),UnaryOp("-",IntLiteral(1)),([],[Assign(Id("a"),BinaryOp("+",Id("a"),Id("b")))]))])],([],[])),Return(BinaryOp("+",Id("a"),CallExpr(Id("func"),[])))])),FuncDecl(Id("main"),[],([],[CallStmt(Id("func"),[]),Return(IntLiteral(0))])),FuncDecl(Id("boo"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0)),VarDecl(Id("j"),[],None),VarDecl(Id("a"),[3],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))],[Dowhile(([VarDecl(Id("i"),[],IntLiteral(0)),VarDecl(Id("j"),[],None),VarDecl(Id("a"),[3],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))],[For(Id("j"),IntLiteral(0),BinaryOp("<",Id("j"),IntLiteral(3)),IntLiteral(1),([],[If([(BinaryOp("==",Id("i"),Id("j")),[],[Continue()])],([],[])),Assign(ArrayCell(Id("a"),[Id("j")]),BinaryOp("*",Id("j"),Id("i")))])),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]),BinaryOp("<",Id("i"),IntLiteral(10)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    def test_357(self):
        input = """
        ** this is a comment **
        Var: a[2] = {True,{2,3}}, str = "string";
        Function: func
        Body:
            For (i = 10, i >= 0, -1) Do
                a = a + b;
            EndFor.
            Return a+func();
        EndBody.
        Function: main
        Body:
            func();
            Return 0;
        EndBody.
        """
        expect = Program([VarDecl(Id("a"),[2],ArrayLiteral([BooleanLiteral(True),ArrayLiteral([IntLiteral(2),IntLiteral(3)])])),VarDecl(Id("str"),[],StringLiteral("string")),FuncDecl(Id("func"),[],([],[For(Id("i"),IntLiteral(10),BinaryOp(">=",Id("i"),IntLiteral(0)),UnaryOp("-",IntLiteral(1)),([],[Assign(Id("a"),BinaryOp("+",Id("a"),Id("b")))])),Return(BinaryOp("+",Id("a"),CallExpr(Id("func"),[])))])),FuncDecl(Id("main"),[],([],[CallStmt(Id("func"),[]),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))
    
    def test_358(self):
        input = """
        ** this is a comment **
        Var: a[2] = {True,{2,3}}, str = "string";
        Function: func
        Body:
            For (i = 10, i >= 0, -1) Do
                a = a + b;
                For (i = 10, i >= 0, -1) Do
                    a = a + b;
                EndFor.
            EndFor.
            Return a+func();
        EndBody.
        Function: main
        Body:
            func();
            Return 0;
        EndBody.
        """
        expect = Program([VarDecl(Id("a"),[2],ArrayLiteral([BooleanLiteral(True),ArrayLiteral([IntLiteral(2),IntLiteral(3)])])),VarDecl(Id("str"),[],StringLiteral("string")),FuncDecl(Id("func"),[],([],[For(Id("i"),IntLiteral(10),BinaryOp(">=",Id("i"),IntLiteral(0)),UnaryOp("-",IntLiteral(1)),([],[Assign(Id("a"),BinaryOp("+",Id("a"),Id("b"))),For(Id("i"),IntLiteral(10),BinaryOp(">=",Id("i"),IntLiteral(0)),UnaryOp("-",IntLiteral(1)),([],[Assign(Id("a"),BinaryOp("+",Id("a"),Id("b")))]))])),Return(BinaryOp("+",Id("a"),CallExpr(Id("func"),[])))])),FuncDecl(Id("main"),[],([],[CallStmt(Id("func"),[]),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))
    
    def test_359(self):
        input = """
        ** this is a comment **
        Var: a[2] = {True,{2,3}}, str = "string";
        Function: func
        Body:
            For (i = 10, i >= 0, -1) Do
                a = a + b;
                For (i = 10, i >= 0, -1) Do
                    a = a + b;
                EndFor.
            EndFor.
            Return a+func();
        EndBody.
        Function: main
        Body:
            func();
            Return 0;
        EndBody.
        """
        expect = Program([VarDecl(Id("a"),[2],ArrayLiteral([BooleanLiteral(True),ArrayLiteral([IntLiteral(2),IntLiteral(3)])])),VarDecl(Id("str"),[],StringLiteral("string")),FuncDecl(Id("func"),[],([],[For(Id("i"),IntLiteral(10),BinaryOp(">=",Id("i"),IntLiteral(0)),UnaryOp("-",IntLiteral(1)),([],[Assign(Id("a"),BinaryOp("+",Id("a"),Id("b"))),For(Id("i"),IntLiteral(10),BinaryOp(">=",Id("i"),IntLiteral(0)),UnaryOp("-",IntLiteral(1)),([],[Assign(Id("a"),BinaryOp("+",Id("a"),Id("b")))]))])),Return(BinaryOp("+",Id("a"),CallExpr(Id("func"),[])))])),FuncDecl(Id("main"),[],([],[CallStmt(Id("func"),[]),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))
    def test_360(self):
        input = """
        Var: a[2] = {3}, str = "string";
        Var: a[2][3] = { {4},{5}}, str = "string";
        Function: func
        Body:
            For (i = 10, i >= 0, -1) Do
                a = a + b;
                For (i = 10, i >= 0, -1) Do
                    a = a + b;
                EndFor.
            EndFor.
            Return a+func();
        EndBody.
        Function: whi
        Parameter: a, b
        Body:
            Do
                b = b+2;
            While a > 10 EndDo.
        EndBody.
        Function: main
        Body:
            func();
            Return 0;
        EndBody.
        """
        expect = Program([VarDecl(Id("a"),[2],ArrayLiteral([IntLiteral(3)])),VarDecl(Id("str"),[],StringLiteral("string")),VarDecl(Id("a"),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(4)]),ArrayLiteral([IntLiteral(5)])])),VarDecl(Id("str"),[],StringLiteral("string")),FuncDecl(Id("func"),[],([],[For(Id("i"),IntLiteral(10),BinaryOp(">=",Id("i"),IntLiteral(0)),UnaryOp("-",IntLiteral(1)),([],[Assign(Id("a"),BinaryOp("+",Id("a"),Id("b"))),For(Id("i"),IntLiteral(10),BinaryOp(">=",Id("i"),IntLiteral(0)),UnaryOp("-",IntLiteral(1)),([],[Assign(Id("a"),BinaryOp("+",Id("a"),Id("b")))]))])),Return(BinaryOp("+",Id("a"),CallExpr(Id("func"),[])))])),FuncDecl(Id("whi"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([],[Dowhile(([],[Assign(Id("b"),BinaryOp("+",Id("b"),IntLiteral(2)))]),BinaryOp(">",Id("a"),IntLiteral(10)))])),FuncDecl(Id("main"),[],([],[CallStmt(Id("func"),[]),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))
    
    def test_361(self):
        input = """
        Var: a[2] = {3}, str = "string";
        Var: str = "string";
        Function: func
        Body:
            For (i = 10, i >= 0, -1) Do
                a = a + b;
                For (i = 10, i >= 0, -1) Do
                    a = a + b;
                EndFor.
            EndFor.
            Return a+func();
        EndBody.
        Function: whi
        Parameter: a, b
        Body:
            Do
                For (i = 10, i >= 0, -1) Do
                    a = a + b;
                EndFor.
            While a > 10 EndDo.
        EndBody.
        Function: main
        Body:
            func();
            Return 0;
        EndBody.
        """
        expect = Program([VarDecl(Id("a"),[2],ArrayLiteral([IntLiteral(3)])),VarDecl(Id("str"),[],StringLiteral("string")),VarDecl(Id("str"),[],StringLiteral("string")),FuncDecl(Id("func"),[],([],[For(Id("i"),IntLiteral(10),BinaryOp(">=",Id("i"),IntLiteral(0)),UnaryOp("-",IntLiteral(1)),([],[Assign(Id("a"),BinaryOp("+",Id("a"),Id("b"))),For(Id("i"),IntLiteral(10),BinaryOp(">=",Id("i"),IntLiteral(0)),UnaryOp("-",IntLiteral(1)),([],[Assign(Id("a"),BinaryOp("+",Id("a"),Id("b")))]))])),Return(BinaryOp("+",Id("a"),CallExpr(Id("func"),[])))])),FuncDecl(Id("whi"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([],[Dowhile(([],[For(Id("i"),IntLiteral(10),BinaryOp(">=",Id("i"),IntLiteral(0)),UnaryOp("-",IntLiteral(1)),([],[Assign(Id("a"),BinaryOp("+",Id("a"),Id("b")))]))]),BinaryOp(">",Id("a"),IntLiteral(10)))])),FuncDecl(Id("main"),[],([],[CallStmt(Id("func"),[]),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))
    def test_362(self):
        input = """
        Var: a[4] = {3}, str = "string";
        Var: str = "string";
        Function: func
        Body:
            For (i = 10, i >= 0, -1) Do
                a[3][func()] = b;
                For (i = 10, i >= 0, -1) Do
                    a = a + b;
                EndFor.
            EndFor.
            Return a+func();
        EndBody.
        Function: whi
        Parameter: a, b
        Body:
            Do
                If a > b Then
                    a = a + b;
                EndIf.
            While a > 10 EndDo.
        EndBody.
        Function: main
        Body:
            func();
            Return 0;
        EndBody.
        """
        expect = Program([VarDecl(Id("a"),[4],ArrayLiteral([IntLiteral(3)])),VarDecl(Id("str"),[],StringLiteral("string")),VarDecl(Id("str"),[],StringLiteral("string")),FuncDecl(Id("func"),[],([],[For(Id("i"),IntLiteral(10),BinaryOp(">=",Id("i"),IntLiteral(0)),UnaryOp("-",IntLiteral(1)),([],[Assign(ArrayCell(ArrayCell(Id("a"),[IntLiteral(3)]),[CallExpr(Id("func"),[])]),Id("b")),For(Id("i"),IntLiteral(10),BinaryOp(">=",Id("i"),IntLiteral(0)),UnaryOp("-",IntLiteral(1)),([],[Assign(Id("a"),BinaryOp("+",Id("a"),Id("b")))]))])),Return(BinaryOp("+",Id("a"),CallExpr(Id("func"),[])))])),FuncDecl(Id("whi"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([],[Dowhile(([],[If([(BinaryOp(">",Id("a"),Id("b")),[],[Assign(Id("a"),BinaryOp("+",Id("a"),Id("b")))])],([],[]))]),BinaryOp(">",Id("a"),IntLiteral(10)))])),FuncDecl(Id("main"),[],([],[CallStmt(Id("func"),[]),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))
    def test_363(self):
        input = """
        Var: a[4] = {5}, str = "string";
        Var: str = "string";
        Function: main
        Body:
            
            func();
            Return 0;
        EndBody.
        """
        expect = Program([VarDecl(Id("a"),[4],ArrayLiteral([IntLiteral(5)])),VarDecl(Id("str"),[],StringLiteral("string")),VarDecl(Id("str"),[],StringLiteral("string")),FuncDecl(Id("main"),[],([],[CallStmt(Id("func"),[]),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))
    
    def test_364(self):
        input = """
        Function: foo
        Body:
            Do a = b + 3; c[2][3] = 5; While x == y EndDo.
        EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],([],[Dowhile(([],[Assign(Id("a"),BinaryOp("+",Id("b"),IntLiteral(3))),Assign(ArrayCell(ArrayCell(Id("c"),[IntLiteral(2)]),[IntLiteral(3)]),IntLiteral(5))]),BinaryOp("==",Id("x"),Id("y")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))
    
    def test_365(self):
        input = """
        Function: foo
        Parameter: a[123], b
        Body:
            Do 
                a = b + 3; 
                c[2][3] = 5+.10.2*func()+a[2+func()+c[4]]; 
            While (x == y)  EndDo.
        EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None)],([],[Dowhile(([],[Assign(Id("a"),BinaryOp("+",Id("b"),IntLiteral(3))),Assign(ArrayCell(ArrayCell(Id("c"),[IntLiteral(2)]),[IntLiteral(3)]),BinaryOp("+",BinaryOp("+.",IntLiteral(5),BinaryOp("*",FloatLiteral(10.2),CallExpr(Id("func"),[]))),ArrayCell(Id("a"),[BinaryOp("+",BinaryOp("+",IntLiteral(2),CallExpr(Id("func"),[])),ArrayCell(Id("c"),[IntLiteral(4)]))])))]),BinaryOp("==",Id("x"),Id("y")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    def test_366(self):
        input = """
        Function: foo
        Parameter: a[123], b
        Body:
            If a[12] > b Then
                Do 
                    a = b + 3; 
                    c[2][3] = 5+.10.2*func()+a[2+func()+c[4]]; 
                While (x == y)  EndDo.
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None)],([],[If([(BinaryOp(">",ArrayCell(Id("a"),[IntLiteral(12)]),Id("b")),[],[Dowhile(([],[Assign(Id("a"),BinaryOp("+",Id("b"),IntLiteral(3))),Assign(ArrayCell(ArrayCell(Id("c"),[IntLiteral(2)]),[IntLiteral(3)]),BinaryOp("+",BinaryOp("+.",IntLiteral(5),BinaryOp("*",FloatLiteral(10.2),CallExpr(Id("func"),[]))),ArrayCell(Id("a"),[BinaryOp("+",BinaryOp("+",IntLiteral(2),CallExpr(Id("func"),[])),ArrayCell(Id("c"),[IntLiteral(4)]))])))]),BinaryOp("==",Id("x"),Id("y")))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))
    
    def test_367(self):
        input = """
        Function: foo
        Parameter: a[123], b
        Body:
            If a[12] > b Then
                Do 
                    a = b + 3; 
                    c[2][3] = 5+.10.2*func()+a[2+func()+c[4]]; 
                While (x == y)  EndDo.
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None)],([],[If([(BinaryOp(">",ArrayCell(Id("a"),[IntLiteral(12)]),Id("b")),[],[Dowhile(([],[Assign(Id("a"),BinaryOp("+",Id("b"),IntLiteral(3))),Assign(ArrayCell(ArrayCell(Id("c"),[IntLiteral(2)]),[IntLiteral(3)]),BinaryOp("+",BinaryOp("+.",IntLiteral(5),BinaryOp("*",FloatLiteral(10.2),CallExpr(Id("func"),[]))),ArrayCell(Id("a"),[BinaryOp("+",BinaryOp("+",IntLiteral(2),CallExpr(Id("func"),[])),ArrayCell(Id("c"),[IntLiteral(4)]))])))]),BinaryOp("==",Id("x"),Id("y")))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test_368(self):
        input = """
        Function: foo
        Parameter: a[123], b
        Body:
            If a[12] > b Then
                Do 
                    a = b + 3; 
                    c[2][3] = 5+.10.2*func(a,b,c)+a[2+func()+c[4]]; 
                While (x == y)  EndDo.
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None)],([],[If([(BinaryOp(">",ArrayCell(Id("a"),[IntLiteral(12)]),Id("b")),[],[Dowhile(([],[Assign(Id("a"),BinaryOp("+",Id("b"),IntLiteral(3))),Assign(ArrayCell(ArrayCell(Id("c"),[IntLiteral(2)]),[IntLiteral(3)]),BinaryOp("+",BinaryOp("+.",IntLiteral(5),BinaryOp("*",FloatLiteral(10.2),CallExpr(Id("func"),[Id("a"),Id("b"),Id("c")]))),ArrayCell(Id("a"),[BinaryOp("+",BinaryOp("+",IntLiteral(2),CallExpr(Id("func"),[])),ArrayCell(Id("c"),[IntLiteral(4)]))])))]),BinaryOp("==",Id("x"),Id("y")))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))
    def test_369(self):
        input = """
        Function: foo
        Parameter: a[123], b
        Body:
            If a[12] > b Then
                Do 
                    a = b + 3; 
                    c[2][3] = 5+.10.2-.func(a,b,c)+a[2+func()+c[4]]; 
                While (x == y)  EndDo.
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None)],([],[If([(BinaryOp(">",ArrayCell(Id("a"),[IntLiteral(12)]),Id("b")),[],[Dowhile(([],[Assign(Id("a"),BinaryOp("+",Id("b"),IntLiteral(3))),Assign(ArrayCell(ArrayCell(Id("c"),[IntLiteral(2)]),[IntLiteral(3)]),BinaryOp("+",BinaryOp("-.",BinaryOp("+.",IntLiteral(5),FloatLiteral(10.2)),CallExpr(Id("func"),[Id("a"),Id("b"),Id("c")])),ArrayCell(Id("a"),[BinaryOp("+",BinaryOp("+",IntLiteral(2),CallExpr(Id("func"),[])),ArrayCell(Id("c"),[IntLiteral(4)]))])))]),BinaryOp("==",Id("x"),Id("y")))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))
    
    def test_370(self):
        input = """
        Function: foo
        Parameter: a[123], b
        Body:
            If a[12] > b Then
                Do 
                    a = b + 3; 
                    c[2][3] = 5+.10.2-.func(a,b,c)+a[2+func()+c[4]]; 
                While (x == y)  EndDo.
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None)],([],[If([(BinaryOp(">",ArrayCell(Id("a"),[IntLiteral(12)]),Id("b")),[],[Dowhile(([],[Assign(Id("a"),BinaryOp("+",Id("b"),IntLiteral(3))),Assign(ArrayCell(ArrayCell(Id("c"),[IntLiteral(2)]),[IntLiteral(3)]),BinaryOp("+",BinaryOp("-.",BinaryOp("+.",IntLiteral(5),FloatLiteral(10.2)),CallExpr(Id("func"),[Id("a"),Id("b"),Id("c")])),ArrayCell(Id("a"),[BinaryOp("+",BinaryOp("+",IntLiteral(2),CallExpr(Id("func"),[])),ArrayCell(Id("c"),[IntLiteral(4)]))])))]),BinaryOp("==",Id("x"),Id("y")))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    def test_371(self):
        input = """
        Var: a = True, d;
        Function: foods
        Parameter: a[123], b
        Body:
            If a[12] > b Then
                Do 
                    a = b + 3; 
                    c[2][3] = 5+.10.2-.func(a,b,c)+a[2+func()+c[4]]; 
                While (x == y)  EndDo.
            EndIf.
        EndBody.
        Function: foo
        Parameter: a[123], b
        Body:
            If a[12] > b Then
                Do 
                    a = b + 3; 
                    c[2][3] = 5+.10.2-.func(a,b,c)+a[2+func()+c[4]]; 
                While (x == y)  EndDo.
            EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id("a"),[],BooleanLiteral(True)),VarDecl(Id("d"),[],None),FuncDecl(Id("foods"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None)],([],[If([(BinaryOp(">",ArrayCell(Id("a"),[IntLiteral(12)]),Id("b")),[],[Dowhile(([],[Assign(Id("a"),BinaryOp("+",Id("b"),IntLiteral(3))),Assign(ArrayCell(ArrayCell(Id("c"),[IntLiteral(2)]),[IntLiteral(3)]),BinaryOp("+",BinaryOp("-.",BinaryOp("+.",IntLiteral(5),FloatLiteral(10.2)),CallExpr(Id("func"),[Id("a"),Id("b"),Id("c")])),ArrayCell(Id("a"),[BinaryOp("+",BinaryOp("+",IntLiteral(2),CallExpr(Id("func"),[])),ArrayCell(Id("c"),[IntLiteral(4)]))])))]),BinaryOp("==",Id("x"),Id("y")))])],([],[]))])),FuncDecl(Id("foo"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None)],([],[If([(BinaryOp(">",ArrayCell(Id("a"),[IntLiteral(12)]),Id("b")),[],[Dowhile(([],[Assign(Id("a"),BinaryOp("+",Id("b"),IntLiteral(3))),Assign(ArrayCell(ArrayCell(Id("c"),[IntLiteral(2)]),[IntLiteral(3)]),BinaryOp("+",BinaryOp("-.",BinaryOp("+.",IntLiteral(5),FloatLiteral(10.2)),CallExpr(Id("func"),[Id("a"),Id("b"),Id("c")])),ArrayCell(Id("a"),[BinaryOp("+",BinaryOp("+",IntLiteral(2),CallExpr(Id("func"),[])),ArrayCell(Id("c"),[IntLiteral(4)]))])))]),BinaryOp("==",Id("x"),Id("y")))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    def test_372(self):
        input = """
        Var: a = True, d;
        Function: foods
        Parameter: a[123], b
        Body:
            If a[12] > b Then
                Do 
                    a = b + 3; 
                    c[2][3] = 5+.10.2-.func(a,b,c)+a[2+func()+c[4]]; 
                While (x == y)  EndDo.
            EndIf.
        EndBody.
        Function: abc
        Parameter: a[123], b , x
        Body:
            Do 
                foods(a,v,t);
            While x+y EndDo.
        EndBody.
        """
        expect = Program([VarDecl(Id("a"),[],BooleanLiteral(True)),VarDecl(Id("d"),[],None),FuncDecl(Id("foods"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None)],([],[If([(BinaryOp(">",ArrayCell(Id("a"),[IntLiteral(12)]),Id("b")),[],[Dowhile(([],[Assign(Id("a"),BinaryOp("+",Id("b"),IntLiteral(3))),Assign(ArrayCell(ArrayCell(Id("c"),[IntLiteral(2)]),[IntLiteral(3)]),BinaryOp("+",BinaryOp("-.",BinaryOp("+.",IntLiteral(5),FloatLiteral(10.2)),CallExpr(Id("func"),[Id("a"),Id("b"),Id("c")])),ArrayCell(Id("a"),[BinaryOp("+",BinaryOp("+",IntLiteral(2),CallExpr(Id("func"),[])),ArrayCell(Id("c"),[IntLiteral(4)]))])))]),BinaryOp("==",Id("x"),Id("y")))])],([],[]))])),FuncDecl(Id("abc"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None),VarDecl(Id("x"),[],None)],([],[Dowhile(([],[CallStmt(Id("foods"),[Id("a"),Id("v"),Id("t")])]),BinaryOp("+",Id("x"),Id("y")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test_373(self):
        input = """
        Var: a = True, d;
        Function: foods
        Parameter: a[123], b
        Body:
            If a[12] > b Then
                Do 
                    Var: a = True, d;
                    a = (b + 3 - c * d >. 5) || (b-d<.10); 
                    c[2][3] = 5+.10.2-.func(a,b,c)+a[2+func()+c[4]]; 
                While (x == y)  EndDo.
            EndIf.
        EndBody.
        Function: abc
        Parameter: a[123], b , x
        Body:
            Do 
                foods(a,v,t);
            While x+y EndDo.
        EndBody.
        """
        expect = Program([VarDecl(Id("a"),[],BooleanLiteral(True)),VarDecl(Id("d"),[],None),FuncDecl(Id("foods"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None)],([],[If([(BinaryOp(">",ArrayCell(Id("a"),[IntLiteral(12)]),Id("b")),[],[Dowhile(([VarDecl(Id("a"),[],BooleanLiteral(True)),VarDecl(Id("d"),[],None)],[Assign(Id("a"),BinaryOp("||",BinaryOp(">.",BinaryOp("-",BinaryOp("+",Id("b"),IntLiteral(3)),BinaryOp("*",Id("c"),Id("d"))),IntLiteral(5)),BinaryOp("<.",BinaryOp("-",Id("b"),Id("d")),IntLiteral(10)))),Assign(ArrayCell(ArrayCell(Id("c"),[IntLiteral(2)]),[IntLiteral(3)]),BinaryOp("+",BinaryOp("-.",BinaryOp("+.",IntLiteral(5),FloatLiteral(10.2)),CallExpr(Id("func"),[Id("a"),Id("b"),Id("c")])),ArrayCell(Id("a"),[BinaryOp("+",BinaryOp("+",IntLiteral(2),CallExpr(Id("func"),[])),ArrayCell(Id("c"),[IntLiteral(4)]))])))]),BinaryOp("==",Id("x"),Id("y")))])],([],[]))])),FuncDecl(Id("abc"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None),VarDecl(Id("x"),[],None)],([],[Dowhile(([],[CallStmt(Id("foods"),[Id("a"),Id("v"),Id("t")])]),BinaryOp("+",Id("x"),Id("y")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))
    
    def test_374(self):
        input = """
        Var: a = True, d;
        Function: foods
        Parameter: a[123], b
        Body:
            If a[12] > b Then
                Do 
                    Var: a = True, d;
                    a = (b + 3 - c * d =/= 5) || (b-d<.10); 
                    c[2][3] = 5\\10.2\\.func(a,b,c)+a[2+func()+c[4]]; 
                While (x == y)  EndDo.
            EndIf.
        EndBody.
        Function: abc
        Parameter: a[123], b , x
        Body:
            Do 
                foods(a,v,t);
            While x+y EndDo.
        EndBody.
        """
        expect = Program([VarDecl(Id("a"),[],BooleanLiteral(True)),VarDecl(Id("d"),[],None),FuncDecl(Id("foods"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None)],([],[If([(BinaryOp(">",ArrayCell(Id("a"),[IntLiteral(12)]),Id("b")),[],[Dowhile(([VarDecl(Id("a"),[],BooleanLiteral(True)),VarDecl(Id("d"),[],None)],[Assign(Id("a"),BinaryOp("||",BinaryOp("=/=",BinaryOp("-",BinaryOp("+",Id("b"),IntLiteral(3)),BinaryOp("*",Id("c"),Id("d"))),IntLiteral(5)),BinaryOp("<.",BinaryOp("-",Id("b"),Id("d")),IntLiteral(10)))),Assign(ArrayCell(ArrayCell(Id("c"),[IntLiteral(2)]),[IntLiteral(3)]),BinaryOp("+",BinaryOp("\.",BinaryOp("\\",IntLiteral(5),FloatLiteral(10.2)),CallExpr(Id("func"),[Id("a"),Id("b"),Id("c")])),ArrayCell(Id("a"),[BinaryOp("+",BinaryOp("+",IntLiteral(2),CallExpr(Id("func"),[])),ArrayCell(Id("c"),[IntLiteral(4)]))])))]),BinaryOp("==",Id("x"),Id("y")))])],([],[]))])),FuncDecl(Id("abc"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None),VarDecl(Id("x"),[],None)],([],[Dowhile(([],[CallStmt(Id("foods"),[Id("a"),Id("v"),Id("t")])]),BinaryOp("+",Id("x"),Id("y")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test_375(self):
        input = """
        Var: a = True, d = "string\'\"";
        **this  is comment**
        Function: abc
        Parameter: a[123], b , x
        Body:
            Do 
                foods(a,v,t);
            While x+y EndDo.
        EndBody.
        """
        expect = Program([VarDecl(Id("a"),[],BooleanLiteral(True)),VarDecl(Id("d"),[],StringLiteral("string\'\"")),FuncDecl(Id("abc"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None),VarDecl(Id("x"),[],None)],([],[Dowhile(([],[CallStmt(Id("foods"),[Id("a"),Id("v"),Id("t")])]),BinaryOp("+",Id("x"),Id("y")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))
    def test_376(self):
        input = """
        Var: a = True, d = "string\\b";
        **this  is comment**
        Function: abc
        Parameter: a[123], b , x
        Body:
            Do 
                foods(a,v,t);
            While x+y EndDo.
        EndBody.
        """
        expect = Program([VarDecl(Id("a"),[],BooleanLiteral(True)),VarDecl(Id("d"),[],StringLiteral("string\\b")),FuncDecl(Id("abc"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None),VarDecl(Id("x"),[],None)],([],[Dowhile(([],[CallStmt(Id("foods"),[Id("a"),Id("v"),Id("t")])]),BinaryOp("+",Id("x"),Id("y")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))
    def test_377(self):
        input = """
        Var: a = True, d = "string\\b";
        **this  is comment**
        Function: abc
        Parameter: a[123], b , x
        Body:
            For (i=0,i<=10,i+1) Do
                foods(a,v,t);
            EndFor.
        EndBody.
        """
        expect = Program([VarDecl(Id("a"),[],BooleanLiteral(True)),VarDecl(Id("d"),[],StringLiteral("string\\b")),FuncDecl(Id("abc"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None),VarDecl(Id("x"),[],None)],([],[For(Id("i"),IntLiteral(0),BinaryOp("<=",Id("i"),IntLiteral(10)),BinaryOp("+",Id("i"),IntLiteral(1)),([],[CallStmt(Id("foods"),[Id("a"),Id("v"),Id("t")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))
    
    def test_378(self):
        input = """
        Var: a = True, d = "string\\b";
        **this  is comment**
        Function: abc
        Parameter: a[123], b , x
        Body:
            If 1 Then
                foods(a,v,t);
            EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id("a"),[],BooleanLiteral(True)),VarDecl(Id("d"),[],StringLiteral("string\\b")),FuncDecl(Id("abc"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None),VarDecl(Id("x"),[],None)],([],[If([(IntLiteral(1),[],[CallStmt(Id("foods"),[Id("a"),Id("v"),Id("t")])])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))
    
    def test_379(self):
        input = """
        Function: abc
        Parameter: a[123], b , x
        Body:
            a = !((-.2.0 + 3 * func() \\. 100.0 % arr[300] > 10)|| (-(a*.5-2))=/=10);
        EndBody.
        """
        expect = Program([FuncDecl(Id("abc"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None),VarDecl(Id("x"),[],None)],([],[Assign(Id("a"),UnaryOp("!",BinaryOp("=/=",BinaryOp("||",BinaryOp(">",BinaryOp("+",UnaryOp("-.",FloatLiteral(2.0)),BinaryOp("%",BinaryOp("\.",BinaryOp("*",IntLiteral(3),CallExpr(Id("func"),[])),FloatLiteral(100.0)),ArrayCell(Id("arr"),[IntLiteral(300)]))),IntLiteral(10)),UnaryOp("-",BinaryOp("-",BinaryOp("*.",Id("a"),IntLiteral(5)),IntLiteral(2)))),IntLiteral(10))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))
    def test_380(self):
        input = """
        Function: abc_323GAGD
        Parameter: a[123], b , x
        Body:
            a = !((-.2.0 + 3 * func() \\. 100.0 % arr[300] > 10)|| (-(a*.5-2))=/=10);
            arr[3] = {123,{True,"string"}};
            If a > 10 Then
                For (i =i+10,a-3,4+6) Do
                    Do 
                        Var: x;
                        x = 10;
                        i = 1+a*.x-y;
                        While a == 100 Do
                            func(---.---1);
                        EndWhile.
                    While !(10>100) || (99+100 > "act" * func(a[123])) EndDo.
                    
                EndFor.
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("abc_323GAGD"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None),VarDecl(Id("x"),[],None)],([],[Assign(Id("a"),UnaryOp("!",BinaryOp("=/=",BinaryOp("||",BinaryOp(">",BinaryOp("+",UnaryOp("-.",FloatLiteral(2.0)),BinaryOp("%",BinaryOp("\.",BinaryOp("*",IntLiteral(3),CallExpr(Id("func"),[])),FloatLiteral(100.0)),ArrayCell(Id("arr"),[IntLiteral(300)]))),IntLiteral(10)),UnaryOp("-",BinaryOp("-",BinaryOp("*.",Id("a"),IntLiteral(5)),IntLiteral(2)))),IntLiteral(10)))),Assign(ArrayCell(Id("arr"),[IntLiteral(3)]),ArrayLiteral([IntLiteral(123),ArrayLiteral([BooleanLiteral(True),StringLiteral("string")])])),If([(BinaryOp(">",Id("a"),IntLiteral(10)),[],[For(Id("i"),BinaryOp("+",Id("i"),IntLiteral(10)),BinaryOp("-",Id("a"),IntLiteral(3)),BinaryOp("+",IntLiteral(4),IntLiteral(6)),([],[Dowhile(([VarDecl(Id("x"),[],None)],[Assign(Id("x"),IntLiteral(10)),Assign(Id("i"),BinaryOp("-",BinaryOp("+",IntLiteral(1),BinaryOp("*.",Id("a"),Id("x"))),Id("y"))),While(BinaryOp("==",Id("a"),IntLiteral(100)),([],[CallStmt(Id("func"),[UnaryOp("-",UnaryOp("-",UnaryOp("-.",UnaryOp("-",UnaryOp("-",UnaryOp("-",IntLiteral(1)))))))])]))]),BinaryOp("||",UnaryOp("!",BinaryOp(">",IntLiteral(10),IntLiteral(100))),BinaryOp(">",BinaryOp("+",IntLiteral(99),IntLiteral(100)),BinaryOp("*",StringLiteral("act"),CallExpr(Id("func"),[ArrayCell(Id("a"),[IntLiteral(123)])])))))]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))
    def test_381(self):
        input = """
        Function: abc_323GAGD
        Parameter: a[123], b , x
        Body:
            a = !((-.2.0 + 3 * func() \\. 100.0 % arr[300] > 10)|| (-(a*.5-2))=/=10);
            If a > 10 Then
                For (i =i+10,a-3,4+6) Do
                    Do 
                        Var: x;
                        If abc == 100 Then
                        ElseIf 9 == 10 Then 
                        ElseIf a == "string" Then
                        Else a=100;
                        EndIf. 
                        x = 10;
                        i = 1+a*.x-y;
                        While a == 100 Do
                            func(---.---1);
                        EndWhile.
                    While !(10>100) || (99+100 > "act" * func(a[123])) EndDo.
                    
                EndFor.
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("abc_323GAGD"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None),VarDecl(Id("x"),[],None)],([],[Assign(Id("a"),UnaryOp("!",BinaryOp("=/=",BinaryOp("||",BinaryOp(">",BinaryOp("+",UnaryOp("-.",FloatLiteral(2.0)),BinaryOp("%",BinaryOp("\.",BinaryOp("*",IntLiteral(3),CallExpr(Id("func"),[])),FloatLiteral(100.0)),ArrayCell(Id("arr"),[IntLiteral(300)]))),IntLiteral(10)),UnaryOp("-",BinaryOp("-",BinaryOp("*.",Id("a"),IntLiteral(5)),IntLiteral(2)))),IntLiteral(10)))),If([(BinaryOp(">",Id("a"),IntLiteral(10)),[],[For(Id("i"),BinaryOp("+",Id("i"),IntLiteral(10)),BinaryOp("-",Id("a"),IntLiteral(3)),BinaryOp("+",IntLiteral(4),IntLiteral(6)),([],[Dowhile(([VarDecl(Id("x"),[],None)],[If([(BinaryOp("==",Id("abc"),IntLiteral(100)),[],[]),(BinaryOp("==",IntLiteral(9),IntLiteral(10)),[],[]),(BinaryOp("==",Id("a"),StringLiteral("string")),[],[])],([],[Assign(Id("a"),IntLiteral(100))])),Assign(Id("x"),IntLiteral(10)),Assign(Id("i"),BinaryOp("-",BinaryOp("+",IntLiteral(1),BinaryOp("*.",Id("a"),Id("x"))),Id("y"))),While(BinaryOp("==",Id("a"),IntLiteral(100)),([],[CallStmt(Id("func"),[UnaryOp("-",UnaryOp("-",UnaryOp("-.",UnaryOp("-",UnaryOp("-",UnaryOp("-",IntLiteral(1)))))))])]))]),BinaryOp("||",UnaryOp("!",BinaryOp(">",IntLiteral(10),IntLiteral(100))),BinaryOp(">",BinaryOp("+",IntLiteral(99),IntLiteral(100)),BinaryOp("*",StringLiteral("act"),CallExpr(Id("func"),[ArrayCell(Id("a"),[IntLiteral(123)])])))))]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test_382(self):
        input = """
        Function: abc_323GAGD
        Parameter: a[123], b , x
        Body:
            a = !((-.2.0 + 3 * func() \\. 100.0 % arr[300] > 10)|| (-(a*.5-2))=/=10);
            If a > 10 Then
                For (i =i+10,a-3,4+6) Do
                    Do 
                        Var: x;
                        If abc == 100 Then
                        ElseIf 9 == 10 Then 
                        ElseIf "string" Then
                        Else a=100;
                        EndIf. 
                        x = 10;
                        i = 1+a*.x-y;
                        While a == 100 Do
                            func(---.---1);
                        EndWhile.
                    While !(10>100) || (99+100 > "act" * func(a[123])) EndDo.
                    
                EndFor.
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("abc_323GAGD"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None),VarDecl(Id("x"),[],None)],([],[Assign(Id("a"),UnaryOp("!",BinaryOp("=/=",BinaryOp("||",BinaryOp(">",BinaryOp("+",UnaryOp("-.",FloatLiteral(2.0)),BinaryOp("%",BinaryOp("\.",BinaryOp("*",IntLiteral(3),CallExpr(Id("func"),[])),FloatLiteral(100.0)),ArrayCell(Id("arr"),[IntLiteral(300)]))),IntLiteral(10)),UnaryOp("-",BinaryOp("-",BinaryOp("*.",Id("a"),IntLiteral(5)),IntLiteral(2)))),IntLiteral(10)))),If([(BinaryOp(">",Id("a"),IntLiteral(10)),[],[For(Id("i"),BinaryOp("+",Id("i"),IntLiteral(10)),BinaryOp("-",Id("a"),IntLiteral(3)),BinaryOp("+",IntLiteral(4),IntLiteral(6)),([],[Dowhile(([VarDecl(Id("x"),[],None)],[If([(BinaryOp("==",Id("abc"),IntLiteral(100)),[],[]),(BinaryOp("==",IntLiteral(9),IntLiteral(10)),[],[]),(StringLiteral("string"),[],[])],([],[Assign(Id("a"),IntLiteral(100))])),Assign(Id("x"),IntLiteral(10)),Assign(Id("i"),BinaryOp("-",BinaryOp("+",IntLiteral(1),BinaryOp("*.",Id("a"),Id("x"))),Id("y"))),While(BinaryOp("==",Id("a"),IntLiteral(100)),([],[CallStmt(Id("func"),[UnaryOp("-",UnaryOp("-",UnaryOp("-.",UnaryOp("-",UnaryOp("-",UnaryOp("-",IntLiteral(1)))))))])]))]),BinaryOp("||",UnaryOp("!",BinaryOp(">",IntLiteral(10),IntLiteral(100))),BinaryOp(">",BinaryOp("+",IntLiteral(99),IntLiteral(100)),BinaryOp("*",StringLiteral("act"),CallExpr(Id("func"),[ArrayCell(Id("a"),[IntLiteral(123)])])))))]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))
    def test_383(self):
        input = """
        Function: abc_323GAGD
        Parameter: a[123], b , x
        Body:
            a = !((-.2.0 + 3 * func() \\. 100.0 % arr[300] > 10)|| (-(a*.5-2))=/=10);
            If a > 10 Then
                For (i =i+10,a-3,4+6) Do
                    Do 
                        Var: x;
                        If abc == 100 Then
                        ElseIf 9 == 10 Then 
                        ElseIf "string" Then
                        Else a=100;
                        EndIf. 
                        x = 10;
                        i = 1+a*.x-y;
                        While a == 100 Do
                        EndWhile.
                    While !(10>100) || (99+100 > "act" * func(a[123])) EndDo.
                    
                EndFor.
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("abc_323GAGD"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None),VarDecl(Id("x"),[],None)],([],[Assign(Id("a"),UnaryOp("!",BinaryOp("=/=",BinaryOp("||",BinaryOp(">",BinaryOp("+",UnaryOp("-.",FloatLiteral(2.0)),BinaryOp("%",BinaryOp("\.",BinaryOp("*",IntLiteral(3),CallExpr(Id("func"),[])),FloatLiteral(100.0)),ArrayCell(Id("arr"),[IntLiteral(300)]))),IntLiteral(10)),UnaryOp("-",BinaryOp("-",BinaryOp("*.",Id("a"),IntLiteral(5)),IntLiteral(2)))),IntLiteral(10)))),If([(BinaryOp(">",Id("a"),IntLiteral(10)),[],[For(Id("i"),BinaryOp("+",Id("i"),IntLiteral(10)),BinaryOp("-",Id("a"),IntLiteral(3)),BinaryOp("+",IntLiteral(4),IntLiteral(6)),([],[Dowhile(([VarDecl(Id("x"),[],None)],[If([(BinaryOp("==",Id("abc"),IntLiteral(100)),[],[]),(BinaryOp("==",IntLiteral(9),IntLiteral(10)),[],[]),(StringLiteral("string"),[],[])],([],[Assign(Id("a"),IntLiteral(100))])),Assign(Id("x"),IntLiteral(10)),Assign(Id("i"),BinaryOp("-",BinaryOp("+",IntLiteral(1),BinaryOp("*.",Id("a"),Id("x"))),Id("y"))),While(BinaryOp("==",Id("a"),IntLiteral(100)),([],[]))]),BinaryOp("||",UnaryOp("!",BinaryOp(">",IntLiteral(10),IntLiteral(100))),BinaryOp(">",BinaryOp("+",IntLiteral(99),IntLiteral(100)),BinaryOp("*",StringLiteral("act"),CallExpr(Id("func"),[ArrayCell(Id("a"),[IntLiteral(123)])])))))]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))
    def test_384(self):
        input = """
        Function: abc_323GAGD
        Parameter: a[123], b , x
        Body:
            a = !((-.2.0 + 3 * func() \\. 100.0 % arr[300] > 10)|| (-(a*.5-2))=/=10);
            If a > 10 Then
                For (i =i+10,a-3,4+6) Do
                    Do 
                        Var: x;
                        If abc == 100 Then
                        ElseIf 9 == 10 Then 
                        ElseIf "string" Then
                        Else a=100;
                        EndIf. 
                        x = 10;
                        i = 1+a*.x-y;
                        While a == 100 Do
                        EndWhile.
                    While !(10>100) || (99+100 > "act" * func(a[123])) EndDo.
                    
                EndFor.
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("abc_323GAGD"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None),VarDecl(Id("x"),[],None)],([],[Assign(Id("a"),UnaryOp("!",BinaryOp("=/=",BinaryOp("||",BinaryOp(">",BinaryOp("+",UnaryOp("-.",FloatLiteral(2.0)),BinaryOp("%",BinaryOp("\.",BinaryOp("*",IntLiteral(3),CallExpr(Id("func"),[])),FloatLiteral(100.0)),ArrayCell(Id("arr"),[IntLiteral(300)]))),IntLiteral(10)),UnaryOp("-",BinaryOp("-",BinaryOp("*.",Id("a"),IntLiteral(5)),IntLiteral(2)))),IntLiteral(10)))),If([(BinaryOp(">",Id("a"),IntLiteral(10)),[],[For(Id("i"),BinaryOp("+",Id("i"),IntLiteral(10)),BinaryOp("-",Id("a"),IntLiteral(3)),BinaryOp("+",IntLiteral(4),IntLiteral(6)),([],[Dowhile(([VarDecl(Id("x"),[],None)],[If([(BinaryOp("==",Id("abc"),IntLiteral(100)),[],[]),(BinaryOp("==",IntLiteral(9),IntLiteral(10)),[],[]),(StringLiteral("string"),[],[])],([],[Assign(Id("a"),IntLiteral(100))])),Assign(Id("x"),IntLiteral(10)),Assign(Id("i"),BinaryOp("-",BinaryOp("+",IntLiteral(1),BinaryOp("*.",Id("a"),Id("x"))),Id("y"))),While(BinaryOp("==",Id("a"),IntLiteral(100)),([],[]))]),BinaryOp("||",UnaryOp("!",BinaryOp(">",IntLiteral(10),IntLiteral(100))),BinaryOp(">",BinaryOp("+",IntLiteral(99),IntLiteral(100)),BinaryOp("*",StringLiteral("act"),CallExpr(Id("func"),[ArrayCell(Id("a"),[IntLiteral(123)])])))))]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))
    def test_385(self):
        input = """
        Function: abc_323GAGD
        Parameter: a[123], b , x
        Body:
            a = !((-.2.0 + 3 * func() \\. 100.0 % arr[300] > 10)|| (-(a*.5-2))=/=10);
            If a > 10 Then
                For (i =i+10,a-3,4+6) Do
                    Do 
                        
                    While !(10>100) || (99+100 > "act" * func(a[123])) EndDo.
                    
                EndFor.
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("abc_323GAGD"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None),VarDecl(Id("x"),[],None)],([],[Assign(Id("a"),UnaryOp("!",BinaryOp("=/=",BinaryOp("||",BinaryOp(">",BinaryOp("+",UnaryOp("-.",FloatLiteral(2.0)),BinaryOp("%",BinaryOp("\.",BinaryOp("*",IntLiteral(3),CallExpr(Id("func"),[])),FloatLiteral(100.0)),ArrayCell(Id("arr"),[IntLiteral(300)]))),IntLiteral(10)),UnaryOp("-",BinaryOp("-",BinaryOp("*.",Id("a"),IntLiteral(5)),IntLiteral(2)))),IntLiteral(10)))),If([(BinaryOp(">",Id("a"),IntLiteral(10)),[],[For(Id("i"),BinaryOp("+",Id("i"),IntLiteral(10)),BinaryOp("-",Id("a"),IntLiteral(3)),BinaryOp("+",IntLiteral(4),IntLiteral(6)),([],[Dowhile(([],[]),BinaryOp("||",UnaryOp("!",BinaryOp(">",IntLiteral(10),IntLiteral(100))),BinaryOp(">",BinaryOp("+",IntLiteral(99),IntLiteral(100)),BinaryOp("*",StringLiteral("act"),CallExpr(Id("func"),[ArrayCell(Id("a"),[IntLiteral(123)])])))))]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))
    
    def test_386(self):
        input = """
        Function: abc_323GAGD
        Parameter: a[123], b , x
        Body:
            a = !((-.2.0 + 3 * func() \\. 100.0 % arr[300] > 10)|| (-(a*.5-2))=/=10);
            If a > 10 Then
                For (i =i+10,a-3,4+6) Do
                
                EndFor.
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("abc_323GAGD"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None),VarDecl(Id("x"),[],None)],([],[Assign(Id("a"),UnaryOp("!",BinaryOp("=/=",BinaryOp("||",BinaryOp(">",BinaryOp("+",UnaryOp("-.",FloatLiteral(2.0)),BinaryOp("%",BinaryOp("\.",BinaryOp("*",IntLiteral(3),CallExpr(Id("func"),[])),FloatLiteral(100.0)),ArrayCell(Id("arr"),[IntLiteral(300)]))),IntLiteral(10)),UnaryOp("-",BinaryOp("-",BinaryOp("*.",Id("a"),IntLiteral(5)),IntLiteral(2)))),IntLiteral(10)))),If([(BinaryOp(">",Id("a"),IntLiteral(10)),[],[For(Id("i"),BinaryOp("+",Id("i"),IntLiteral(10)),BinaryOp("-",Id("a"),IntLiteral(3)),BinaryOp("+",IntLiteral(4),IntLiteral(6)),([],[]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))
    def test_387(self):
        input = """
        Function: abc_323GAGD
        Parameter: a[123], b , x
        Body:
            a = !((-.2.0 + 3 * func() \\. 100.0 % arr[300] > 10)|| (-(a*.5-2))=/=10);
            If a > 10 Then
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("abc_323GAGD"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None),VarDecl(Id("x"),[],None)],([],[Assign(Id("a"),UnaryOp("!",BinaryOp("=/=",BinaryOp("||",BinaryOp(">",BinaryOp("+",UnaryOp("-.",FloatLiteral(2.0)),BinaryOp("%",BinaryOp("\.",BinaryOp("*",IntLiteral(3),CallExpr(Id("func"),[])),FloatLiteral(100.0)),ArrayCell(Id("arr"),[IntLiteral(300)]))),IntLiteral(10)),UnaryOp("-",BinaryOp("-",BinaryOp("*.",Id("a"),IntLiteral(5)),IntLiteral(2)))),IntLiteral(10)))),If([(BinaryOp(">",Id("a"),IntLiteral(10)),[],[])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))
    def test_388(self):
        input = """
        Function: abc_323GAGD
        Parameter: a[123], b , x
        Body:
            
        EndBody.
        """
        expect = Program([FuncDecl(Id("abc_323GAGD"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None),VarDecl(Id("x"),[],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))
    def test_389(self):
        input = """
        Function: main
        Body:
            
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))
    
    
    def test_390(self):
        input = """
        Var: a[1][2] = {123,{1.25E-36,1.25E+36}};
        Function: main
        Parameter: a[123], b , x
        Body:
            
        EndBody.
        """
        expect = Program([VarDecl(Id("a"),[1,2],ArrayLiteral([IntLiteral(123),ArrayLiteral([FloatLiteral(1.25e-36),FloatLiteral(1.25e+36)])])),FuncDecl(Id("main"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None),VarDecl(Id("x"),[],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))
    
    def test_391(self):
        input = """
        Var: a[1][2] = {0xABC,{1.25E-36,1.25E+36}};
        Function: main
        Parameter: a[123], b , x
        Body:
            
        EndBody.
        """
        expect = Program([VarDecl(Id("a"),[1,2],ArrayLiteral([IntLiteral(2748),ArrayLiteral([FloatLiteral(1.25e-36),FloatLiteral(1.25e+36)])])),FuncDecl(Id("main"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None),VarDecl(Id("x"),[],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))
    def test_392(self):
        input = """
        Var: a[1][2] = {0o7012,{1.25E-36,1.25E+36}};
        Function: main
        Parameter: a[123], b , x
        Body:
            
        EndBody.
        """
        expect = Program([VarDecl(Id("a"),[1,2],ArrayLiteral([IntLiteral(3594),ArrayLiteral([FloatLiteral(1.25e-36),FloatLiteral(1.25e+36)])])),FuncDecl(Id("main"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None),VarDecl(Id("x"),[],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))
    
    def test_393(self):
        input = """
        Var: a[1][0xABC] = {0o7023,{1.25E-36,1.25E+36}};
        Function: main
        Parameter: a[123], b , x
        Body:
            
        EndBody.
        """
        expect = Program([VarDecl(Id("a"),[1,2748],ArrayLiteral([IntLiteral(3603),ArrayLiteral([FloatLiteral(1.25e-36),FloatLiteral(1.25e+36)])])),FuncDecl(Id("main"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None),VarDecl(Id("x"),[],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))
    def test_394(self):
        input = """
        Var: a[1][0xABC] = {0o7023,{1.25E-36,1.25E+36}};
        Function: main
        Parameter: a[123], b , x
        Body:
            a = !((-.2.0 + 3 * func() \\. 100.0 % arr[300] > 10)|| (-(a*.5-2))=/=10);
            If a > 10 Then
                For (i =i+10,a-3,4+6) Do
                    Do 
                        a = b+-5;
                    While !(10>100) || (99+100 > "act" * func(a[123])) EndDo.
                    
                EndFor.
            EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id("a"),[1,2748],ArrayLiteral([IntLiteral(3603),ArrayLiteral([FloatLiteral(1.25e-36),FloatLiteral(1.25e+36)])])),FuncDecl(Id("main"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None),VarDecl(Id("x"),[],None)],([],[Assign(Id("a"),UnaryOp("!",BinaryOp("=/=",BinaryOp("||",BinaryOp(">",BinaryOp("+",UnaryOp("-.",FloatLiteral(2.0)),BinaryOp("%",BinaryOp("\.",BinaryOp("*",IntLiteral(3),CallExpr(Id("func"),[])),FloatLiteral(100.0)),ArrayCell(Id("arr"),[IntLiteral(300)]))),IntLiteral(10)),UnaryOp("-",BinaryOp("-",BinaryOp("*.",Id("a"),IntLiteral(5)),IntLiteral(2)))),IntLiteral(10)))),If([(BinaryOp(">",Id("a"),IntLiteral(10)),[],[For(Id("i"),BinaryOp("+",Id("i"),IntLiteral(10)),BinaryOp("-",Id("a"),IntLiteral(3)),BinaryOp("+",IntLiteral(4),IntLiteral(6)),([],[Dowhile(([],[Assign(Id("a"),BinaryOp("+",Id("b"),UnaryOp("-",IntLiteral(5))))]),BinaryOp("||",UnaryOp("!",BinaryOp(">",IntLiteral(10),IntLiteral(100))),BinaryOp(">",BinaryOp("+",IntLiteral(99),IntLiteral(100)),BinaryOp("*",StringLiteral("act"),CallExpr(Id("func"),[ArrayCell(Id("a"),[IntLiteral(123)])])))))]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))
    def test_395(self):
        input = """
        Var: a[1][0xABC] = {0o7023,{1.25E-36,1.25E+36}};
        Function: main
        Parameter: a[123], b , x
        Body:
            a = !((-.2.0 + 3 * func() \\. 100.0 % arr[300] > 10)|| (-(a*.5-2))=/=10);
            If a > 10 Then
                For (i =i+10,a-3,4+6) Do
                    Do 
                        a = !((-.2.0 + 3 * func()));
                    While !(10>100) || (99+100 > "act" * func(a[123])) EndDo.
                EndFor.
            EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id("a"),[1,2748],ArrayLiteral([IntLiteral(3603),ArrayLiteral([FloatLiteral(1.25e-36),FloatLiteral(1.25e+36)])])),FuncDecl(Id("main"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None),VarDecl(Id("x"),[],None)],([],[Assign(Id("a"),UnaryOp("!",BinaryOp("=/=",BinaryOp("||",BinaryOp(">",BinaryOp("+",UnaryOp("-.",FloatLiteral(2.0)),BinaryOp("%",BinaryOp("\.",BinaryOp("*",IntLiteral(3),CallExpr(Id("func"),[])),FloatLiteral(100.0)),ArrayCell(Id("arr"),[IntLiteral(300)]))),IntLiteral(10)),UnaryOp("-",BinaryOp("-",BinaryOp("*.",Id("a"),IntLiteral(5)),IntLiteral(2)))),IntLiteral(10)))),If([(BinaryOp(">",Id("a"),IntLiteral(10)),[],[For(Id("i"),BinaryOp("+",Id("i"),IntLiteral(10)),BinaryOp("-",Id("a"),IntLiteral(3)),BinaryOp("+",IntLiteral(4),IntLiteral(6)),([],[Dowhile(([],[Assign(Id("a"),UnaryOp("!",BinaryOp("+",UnaryOp("-.",FloatLiteral(2.0)),BinaryOp("*",IntLiteral(3),CallExpr(Id("func"),[])))))]),BinaryOp("||",UnaryOp("!",BinaryOp(">",IntLiteral(10),IntLiteral(100))),BinaryOp(">",BinaryOp("+",IntLiteral(99),IntLiteral(100)),BinaryOp("*",StringLiteral("act"),CallExpr(Id("func"),[ArrayCell(Id("a"),[IntLiteral(123)])])))))]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))
    
    def test_396(self):
        input = """
        
        Function: main
        Parameter: a[123], b , x
        Body:
            Var: a[1][0xABC] = {0o7023,{1.25E-36,1.25E+36}};
            a = !((-.2.0 + 3 * func() \\. 100.0 % arr[300] > 10)|| (-(a*.5-2))=/=10);
            If a > 10 Then
                For (i =i+10,a-3,4+6) Do
                    Do 
                        a = !((-.2.0 + 3 * func()));
                    While !(10>100) || (99+100 > "act" * func(a[123])) EndDo.
                EndFor.
            EndIf.
        EndBody.
        Function: main
        Parameter: a[123], b , x
        Body:
            a = !((-.2.0 + 3 * func() \\. 100.0 % arr[300] > 10)|| (-(a*.5-2))=/=10);
            If a > 10 Then
                For (i =i+10,a-3,4+6) Do
                    Do 
                        a = !((-.2.0 + 3 * func()));
                        Break;
                    While !(10>100) || (99+100 > "act" * func(a[123])) EndDo.
                EndFor.
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None),VarDecl(Id("x"),[],None)],([VarDecl(Id("a"),[1,2748],ArrayLiteral([IntLiteral(3603),ArrayLiteral([FloatLiteral(1.25e-36),FloatLiteral(1.25e+36)])]))],[Assign(Id("a"),UnaryOp("!",BinaryOp("=/=",BinaryOp("||",BinaryOp(">",BinaryOp("+",UnaryOp("-.",FloatLiteral(2.0)),BinaryOp("%",BinaryOp("\.",BinaryOp("*",IntLiteral(3),CallExpr(Id("func"),[])),FloatLiteral(100.0)),ArrayCell(Id("arr"),[IntLiteral(300)]))),IntLiteral(10)),UnaryOp("-",BinaryOp("-",BinaryOp("*.",Id("a"),IntLiteral(5)),IntLiteral(2)))),IntLiteral(10)))),If([(BinaryOp(">",Id("a"),IntLiteral(10)),[],[For(Id("i"),BinaryOp("+",Id("i"),IntLiteral(10)),BinaryOp("-",Id("a"),IntLiteral(3)),BinaryOp("+",IntLiteral(4),IntLiteral(6)),([],[Dowhile(([],[Assign(Id("a"),UnaryOp("!",BinaryOp("+",UnaryOp("-.",FloatLiteral(2.0)),BinaryOp("*",IntLiteral(3),CallExpr(Id("func"),[])))))]),BinaryOp("||",UnaryOp("!",BinaryOp(">",IntLiteral(10),IntLiteral(100))),BinaryOp(">",BinaryOp("+",IntLiteral(99),IntLiteral(100)),BinaryOp("*",StringLiteral("act"),CallExpr(Id("func"),[ArrayCell(Id("a"),[IntLiteral(123)])])))))]))])],([],[]))])),FuncDecl(Id("main"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None),VarDecl(Id("x"),[],None)],([],[Assign(Id("a"),UnaryOp("!",BinaryOp("=/=",BinaryOp("||",BinaryOp(">",BinaryOp("+",UnaryOp("-.",FloatLiteral(2.0)),BinaryOp("%",BinaryOp("\.",BinaryOp("*",IntLiteral(3),CallExpr(Id("func"),[])),FloatLiteral(100.0)),ArrayCell(Id("arr"),[IntLiteral(300)]))),IntLiteral(10)),UnaryOp("-",BinaryOp("-",BinaryOp("*.",Id("a"),IntLiteral(5)),IntLiteral(2)))),IntLiteral(10)))),If([(BinaryOp(">",Id("a"),IntLiteral(10)),[],[For(Id("i"),BinaryOp("+",Id("i"),IntLiteral(10)),BinaryOp("-",Id("a"),IntLiteral(3)),BinaryOp("+",IntLiteral(4),IntLiteral(6)),([],[Dowhile(([],[Assign(Id("a"),UnaryOp("!",BinaryOp("+",UnaryOp("-.",FloatLiteral(2.0)),BinaryOp("*",IntLiteral(3),CallExpr(Id("func"),[]))))),Break()]),BinaryOp("||",UnaryOp("!",BinaryOp(">",IntLiteral(10),IntLiteral(100))),BinaryOp(">",BinaryOp("+",IntLiteral(99),IntLiteral(100)),BinaryOp("*",StringLiteral("act"),CallExpr(Id("func"),[ArrayCell(Id("a"),[IntLiteral(123)])])))))]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))

    def test_397(self):
        input = """
        Var: a[1][0xABC] = {0o7023,{1.25E-36,1.25E+36}};
        Function: main
        Parameter: a[123], b , x
        Body:
            a = !((-.2.0 + 3 * func() \\. 100.0 % arr[300] > 10)|| (-(a*.5-2))=/=10);
            If a > 10 Then
                If b % 10 Then 
                    a[b[e]] = 10;
                ElseIf c =/= 10e-10 Then
                    a = a[b[e]];
                ElseIf d == 100 Then
                Else
                    Var: a;
                    x = a\\.10;
                EndIf.
            EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id("a"),[1,2748],ArrayLiteral([IntLiteral(3603),ArrayLiteral([FloatLiteral(1.25e-36),FloatLiteral(1.25e+36)])])),FuncDecl(Id("main"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None),VarDecl(Id("x"),[],None)],([],[Assign(Id("a"),UnaryOp("!",BinaryOp("=/=",BinaryOp("||",BinaryOp(">",BinaryOp("+",UnaryOp("-.",FloatLiteral(2.0)),BinaryOp("%",BinaryOp("\.",BinaryOp("*",IntLiteral(3),CallExpr(Id("func"),[])),FloatLiteral(100.0)),ArrayCell(Id("arr"),[IntLiteral(300)]))),IntLiteral(10)),UnaryOp("-",BinaryOp("-",BinaryOp("*.",Id("a"),IntLiteral(5)),IntLiteral(2)))),IntLiteral(10)))),If([(BinaryOp(">",Id("a"),IntLiteral(10)),[],[If([(BinaryOp("%",Id("b"),IntLiteral(10)),[],[Assign(ArrayCell(Id("a"),[ArrayCell(Id("b"),[Id("e")])]),IntLiteral(10))]),(BinaryOp("=/=",Id("c"),FloatLiteral(1e-09)),[],[Assign(Id("a"),ArrayCell(Id("a"),[ArrayCell(Id("b"),[Id("e")])]))]),(BinaryOp("==",Id("d"),IntLiteral(100)),[],[])],([VarDecl(Id("a"),[],None)],[Assign(Id("x"),BinaryOp("\.",Id("a"),IntLiteral(10)))]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))
    def test_398(self):
        input = """
        Var: a[1][0xABC] = {0o7023,{1.25E-36,1.25E+36}};
        Function: main
        Parameter: a[123], b , x
        Body:
            a = !((-.2.0 + 3 * func() \\. 100.0 % arr[300] > 10)|| (-(a*.5-2))=/=10);
            If a > 10 Then
                If b % 10 Then 
                    a[b[e]] = 10;
                ElseIf c =/= 10e-10 Then
                    a = a[b[e]];
                    While 0 Do 
                        Continue;
                    EndWhile.
                ElseIf d == 100 Then
                Else
                    Var: a;
                    x = a\\.10;
                EndIf.
            EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id("a"),[1,2748],ArrayLiteral([IntLiteral(3603),ArrayLiteral([FloatLiteral(1.25e-36),FloatLiteral(1.25e+36)])])),FuncDecl(Id("main"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None),VarDecl(Id("x"),[],None)],([],[Assign(Id("a"),UnaryOp("!",BinaryOp("=/=",BinaryOp("||",BinaryOp(">",BinaryOp("+",UnaryOp("-.",FloatLiteral(2.0)),BinaryOp("%",BinaryOp("\.",BinaryOp("*",IntLiteral(3),CallExpr(Id("func"),[])),FloatLiteral(100.0)),ArrayCell(Id("arr"),[IntLiteral(300)]))),IntLiteral(10)),UnaryOp("-",BinaryOp("-",BinaryOp("*.",Id("a"),IntLiteral(5)),IntLiteral(2)))),IntLiteral(10)))),If([(BinaryOp(">",Id("a"),IntLiteral(10)),[],[If([(BinaryOp("%",Id("b"),IntLiteral(10)),[],[Assign(ArrayCell(Id("a"),[ArrayCell(Id("b"),[Id("e")])]),IntLiteral(10))]),(BinaryOp("=/=",Id("c"),FloatLiteral(1e-09)),[],[Assign(Id("a"),ArrayCell(Id("a"),[ArrayCell(Id("b"),[Id("e")])])),While(IntLiteral(0),([],[Continue()]))]),(BinaryOp("==",Id("d"),IntLiteral(100)),[],[])],([VarDecl(Id("a"),[],None)],[Assign(Id("x"),BinaryOp("\.",Id("a"),IntLiteral(10)))]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))
    def test_399(self):
        input = """
        Var: a[1][0xABC] = {0o7023,{1.25E-36,1.25E+36}};
        Function: main
        Parameter: a[123], b , x
        Body:
            a = !((-.2.0 + 3 * func() \\. 100.0 % arr[300] > 10)|| (-(a*.5-2))=/=10);
            If a > 10 Then
                If b % 10 Then 
                    a[b[e]] = 10;
                ElseIf c =/= 10e-10 Then
                    a = a[b[e]];
                    func(func(a[2][3]));
                ElseIf d == 100 Then
                Else
                    Var: a;
                    x = a\\.10;
                EndIf.
            EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id("a"),[1,2748],ArrayLiteral([IntLiteral(3603),ArrayLiteral([FloatLiteral(1.25e-36),FloatLiteral(1.25e+36)])])),FuncDecl(Id("main"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None),VarDecl(Id("x"),[],None)],([],[Assign(Id("a"),UnaryOp("!",BinaryOp("=/=",BinaryOp("||",BinaryOp(">",BinaryOp("+",UnaryOp("-.",FloatLiteral(2.0)),BinaryOp("%",BinaryOp("\.",BinaryOp("*",IntLiteral(3),CallExpr(Id("func"),[])),FloatLiteral(100.0)),ArrayCell(Id("arr"),[IntLiteral(300)]))),IntLiteral(10)),UnaryOp("-",BinaryOp("-",BinaryOp("*.",Id("a"),IntLiteral(5)),IntLiteral(2)))),IntLiteral(10)))),If([(BinaryOp(">",Id("a"),IntLiteral(10)),[],[If([(BinaryOp("%",Id("b"),IntLiteral(10)),[],[Assign(ArrayCell(Id("a"),[ArrayCell(Id("b"),[Id("e")])]),IntLiteral(10))]),(BinaryOp("=/=",Id("c"),FloatLiteral(1e-09)),[],[Assign(Id("a"),ArrayCell(Id("a"),[ArrayCell(Id("b"),[Id("e")])])),CallStmt(Id("func"),[CallExpr(Id("func"),[ArrayCell(ArrayCell(Id("a"),[IntLiteral(2)]),[IntLiteral(3)])])])]),(BinaryOp("==",Id("d"),IntLiteral(100)),[],[])],([VarDecl(Id("a"),[],None)],[Assign(Id("x"),BinaryOp("\.",Id("a"),IntLiteral(10)))]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))
    def test_400(self):
        input = """
        Var: a[1][0xABC] = {0o7023,{1.25E-36,1.25E+36}};
        Function: main
        Parameter: a[123], b , x
        Body:
            a = !((-.2.0 + 3 * func() \\. 100.0 % arr[300] > 10)|| (-(a*.5-2))=/=10);
            If a > 10 Then
                If b % 10 Then 
                    a[b[e]] = 10;
                ElseIf c =/= 10e-10 Then
                    a = a[b[e]];
                    Return func(func(a[2][3]));
                EndIf.
            EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id("a"),[1,2748],ArrayLiteral([IntLiteral(3603),ArrayLiteral([FloatLiteral(1.25e-36),FloatLiteral(1.25e+36)])])),FuncDecl(Id("main"),[VarDecl(Id("a"),[123],None),VarDecl(Id("b"),[],None),VarDecl(Id("x"),[],None)],([],[Assign(Id("a"),UnaryOp("!",BinaryOp("=/=",BinaryOp("||",BinaryOp(">",BinaryOp("+",UnaryOp("-.",FloatLiteral(2.0)),BinaryOp("%",BinaryOp("\.",BinaryOp("*",IntLiteral(3),CallExpr(Id("func"),[])),FloatLiteral(100.0)),ArrayCell(Id("arr"),[IntLiteral(300)]))),IntLiteral(10)),UnaryOp("-",BinaryOp("-",BinaryOp("*.",Id("a"),IntLiteral(5)),IntLiteral(2)))),IntLiteral(10)))),If([(BinaryOp(">",Id("a"),IntLiteral(10)),[],[If([(BinaryOp("%",Id("b"),IntLiteral(10)),[],[Assign(ArrayCell(Id("a"),[ArrayCell(Id("b"),[Id("e")])]),IntLiteral(10))]),(BinaryOp("=/=",Id("c"),FloatLiteral(1e-09)),[],[Assign(Id("a"),ArrayCell(Id("a"),[ArrayCell(Id("b"),[Id("e")])])),Return(CallExpr(Id("func"),[CallExpr(Id("func"),[ArrayCell(ArrayCell(Id("a"),[IntLiteral(2)]),[IntLiteral(3)])])]))])],([],[]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 400))
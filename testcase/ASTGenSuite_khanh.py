import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_00(self):
        """Simple program: int main() {} """
        input = """Var:x=5;"""
        expect = Program([VarDecl(Id("x"),[],IntLiteral(5))])
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_01(self):
        input = """
                    Var:abc, a[23]={{}, 654, "6396"};
                    Function: fas_cko_8rfkw
                        Parameter: a[15], q[68], acf5qf4_iuqw
                        Body:
                            Var: wf87[752]={};
                            Do
                                 Do
                                    Break;
                                    If True Then EndIf.
                                While (foo() -. 1.9e7 + "ekigk") EndDo.
                                    soooo(wfwe[234\\soo()]);
                            While (foo() -. 1.9e7 + "ekigk")  EndDo.
                        EndBody.
                """
        expect = Program([VarDecl(Id("abc"),[],None),VarDecl(Id("a"),[23],ArrayLiteral([ArrayLiteral([]),IntLiteral(654),StringLiteral("6396")])),FuncDecl(Id("fas_cko_8rfkw"),[VarDecl(Id("a"),[15],None),VarDecl(Id("q"),[68],None),VarDecl(Id("acf5qf4_iuqw"),[],None)],tuple([[VarDecl(Id("wf87"),[752],ArrayLiteral([]))],[Dowhile(tuple([[],[Dowhile(tuple([[],[Break(),If([tuple([BooleanLiteral(True),[],[]])],tuple([[],[]]))]]),BinaryOp("+",BinaryOp("-.",CallExpr(Id("foo"),[]),FloatLiteral(19000000.0)),StringLiteral("ekigk"))),CallStmt(Id("soooo"),[ArrayCell(Id("wfwe"),[BinaryOp("\\",IntLiteral(234),CallExpr(Id("soo"),[]))])])]]),BinaryOp("+",BinaryOp("-.",CallExpr(Id("foo"),[]),FloatLiteral(19000000.0)),StringLiteral("ekigk")))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_02(self):
        input = """
                    Var: a[5][6][23]={12,2,5,{65,9,5}};
                """
        expect = Program([VarDecl(Id("a"),[5,6,23],ArrayLiteral([IntLiteral(12),IntLiteral(2),IntLiteral(5),ArrayLiteral([IntLiteral(65),IntLiteral(9),IntLiteral(5)])]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_03(self):
        input = """
                    Var: xx;
                    Function:afc
                        Parameter: a
                        Body:
                            If {1,2,3}==True Then
                            dosomefckingthigs(some_param); EndIf.
                        EndBody.
                """
        expect = Program([VarDecl(Id("xx"),[],None),FuncDecl(Id("afc"),[VarDecl(Id("a"),[],None)],tuple([[],[If([tuple([BinaryOp("==",ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),BooleanLiteral(True)),[],[CallStmt(Id("dosomefckingthigs"),[Id("some_param")])]])],tuple([[],[]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_04(self):
        input = """
                    Var: awe,f,wef,we,a[4];
                    Function:zwt56dm
                        Parameter:s,nt,yh,y6r
                        Body:
                            If abcd+ foo() + a[foo()] Then
                                ElseIf st&&st Then ok_man();
                                EndIf.
                        EndBody.
                """
        expect = Program([VarDecl(Id("awe"),[],None),VarDecl(Id("f"),[],None),VarDecl(Id("wef"),[],None),VarDecl(Id("we"),[],None),VarDecl(Id("a"),[4],None),FuncDecl(Id("zwt56dm"),[VarDecl(Id("s"),[],None),VarDecl(Id("nt"),[],None),VarDecl(Id("yh"),[],None),VarDecl(Id("y6r"),[],None)],tuple([[],[If([tuple([BinaryOp("+",BinaryOp("+",Id("abcd"),CallExpr(Id("foo"),[])),ArrayCell(Id("a"),[CallExpr(Id("foo"),[])])),[],[]]),tuple([BinaryOp("&&",Id("st"),Id("st")),[],[CallStmt(Id("ok_man"),[])]])],tuple([[],[]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_05(self):
        input = """
                    Var: awe,f,wef,we,a[4];
                    Function:zwt56dm
                        Parameter:s,nt,yh,y6r
                        Body:
                            If abcd+ foo() + a[foo()] Then
                                    If fcking()-234>=.1.9+.34e4 Then kool();
                                    ElseIf abcd Then e=p+1;
                                    Else op();
                                    EndIf.
                                ElseIf st&&st Then ok_man();
                                EndIf.
                        EndBody.
                """
        expect = Program([VarDecl(Id("awe"),[],None),VarDecl(Id("f"),[],None),VarDecl(Id("wef"),[],None),VarDecl(Id("we"),[],None),VarDecl(Id("a"),[4],None),FuncDecl(Id("zwt56dm"),[VarDecl(Id("s"),[],None),VarDecl(Id("nt"),[],None),VarDecl(Id("yh"),[],None),VarDecl(Id("y6r"),[],None)],tuple([[],[If([tuple([BinaryOp("+",BinaryOp("+",Id("abcd"),CallExpr(Id("foo"),[])),ArrayCell(Id("a"),[CallExpr(Id("foo"),[])])),[],[If([tuple([BinaryOp(">=.",BinaryOp("-",CallExpr(Id("fcking"),[]),IntLiteral(234)),BinaryOp("+.",FloatLiteral(1.9),FloatLiteral(340000.0))),[],[CallStmt(Id("kool"),[])]]),tuple([Id("abcd"),[],[Assign(Id("e"),BinaryOp("+",Id("p"),IntLiteral(1)))]])],tuple([[],[CallStmt(Id("op"),[])]]))]]),tuple([BinaryOp("&&",Id("st"),Id("st")),[],[CallStmt(Id("ok_man"),[])]])],tuple([[],[]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_06(self):
        input = """
                    Var: awe,f,wef,we,a[4];
                    Function:zwt56dm
                        Parameter:s,nt,yh,y6r
                        Body:
                            If abcd+ foo() + a[foo()] Then
                                    If fcking()-234>=.1.9+.34e4 Then kool();
                                    ElseIf abcd Then e=p+1;
                                    Else op();
                                    EndIf.
                                ElseIf st&&st Then ok_man();
                                ElseIf 72%7&&cqwiw+(ad+q3) Then
                                a=1-2;
                                foo();
                                EndIf.
                        EndBody.
                """
        expect = Program([VarDecl(Id("awe"),[],None),VarDecl(Id("f"),[],None),VarDecl(Id("wef"),[],None),VarDecl(Id("we"),[],None),VarDecl(Id("a"),[4],None),FuncDecl(Id("zwt56dm"),[VarDecl(Id("s"),[],None),VarDecl(Id("nt"),[],None),VarDecl(Id("yh"),[],None),VarDecl(Id("y6r"),[],None)],tuple([[],[If([tuple([BinaryOp("+",BinaryOp("+",Id("abcd"),CallExpr(Id("foo"),[])),ArrayCell(Id("a"),[CallExpr(Id("foo"),[])])),[],[If([tuple([BinaryOp(">=.",BinaryOp("-",CallExpr(Id("fcking"),[]),IntLiteral(234)),BinaryOp("+.",FloatLiteral(1.9),FloatLiteral(340000.0))),[],[CallStmt(Id("kool"),[])]]),tuple([Id("abcd"),[],[Assign(Id("e"),BinaryOp("+",Id("p"),IntLiteral(1)))]])],tuple([[],[CallStmt(Id("op"),[])]]))]]),tuple([BinaryOp("&&",Id("st"),Id("st")),[],[CallStmt(Id("ok_man"),[])]]),tuple([BinaryOp("&&",BinaryOp("%",IntLiteral(72),IntLiteral(7)),BinaryOp("+",Id("cqwiw"),BinaryOp("+",Id("ad"),Id("q3")))),[],[Assign(Id("a"),BinaryOp("-",IntLiteral(1),IntLiteral(2))),CallStmt(Id("foo"),[])]])],tuple([[],[]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_07(self):
        input = """
                    Var: awe,f,wef,we,a[4];
                    Function:zwt56dm
                        Parameter:s,nt,yh,y6r
                        Body:
                        Var:a=3;
                            If abcd+ foo() + a[foo()] Then
                                    If fcking()-234>=.1.9+.34e4 Then kool();
                                    ElseIf abcd Then e=p+1;
                                    Else op();
                                    EndIf.
                                ElseIf st&&st Then ok_man();
                                ElseIf 72%7&&cqwiw+(ad+q3) Then
                                a=1-2;
                                foo();
                                EndIf.

                        If abcd+ foo() + a[foo()] Then
                                If fcking()-234>=.1.9+.34e4 Then kool();
                                EndIf.
                            ElseIf st&&st Then
                            ElseIf 72%7&&cqwiw+(ad+q3) Then
                            EndIf.
                        EndBody.
                """
        expect = Program([VarDecl(Id("awe"),[],None),VarDecl(Id("f"),[],None),VarDecl(Id("wef"),[],None),VarDecl(Id("we"),[],None),VarDecl(Id("a"),[4],None),FuncDecl(Id("zwt56dm"),[VarDecl(Id("s"),[],None),VarDecl(Id("nt"),[],None),VarDecl(Id("yh"),[],None),VarDecl(Id("y6r"),[],None)],tuple([[VarDecl(Id("a"),[],IntLiteral(3))],[If([tuple([BinaryOp("+",BinaryOp("+",Id("abcd"),CallExpr(Id("foo"),[])),ArrayCell(Id("a"),[CallExpr(Id("foo"),[])])),[],[If([tuple([BinaryOp(">=.",BinaryOp("-",CallExpr(Id("fcking"),[]),IntLiteral(234)),BinaryOp("+.",FloatLiteral(1.9),FloatLiteral(340000.0))),[],[CallStmt(Id("kool"),[])]]),tuple([Id("abcd"),[],[Assign(Id("e"),BinaryOp("+",Id("p"),IntLiteral(1)))]])],tuple([[],[CallStmt(Id("op"),[])]]))]]),tuple([BinaryOp("&&",Id("st"),Id("st")),[],[CallStmt(Id("ok_man"),[])]]),tuple([BinaryOp("&&",BinaryOp("%",IntLiteral(72),IntLiteral(7)),BinaryOp("+",Id("cqwiw"),BinaryOp("+",Id("ad"),Id("q3")))),[],[Assign(Id("a"),BinaryOp("-",IntLiteral(1),IntLiteral(2))),CallStmt(Id("foo"),[])]])],tuple([[],[]])),If([tuple([BinaryOp("+",BinaryOp("+",Id("abcd"),CallExpr(Id("foo"),[])),ArrayCell(Id("a"),[CallExpr(Id("foo"),[])])),[],[If([tuple([BinaryOp(">=.",BinaryOp("-",CallExpr(Id("fcking"),[]),IntLiteral(234)),BinaryOp("+.",FloatLiteral(1.9),FloatLiteral(340000.0))),[],[CallStmt(Id("kool"),[])]])],tuple([[],[]]))]]),tuple([BinaryOp("&&",Id("st"),Id("st")),[],[]]),tuple([BinaryOp("&&",BinaryOp("%",IntLiteral(72),IntLiteral(7)),BinaryOp("+",Id("cqwiw"),BinaryOp("+",Id("ad"),Id("q3")))),[],[]])],tuple([[],[]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_08(self):
        input = """
                    Var: awe,f,wef,we,a[4];
                    Function:zwt56dm
                        Parameter:s,nt,yh,y6r
                        Body:
                        Var:a=3;
                            If abcd+ foo() + a[foo()] Then
                                    If fcking()
                                    -234>=.1.9+.34e4 Then kool();
                                    ElseIf abcd Then e=p+1;
                                    EndIf.
                                ElseIf (90 % 4**2r3hbh232r0918**) Then ft=-ok_();
                                ElseIf 72%7&&
                                cqwiw+(ad+q3) Then
                                a=1-2;
                                foo();
                                EndIf.

                        If abcd+ foo() + a[foo()] Then
                                If fcking()-234>=.1.9+.34e4 Then kool();
                                EndIf.
                            ElseIf st&&st Then**bd a3tq235vy
                            ElseIf 72%7&&cqwiw+(ad+q3) Then**
                            EndIf.
                        EndBody.
                """
        expect = Program([VarDecl(Id("awe"),[],None),VarDecl(Id("f"),[],None),VarDecl(Id("wef"),[],None),VarDecl(Id("we"),[],None),VarDecl(Id("a"),[4],None),FuncDecl(Id("zwt56dm"),[VarDecl(Id("s"),[],None),VarDecl(Id("nt"),[],None),VarDecl(Id("yh"),[],None),VarDecl(Id("y6r"),[],None)],tuple([[VarDecl(Id("a"),[],IntLiteral(3))],[If([tuple([BinaryOp("+",BinaryOp("+",Id("abcd"),CallExpr(Id("foo"),[])),ArrayCell(Id("a"),[CallExpr(Id("foo"),[])])),[],[If([tuple([BinaryOp(">=.",BinaryOp("-",CallExpr(Id("fcking"),[]),IntLiteral(234)),BinaryOp("+.",FloatLiteral(1.9),FloatLiteral(340000.0))),[],[CallStmt(Id("kool"),[])]]),tuple([Id("abcd"),[],[Assign(Id("e"),BinaryOp("+",Id("p"),IntLiteral(1)))]])],tuple([[],[]]))]]),tuple([BinaryOp("%",IntLiteral(90),IntLiteral(4)),[],[Assign(Id("ft"),UnaryOp("-",CallExpr(Id("ok_"),[])))]]),tuple([BinaryOp("&&",BinaryOp("%",IntLiteral(72),IntLiteral(7)),BinaryOp("+",Id("cqwiw"),BinaryOp("+",Id("ad"),Id("q3")))),[],[Assign(Id("a"),BinaryOp("-",IntLiteral(1),IntLiteral(2))),CallStmt(Id("foo"),[])]])],tuple([[],[]])),If([tuple([BinaryOp("+",BinaryOp("+",Id("abcd"),CallExpr(Id("foo"),[])),ArrayCell(Id("a"),[CallExpr(Id("foo"),[])])),[],[If([tuple([BinaryOp(">=.",BinaryOp("-",CallExpr(Id("fcking"),[]),IntLiteral(234)),BinaryOp("+.",FloatLiteral(1.9),FloatLiteral(340000.0))),[],[CallStmt(Id("kool"),[])]])],tuple([[],[]]))]]),tuple([BinaryOp("&&",Id("st"),Id("st")),[],[]])],tuple([[],[]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_09(self):
        input = """
                    Var: awe,f,wef,we,a[4];
                    Function:zwt56dm
                        Parameter:s,nt,yh,y6r
                        Body:
                            If abcd+ foo() + a[foo()] Then
                                    If fcking()-234>=.1.9+.34e4 Then kool();
                                    ElseIf abcd Then e=p+1;
                                ElseIf st&&st Then ok_man();
                                EndIf.
                                EndIf.
                        EndBody.
                """
        expect = Program([VarDecl(Id("awe"),[],None),VarDecl(Id("f"),[],None),VarDecl(Id("wef"),[],None),VarDecl(Id("we"),[],None),VarDecl(Id("a"),[4],None),FuncDecl(Id("zwt56dm"),[VarDecl(Id("s"),[],None),VarDecl(Id("nt"),[],None),VarDecl(Id("yh"),[],None),VarDecl(Id("y6r"),[],None)],tuple([[],[If([tuple([BinaryOp("+",BinaryOp("+",Id("abcd"),CallExpr(Id("foo"),[])),ArrayCell(Id("a"),[CallExpr(Id("foo"),[])])),[],[If([tuple([BinaryOp(">=.",BinaryOp("-",CallExpr(Id("fcking"),[]),IntLiteral(234)),BinaryOp("+.",FloatLiteral(1.9),FloatLiteral(340000.0))),[],[CallStmt(Id("kool"),[])]]),tuple([Id("abcd"),[],[Assign(Id("e"),BinaryOp("+",Id("p"),IntLiteral(1)))]]),tuple([BinaryOp("&&",Id("st"),Id("st")),[],[CallStmt(Id("ok_man"),[])]])],tuple([[],[]]))]])],tuple([[],[]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_10(self):
        input = """
                    Var: awe,f,wef,we,a[4];
                    Function:zwt56dm
                        Parameter:s,nt,yh,y6r
                        Body:
                        Var:a=3;
                            If abcd+ foo() + a[foo()] Then
                                    If fcking()-234>=.1.9+.34e4 Then kool();
                                    fucking();
                                EndIf.

                        If abcd+ foo() + a[foo()] Then
                                Var: ocr=0;
                                EndIf.
                                EndIf.
                        EndBody.
                """
        expect = Program([VarDecl(Id("awe"),[],None),VarDecl(Id("f"),[],None),VarDecl(Id("wef"),[],None),VarDecl(Id("we"),[],None),VarDecl(Id("a"),[4],None),FuncDecl(Id("zwt56dm"),[VarDecl(Id("s"),[],None),VarDecl(Id("nt"),[],None),VarDecl(Id("yh"),[],None),VarDecl(Id("y6r"),[],None)],tuple([[VarDecl(Id("a"),[],IntLiteral(3))],[If([tuple([BinaryOp("+",BinaryOp("+",Id("abcd"),CallExpr(Id("foo"),[])),ArrayCell(Id("a"),[CallExpr(Id("foo"),[])])),[],[If([tuple([BinaryOp(">=.",BinaryOp("-",CallExpr(Id("fcking"),[]),IntLiteral(234)),BinaryOp("+.",FloatLiteral(1.9),FloatLiteral(340000.0))),[],[CallStmt(Id("kool"),[]),CallStmt(Id("fucking"),[])]])],tuple([[],[]])),If([tuple([BinaryOp("+",BinaryOp("+",Id("abcd"),CallExpr(Id("foo"),[])),ArrayCell(Id("a"),[CallExpr(Id("foo"),[])])),[VarDecl(Id("ocr"),[],IntLiteral(0))],[]])],tuple([[],[]]))]])],tuple([[],[]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_11(self):
        input = """
                    Var:ww51,f32fg=2.e907,b[656465]={};
                    Function: a
                        Parameter: dcm
                        Body:
                            For (awer=10,awer[foo()],arw < 6) Do fcking();
                            EndFor.
                        EndBody.
                """
        expect = Program([VarDecl(Id("ww51"),[],None),VarDecl(Id("f32fg"),[],FloatLiteral(2.e907)),VarDecl(Id("b"),[656465],ArrayLiteral([])),FuncDecl(Id("a"),[VarDecl(Id("dcm"),[],None)],tuple([[],[For(Id("awer"),IntLiteral(10),ArrayCell(Id("awer"),[CallExpr(Id("foo"),[])]),BinaryOp("<",Id("arw"),IntLiteral(6)),tuple([[],[CallStmt(Id("fcking"),[])]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_12(self):
        input = """
                    Var:ww51,f32fg=2.e907,b[656465]={};
                    Function:d
                        Parameter:fwe
                        Body:
                            For (awer=10,awer[foo()],arw < 6) Do fcking();
                            ae = a[True] -. 0x78;
                                For (x=1,x,x) Do EndFor.
                            EndFor.
                        EndBody.
                """
        expect = Program([VarDecl(Id("ww51"),[],None),VarDecl(Id("f32fg"),[],FloatLiteral(2.e907)),VarDecl(Id("b"),[656465],ArrayLiteral([])),FuncDecl(Id("d"),[VarDecl(Id("fwe"),[],None)],tuple([[],[For(Id("awer"),IntLiteral(10),ArrayCell(Id("awer"),[CallExpr(Id("foo"),[])]),BinaryOp("<",Id("arw"),IntLiteral(6)),tuple([[],[CallStmt(Id("fcking"),[]),Assign(Id("ae"),BinaryOp("-.",ArrayCell(Id("a"),[BooleanLiteral(True)]),IntLiteral(120))),For(Id("x"),IntLiteral(1),Id("x"),Id("x"),tuple([[],[]]))]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_13(self):
        input = """
                    Var:ww51,f32fg=2.e907,b[656465]={};
                    Function:d
                        Parameter:fwe
                        Body:
                            For (awer=10,awer[foo()],arw < 6) Do fcking();
                            ae = a[True] -. 0x78;
                                For (e=False,st,{{"2"}}) Do
                                goi_em_la_du_du = foo();
                                EndFor.
                            EndFor.
                        EndBody.
                """
        expect = Program([VarDecl(Id("ww51"),[],None),VarDecl(Id("f32fg"),[],FloatLiteral(2.e907)),VarDecl(Id("b"),[656465],ArrayLiteral([])),FuncDecl(Id("d"),[VarDecl(Id("fwe"),[],None)],tuple([[],[For(Id("awer"),IntLiteral(10),ArrayCell(Id("awer"),[CallExpr(Id("foo"),[])]),BinaryOp("<",Id("arw"),IntLiteral(6)),tuple([[],[CallStmt(Id("fcking"),[]),Assign(Id("ae"),BinaryOp("-.",ArrayCell(Id("a"),[BooleanLiteral(True)]),IntLiteral(120))),For(Id("e"),BooleanLiteral(False),Id("st"),ArrayLiteral([ArrayLiteral([StringLiteral("2")])]),tuple([[],[Assign(Id("goi_em_la_du_du"),CallExpr(Id("foo"),[]))]]))]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_14(self):
        input = """
                    Var:ww51,f32fg=2.e907,b[656465]={};
                    Function:d
                        Parameter:fwe
                        Body:
                            For (awer=10,awer[foo()],arw < 6) Do fcking();
                            ae = a[True] -. 0x78;
                            If a Then abcxyz();
                                For (e=False,st,{{"2"}}) Do
                                goi_em_la_du_du = foo();
                                EndFor.
                                EndIf.
                            EndFor.
                        EndBody.
                """
        expect = Program([VarDecl(Id("ww51"),[],None),VarDecl(Id("f32fg"),[],FloatLiteral(2.e907)),VarDecl(Id("b"),[656465],ArrayLiteral([])),FuncDecl(Id("d"),[VarDecl(Id("fwe"),[],None)],tuple([[],[For(Id("awer"),IntLiteral(10),ArrayCell(Id("awer"),[CallExpr(Id("foo"),[])]),BinaryOp("<",Id("arw"),IntLiteral(6)),tuple([[],[CallStmt(Id("fcking"),[]),Assign(Id("ae"),BinaryOp("-.",ArrayCell(Id("a"),[BooleanLiteral(True)]),IntLiteral(120))),If([tuple([Id("a"),[],[CallStmt(Id("abcxyz"),[]),For(Id("e"),BooleanLiteral(False),Id("st"),ArrayLiteral([ArrayLiteral([StringLiteral("2")])]),tuple([[],[Assign(Id("goi_em_la_du_du"),CallExpr(Id("foo"),[]))]]))]])],tuple([[],[]]))]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_15(self):
        input = """
                    Var:ww51,f32fg=2.e907,b[656465]={};
                    Function:we
                        Parameter:ac,we
                        Body:
                            For (awer=10,awer[foo()],arw < 6) Do fcking();
                            EndFor.
                        EndBody.
                """
        expect = Program([VarDecl(Id("ww51"),[],None),VarDecl(Id("f32fg"),[],FloatLiteral(2.e907)),VarDecl(Id("b"),[656465],ArrayLiteral([])),FuncDecl(Id("we"),[VarDecl(Id("ac"),[],None),VarDecl(Id("we"),[],None)],tuple([[],[For(Id("awer"),IntLiteral(10),ArrayCell(Id("awer"),[CallExpr(Id("foo"),[])]),BinaryOp("<",Id("arw"),IntLiteral(6)),tuple([[],[CallStmt(Id("fcking"),[])]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_16(self):
        input = """
                    Var:ww51,f32fg=2.e907,b[656465]={};
                    Function:d
                        Parameter:fwe
                        Body:
                            For (awer=10,awer[foo()],arw < 6) Do fcking();
                            ae = a[True] -. 0x78;
                                For (e=False,st,{{"2"}}) Do
                                Var: baby_shark_do_do_do_do = 5;
                                goi_em_la_du_du = foo();
                                EndFor.
                            EndFor.
                        EndBody.
                """
        expect = Program([VarDecl(Id("ww51"),[],None),VarDecl(Id("f32fg"),[],FloatLiteral(2.e907)),VarDecl(Id("b"),[656465],ArrayLiteral([])),FuncDecl(Id("d"),[VarDecl(Id("fwe"),[],None)],tuple([[],[For(Id("awer"),IntLiteral(10),ArrayCell(Id("awer"),[CallExpr(Id("foo"),[])]),BinaryOp("<",Id("arw"),IntLiteral(6)),tuple([[],[CallStmt(Id("fcking"),[]),Assign(Id("ae"),BinaryOp("-.",ArrayCell(Id("a"),[BooleanLiteral(True)]),IntLiteral(120))),For(Id("e"),BooleanLiteral(False),Id("st"),ArrayLiteral([ArrayLiteral([StringLiteral("2")])]),tuple([[VarDecl(Id("baby_shark_do_do_do_do"),[],IntLiteral(5))],[Assign(Id("goi_em_la_du_du"),CallExpr(Id("foo"),[]))]]))]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_17(self):
        input = """
                    Var:ww51,f32fg=2.e907,b[656465]={};
                    Function:d
                        Parameter:fwe
                        Body:
                            For (awer=10,awer[foo()],arw < 6) Do fcking();
                            ae = a[True] -. 0x78;
                                For (e=False,st,{{"2"}}) Do
                                goi_em_la_du_du = foo();
                                If False Then For (x=1,x,x) Do EndFor. EndIf.
                                EndFor.
                            EndFor.
                        EndBody.
                """
        expect = Program([VarDecl(Id("ww51"),[],None),VarDecl(Id("f32fg"),[],FloatLiteral(2.e907)),VarDecl(Id("b"),[656465],ArrayLiteral([])),FuncDecl(Id("d"),[VarDecl(Id("fwe"),[],None)],tuple([[],[For(Id("awer"),IntLiteral(10),ArrayCell(Id("awer"),[CallExpr(Id("foo"),[])]),BinaryOp("<",Id("arw"),IntLiteral(6)),tuple([[],[CallStmt(Id("fcking"),[]),Assign(Id("ae"),BinaryOp("-.",ArrayCell(Id("a"),[BooleanLiteral(True)]),IntLiteral(120))),For(Id("e"),BooleanLiteral(False),Id("st"),ArrayLiteral([ArrayLiteral([StringLiteral("2")])]),tuple([[],[Assign(Id("goi_em_la_du_du"),CallExpr(Id("foo"),[])),If([tuple([BooleanLiteral(False),[],[For(Id("x"),IntLiteral(1),Id("x"),Id("x"),tuple([[],[]]))]])],tuple([[],[]]))]]))]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_18(self):
        input = """
                    Var:abc, a[23]={{}, 654, "6396"};
                    Function: fas_cko_8rfkw
                        Parameter: a[15], q[68], acf5qf4_iuqw
                        Body:
                            Var: wf87[752]={};
                            While foo() -. 1.9e7 + "ekigk" Do
                                If True Then EndIf.
                                soooo(wfwe[234\\soo()]);
                                EndWhile.
                        EndBody.
                """
        expect = Program([VarDecl(Id("abc"),[],None),VarDecl(Id("a"),[23],ArrayLiteral([ArrayLiteral([]),IntLiteral(654),StringLiteral("6396")])),FuncDecl(Id("fas_cko_8rfkw"),[VarDecl(Id("a"),[15],None),VarDecl(Id("q"),[68],None),VarDecl(Id("acf5qf4_iuqw"),[],None)],tuple([[VarDecl(Id("wf87"),[752],ArrayLiteral([]))],[While(BinaryOp("+",BinaryOp("-.",CallExpr(Id("foo"),[]),FloatLiteral(19000000.0)),StringLiteral("ekigk")),tuple([[],[If([tuple([BooleanLiteral(True),[],[]])],tuple([[],[]])),CallStmt(Id("soooo"),[ArrayCell(Id("wfwe"),[BinaryOp("\\",IntLiteral(234),CallExpr(Id("soo"),[]))])])]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_19(self):
        input = """
                    Var:abc, a[23]={{}, 654, "6396"};
                    Function: fas_cko_8rfkw
                        Parameter: a[15], q[68], acf5qf4_iuqw
                        Body:
                            Var: wf87[752]={};
                            While (foo() -. 1.9e7 + "ekigk") Do
                                While (foo() -. 1.9e7 + "ekigk") Do
                                    Break;
                                    If True Then EndIf.
                                    soooo(wfwe[234\\soo()]);
                                EndWhile.
                            EndWhile.
                        EndBody.
                """
        expect = Program([VarDecl(Id("abc"),[],None),VarDecl(Id("a"),[23],ArrayLiteral([ArrayLiteral([]),IntLiteral(654),StringLiteral("6396")])),FuncDecl(Id("fas_cko_8rfkw"),[VarDecl(Id("a"),[15],None),VarDecl(Id("q"),[68],None),VarDecl(Id("acf5qf4_iuqw"),[],None)],tuple([[VarDecl(Id("wf87"),[752],ArrayLiteral([]))],[While(BinaryOp("+",BinaryOp("-.",CallExpr(Id("foo"),[]),FloatLiteral(19000000.0)),StringLiteral("ekigk")),tuple([[],[While(BinaryOp("+",BinaryOp("-.",CallExpr(Id("foo"),[]),FloatLiteral(19000000.0)),StringLiteral("ekigk")),tuple([[],[Break(),If([tuple([BooleanLiteral(True),[],[]])],tuple([[],[]])),CallStmt(Id("soooo"),[ArrayCell(Id("wfwe"),[BinaryOp("\\",IntLiteral(234),CallExpr(Id("soo"),[]))])])]]))]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_20(self):
        input = """
                    Var:abc, a[23]={{}, 654, "6396"};
                    Function: fas_cko_8rfkw
                        Parameter: a[15], q[68], acf5qf4_iuqw
                        Body:
                            Var: wf87[752]={};
                            Do
                                While (foo() -. 1.9e7 + "ekigk") Do
                                    Break;
                                    If True Then EndIf.
                                    soooo(wfwe[234\\soo()]);
                                EndWhile.
                            While (foo() -. 1.9e7 + "ekigk")  EndDo.
                        EndBody.
                """
        expect = Program([VarDecl(Id("abc"),[],None),VarDecl(Id("a"),[23],ArrayLiteral([ArrayLiteral([]),IntLiteral(654),StringLiteral("6396")])),FuncDecl(Id("fas_cko_8rfkw"),[VarDecl(Id("a"),[15],None),VarDecl(Id("q"),[68],None),VarDecl(Id("acf5qf4_iuqw"),[],None)],tuple([[VarDecl(Id("wf87"),[752],ArrayLiteral([]))],[Dowhile(tuple([[],[While(BinaryOp("+",BinaryOp("-.",CallExpr(Id("foo"),[]),FloatLiteral(19000000.0)),StringLiteral("ekigk")),tuple([[],[Break(),If([tuple([BooleanLiteral(True),[],[]])],tuple([[],[]])),CallStmt(Id("soooo"),[ArrayCell(Id("wfwe"),[BinaryOp("\\",IntLiteral(234),CallExpr(Id("soo"),[]))])])]]))]]),BinaryOp("+",BinaryOp("-.",CallExpr(Id("foo"),[]),FloatLiteral(19000000.0)),StringLiteral("ekigk")))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_21(self):
        input = """
                    Var:abc, a[23]={{}, 654, "6396"};
                    Function: fas_cko_8rfkw
                        Parameter: a[15], q[68], acf5qf4_iuqw
                        Body:
                            Var: wf87[752]={};
                            Do
                                 Do
                                    Break;
                                    If True Then EndIf.
                                While (foo() -. 1.9e7 + "ekigk") EndDo.
                                    soooo(wfwe[234\\soo()]);
                            While (foo() -. 1.9e7 + "ekigk")  EndDo.
                        EndBody.
                """
        expect = Program([VarDecl(Id("abc"),[],None),VarDecl(Id("a"),[23],ArrayLiteral([ArrayLiteral([]),IntLiteral(654),StringLiteral("6396")])),FuncDecl(Id("fas_cko_8rfkw"),[VarDecl(Id("a"),[15],None),VarDecl(Id("q"),[68],None),VarDecl(Id("acf5qf4_iuqw"),[],None)],tuple([[VarDecl(Id("wf87"),[752],ArrayLiteral([]))],[Dowhile(tuple([[],[Dowhile(tuple([[],[Break(),If([tuple([BooleanLiteral(True),[],[]])],tuple([[],[]]))]]),BinaryOp("+",BinaryOp("-.",CallExpr(Id("foo"),[]),FloatLiteral(19000000.0)),StringLiteral("ekigk"))),CallStmt(Id("soooo"),[ArrayCell(Id("wfwe"),[BinaryOp("\\",IntLiteral(234),CallExpr(Id("soo"),[]))])])]]),BinaryOp("+",BinaryOp("-.",CallExpr(Id("foo"),[]),FloatLiteral(19000000.0)),StringLiteral("ekigk")))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_22(self):
        input = """
                    Var:abc, a[23]={{}, 654, "6396"};
                    Function: fas_cko_8rfkw
                        Parameter: a[15], q[68], acf5qf4_iuqw
                        Body:
                            Var: wf87[752]={};
                            Do
                            soooo(wfwe[234\\soo()]);
                                 Do
                                    Break;
                                    If True Then EndIf.
                                    While (foo() -. 1.9e7 + "ekigk")DoEndWhile.
                                While (foo() -. 1.9e7 + "ekigk")
                            EndDo.
                            While foo()||co
                            EndDo.
                        EndBody.
                """
        expect = Program([VarDecl(Id("abc"),[],None),VarDecl(Id("a"),[23],ArrayLiteral([ArrayLiteral([]),IntLiteral(654),StringLiteral("6396")])),FuncDecl(Id("fas_cko_8rfkw"),[VarDecl(Id("a"),[15],None),VarDecl(Id("q"),[68],None),VarDecl(Id("acf5qf4_iuqw"),[],None)],tuple([[VarDecl(Id("wf87"),[752],ArrayLiteral([]))],[Dowhile(tuple([[],[CallStmt(Id("soooo"),[ArrayCell(Id("wfwe"),[BinaryOp("\\",IntLiteral(234),CallExpr(Id("soo"),[]))])]),Dowhile(tuple([[],[Break(),If([tuple([BooleanLiteral(True),[],[]])],tuple([[],[]])),While(BinaryOp("+",BinaryOp("-.",CallExpr(Id("foo"),[]),FloatLiteral(19000000.0)),StringLiteral("ekigk")),tuple([[],[]]))]]),BinaryOp("+",BinaryOp("-.",CallExpr(Id("foo"),[]),FloatLiteral(19000000.0)),StringLiteral("ekigk")))]]),BinaryOp("||",CallExpr(Id("foo"),[]),Id("co")))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_23(self):
        input = """
                    Var: a=1;
                    Function: a
                        Parameter: x[12][1]
                        Body:
                            x[foo()||1.e8][6\\8*.1.] = {{**"1.2"}, {1,2,3**}, 0e89};

                        EndBody.
                """
        expect = Program([VarDecl(Id("a"),[],IntLiteral(1)),FuncDecl(Id("a"),[VarDecl(Id("x"),[12,1],None)],tuple([[],[Assign(ArrayCell(Id("x"),[BinaryOp("||",CallExpr(Id("foo"),[]),FloatLiteral(100000000.0)),BinaryOp("*.",BinaryOp("\\",IntLiteral(6),IntLiteral(8)),FloatLiteral(1.0))]),ArrayLiteral([ArrayLiteral([]),FloatLiteral(0.0)]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_24(self):
        input = """
                    Var: a=1;
                    Function: a
                        Parameter: x[12][1], a
                        Body:
                            x[foo()||1.e8][6\\8*.1.] = a =/= {{**"1.2"}, {1,2,3**}, 0e89}||False;
                            While (x["vseokaef"]) Do EndWhile.
                        EndBody.
                """
        expect = Program([VarDecl(Id("a"),[],IntLiteral(1)),FuncDecl(Id("a"),[VarDecl(Id("x"),[12,1],None),VarDecl(Id("a"),[],None)],tuple([[],[Assign(ArrayCell(Id("x"),[BinaryOp("||",CallExpr(Id("foo"),[]),FloatLiteral(100000000.0)),BinaryOp("*.",BinaryOp("\\",IntLiteral(6),IntLiteral(8)),FloatLiteral(1.0))]),BinaryOp("=/=",Id("a"),BinaryOp("||",ArrayLiteral([ArrayLiteral([]),FloatLiteral(0.0)]),BooleanLiteral(False)))),While(ArrayCell(Id("x"),[StringLiteral("vseokaef")]),tuple([[],[]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_25(self):
        input = """
                    Var: a=1;
                    Function: a
                        Parameter: x[12][1], a
                        Body:
                            x[foo()||1.e8][6\\8*.1.] = a =/= {{**"1.2"}, {1,2,3**}, 0e89}||False;
                            While (x["vseokaef"]) Do EndWhile.
                        EndBody.
                """
        expect = Program([VarDecl(Id("a"),[],IntLiteral(1)),FuncDecl(Id("a"),[VarDecl(Id("x"),[12,1],None),VarDecl(Id("a"),[],None)],tuple([[],[Assign(ArrayCell(Id("x"),[BinaryOp("||",CallExpr(Id("foo"),[]),FloatLiteral(100000000.0)),BinaryOp("*.",BinaryOp("\\",IntLiteral(6),IntLiteral(8)),FloatLiteral(1.0))]),BinaryOp("=/=",Id("a"),BinaryOp("||",ArrayLiteral([ArrayLiteral([]),FloatLiteral(0.0)]),BooleanLiteral(False)))),While(ArrayCell(Id("x"),[StringLiteral("vseokaef")]),tuple([[],[]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_26(self):
        input = """
                    Var: a ,b,c;
                    Function: day_la_func_0
                        Parameter: x, a[256][45]
                        Body:
                            Return dung_noi_chia_tay();
                            For (x=1,x,x) Do Break; EndFor.
                        EndBody.
                    Function: day_la_func_1
                        Parameter: x[656], a[256][45]
                        Body:
                            For (x=1,x,x) Do Continue; EndFor.
                            Return dung_noi_chia_tay();
                        EndBody.
                """
        expect = Program([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None),FuncDecl(Id("day_la_func_0"),[VarDecl(Id("x"),[],None),VarDecl(Id("a"),[256,45],None)],tuple([[],[Return(CallExpr(Id("dung_noi_chia_tay"),[])),For(Id("x"),IntLiteral(1),Id("x"),Id("x"),tuple([[],[Break()]]))]])),FuncDecl(Id("day_la_func_1"),[VarDecl(Id("x"),[656],None),VarDecl(Id("a"),[256,45],None)],tuple([[],[For(Id("x"),IntLiteral(1),Id("x"),Id("x"),tuple([[],[Continue()]])),Return(CallExpr(Id("dung_noi_chia_tay"),[]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_27(self):
        input = """
                    Var: a ,b,c;
                    Function: day_la_func_0
                        Parameter: x, a[256][45]
                        Body:
                            Return dung_noi_chia_tay(34\\23);
                            For (x=1,x,x) Do Break; Return (123); EndFor.
                        EndBody.
                    Function: day_la_func_1
                        Parameter: x[656], a[256][45]
                        Body:
                            For (x=1,x,x) Do Continue; EndFor.
                            Return dung_noi_chia_tay({1,9,56}) +"gwaregqaqe";
                        EndBody.
                """
        expect = Program([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None),FuncDecl(Id("day_la_func_0"),[VarDecl(Id("x"),[],None),VarDecl(Id("a"),[256,45],None)],tuple([[],[Return(CallExpr(Id("dung_noi_chia_tay"),[BinaryOp("\\",IntLiteral(34),IntLiteral(23))])),For(Id("x"),IntLiteral(1),Id("x"),Id("x"),tuple([[],[Break(),Return(IntLiteral(123))]]))]])),FuncDecl(Id("day_la_func_1"),[VarDecl(Id("x"),[656],None),VarDecl(Id("a"),[256,45],None)],tuple([[],[For(Id("x"),IntLiteral(1),Id("x"),Id("x"),tuple([[],[Continue()]])),Return(BinaryOp("+",CallExpr(Id("dung_noi_chia_tay"),[ArrayLiteral([IntLiteral(1),IntLiteral(9),IntLiteral(56)])]),StringLiteral("gwaregqaqe")))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_28(self):
        input = """
                    Var: a, b,c;
                    Function: day_la_func_0
                        Parameter: x, a[256][45]
                        Body:
                            Continue;
                            Return dung_noi_chia_tay(34\\23);
                            For (x=1,x,x) Do Break; Return (123); EndFor.
                        EndBody.
                    Function: day_la_func_1
                        Body:
                            While x Do Continue; EndWhile.
                            Return dung_noi_chia_tay({1,9,56}) || 78 >7-."gwaregqaqe";
                        EndBody.
                """
        expect = Program([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None),FuncDecl(Id("day_la_func_0"),[VarDecl(Id("x"),[],None),VarDecl(Id("a"),[256,45],None)],tuple([[],[Continue(),Return(CallExpr(Id("dung_noi_chia_tay"),[BinaryOp("\\",IntLiteral(34),IntLiteral(23))])),For(Id("x"),IntLiteral(1),Id("x"),Id("x"),tuple([[],[Break(),Return(IntLiteral(123))]]))]])),FuncDecl(Id("day_la_func_1"),[],tuple([[],[While(Id("x"),tuple([[],[Continue()]])),Return(BinaryOp(">",BinaryOp("||",CallExpr(Id("dung_noi_chia_tay"),[ArrayLiteral([IntLiteral(1),IntLiteral(9),IntLiteral(56)])]),IntLiteral(78)),BinaryOp("-.",IntLiteral(7),StringLiteral("gwaregqaqe"))))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_29(self):
        input = """
                    Var:a,b[2],c[3][4];
                    Function: acbd_4567_ABCD
                        Parameter:d[1][52][96596][654569], cwij439f
                        Body:
                            a["fwck"]=vsvelv;
                        EndBody.
                """
        expect = Program([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2],None),VarDecl(Id("c"),[3,4],None),FuncDecl(Id("acbd_4567_ABCD"),[VarDecl(Id("d"),[1,52,96596,654569],None),VarDecl(Id("cwij439f"),[],None)],tuple([[],[Assign(ArrayCell(Id("a"),[StringLiteral("fwck")]),Id("vsvelv"))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_30(self):
        input = """
                    Var:a,b[2],c[3][4];
                    Function: acbd_4567_ABCD
                        Parameter:d[1][52][96596][654569], cwij439f
                        Body:
                            a["fwck"]=erw[gw652][{"abcdf w" }+123];
                        EndBody.
                """
        expect = Program([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2],None),VarDecl(Id("c"),[3,4],None),FuncDecl(Id("acbd_4567_ABCD"),[VarDecl(Id("d"),[1,52,96596,654569],None),VarDecl(Id("cwij439f"),[],None)],tuple([[],[Assign(ArrayCell(Id("a"),[StringLiteral("fwck")]),ArrayCell(Id("erw"),[Id("gw652"),BinaryOp("+",ArrayLiteral([StringLiteral("abcdf w")]),IntLiteral(123))]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_31(self):
        input = """
                    Var:a,b[2],c[3][4];
                    Function: acbd_4567_ABCD
                        Parameter:d[1][52][96596][654569], cwij439f
                        Body:
                            a["fwck"]=erw[gw652][{"abcdf w" }+123];
                            If 224+a[awf+{25, "ee"}] Then y[xxx] = {{{},{}},{}}; EndIf.
                        EndBody.
                """
        expect = Program([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2],None),VarDecl(Id("c"),[3,4],None),FuncDecl(Id("acbd_4567_ABCD"),[VarDecl(Id("d"),[1,52,96596,654569],None),VarDecl(Id("cwij439f"),[],None)],tuple([[],[Assign(ArrayCell(Id("a"),[StringLiteral("fwck")]),ArrayCell(Id("erw"),[Id("gw652"),BinaryOp("+",ArrayLiteral([StringLiteral("abcdf w")]),IntLiteral(123))])),If([tuple([BinaryOp("+",IntLiteral(224),ArrayCell(Id("a"),[BinaryOp("+",Id("awf"),ArrayLiteral([IntLiteral(25),StringLiteral("ee")]))])),[],[Assign(ArrayCell(Id("y"),[Id("xxx")]),ArrayLiteral([ArrayLiteral([ArrayLiteral([]),ArrayLiteral([])]),ArrayLiteral([])]))]])],tuple([[],[]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_32(self):
        input = """
                    Var:a,b[2],c[3][4];
                    Function: acbd_4567_ABCD
                        Parameter:d[1][52][96596][654569], cwij439f
                        Body:
                            a["fwck"]=erw[gw652]**a[{"abcdf w" }+123];
                            If 224+a[awf+{25, "ee"}] Then y**[xxx]== {{{},{}},{}}; Continue;
                            a[6*{8}] = (a[{1,2,3}]-{34,"51",1e4});
                        EndBody.
                """
        expect = Program([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2],None),VarDecl(Id("c"),[3,4],None),FuncDecl(Id("acbd_4567_ABCD"),[VarDecl(Id("d"),[1,52,96596,654569],None),VarDecl(Id("cwij439f"),[],None)],tuple([[],[Assign(ArrayCell(Id("a"),[StringLiteral("fwck")]),BinaryOp("==",ArrayCell(Id("erw"),[Id("gw652"),Id("xxx")]),ArrayLiteral([ArrayLiteral([ArrayLiteral([]),ArrayLiteral([])]),ArrayLiteral([])]))),Continue(),Assign(ArrayCell(Id("a"),[BinaryOp("*",IntLiteral(6),ArrayLiteral([IntLiteral(8)]))]),BinaryOp("-",ArrayCell(Id("a"),[ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])]),ArrayLiteral([IntLiteral(34),StringLiteral("51"),FloatLiteral(10000.0)])))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_33(self):
        input = """
                    Var:a,b[2],c[3][4];
                    Function: acbd_4567_ABCD
                        Parameter:d[1][52][96596][654569], cwij439f
                        Body:
                            call_some_fck_func({1,3}+0, 7*.8.7e8);
                            call_some_fck_func({1,3}+0, 7*.8.7e8, True);
                            a[fucking()]=call_some_fck_func({1,3}+0, 7*.8.7e8, a[1.5])+1;

                        EndBody.
                """
        expect = Program([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2],None),VarDecl(Id("c"),[3,4],None),FuncDecl(Id("acbd_4567_ABCD"),[VarDecl(Id("d"),[1,52,96596,654569],None),VarDecl(Id("cwij439f"),[],None)],tuple([[],[CallStmt(Id("call_some_fck_func"),[BinaryOp("+",ArrayLiteral([IntLiteral(1),IntLiteral(3)]),IntLiteral(0)),BinaryOp("*.",IntLiteral(7),FloatLiteral(870000000.0))]),CallStmt(Id("call_some_fck_func"),[BinaryOp("+",ArrayLiteral([IntLiteral(1),IntLiteral(3)]),IntLiteral(0)),BinaryOp("*.",IntLiteral(7),FloatLiteral(870000000.0)),BooleanLiteral(True)]),Assign(ArrayCell(Id("a"),[CallExpr(Id("fucking"),[])]),BinaryOp("+",CallExpr(Id("call_some_fck_func"),[BinaryOp("+",ArrayLiteral([IntLiteral(1),IntLiteral(3)]),IntLiteral(0)),BinaryOp("*.",IntLiteral(7),FloatLiteral(870000000.0)),ArrayCell(Id("a"),[FloatLiteral(1.5)])]),IntLiteral(1)))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_34(self):
        input = """
                    Var:a,b[2],c[3][4];
                    Function: acbd_4567_ABCD
                        Parameter:d[1][52][96596][654569], cwij439f
                        Body:
                            call_some_fck_func({1,3}+0, 7*.8.7e8);
                            call_some_fck_func({1,3}+0, 7*.8.7e8, True);
                            a[fucking()]=call_some_fck_func({1,3}+0, 7*.8.7e8, a[1.5]+1);

                        EndBody.
                """
        expect = Program([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2],None),VarDecl(Id("c"),[3,4],None),FuncDecl(Id("acbd_4567_ABCD"),[VarDecl(Id("d"),[1,52,96596,654569],None),VarDecl(Id("cwij439f"),[],None)],tuple([[],[CallStmt(Id("call_some_fck_func"),[BinaryOp("+",ArrayLiteral([IntLiteral(1),IntLiteral(3)]),IntLiteral(0)),BinaryOp("*.",IntLiteral(7),FloatLiteral(870000000.0))]),CallStmt(Id("call_some_fck_func"),[BinaryOp("+",ArrayLiteral([IntLiteral(1),IntLiteral(3)]),IntLiteral(0)),BinaryOp("*.",IntLiteral(7),FloatLiteral(870000000.0)),BooleanLiteral(True)]),Assign(ArrayCell(Id("a"),[CallExpr(Id("fucking"),[])]),CallExpr(Id("call_some_fck_func"),[BinaryOp("+",ArrayLiteral([IntLiteral(1),IntLiteral(3)]),IntLiteral(0)),BinaryOp("*.",IntLiteral(7),FloatLiteral(870000000.0)),BinaryOp("+",ArrayCell(Id("a"),[FloatLiteral(1.5)]),IntLiteral(1))]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    def test_35(self):
        input = """
                    Var:a,b[2],c[3][4];
                    Function: acbd_4567_ABCD
                        Parameter:d[1][52][96596][654569], cwij439f
                        Body:
                            call_some_fck_func({1,3}+0, 7*.8.7e8);
                            call_some_fck_func({"1\\n6",3}+0, 7*.8.7e8, True);
                            a[fucking()]=call_some_fck_func({1,3}+0, 7*.8.7e8==9, a[1.5])==7+1;

                        EndBody.
                """
        expect = Program([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2],None),VarDecl(Id("c"),[3,4],None),FuncDecl(Id("acbd_4567_ABCD"),[VarDecl(Id("d"),[1,52,96596,654569],None),VarDecl(Id("cwij439f"),[],None)],tuple([[],[CallStmt(Id("call_some_fck_func"),[BinaryOp("+",ArrayLiteral([IntLiteral(1),IntLiteral(3)]),IntLiteral(0)),BinaryOp("*.",IntLiteral(7),FloatLiteral(870000000.0))]),CallStmt(Id("call_some_fck_func"),[BinaryOp("+",ArrayLiteral([StringLiteral("1\\n6"),IntLiteral(3)]),IntLiteral(0)),BinaryOp("*.",IntLiteral(7),FloatLiteral(870000000.0)),BooleanLiteral(True)]),Assign(ArrayCell(Id("a"),[CallExpr(Id("fucking"),[])]),BinaryOp("==",CallExpr(Id("call_some_fck_func"),[BinaryOp("+",ArrayLiteral([IntLiteral(1),IntLiteral(3)]),IntLiteral(0)),BinaryOp("==",BinaryOp("*.",IntLiteral(7),FloatLiteral(870000000.0)),IntLiteral(9)),ArrayCell(Id("a"),[FloatLiteral(1.5)])]),BinaryOp("+",IntLiteral(7),IntLiteral(1))))]]))])


        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_36(self):
        input = """
                    Var:a,b[2],c[3][4];
                    Function: acbd_4567_ABCD
                        Parameter:d[1][52][96596][654569], cwij439f
                        Body:
                            call_some_fck_func({1,3}+0, 7*.8.7e8);
                            call_some_fck_func({"1\\n6",3}+0, 7*.8.7e8, True);
                            a[fucking()]=call_some_fck_func({1,3}+0, 7*.8.7e8==9, a[1.5])==7+1;
                            Return st(8**324 fcnq24jf32r3q4%^&*23 3**, fq, 24,{"'""}+8);
                        EndBody.
                """
        expect = Program([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2],None),VarDecl(Id("c"),[3,4],None),FuncDecl(Id("acbd_4567_ABCD"),[VarDecl(Id("d"),[1,52,96596,654569],None),VarDecl(Id("cwij439f"),[],None)],tuple([[],[CallStmt(Id("call_some_fck_func"),[BinaryOp("+",ArrayLiteral([IntLiteral(1),IntLiteral(3)]),IntLiteral(0)),BinaryOp("*.",IntLiteral(7),FloatLiteral(870000000.0))]),CallStmt(Id("call_some_fck_func"),[BinaryOp("+",ArrayLiteral([StringLiteral("1\\n6"),IntLiteral(3)]),IntLiteral(0)),BinaryOp("*.",IntLiteral(7),FloatLiteral(870000000.0)),BooleanLiteral(True)]),Assign(ArrayCell(Id("a"),[CallExpr(Id("fucking"),[])]),BinaryOp("==",CallExpr(Id("call_some_fck_func"),[BinaryOp("+",ArrayLiteral([IntLiteral(1),IntLiteral(3)]),IntLiteral(0)),BinaryOp("==",BinaryOp("*.",IntLiteral(7),FloatLiteral(870000000.0)),IntLiteral(9)),ArrayCell(Id("a"),[FloatLiteral(1.5)])]),BinaryOp("+",IntLiteral(7),IntLiteral(1)))),Return(CallExpr(Id("st"),[IntLiteral(8),Id("fq"),IntLiteral(24),BinaryOp("+",ArrayLiteral([StringLiteral("\'\"")]),IntLiteral(8))]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_37(self):
        input = """
                    Var:a,b[2],c[3][4];
                    Function: acbd_4567_ABCD
                        Parameter:d[1][52][96596][654569], cwij439f
                        Body:
                            call_some_fck_func({1,3}+0, 7*.8.7e8);
                            call_some_fck_func({"1\\n6",3}+0, 7*.8.7e8, True);
                            a[fucking()]=call_some_fck_func({1,3}+0, 7*.8.7e8==9, a[1.5])==7+1;
                            Return func(ajsceu,"2b275")+st(8**324 fcnq24jf32r3q4%^&*23 3**, fq, 24,{"'""}+8);
                        EndBody.
                """
        expect = Program([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2],None),VarDecl(Id("c"),[3,4],None),FuncDecl(Id("acbd_4567_ABCD"),[VarDecl(Id("d"),[1,52,96596,654569],None),VarDecl(Id("cwij439f"),[],None)],tuple([[],[CallStmt(Id("call_some_fck_func"),[BinaryOp("+",ArrayLiteral([IntLiteral(1),IntLiteral(3)]),IntLiteral(0)),BinaryOp("*.",IntLiteral(7),FloatLiteral(870000000.0))]),CallStmt(Id("call_some_fck_func"),[BinaryOp("+",ArrayLiteral([StringLiteral("1\\n6"),IntLiteral(3)]),IntLiteral(0)),BinaryOp("*.",IntLiteral(7),FloatLiteral(870000000.0)),BooleanLiteral(True)]),Assign(ArrayCell(Id("a"),[CallExpr(Id("fucking"),[])]),BinaryOp("==",CallExpr(Id("call_some_fck_func"),[BinaryOp("+",ArrayLiteral([IntLiteral(1),IntLiteral(3)]),IntLiteral(0)),BinaryOp("==",BinaryOp("*.",IntLiteral(7),FloatLiteral(870000000.0)),IntLiteral(9)),ArrayCell(Id("a"),[FloatLiteral(1.5)])]),BinaryOp("+",IntLiteral(7),IntLiteral(1)))),Return(BinaryOp("+",CallExpr(Id("func"),[Id("ajsceu"),StringLiteral("2b275")]),CallExpr(Id("st"),[IntLiteral(8),Id("fq"),IntLiteral(24),BinaryOp("+",ArrayLiteral([StringLiteral("\'\"")]),IntLiteral(8))])))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_38(self):
        input = """
                    Var: x = 1.5e-12, y ,u, o=8, q="vwf";
                """
        expect = Program([VarDecl(Id("x"),[],FloatLiteral(1.5e-12)),VarDecl(Id("y"),[],None),VarDecl(Id("u"),[],None),VarDecl(Id("o"),[],IntLiteral(8)),VarDecl(Id("q"),[],StringLiteral("vwf"))])

        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_39(self):
        input = """
                    Var: xxxxx, az=898e-43, q={8,9849,9,5,"\\n"};
                    Var: xxx[1], aaaa= {{}, 5}, a[0]={ {** "acbd" **1, 86015}};
                """
        expect = Program([VarDecl(Id("xxxxx"),[],None),VarDecl(Id("az"),[],FloatLiteral(8.98e-41)),VarDecl(Id("q"),[],ArrayLiteral([IntLiteral(8),IntLiteral(9849),IntLiteral(9),IntLiteral(5),StringLiteral("\\n")])),VarDecl(Id("xxx"),[1],None),VarDecl(Id("aaaa"),[],ArrayLiteral([ArrayLiteral([]),IntLiteral(5)])),VarDecl(Id("a"),[0],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(86015)])]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_40(self):
        input = """
                    Var: **a= {a[bdbb5r]}** a[5 ]={{}, {{1,651,7}}};
                """
        expect = Program([VarDecl(Id("a"),[5],ArrayLiteral([ArrayLiteral([]),ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(651),IntLiteral(7)])])]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_41(self):
        input = """
                    Var: x = 1.5e-12, y ,u, o=8, q;
                    Function: cvas4d92654
                        Parameter: a, a[66], r[8]
                        Body:
                            Var: vawmr, avaWC, qrfd[4];
                            foo();

                        EndBody.
                    Function: cvas4d92654
                        Parameter: a, a[66], r[8]
                        Body:
                            Var: vawmr, avaWC, qrfd[4];
                            foo();

                        EndBody.
                """
        expect = Program([VarDecl(Id("x"),[],FloatLiteral(1.5e-12)),VarDecl(Id("y"),[],None),VarDecl(Id("u"),[],None),VarDecl(Id("o"),[],IntLiteral(8)),VarDecl(Id("q"),[],None),FuncDecl(Id("cvas4d92654"),[VarDecl(Id("a"),[],None),VarDecl(Id("a"),[66],None),VarDecl(Id("r"),[8],None)],tuple([[VarDecl(Id("vawmr"),[],None),VarDecl(Id("avaWC"),[],None),VarDecl(Id("qrfd"),[4],None)],[CallStmt(Id("foo"),[])]])),FuncDecl(Id("cvas4d92654"),[VarDecl(Id("a"),[],None),VarDecl(Id("a"),[66],None),VarDecl(Id("r"),[8],None)],tuple([[VarDecl(Id("vawmr"),[],None),VarDecl(Id("avaWC"),[],None),VarDecl(Id("qrfd"),[4],None)],[CallStmt(Id("foo"),[])]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_42(self):
        input = """
                    Var: x, y,sr,arr,uer, wa = 8;
                    Var: cascdv,v = {{}}, z = 5;
                    Function: sgvemo45_____
                        Parameter: ojoijoj[1], a69656[0], x5
                        Body:
                            a=42524+4+a*-ab > 5;
                            If True Then fucking();
                            EndIf.
                            Return dddd+1e-5;
                        EndBody.
                """
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("sr"),[],None),VarDecl(Id("arr"),[],None),VarDecl(Id("uer"),[],None),VarDecl(Id("wa"),[],IntLiteral(8)),VarDecl(Id("cascdv"),[],None),VarDecl(Id("v"),[],ArrayLiteral([ArrayLiteral([])])),VarDecl(Id("z"),[],IntLiteral(5)),FuncDecl(Id("sgvemo45_____"),[VarDecl(Id("ojoijoj"),[1],None),VarDecl(Id("a69656"),[0],None),VarDecl(Id("x5"),[],None)],tuple([[],[Assign(Id("a"),BinaryOp(">",BinaryOp("+",BinaryOp("+",IntLiteral(42524),IntLiteral(4)),BinaryOp("*",Id("a"),UnaryOp("-",Id("ab")))),IntLiteral(5))),If([tuple([BooleanLiteral(True),[],[CallStmt(Id("fucking"),[])]])],tuple([[],[]])),Return(BinaryOp("+",Id("dddd"),FloatLiteral(1e-05)))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_43(self):
        input = """
                    Var: a[5][6][3]={12,2,5,{65,9,5}};
                    Function: josie349arw
                        Parameter: a24mnaaa,h44qa43t,r,qrra,az
                        Body:
                            sjeg(**lsokf**sfle,zugse, 0, 8+9+7);
                            Continue;
                        EndBody.

                    Function: dcmasci
                        Parameter: t4t2, a4, m_34dwq, vwe[6454]
                        Body:
                            Var: tngh[7647443]={};
                            Break;
                        EndBody.
                """
        expect = Program([VarDecl(Id("a"),[5,6,3],ArrayLiteral([IntLiteral(12),IntLiteral(2),IntLiteral(5),ArrayLiteral([IntLiteral(65),IntLiteral(9),IntLiteral(5)])])),FuncDecl(Id("josie349arw"),[VarDecl(Id("a24mnaaa"),[],None),VarDecl(Id("h44qa43t"),[],None),VarDecl(Id("r"),[],None),VarDecl(Id("qrra"),[],None),VarDecl(Id("az"),[],None)],tuple([[],[CallStmt(Id("sjeg"),[Id("sfle"),Id("zugse"),IntLiteral(0),BinaryOp("+",BinaryOp("+",IntLiteral(8),IntLiteral(9)),IntLiteral(7))]),Continue()]])),FuncDecl(Id("dcmasci"),[VarDecl(Id("t4t2"),[],None),VarDecl(Id("a4"),[],None),VarDecl(Id("m_34dwq"),[],None),VarDecl(Id("vwe"),[6454],None)],tuple([[VarDecl(Id("tngh"),[7647443],ArrayLiteral([]))],[Break()]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_44(self):
        input = """
                    Var: a[9]= "265\\n";
                    Function: josie349arw
                        Parameter: a24mnaaa,h44qa43t,r,qrra,az
                        Body:
                            sjeg(**lsokf**sfle,zugse, 0, 8+9+7);
                            u[******wem\\n**"2we820-gq"] = 8 + 12e5 * 0o42 || False;
                            Continue;
                        EndBody.

                    Function: dcmasci
                        Parameter: t4t2, a4, m_34dwq
                        Body:
                            Var: tngh[767443]={};
                            For (x=4,3,4) Do foo(fuckinggoo()); EndFor.
                            Break;
                        EndBody.
                """
        expect = Program([VarDecl(Id("a"),[9],StringLiteral("265\\n")),FuncDecl(Id("josie349arw"),[VarDecl(Id("a24mnaaa"),[],None),VarDecl(Id("h44qa43t"),[],None),VarDecl(Id("r"),[],None),VarDecl(Id("qrra"),[],None),VarDecl(Id("az"),[],None)],tuple([[],[CallStmt(Id("sjeg"),[Id("sfle"),Id("zugse"),IntLiteral(0),BinaryOp("+",BinaryOp("+",IntLiteral(8),IntLiteral(9)),IntLiteral(7))]),Assign(ArrayCell(Id("u"),[StringLiteral("2we820-gq")]),BinaryOp("||",BinaryOp("+",IntLiteral(8),BinaryOp("*",FloatLiteral(1200000.0),IntLiteral(34))),BooleanLiteral(False))),Continue()]])),FuncDecl(Id("dcmasci"),[VarDecl(Id("t4t2"),[],None),VarDecl(Id("a4"),[],None),VarDecl(Id("m_34dwq"),[],None)],tuple([[VarDecl(Id("tngh"),[767443],ArrayLiteral([]))],[For(Id("x"),IntLiteral(4),IntLiteral(3),IntLiteral(4),tuple([[],[CallStmt(Id("foo"),[CallExpr(Id("fuckinggoo"),[])])]])),Break()]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_45(self):
        input = """
                    Var: a[9]= "265\\n";
                    Function: josie349arw
                        Parameter: a24mnaaa,h44qa43t,r,qrra,az
                        Body:
                            Var: xxxxx, az=898e-43, q={8,9849,9,5,"\\n"};
                            xxx[q||c *c \ q]=1;
                            aaaa= {{}, 5};
                            a[a]={ {** "acbd" **1e1, 86015}};
                            sjeg(**lsokf**sfle,zugse, 0, 8+9+7);
                            u[******wem\\n**"2we820-gq"] = 8 + 12e5 * 0o42 || False;
                            Continue;
                        EndBody.

                    Function: dcmasci
                        Parameter: t4t2, a4, m_34dwq[88]
                        Body:
                            Var: tngh[767443]={};
                            Break;
                            true = !True;
                        EndBody.
                """
        expect = Program([VarDecl(Id("a"),[9],StringLiteral("265\\n")),FuncDecl(Id("josie349arw"),[VarDecl(Id("a24mnaaa"),[],None),VarDecl(Id("h44qa43t"),[],None),VarDecl(Id("r"),[],None),VarDecl(Id("qrra"),[],None),VarDecl(Id("az"),[],None)],tuple([[VarDecl(Id("xxxxx"),[],None),VarDecl(Id("az"),[],FloatLiteral(8.98e-41)),VarDecl(Id("q"),[],ArrayLiteral([IntLiteral(8),IntLiteral(9849),IntLiteral(9),IntLiteral(5),StringLiteral("\\n")]))],[Assign(ArrayCell(Id("xxx"),[BinaryOp("||",Id("q"),BinaryOp("\\",BinaryOp("*",Id("c"),Id("c")),Id("q")))]),IntLiteral(1)),Assign(Id("aaaa"),ArrayLiteral([ArrayLiteral([]),IntLiteral(5)])),Assign(ArrayCell(Id("a"),[Id("a")]),ArrayLiteral([ArrayLiteral([FloatLiteral(10.0),IntLiteral(86015)])])),CallStmt(Id("sjeg"),[Id("sfle"),Id("zugse"),IntLiteral(0),BinaryOp("+",BinaryOp("+",IntLiteral(8),IntLiteral(9)),IntLiteral(7))]),Assign(ArrayCell(Id("u"),[StringLiteral("2we820-gq")]),BinaryOp("||",BinaryOp("+",IntLiteral(8),BinaryOp("*",FloatLiteral(1200000.0),IntLiteral(34))),BooleanLiteral(False))),Continue()]])),FuncDecl(Id("dcmasci"),[VarDecl(Id("t4t2"),[],None),VarDecl(Id("a4"),[],None),VarDecl(Id("m_34dwq"),[88],None)],tuple([[VarDecl(Id("tngh"),[767443],ArrayLiteral([]))],[Break(),Assign(Id("true"),UnaryOp("!",BooleanLiteral(True)))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_46(self):
        input = """
                    Var: **a= {a[bdbb5r]}** a[5]={{}, {{1,651,7}}};
                    Function: kovkap__o
                        Parameter: op9v, s5sw, o__iksc
                        Body:
                            Var: fwa6a, trUe, it={{35,892,69,5,0x1},{True, 2.0e-15}};
                            For(b=5,-.b,foo()-10) Do Continue; EndFor.
                        EndBody.
                """
        expect = Program([VarDecl(Id("a"),[5],ArrayLiteral([ArrayLiteral([]),ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(651),IntLiteral(7)])])])),FuncDecl(Id("kovkap__o"),[VarDecl(Id("op9v"),[],None),VarDecl(Id("s5sw"),[],None),VarDecl(Id("o__iksc"),[],None)],tuple([[VarDecl(Id("fwa6a"),[],None),VarDecl(Id("trUe"),[],None),VarDecl(Id("it"),[],ArrayLiteral([ArrayLiteral([IntLiteral(35),IntLiteral(892),IntLiteral(69),IntLiteral(5),IntLiteral(1)]),ArrayLiteral([BooleanLiteral(True),FloatLiteral(2e-15)])]))],[For(Id("b"),IntLiteral(5),UnaryOp("-.",Id("b")),BinaryOp("-",CallExpr(Id("foo"),[]),IntLiteral(10)),tuple([[],[Continue()]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_47(self):
        input = """
                    Var: a={};
                    Function: x
                        Parameter: v[55]
                        Body:
                            x[78||True] = 3 + ({154, 654, {"555"}});
                        EndBody.
                """
        expect = Program([VarDecl(Id("a"),[],ArrayLiteral([])),FuncDecl(Id("x"),[VarDecl(Id("v"),[55],None)],tuple([[],[Assign(ArrayCell(Id("x"),[BinaryOp("||",IntLiteral(78),BooleanLiteral(True))]),BinaryOp("+",IntLiteral(3),ArrayLiteral([IntLiteral(154),IntLiteral(654),ArrayLiteral([StringLiteral("555")])])))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_48(self):
        input = """
                    Var:bcbcb,x,x,a[0]={4,5,6,"cw a={}"};
                    Function: bse
                        Parameter: mncx**=a={21sv15s$%$W}**[789]
                        Body:
                            mybaby = wwife[1] + me[24][256]+{24,"v",1.e6};
                        EndBody.
                """
        expect = Program([VarDecl(Id("bcbcb"),[],None),VarDecl(Id("x"),[],None),VarDecl(Id("x"),[],None),VarDecl(Id("a"),[0],ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6),StringLiteral("cw a={}")])),FuncDecl(Id("bse"),[VarDecl(Id("mncx"),[789],None)],tuple([[],[Assign(Id("mybaby"),BinaryOp("+",BinaryOp("+",ArrayCell(Id("wwife"),[IntLiteral(1)]),ArrayCell(Id("me"),[IntLiteral(24),IntLiteral(256)])),ArrayLiteral([IntLiteral(24),StringLiteral("v"),FloatLiteral(1000000.0)])))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_49(self):
        input = """
                    Var: fy7w, a0={{1.0}, {"651"}};
                    Function: aw
                        Parameter: wtf[4]
                        Body:
                            Var: kn[5596]=78;
                            uk=**cwekjcj{26}5r[26]4()66** {"25164"};
                        EndBody.
                """
        expect = Program([VarDecl(Id("fy7w"),[],None),VarDecl(Id("a0"),[],ArrayLiteral([ArrayLiteral([FloatLiteral(1.0)]),ArrayLiteral([StringLiteral("651")])])),FuncDecl(Id("aw"),[VarDecl(Id("wtf"),[4],None)],tuple([[VarDecl(Id("kn"),[5596],IntLiteral(78))],[Assign(Id("uk"),ArrayLiteral([StringLiteral("25164")]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_50(self):
        input = """
                    Var:q67[73][285][3][9]={"dw"};
                    Function:ca
                        Parameter:khongcoparam, o[0]
                        Body:
                            a[4] = {"array", 0, {},"\\nvui\\n"};
                        EndBody.
                """
        expect = Program([VarDecl(Id("q67"),[73,285,3,9],ArrayLiteral([StringLiteral("dw")])),FuncDecl(Id("ca"),[VarDecl(Id("khongcoparam"),[],None),VarDecl(Id("o"),[0],None)],tuple([[],[Assign(ArrayCell(Id("a"),[IntLiteral(4)]),ArrayLiteral([StringLiteral("array"),IntLiteral(0),ArrayLiteral([]),StringLiteral("\\nvui\\n")]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test_51(self):
        input = """
                    Var: toi_khong_co_don = {"012"}, a = 10;
                    Function:qae
                        Parameter:vaw, doi_toi
                        Body:
                        Var: football_match = {789, 2.e5};
                            khong_con_gi_het = het_tien[0x789];
                        EndBody.
                """
        expect = Program([VarDecl(Id("toi_khong_co_don"),[],ArrayLiteral([StringLiteral("012")])),VarDecl(Id("a"),[],IntLiteral(10)),FuncDecl(Id("qae"),[VarDecl(Id("vaw"),[],None),VarDecl(Id("doi_toi"),[],None)],tuple([[VarDecl(Id("football_match"),[],ArrayLiteral([IntLiteral(789),FloatLiteral(200000.0)]))],[Assign(Id("khong_con_gi_het"),ArrayCell(Id("het_tien"),[IntLiteral(1929)]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_52(self):
        input = """
                    Var: awe,f,wef,we,a[4];
                    Function:zwt56dm
                        Parameter:s,nt,yh,y6r
                        Body:
                            If abcd+ foo() + a[foo()] Then
                                    If fcking()-234>=.1.9+.34e4 Then kool();
                                    ElseIf abcd Then e=p+1;
                                    Else op(); EndIf.
                                ElseIf st&&st Then ok_man();
                                EndIf.
                        EndBody.
                """
        expect = Program([VarDecl(Id("awe"),[],None),VarDecl(Id("f"),[],None),VarDecl(Id("wef"),[],None),VarDecl(Id("we"),[],None),VarDecl(Id("a"),[4],None),FuncDecl(Id("zwt56dm"),[VarDecl(Id("s"),[],None),VarDecl(Id("nt"),[],None),VarDecl(Id("yh"),[],None),VarDecl(Id("y6r"),[],None)],tuple([[],[If([tuple([BinaryOp("+",BinaryOp("+",Id("abcd"),CallExpr(Id("foo"),[])),ArrayCell(Id("a"),[CallExpr(Id("foo"),[])])),[],[If([tuple([BinaryOp(">=.",BinaryOp("-",CallExpr(Id("fcking"),[]),IntLiteral(234)),BinaryOp("+.",FloatLiteral(1.9),FloatLiteral(340000.0))),[],[CallStmt(Id("kool"),[])]]),tuple([Id("abcd"),[],[Assign(Id("e"),BinaryOp("+",Id("p"),IntLiteral(1)))]])],tuple([[],[CallStmt(Id("op"),[])]]))]]),tuple([BinaryOp("&&",Id("st"),Id("st")),[],[CallStmt(Id("ok_man"),[])]])],tuple([[],[]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_53(self):
        input = """
                    Var: awe,f,wef,we,a[4];
                    Function:zwt56dm
                        Parameter:s,nt,yh,y6r
                        Body:
                        Var:a=3;
                            If abcd+ foo() + a[foo()] Then
                                    If fcking()-234>=.1.9+.34e4 Then kool();
                                    ElseIf abcd Then e=p+1;
                                    Else op();
                                    EndIf.
                                ElseIf st&&st Then ok_man();
                                ElseIf 72%7&&cqwiw+(ad+q3) Then
                                a=1-2;
                                foo();
                                EndIf.

                        If abcd+ foo() + a[foo()] Then
                                If fcking()-234>=.1.9+.34e4 Then kool();
                                EndIf.
                            ElseIf 72%7&&cqwiw+(ad+q3) Then
                            Var: a, t=3, a[4];
                            foo(cho_toi_tay_vin);
                            Return tau_nhanh_500k();
                            EndIf.
                        EndBody.
                """
        expect = Program([VarDecl(Id("awe"),[],None),VarDecl(Id("f"),[],None),VarDecl(Id("wef"),[],None),VarDecl(Id("we"),[],None),VarDecl(Id("a"),[4],None),FuncDecl(Id("zwt56dm"),[VarDecl(Id("s"),[],None),VarDecl(Id("nt"),[],None),VarDecl(Id("yh"),[],None),VarDecl(Id("y6r"),[],None)],tuple([[VarDecl(Id("a"),[],IntLiteral(3))],[If([tuple([BinaryOp("+",BinaryOp("+",Id("abcd"),CallExpr(Id("foo"),[])),ArrayCell(Id("a"),[CallExpr(Id("foo"),[])])),[],[If([tuple([BinaryOp(">=.",BinaryOp("-",CallExpr(Id("fcking"),[]),IntLiteral(234)),BinaryOp("+.",FloatLiteral(1.9),FloatLiteral(340000.0))),[],[CallStmt(Id("kool"),[])]]),tuple([Id("abcd"),[],[Assign(Id("e"),BinaryOp("+",Id("p"),IntLiteral(1)))]])],tuple([[],[CallStmt(Id("op"),[])]]))]]),tuple([BinaryOp("&&",Id("st"),Id("st")),[],[CallStmt(Id("ok_man"),[])]]),tuple([BinaryOp("&&",BinaryOp("%",IntLiteral(72),IntLiteral(7)),BinaryOp("+",Id("cqwiw"),BinaryOp("+",Id("ad"),Id("q3")))),[],[Assign(Id("a"),BinaryOp("-",IntLiteral(1),IntLiteral(2))),CallStmt(Id("foo"),[])]])],tuple([[],[]])),If([tuple([BinaryOp("+",BinaryOp("+",Id("abcd"),CallExpr(Id("foo"),[])),ArrayCell(Id("a"),[CallExpr(Id("foo"),[])])),[],[If([tuple([BinaryOp(">=.",BinaryOp("-",CallExpr(Id("fcking"),[]),IntLiteral(234)),BinaryOp("+.",FloatLiteral(1.9),FloatLiteral(340000.0))),[],[CallStmt(Id("kool"),[])]])],tuple([[],[]]))]]),tuple([BinaryOp("&&",BinaryOp("%",IntLiteral(72),IntLiteral(7)),BinaryOp("+",Id("cqwiw"),BinaryOp("+",Id("ad"),Id("q3")))),[VarDecl(Id("a"),[],None),VarDecl(Id("t"),[],IntLiteral(3)),VarDecl(Id("a"),[4],None)],[CallStmt(Id("foo"),[Id("cho_toi_tay_vin")]),Return(CallExpr(Id("tau_nhanh_500k"),[]))]])],tuple([[],[]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_54(self):
        input = """
                        Var:ww51,f32fg=2.e907,b[656465]={};
                        Function:d
                            Parameter:fwe
                            Body:
                                For (awer=10,awer[foo()],arw < 6) Do fcking();
                                ae = a[True] -. 0x78;
                                    For (e=False,st,{{"2"}}) Do
                                    goi_em_la_du_du = foo();
                                    If abc Then
                                    While fucking Do nothing(); EndWhile.
                                    EndIf.
                                    EndFor.
                                EndFor.
                            EndBody.
                """
        expect = Program([VarDecl(Id("ww51"),[],None),VarDecl(Id("f32fg"),[],FloatLiteral(2.e907)),VarDecl(Id("b"),[656465],ArrayLiteral([])),FuncDecl(Id("d"),[VarDecl(Id("fwe"),[],None)],tuple([[],[For(Id("awer"),IntLiteral(10),ArrayCell(Id("awer"),[CallExpr(Id("foo"),[])]),BinaryOp("<",Id("arw"),IntLiteral(6)),tuple([[],[CallStmt(Id("fcking"),[]),Assign(Id("ae"),BinaryOp("-.",ArrayCell(Id("a"),[BooleanLiteral(True)]),IntLiteral(120))),For(Id("e"),BooleanLiteral(False),Id("st"),ArrayLiteral([ArrayLiteral([StringLiteral("2")])]),tuple([[],[Assign(Id("goi_em_la_du_du"),CallExpr(Id("foo"),[])),If([tuple([Id("abc"),[],[While(Id("fucking"),tuple([[],[CallStmt(Id("nothing"),[])]]))]])],tuple([[],[]]))]]))]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_55(self):
        input = """
                        Var:abc, a[23]={{}, 654, "6396"};
                        Function: fas_cko_8rfkw
                            Parameter: a[15], q[68], acf5qf4_iuqw
                            Body:
                                Var: wf87[752]={};
                                While foo() -. 1.9e7 + "ekigk" Do
                                    If True Then EndIf. Do Break;
                                    soooo(wfwe[234\\soo()]);
                                    While x+y EndDo.
                                    EndWhile.
                            EndBody.
                """
        expect = Program([VarDecl(Id("abc"),[],None),VarDecl(Id("a"),[23],ArrayLiteral([ArrayLiteral([]),IntLiteral(654),StringLiteral("6396")])),FuncDecl(Id("fas_cko_8rfkw"),[VarDecl(Id("a"),[15],None),VarDecl(Id("q"),[68],None),VarDecl(Id("acf5qf4_iuqw"),[],None)],tuple([[VarDecl(Id("wf87"),[752],ArrayLiteral([]))],[While(BinaryOp("+",BinaryOp("-.",CallExpr(Id("foo"),[]),FloatLiteral(19000000.0)),StringLiteral("ekigk")),tuple([[],[If([tuple([BooleanLiteral(True),[],[]])],tuple([[],[]])),Dowhile(tuple([[],[Break(),CallStmt(Id("soooo"),[ArrayCell(Id("wfwe"),[BinaryOp("\\",IntLiteral(234),CallExpr(Id("soo"),[]))])])]]),BinaryOp("+",Id("x"),Id("y")))]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_56(self):
        input = """
                    Var:abc, a[23]={{}, 654, "6396"};
                    Function: fas_cko_8rfkw
                        Parameter: a[15], q[68], acf5qf4_iuqw
                        Body:
                            Var: wf87[752]={};
                            Do
                            soooo(wfwe[234\\soo()]);
                                 Do
                                    Break;
                                    If True Then EndIf.
                                While (foo() -. 1.9e7 + "ekigk") Do
                            While (foo() -. 1.9e7 + "ekigk")DoEndWhile.EndWhile.
                            While foo()||co
                            EndDo.
                            While xxx+yyy||123-1e9
                            EndDo.
                        EndBody.
                """
        expect = Program([VarDecl(Id("abc"),[],None),VarDecl(Id("a"),[23],ArrayLiteral([ArrayLiteral([]),IntLiteral(654),StringLiteral("6396")])),FuncDecl(Id("fas_cko_8rfkw"),[VarDecl(Id("a"),[15],None),VarDecl(Id("q"),[68],None),VarDecl(Id("acf5qf4_iuqw"),[],None)],tuple([[VarDecl(Id("wf87"),[752],ArrayLiteral([]))],[Dowhile(tuple([[],[CallStmt(Id("soooo"),[ArrayCell(Id("wfwe"),[BinaryOp("\\",IntLiteral(234),CallExpr(Id("soo"),[]))])]),Dowhile(tuple([[],[Break(),If([tuple([BooleanLiteral(True),[],[]])],tuple([[],[]])),While(BinaryOp("+",BinaryOp("-.",CallExpr(Id("foo"),[]),FloatLiteral(19000000.0)),StringLiteral("ekigk")),tuple([[],[While(BinaryOp("+",BinaryOp("-.",CallExpr(Id("foo"),[]),FloatLiteral(19000000.0)),StringLiteral("ekigk")),tuple([[],[]]))]]))]]),BinaryOp("||",CallExpr(Id("foo"),[]),Id("co")))]]),BinaryOp("||",BinaryOp("+",Id("xxx"),Id("yyy")),BinaryOp("-",IntLiteral(123),FloatLiteral(1000000000.0))))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_57(self):
        input = """
                    Var:abc, a[23]={{}, 654, "6396"};
                    Function: fas_cko_8rfkw
                        Parameter: a[15], q[68], acf5qf4_iuqw
                        Body:
                            Var: wf87[752]={};
                            Do Do While (foo() -. 1.9e7 + "ekigk") Do
                            While r Do EndWhile. Do While 4 EndDo. EndWhile.
                            While 10-5+et EndDo.
                            While a EndDo.
                        EndBody.
                """
        expect = Program([VarDecl(Id("abc"),[],None),VarDecl(Id("a"),[23],ArrayLiteral([ArrayLiteral([]),IntLiteral(654),StringLiteral("6396")])),FuncDecl(Id("fas_cko_8rfkw"),[VarDecl(Id("a"),[15],None),VarDecl(Id("q"),[68],None),VarDecl(Id("acf5qf4_iuqw"),[],None)],tuple([[VarDecl(Id("wf87"),[752],ArrayLiteral([]))],[Dowhile(tuple([[],[Dowhile(tuple([[],[While(BinaryOp("+",BinaryOp("-.",CallExpr(Id("foo"),[]),FloatLiteral(19000000.0)),StringLiteral("ekigk")),tuple([[],[While(Id("r"),tuple([[],[]])),Dowhile(tuple([[],[]]),IntLiteral(4))]]))]]),BinaryOp("+",BinaryOp("-",IntLiteral(10),IntLiteral(5)),Id("et")))]]),Id("a"))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_58(self):
        input = """
                    Var: a=1;
                    Function: a
                        Parameter: x[12][1], a
                        Body:
                            While (x["vseokaef"]) Do EndWhile.
                            If (oham>=.7536e89) + {{},{}} Then x=5+"65467"*.{}; EndIf.
                            x[foo()||1.e8][6\\8*.1.] = **{a{ *"1.2"}, {1,2,3**{{}, 0e89}||False;
                        EndBody.
                """
        expect = Program([VarDecl(Id("a"),[],IntLiteral(1)),FuncDecl(Id("a"),[VarDecl(Id("x"),[12,1],None),VarDecl(Id("a"),[],None)],tuple([[],[While(ArrayCell(Id("x"),[StringLiteral("vseokaef")]),tuple([[],[]])),If([tuple([BinaryOp("+",BinaryOp(">=.",Id("oham"),FloatLiteral(7.536e+92)),ArrayLiteral([ArrayLiteral([]),ArrayLiteral([])])),[],[Assign(Id("x"),BinaryOp("+",IntLiteral(5),BinaryOp("*.",StringLiteral("65467"),ArrayLiteral([]))))]])],tuple([[],[]])),Assign(ArrayCell(Id("x"),[BinaryOp("||",CallExpr(Id("foo"),[]),FloatLiteral(100000000.0)),BinaryOp("*.",BinaryOp("\\",IntLiteral(6),IntLiteral(8)),FloatLiteral(1.0))]),BinaryOp("||",ArrayLiteral([ArrayLiteral([]),FloatLiteral(0.0)]),BooleanLiteral(False)))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_59(self):
        input = """
                    Var: a ,b,c;
                    Function: day_la_func_0
                        Parameter: x, a[256][45]
                        Body:
                            Break;
                            Return;
                            For (x=1,x,x) DoReturn; EndFor.
                        EndBody.
                    Function:day_la_func_1
                        Body:
                            While x Do Continue; EndWhile.
                            Return;
                        For (x=1,x,x) Do Continue;sothat();EndFor.EndBody.
                """
        expect = Program([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None),FuncDecl(Id("day_la_func_0"),[VarDecl(Id("x"),[],None),VarDecl(Id("a"),[256,45],None)],tuple([[],[Break(),Return(None),For(Id("x"),IntLiteral(1),Id("x"),Id("x"),tuple([[],[Return(None)]]))]])),FuncDecl(Id("day_la_func_1"),[],tuple([[],[While(Id("x"),tuple([[],[Continue()]])),Return(None),For(Id("x"),IntLiteral(1),Id("x"),Id("x"),tuple([[],[Continue(),CallStmt(Id("sothat"),[])]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_60(self):
        input = """
                    Var: a,b,c;
                    Function: day_la_func_0
                        Parameter: x, a[256][45]
                        Body:
                            Break ;
                            Return;
                            For (x=1,x,x) DoReturn ; EndFor.
                            While x Do Continue; EndWhile.
                            Return "qwe"+82284*.foo();
                        For (a=9,foo(),(a[foo() + 8] - too()[9])) Do Continue;sothat();EndFor.
                        EndBody.
                """
        expect = Program([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None),FuncDecl(Id("day_la_func_0"),[VarDecl(Id("x"),[],None),VarDecl(Id("a"),[256,45],None)],tuple([[],[Break(),Return(None),For(Id("x"),IntLiteral(1),Id("x"),Id("x"),tuple([[],[Return(None)]])),While(Id("x"),tuple([[],[Continue()]])),Return(BinaryOp("+",StringLiteral("qwe"),BinaryOp("*.",IntLiteral(82284),CallExpr(Id("foo"),[])))),For(Id("a"),IntLiteral(9),CallExpr(Id("foo"),[]),BinaryOp("-",ArrayCell(Id("a"),[BinaryOp("+",CallExpr(Id("foo"),[]),IntLiteral(8))]),ArrayCell(CallExpr(Id("too"),[]),[IntLiteral(9)])),tuple([[],[Continue(),CallStmt(Id("sothat"),[])]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_61(self):
        input = """
                    Var:a,b[2],c[3][4];
                    Function: acbd_4567_ABCD
                        Parameter:d[1][52][96596][654569], cwij439f
                        Body:
                            a["fwck"]=erw[gw652] \. {"abcdf"} == fo()[x-1e5];
                        EndBody.
                """
        expect = Program([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2],None),VarDecl(Id("c"),[3,4],None),FuncDecl(Id("acbd_4567_ABCD"),[VarDecl(Id("d"),[1,52,96596,654569],None),VarDecl(Id("cwij439f"),[],None)],tuple([[],[Assign(ArrayCell(Id("a"),[StringLiteral("fwck")]),BinaryOp("==",BinaryOp("\\.",ArrayCell(Id("erw"),[Id("gw652")]),ArrayLiteral([StringLiteral("abcdf")])),ArrayCell(CallExpr(Id("fo"),[]),[BinaryOp("-",Id("x"),FloatLiteral(100000.0))])))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_62(self):
        input = """
                    Var:a,b[2],c[3][4];
                    Function: acbd_4567_ABCD
                        Parameter:d[1][52][96596][654569], cwij439f
                        Body:
                            a["fwck"]=erw[gw652]+**a[{"abcdf w" }+123];
                            If 224+a[awf+ngaymaise(xxx, "31")[4e78]+8] Then **y[xxx] == {{{},{}},{}};
                        EndBody.
                """
        expect = Program([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2],None),VarDecl(Id("c"),[3,4],None),FuncDecl(Id("acbd_4567_ABCD"),[VarDecl(Id("d"),[1,52,96596,654569],None),VarDecl(Id("cwij439f"),[],None)],tuple([[],[Assign(ArrayCell(Id("a"),[StringLiteral("fwck")]),BinaryOp("==",BinaryOp("+",ArrayCell(Id("erw"),[Id("gw652")]),ArrayCell(Id("y"),[Id("xxx")])),ArrayLiteral([ArrayLiteral([ArrayLiteral([]),ArrayLiteral([])]),ArrayLiteral([])])))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    def test_63(self):
        input = """
                    Var:a,b[2],c[3][4];
                    Function: acbd_4567_ABCD
                        Parameter:d[1][52][96596][654569], cwij439f
                        Body:
                            call_some_fck_func({1,3}+0, 7*.8.7e8);
                            call_some_fck_func({1,3}+0, 7*.8.7e8, True);
                            Break;
                            If 0-0 Then
                            a[fucking(some_girls - f()[ cse[212][0o75] ])]=call_some_fck_func({1,3}+0, 7*.8.7e8, a[1.5])+1;
                                    Else a=0-0||True;
                                    EndIf.
                        EndBody.
                """
        expect = Program([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2],None),VarDecl(Id("c"),[3,4],None),FuncDecl(Id("acbd_4567_ABCD"),[VarDecl(Id("d"),[1,52,96596,654569],None),VarDecl(Id("cwij439f"),[],None)],tuple([[],[CallStmt(Id("call_some_fck_func"),[BinaryOp("+",ArrayLiteral([IntLiteral(1),IntLiteral(3)]),IntLiteral(0)),BinaryOp("*.",IntLiteral(7),FloatLiteral(870000000.0))]),CallStmt(Id("call_some_fck_func"),[BinaryOp("+",ArrayLiteral([IntLiteral(1),IntLiteral(3)]),IntLiteral(0)),BinaryOp("*.",IntLiteral(7),FloatLiteral(870000000.0)),BooleanLiteral(True)]),Break(),If([tuple([BinaryOp("-",IntLiteral(0),IntLiteral(0)),[],[Assign(ArrayCell(Id("a"),[CallExpr(Id("fucking"),[BinaryOp("-",Id("some_girls"),ArrayCell(CallExpr(Id("f"),[]),[ArrayCell(Id("cse"),[IntLiteral(212),IntLiteral(61)])]))])]),BinaryOp("+",CallExpr(Id("call_some_fck_func"),[BinaryOp("+",ArrayLiteral([IntLiteral(1),IntLiteral(3)]),IntLiteral(0)),BinaryOp("*.",IntLiteral(7),FloatLiteral(870000000.0)),ArrayCell(Id("a"),[FloatLiteral(1.5)])]),IntLiteral(1)))]])],tuple([[],[Assign(Id("a"),BinaryOp("||",BinaryOp("-",IntLiteral(0),IntLiteral(0)),BooleanLiteral(True)))]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_64(self):
        input = """
                    Var:a,b[2],c[3][4];
                    Function: acbd_4567_ABCD
                        Parameter:d[1][52][96596][654569], cwij439f
                        Body:
                            call_some_fck_func({1,3}+0, 7*.8.7e8);
                            call_some_fck_func({"1\\n6",3}+0, 7*.8.7e8, True);
                            a[fucking()]=call_some_fck_func({1,3}+0, 7*.8.7e8==9, a[1.5])==7+1;
                            Return st(8**324 fcnq24jf32r3q4%^&*23 3**, fq, 24,{"'""}+8);
                            For (metooo = "cjwie", 4-23, 1e4) Do
                            Do Var: a[1]={"efw"};
                            xx=baby_shark(do, do, do ,do)[0o7];
                            While True EndDo. EndFor.
                        EndBody.
                """
        expect = Program([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[2],None),VarDecl(Id("c"),[3,4],None),FuncDecl(Id("acbd_4567_ABCD"),[VarDecl(Id("d"),[1,52,96596,654569],None),VarDecl(Id("cwij439f"),[],None)],tuple([[],[CallStmt(Id("call_some_fck_func"),[BinaryOp("+",ArrayLiteral([IntLiteral(1),IntLiteral(3)]),IntLiteral(0)),BinaryOp("*.",IntLiteral(7),FloatLiteral(870000000.0))]),CallStmt(Id("call_some_fck_func"),[BinaryOp("+",ArrayLiteral([StringLiteral("1\\n6"),IntLiteral(3)]),IntLiteral(0)),BinaryOp("*.",IntLiteral(7),FloatLiteral(870000000.0)),BooleanLiteral(True)]),Assign(ArrayCell(Id("a"),[CallExpr(Id("fucking"),[])]),BinaryOp("==",CallExpr(Id("call_some_fck_func"),[BinaryOp("+",ArrayLiteral([IntLiteral(1),IntLiteral(3)]),IntLiteral(0)),BinaryOp("==",BinaryOp("*.",IntLiteral(7),FloatLiteral(870000000.0)),IntLiteral(9)),ArrayCell(Id("a"),[FloatLiteral(1.5)])]),BinaryOp("+",IntLiteral(7),IntLiteral(1)))),Return(CallExpr(Id("st"),[IntLiteral(8),Id("fq"),IntLiteral(24),BinaryOp("+",ArrayLiteral([StringLiteral("\'\"")]),IntLiteral(8))])),For(Id("metooo"),StringLiteral("cjwie"),BinaryOp("-",IntLiteral(4),IntLiteral(23)),FloatLiteral(10000.0),tuple([[],[Dowhile(tuple([[VarDecl(Id("a"),[1],ArrayLiteral([StringLiteral("efw")]))],[Assign(Id("xx"),ArrayCell(CallExpr(Id("baby_shark"),[Id("do"),Id("do"),Id("do"),Id("do")]),[IntLiteral(7)]))]]),BooleanLiteral(True))]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def test_65(self):
        input = """
                    Var:abc, a[23]={{}, 654, "6396"};
                    Function: fas_cko_8rfkw
                        Parameter: a[15], q[68], acf5qf4_iuqw
                        Body:
                            Var: wf87[752]={};
                            While foo() -. 1.9e7 + "ekigk" Do
                            Var: a=89.63;
                                If True Then EndIf.
                                EndWhile.
                            Break;
                            Do rtoooo(); e[12]= {8,1e5,"6549"};
                            While io EndDo.
                        EndBody.
                """
        expect = Program([VarDecl(Id("abc"),[],None),VarDecl(Id("a"),[23],ArrayLiteral([ArrayLiteral([]),IntLiteral(654),StringLiteral("6396")])),FuncDecl(Id("fas_cko_8rfkw"),[VarDecl(Id("a"),[15],None),VarDecl(Id("q"),[68],None),VarDecl(Id("acf5qf4_iuqw"),[],None)],tuple([[VarDecl(Id("wf87"),[752],ArrayLiteral([]))],[While(BinaryOp("+",BinaryOp("-.",CallExpr(Id("foo"),[]),FloatLiteral(19000000.0)),StringLiteral("ekigk")),tuple([[VarDecl(Id("a"),[],FloatLiteral(89.63))],[If([tuple([BooleanLiteral(True),[],[]])],tuple([[],[]]))]])),Break(),Dowhile(tuple([[],[CallStmt(Id("rtoooo"),[]),Assign(ArrayCell(Id("e"),[IntLiteral(12)]),ArrayLiteral([IntLiteral(8),FloatLiteral(100000.0),StringLiteral("6549")]))]]),Id("io"))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    def test_66(self):
        input = """
                    Var:abc, a[23]={{}, 654, "6396"};
                    Function: fas_cko_8rfkw
                        Parameter: a[15], q[68], acf5qf4_iuqw
                        Body:
                            Var: wf87[752]={};
                            While foo() -. 1.9e7 + "ekigk" Do
                            Var: a=89.63;
                                If True Then EndIf.
                                EndWhile.
                            Break;
                            Do rtoooo(); e[12]= {8,1e5,"6549"};
                            While io EndDo.
                        EndBody.
                            Function: acbd_4567_ABCD
                                Parameter:d[1][52][96596][654569], cwij439f
                                Body:
                                    a["fwck"]=erw[gw652]**a[{"abcdf w" }+123];
                                    If 224+a[awf+{25, "ee"}] Then y**[xxx]== {{{},{}},{}}; Continue;
                                    a[6*{8}] = (a[{1,2,3}]-{34,"51",1e4});
                                EndBody.

                Function: acbd_4567_ABCD
                    Parameter:d[1][52][96596][654569], cwij439f
                    Body:
                        a[fucking()]=call_some_fck_func({1,3}+0, 7*.8.7e8, a[1.5])+1;
                        f00();
                        Break; Return {1,2,3};
                    EndBody.
                """
        expect = Program([VarDecl(Id("abc"),[],None),VarDecl(Id("a"),[23],ArrayLiteral([ArrayLiteral([]),IntLiteral(654),StringLiteral("6396")])),FuncDecl(Id("fas_cko_8rfkw"),[VarDecl(Id("a"),[15],None),VarDecl(Id("q"),[68],None),VarDecl(Id("acf5qf4_iuqw"),[],None)],tuple([[VarDecl(Id("wf87"),[752],ArrayLiteral([]))],[While(BinaryOp("+",BinaryOp("-.",CallExpr(Id("foo"),[]),FloatLiteral(19000000.0)),StringLiteral("ekigk")),tuple([[VarDecl(Id("a"),[],FloatLiteral(89.63))],[If([tuple([BooleanLiteral(True),[],[]])],tuple([[],[]]))]])),Break(),Dowhile(tuple([[],[CallStmt(Id("rtoooo"),[]),Assign(ArrayCell(Id("e"),[IntLiteral(12)]),ArrayLiteral([IntLiteral(8),FloatLiteral(100000.0),StringLiteral("6549")]))]]),Id("io"))]])),FuncDecl(Id("acbd_4567_ABCD"),[VarDecl(Id("d"),[1,52,96596,654569],None),VarDecl(Id("cwij439f"),[],None)],tuple([[],[Assign(ArrayCell(Id("a"),[StringLiteral("fwck")]),BinaryOp("==",ArrayCell(Id("erw"),[Id("gw652"),Id("xxx")]),ArrayLiteral([ArrayLiteral([ArrayLiteral([]),ArrayLiteral([])]),ArrayLiteral([])]))),Continue(),Assign(ArrayCell(Id("a"),[BinaryOp("*",IntLiteral(6),ArrayLiteral([IntLiteral(8)]))]),BinaryOp("-",ArrayCell(Id("a"),[ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])]),ArrayLiteral([IntLiteral(34),StringLiteral("51"),FloatLiteral(10000.0)])))]])),FuncDecl(Id("acbd_4567_ABCD"),[VarDecl(Id("d"),[1,52,96596,654569],None),VarDecl(Id("cwij439f"),[],None)],tuple([[],[Assign(ArrayCell(Id("a"),[CallExpr(Id("fucking"),[])]),BinaryOp("+",CallExpr(Id("call_some_fck_func"),[BinaryOp("+",ArrayLiteral([IntLiteral(1),IntLiteral(3)]),IntLiteral(0)),BinaryOp("*.",IntLiteral(7),FloatLiteral(870000000.0)),ArrayCell(Id("a"),[FloatLiteral(1.5)])]),IntLiteral(1))),CallStmt(Id("f00"),[]),Break(),Return(ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_67(self):
        input = """
                    Var: x, y, z = 9, oOoO[0][0] = {{}};
                    Var: vaf, vas, var, vax, vaj = 0e5;
                    Function: do_it
                        Parameter: e, ee, eee, eeee, eeeee
                        Body:
                            Var: okConDe = "\\tcvasvevsi";
                            ** Var: @#$%^&*() **
                            Break;
                            For (x="", go(), lang) Do
                                du_du_durex = 30*k;
                                o[0] = {};
                            EndFor.
                        EndBody.
                """
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],IntLiteral(9)),VarDecl(Id("oOoO"),[0,0],ArrayLiteral([ArrayLiteral([])])),VarDecl(Id("vaf"),[],None),VarDecl(Id("vas"),[],None),VarDecl(Id("var"),[],None),VarDecl(Id("vax"),[],None),VarDecl(Id("vaj"),[],FloatLiteral(0.0)),FuncDecl(Id("do_it"),[VarDecl(Id("e"),[],None),VarDecl(Id("ee"),[],None),VarDecl(Id("eee"),[],None),VarDecl(Id("eeee"),[],None),VarDecl(Id("eeeee"),[],None)],tuple([[VarDecl(Id("okConDe"),[],StringLiteral("\\tcvasvevsi"))],[Break(),For(Id("x"),StringLiteral(""),CallExpr(Id("go"),[]),Id("lang"),tuple([[],[Assign(Id("du_du_durex"),BinaryOp("*",IntLiteral(30),Id("k"))),Assign(ArrayCell(Id("o"),[IntLiteral(0)]),ArrayLiteral([]))]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test_68(self):
        input = """
                    Var: x, y, z = 9, oOoO[0][0] = {{}};
                    Var: vaf, vas, var, vax, vaj = 0e5;
                    Function: do_it
                        Parameter: e, ee, eee, eeee, eeeee
                        Body:
                            Var: okConDe = "\\ncvasvevsi";
                            ** Var: @#$%^&*() **
                            For (x="", go(), lang) Do
                            Var: a;
                            While em_yeu_anh Do
                                du_du_durex = 30*k;
                                EndWhile.
                                o[0] = {};
                                Continue;
                            EndFor.
                        EndBody.
                """
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],IntLiteral(9)),VarDecl(Id("oOoO"),[0,0],ArrayLiteral([ArrayLiteral([])])),VarDecl(Id("vaf"),[],None),VarDecl(Id("vas"),[],None),VarDecl(Id("var"),[],None),VarDecl(Id("vax"),[],None),VarDecl(Id("vaj"),[],FloatLiteral(0.0)),FuncDecl(Id("do_it"),[VarDecl(Id("e"),[],None),VarDecl(Id("ee"),[],None),VarDecl(Id("eee"),[],None),VarDecl(Id("eeee"),[],None),VarDecl(Id("eeeee"),[],None)],tuple([[VarDecl(Id("okConDe"),[],StringLiteral("\\ncvasvevsi"))],[For(Id("x"),StringLiteral(""),CallExpr(Id("go"),[]),Id("lang"),tuple([[VarDecl(Id("a"),[],None)],[While(Id("em_yeu_anh"),tuple([[],[Assign(Id("du_du_durex"),BinaryOp("*",IntLiteral(30),Id("k")))]])),Assign(ArrayCell(Id("o"),[IntLiteral(0)]),ArrayLiteral([])),Continue()]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_69(self):
        input = """
                    Var: x, y, z = 9, oOoO[0][0] = {{}};
                    Var: vaf, vas, var, vax, vaj = 0e5;
                    Function: do_it
                        Parameter: e, ee, eee, eeee, eeeee
                        Body:
                            Var: okConDe = "\\\\cvasvevsi";
                            ** Var: @#$%^&*() **
                            For (x="", go(), lang) Do
                            Var: a;
                            While em_yeu_anh Do
                            Var: taisaolaikhaibaobienoday;
                                du_du_durex = 30*k;
                                EndWhile.
                                o[0] = {};
                                Continue;
                            EndFor.
                        EndBody.
                    Function: do_it
                        Parameter: e, ee, eee, eeee, eeeee
                        Body:
                            For (x="", go(), lang) Do
                            Var: a;
                                du_du_durex = 30*k;
                                o[0] = {};
                                EndFor.
                        EndBody.
                """
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],IntLiteral(9)),VarDecl(Id("oOoO"),[0,0],ArrayLiteral([ArrayLiteral([])])),VarDecl(Id("vaf"),[],None),VarDecl(Id("vas"),[],None),VarDecl(Id("var"),[],None),VarDecl(Id("vax"),[],None),VarDecl(Id("vaj"),[],FloatLiteral(0.0)),FuncDecl(Id("do_it"),[VarDecl(Id("e"),[],None),VarDecl(Id("ee"),[],None),VarDecl(Id("eee"),[],None),VarDecl(Id("eeee"),[],None),VarDecl(Id("eeeee"),[],None)],tuple([[VarDecl(Id("okConDe"),[],StringLiteral("\\\\cvasvevsi"))],[For(Id("x"),StringLiteral(""),CallExpr(Id("go"),[]),Id("lang"),tuple([[VarDecl(Id("a"),[],None)],[While(Id("em_yeu_anh"),tuple([[VarDecl(Id("taisaolaikhaibaobienoday"),[],None)],[Assign(Id("du_du_durex"),BinaryOp("*",IntLiteral(30),Id("k")))]])),Assign(ArrayCell(Id("o"),[IntLiteral(0)]),ArrayLiteral([])),Continue()]]))]])),FuncDecl(Id("do_it"),[VarDecl(Id("e"),[],None),VarDecl(Id("ee"),[],None),VarDecl(Id("eee"),[],None),VarDecl(Id("eeee"),[],None),VarDecl(Id("eeeee"),[],None)],tuple([[],[For(Id("x"),StringLiteral(""),CallExpr(Id("go"),[]),Id("lang"),tuple([[VarDecl(Id("a"),[],None)],[Assign(Id("du_du_durex"),BinaryOp("*",IntLiteral(30),Id("k"))),Assign(ArrayCell(Id("o"),[IntLiteral(0)]),ArrayLiteral([]))]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_70(self):
        input = """
                    Var: x, y, z = 9, oOoO[0][0] = {{}};
                    Function: do_it
                        Body:
                            Var: okConDe = "\\\\cvasvevsi";
                            Var: vaf, vas, var, vax, vaj = 0e5;
                        EndBody.
                    Function: do_it
                        Body:
                            Var: okConDe = "\\tcvasvevsi";
                            Var: vaf, vas, var, vax, vaj = 0e5;
                        EndBody.
                    Function: do_it
                        Body:
                            Var: okConDe = "\\bcvasvevsi";
                            Var: vaf, vas, var, vax, vaj = 0e5;
                        EndBody.
                    Function: do_it
                        Body:
                            Var: okConDe = "\\\\cvasvevsi";
                            Var: vaf, vas, var, vax, vaj = 0e5;
                        EndBody.
                """
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],IntLiteral(9)),VarDecl(Id("oOoO"),[0,0],ArrayLiteral([ArrayLiteral([])])),FuncDecl(Id("do_it"),[],tuple([[VarDecl(Id("okConDe"),[],StringLiteral("\\\\cvasvevsi")),VarDecl(Id("vaf"),[],None),VarDecl(Id("vas"),[],None),VarDecl(Id("var"),[],None),VarDecl(Id("vax"),[],None),VarDecl(Id("vaj"),[],FloatLiteral(0.0))],[]])),FuncDecl(Id("do_it"),[],tuple([[VarDecl(Id("okConDe"),[],StringLiteral("\\tcvasvevsi")),VarDecl(Id("vaf"),[],None),VarDecl(Id("vas"),[],None),VarDecl(Id("var"),[],None),VarDecl(Id("vax"),[],None),VarDecl(Id("vaj"),[],FloatLiteral(0.0))],[]])),FuncDecl(Id("do_it"),[],tuple([[VarDecl(Id("okConDe"),[],StringLiteral("\\bcvasvevsi")),VarDecl(Id("vaf"),[],None),VarDecl(Id("vas"),[],None),VarDecl(Id("var"),[],None),VarDecl(Id("vax"),[],None),VarDecl(Id("vaj"),[],FloatLiteral(0.0))],[]])),FuncDecl(Id("do_it"),[],tuple([[VarDecl(Id("okConDe"),[],StringLiteral("\\\\cvasvevsi")),VarDecl(Id("vaf"),[],None),VarDecl(Id("vas"),[],None),VarDecl(Id("var"),[],None),VarDecl(Id("vax"),[],None),VarDecl(Id("vaj"),[],FloatLiteral(0.0))],[]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_71(self):
        input = """
                    Function: do_it
                        Body:
                            Var: okConDe = "\\\\cvasvevsi";
                            Var: vaf, vas, var, vax, vaj = 0e5;
                            For (r=0, r <= 123, r+1) Do
                                cong_cho_vui_vay_thoi();
                                do_it_right_now(a, as, aa, {}, cowf,dowfl);
                                Return 0;
                            EndFor.
                        EndBody.
                """
        expect = Program([FuncDecl(Id("do_it"),[],tuple([[VarDecl(Id("okConDe"),[],StringLiteral("\\\\cvasvevsi")),VarDecl(Id("vaf"),[],None),VarDecl(Id("vas"),[],None),VarDecl(Id("var"),[],None),VarDecl(Id("vax"),[],None),VarDecl(Id("vaj"),[],FloatLiteral(0.0))],[For(Id("r"),IntLiteral(0),BinaryOp("<=",Id("r"),IntLiteral(123)),BinaryOp("+",Id("r"),IntLiteral(1)),tuple([[],[CallStmt(Id("cong_cho_vui_vay_thoi"),[]),CallStmt(Id("do_it_right_now"),[Id("a"),Id("as"),Id("aa"),ArrayLiteral([]),Id("cowf"),Id("dowfl")]),Return(IntLiteral(0))]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_72(self):
        input = """
                    Function: do_it
                        Body:
                            Var: okConDe = "\\\\cvasvevsi";
                            Var: vaf, vas, var, vax, vaj = 0e5;
                            While a Do EndWhile.
                            Do v = 0 + 0;
                         While False EndDo.
                        EndBody.
                """
        expect = Program([FuncDecl(Id("do_it"),[],tuple([[VarDecl(Id("okConDe"),[],StringLiteral("\\\\cvasvevsi")),VarDecl(Id("vaf"),[],None),VarDecl(Id("vas"),[],None),VarDecl(Id("var"),[],None),VarDecl(Id("vax"),[],None),VarDecl(Id("vaj"),[],FloatLiteral(0.0))],[While(Id("a"),tuple([[],[]])),Dowhile(tuple([[],[Assign(Id("v"),BinaryOp("+",IntLiteral(0),IntLiteral(0)))]]),BooleanLiteral(False))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test_73(self):
        input = """
                    Var: x, a[12];
                    Function: do_it
                        Body:
                            Var: okConDe = "\\\\cvasvevsi";
                            Var: vaf, vas, var, vax, vaj = 0e5,
                                **
                                cwerjfoiwej34fjoivw[ot-0w 3i 5tt23 oir-03qr
                                23'r
                                324't
                                2t'
                                2t
                                2

                                t5
                                **a[5]=10;
                            cal_me_baby(1,2,3,3e4, goo());
                            Return bay_yeu_dau(1298);
                        EndBody.
                """
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("a"),[12],None),FuncDecl(Id("do_it"),[],tuple([[VarDecl(Id("okConDe"),[],StringLiteral("\\\\cvasvevsi")),VarDecl(Id("vaf"),[],None),VarDecl(Id("vas"),[],None),VarDecl(Id("var"),[],None),VarDecl(Id("vax"),[],None),VarDecl(Id("vaj"),[],FloatLiteral(0.0)),VarDecl(Id("a"),[5],IntLiteral(10))],[CallStmt(Id("cal_me_baby"),[IntLiteral(1),IntLiteral(2),IntLiteral(3),FloatLiteral(30000.0),CallExpr(Id("goo"),[])]),Return(CallExpr(Id("bay_yeu_dau"),[IntLiteral(1298)]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_74(self):
        input = """
                    Function: chang_can
                    Parameter: mot, ai, nua
                    Body:
                        bat_ke(ai, cung, du, thua, -89898);
                        For (mot_minh = 1, ngoi_khox, duoi_mua) Do
                            nen_con_dau(tung, hoi, tho);
                            While chang_ngung_nho(mot_nguoi) Do
                                act = quay_buoc() + gia_vo();
                                EndWhile.
                            talk(cung, nhu, em);
                            Return het_thuong(can, nho);
                        EndFor.
                    EndBody.
                """
        expect = Program([FuncDecl(Id("chang_can"),[VarDecl(Id("mot"),[],None),VarDecl(Id("ai"),[],None),VarDecl(Id("nua"),[],None)],tuple([[],[CallStmt(Id("bat_ke"),[Id("ai"),Id("cung"),Id("du"),Id("thua"),UnaryOp("-",IntLiteral(89898))]),For(Id("mot_minh"),IntLiteral(1),Id("ngoi_khox"),Id("duoi_mua"),tuple([[],[CallStmt(Id("nen_con_dau"),[Id("tung"),Id("hoi"),Id("tho")]),While(CallExpr(Id("chang_ngung_nho"),[Id("mot_nguoi")]),tuple([[],[Assign(Id("act"),BinaryOp("+",CallExpr(Id("quay_buoc"),[]),CallExpr(Id("gia_vo"),[])))]])),CallStmt(Id("talk"),[Id("cung"),Id("nhu"),Id("em")]),Return(CallExpr(Id("het_thuong"),[Id("can"),Id("nho")]))]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test_75(self):
        input = """
                    Function: chang_can
                    Parameter: mot, ai, nua[999]
                    Body:
                        bat_ke(ai, cung, du, thua, -89898);
                        For (mot_minh = 1, ngoi_khox, duoi_mua) Do
                            Var: nen, con_dau = 10;
                            Var: hoi, tho = 99.e3;
                            While chang_ngung_nho(mot_nguoi) Do
                                Var: yeu_hay, khong_yeu[0] = {"Noi", {"mot", "loi"}};
                                act = quay_buoc() + gia_vo();
                                Break;
                                EndWhile.
                            talk(cung, nhu, em);
                            Return het_thuong(can, nho);
                        EndFor.
                    EndBody.
                """
        expect = Program([FuncDecl(Id("chang_can"),[VarDecl(Id("mot"),[],None),VarDecl(Id("ai"),[],None),VarDecl(Id("nua"),[999],None)],tuple([[],[CallStmt(Id("bat_ke"),[Id("ai"),Id("cung"),Id("du"),Id("thua"),UnaryOp("-",IntLiteral(89898))]),For(Id("mot_minh"),IntLiteral(1),Id("ngoi_khox"),Id("duoi_mua"),tuple([[VarDecl(Id("nen"),[],None),VarDecl(Id("con_dau"),[],IntLiteral(10)),VarDecl(Id("hoi"),[],None),VarDecl(Id("tho"),[],FloatLiteral(99000.0))],[While(CallExpr(Id("chang_ngung_nho"),[Id("mot_nguoi")]),tuple([[VarDecl(Id("yeu_hay"),[],None),VarDecl(Id("khong_yeu"),[0],ArrayLiteral([StringLiteral("Noi"),ArrayLiteral([StringLiteral("mot"),StringLiteral("loi")])]))],[Assign(Id("act"),BinaryOp("+",CallExpr(Id("quay_buoc"),[]),CallExpr(Id("gia_vo"),[]))),Break()]])),CallStmt(Id("talk"),[Id("cung"),Id("nhu"),Id("em")]),Return(CallExpr(Id("het_thuong"),[Id("can"),Id("nho")]))]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,375))

    def test_76(self):
        input = """
                    Function: chang_can
                    Parameter: mot, ai, nua[999]
                    Body:
                        bat_ke(ai, cung, du, thua, -89898);
                        Do
                            Var: nen, con_dau = 10;
                            Var: hoi, tho = 99.e3;
                            While chang_ngung_nho(mot_nguoi) Do
                                Var: yeu_hay, khong_yeu[0] = {"Noi", {"mot", "loi"}};
                                act = quay_buoc() + gia_vo();
                                Break;
                                EndWhile.
                            talk(cung, nhu, em);
                            Return het_thuong(can, nho);
                        While su_that == chi || mot && nguoi EndDo.
                        het_thuong(can + nho);
                    EndBody.
                """
        expect = Program([FuncDecl(Id("chang_can"),[VarDecl(Id("mot"),[],None),VarDecl(Id("ai"),[],None),VarDecl(Id("nua"),[999],None)],tuple([[],[CallStmt(Id("bat_ke"),[Id("ai"),Id("cung"),Id("du"),Id("thua"),UnaryOp("-",IntLiteral(89898))]),Dowhile(tuple([[VarDecl(Id("nen"),[],None),VarDecl(Id("con_dau"),[],IntLiteral(10)),VarDecl(Id("hoi"),[],None),VarDecl(Id("tho"),[],FloatLiteral(99000.0))],[While(CallExpr(Id("chang_ngung_nho"),[Id("mot_nguoi")]),tuple([[VarDecl(Id("yeu_hay"),[],None),VarDecl(Id("khong_yeu"),[0],ArrayLiteral([StringLiteral("Noi"),ArrayLiteral([StringLiteral("mot"),StringLiteral("loi")])]))],[Assign(Id("act"),BinaryOp("+",CallExpr(Id("quay_buoc"),[]),CallExpr(Id("gia_vo"),[]))),Break()]])),CallStmt(Id("talk"),[Id("cung"),Id("nhu"),Id("em")]),Return(CallExpr(Id("het_thuong"),[Id("can"),Id("nho")]))]]),BinaryOp("==",Id("su_that"),BinaryOp("&&",BinaryOp("||",Id("chi"),Id("mot")),Id("nguoi")))),CallStmt(Id("het_thuong"),[BinaryOp("+",Id("can"),Id("nho"))])]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test_77(self):
        input = """
                    Var: duc, phuc = 10;

                    Function: chang_can
                    Parameter: mot, ai, nua[999]
                    Body:
                        Do
                            Var: nen, con_dau = 10;
                            Var: hoi, tho = 99.e3;
                            While chang_ngung_nho(mot_nguoi) Do
                                Var: yeu_hay, khong_yeu[0] = {"Noi", {"mot", "loi"}};
                                act = quay_buoc() + gia_vo();
                                Break;
                            EndWhile.
                            talk(cung, nhu, em);
                            Return het_thuong(can, nho);
                        While (su_that == chi || mot && nguoi) EndDo.
                        het_thuong(can + nho);
                    EndBody.
                        Function: chang_can
                        Body:
                                Var: nen, con_dau = 10;
                                While su_that == chi || mot && nguoi Do
                                    chia_tay(toi, khong, con, yeu, em, nua);
                                EndWhile.
                                For (dung=0, noi, chia_tay) Do
                                    cho(tam, hon + dau - kho);
                                    Continue;
                                EndFor.
                            het_thuong(can + nho);
                        EndBody.
                """
        expect = Program([VarDecl(Id("duc"),[],None),VarDecl(Id("phuc"),[],IntLiteral(10)),FuncDecl(Id("chang_can"),[VarDecl(Id("mot"),[],None),VarDecl(Id("ai"),[],None),VarDecl(Id("nua"),[999],None)],tuple([[],[Dowhile(tuple([[VarDecl(Id("nen"),[],None),VarDecl(Id("con_dau"),[],IntLiteral(10)),VarDecl(Id("hoi"),[],None),VarDecl(Id("tho"),[],FloatLiteral(99000.0))],[While(CallExpr(Id("chang_ngung_nho"),[Id("mot_nguoi")]),tuple([[VarDecl(Id("yeu_hay"),[],None),VarDecl(Id("khong_yeu"),[0],ArrayLiteral([StringLiteral("Noi"),ArrayLiteral([StringLiteral("mot"),StringLiteral("loi")])]))],[Assign(Id("act"),BinaryOp("+",CallExpr(Id("quay_buoc"),[]),CallExpr(Id("gia_vo"),[]))),Break()]])),CallStmt(Id("talk"),[Id("cung"),Id("nhu"),Id("em")]),Return(CallExpr(Id("het_thuong"),[Id("can"),Id("nho")]))]]),BinaryOp("==",Id("su_that"),BinaryOp("&&",BinaryOp("||",Id("chi"),Id("mot")),Id("nguoi")))),CallStmt(Id("het_thuong"),[BinaryOp("+",Id("can"),Id("nho"))])]])),FuncDecl(Id("chang_can"),[],tuple([[VarDecl(Id("nen"),[],None),VarDecl(Id("con_dau"),[],IntLiteral(10))],[While(BinaryOp("==",Id("su_that"),BinaryOp("&&",BinaryOp("||",Id("chi"),Id("mot")),Id("nguoi"))),tuple([[],[CallStmt(Id("chia_tay"),[Id("toi"),Id("khong"),Id("con"),Id("yeu"),Id("em"),Id("nua")])]])),For(Id("dung"),IntLiteral(0),Id("noi"),Id("chia_tay"),tuple([[],[CallStmt(Id("cho"),[Id("tam"),BinaryOp("-",BinaryOp("+",Id("hon"),Id("dau")),Id("kho"))]),Continue()]])),CallStmt(Id("het_thuong"),[BinaryOp("+",Id("can"),Id("nho"))])]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,377))

    def test_78(self):
        input = """
                    Var: duc, nguyen;
                    Var: quang = 2412;

                    Function: chang_can
                    Parameter: mot, ai, nua[999]
                    Body:
                        Do
                            Var: nen, con_dau = 10;
                            Return het_thuong(can, nho);
                        While su_that == chi || mot && nguoi EndDo.
                        het_thuong(can + nho);
                    EndBody.
                        Function: chang_can
                        Body:
                                Var: nen, con_dau = 10;
                                While su_that == chi || mot && nguoi Do
                                    Var: tran_thi_tuyet_hanh;
                                    Return;
                                EndWhile.
                                ngay_mai = se + khac % se == lai \\ (thay * hang && cay);
                                rat = xanh *. 0;
                                For (dung=0, noi, chia_tay) Do
                                    Continue;
                                EndFor.
                            het_thuong(can + nho);
                        EndBody.
                """
        expect = Program([VarDecl(Id("duc"),[],None),VarDecl(Id("nguyen"),[],None),VarDecl(Id("quang"),[],IntLiteral(2412)),FuncDecl(Id("chang_can"),[VarDecl(Id("mot"),[],None),VarDecl(Id("ai"),[],None),VarDecl(Id("nua"),[999],None)],tuple([[],[Dowhile(tuple([[VarDecl(Id("nen"),[],None),VarDecl(Id("con_dau"),[],IntLiteral(10))],[Return(CallExpr(Id("het_thuong"),[Id("can"),Id("nho")]))]]),BinaryOp("==",Id("su_that"),BinaryOp("&&",BinaryOp("||",Id("chi"),Id("mot")),Id("nguoi")))),CallStmt(Id("het_thuong"),[BinaryOp("+",Id("can"),Id("nho"))])]])),FuncDecl(Id("chang_can"),[],tuple([[VarDecl(Id("nen"),[],None),VarDecl(Id("con_dau"),[],IntLiteral(10))],[While(BinaryOp("==",Id("su_that"),BinaryOp("&&",BinaryOp("||",Id("chi"),Id("mot")),Id("nguoi"))),tuple([[VarDecl(Id("tran_thi_tuyet_hanh"),[],None)],[Return(None)]])),Assign(Id("ngay_mai"),BinaryOp("==",BinaryOp("+",Id("se"),BinaryOp("%",Id("khac"),Id("se"))),BinaryOp("\\",Id("lai"),BinaryOp("&&",BinaryOp("*",Id("thay"),Id("hang")),Id("cay"))))),Assign(Id("rat"),BinaryOp("*.",Id("xanh"),IntLiteral(0))),For(Id("dung"),IntLiteral(0),Id("noi"),Id("chia_tay"),tuple([[],[Continue()]])),CallStmt(Id("het_thuong"),[BinaryOp("+",Id("can"),Id("nho"))])]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,378))

    def test_79(self):
        input = """
                        Var: duc, nguyen;
                        Var: quang = 2412;

                        Function: chang_can
                        Body:
                        EndBody.
                        Function: chang_can
                        Parameter: a[0]
                        Body:
                        ngay_mai = se_khac()[se_lai - thay[99] || hang  >=. !cay][rat == xanh];
                            Do**
                                Var: nen, con_dau = 10;
                                While su_that == chi || mot && nguoi Do
                                    Var: tran_thi_tuyet_hanh;
                                    Return;
                                EndWhile.
                                ngay_mai = se + khac % se == lai / (thay * hang && cay);
                                rat = xanh *. 0;
                                For (dung=0, noi, chia_tay) Do
                                    Continue;
                                EndFor.
                            het_thuong(can + nho);**
                            While 0 EndDo.
                        EndBody.
                """
        expect = Program([VarDecl(Id("duc"),[],None),VarDecl(Id("nguyen"),[],None),VarDecl(Id("quang"),[],IntLiteral(2412)),FuncDecl(Id("chang_can"),[],tuple([[],[]])),FuncDecl(Id("chang_can"),[VarDecl(Id("a"),[0],None)],tuple([[],[Assign(Id("ngay_mai"),ArrayCell(CallExpr(Id("se_khac"),[]),[BinaryOp(">=.",BinaryOp("||",BinaryOp("-",Id("se_lai"),ArrayCell(Id("thay"),[IntLiteral(99)])),Id("hang")),UnaryOp("!",Id("cay"))),BinaryOp("==",Id("rat"),Id("xanh"))])),Dowhile(tuple([[],[]]),IntLiteral(0))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test_80(self):
        input = """
                    Var: loi_noi;
                    Var: chia, tay, sao[0], that[324]={}, kho = "cwijv";
                    Function: vi_con_yeu
                    Parameter: gio, heo, may[13]
                    Body:
                        em_bat_khox = dung_lo(nguoi + xxx);
                        For (phai_chang=la_vi()[12], dieu, do) Do
                            Var: la, vi, yeu[3000];
                            Return nguoi_ta(chang, de, quen);
                            Do aaa = (nhin + thay == nhau);
                            noi_dau(-.thau);
                            thau = thau + cang * sau;
                            While het_yeu[0] EndDo.
                        EndFor.
                        phep_mau(True);
                    EndBody.
                """
        expect = Program([VarDecl(Id("loi_noi"),[],None),VarDecl(Id("chia"),[],None),VarDecl(Id("tay"),[],None),VarDecl(Id("sao"),[0],None),VarDecl(Id("that"),[324],ArrayLiteral([])),VarDecl(Id("kho"),[],StringLiteral("cwijv")),FuncDecl(Id("vi_con_yeu"),[VarDecl(Id("gio"),[],None),VarDecl(Id("heo"),[],None),VarDecl(Id("may"),[13],None)],tuple([[],[Assign(Id("em_bat_khox"),CallExpr(Id("dung_lo"),[BinaryOp("+",Id("nguoi"),Id("xxx"))])),For(Id("phai_chang"),ArrayCell(CallExpr(Id("la_vi"),[]),[IntLiteral(12)]),Id("dieu"),Id("do"),tuple([[VarDecl(Id("la"),[],None),VarDecl(Id("vi"),[],None),VarDecl(Id("yeu"),[3000],None)],[Return(CallExpr(Id("nguoi_ta"),[Id("chang"),Id("de"),Id("quen")])),Dowhile(tuple([[],[Assign(Id("aaa"),BinaryOp("==",BinaryOp("+",Id("nhin"),Id("thay")),Id("nhau"))),CallStmt(Id("noi_dau"),[UnaryOp("-.",Id("thau"))]),Assign(Id("thau"),BinaryOp("+",Id("thau"),BinaryOp("*",Id("cang"),Id("sau"))))]]),ArrayCell(Id("het_yeu"),[IntLiteral(0)]))]])),CallStmt(Id("phep_mau"),[BooleanLiteral(True)])]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,380))

    def test_81(self):
        input = """
                    Var: loi_noi;
                    Var: chia,  kho = "cwijv";
                    Function: vi_con_yeu
                    Parameter: gio, heo[46][84][32316], may[13]
                    Body:
                        em_bat_khox = dung_lo(nguoi + xxx);
                        For (phai_chang=la_vi()[12], dieu, do) Do
                            Do Var: tai, sao;
                            ngu_ngox = qua*qua;
                            aaa = (nhin + thay == nhau);
                            thau = thau + cang * sau;
                            While het_yeu[0] EndDo.
                        EndFor.
                        phep_mau(True);
                        Return dua_ta_ve() + thang_nam(bat && dau * yeu);
                    EndBody.
                """
        expect = Program([VarDecl(Id("loi_noi"),[],None),VarDecl(Id("chia"),[],None),VarDecl(Id("kho"),[],StringLiteral("cwijv")),FuncDecl(Id("vi_con_yeu"),[VarDecl(Id("gio"),[],None),VarDecl(Id("heo"),[46,84,32316],None),VarDecl(Id("may"),[13],None)],tuple([[],[Assign(Id("em_bat_khox"),CallExpr(Id("dung_lo"),[BinaryOp("+",Id("nguoi"),Id("xxx"))])),For(Id("phai_chang"),ArrayCell(CallExpr(Id("la_vi"),[]),[IntLiteral(12)]),Id("dieu"),Id("do"),tuple([[],[Dowhile(tuple([[VarDecl(Id("tai"),[],None),VarDecl(Id("sao"),[],None)],[Assign(Id("ngu_ngox"),BinaryOp("*",Id("qua"),Id("qua"))),Assign(Id("aaa"),BinaryOp("==",BinaryOp("+",Id("nhin"),Id("thay")),Id("nhau"))),Assign(Id("thau"),BinaryOp("+",Id("thau"),BinaryOp("*",Id("cang"),Id("sau"))))]]),ArrayCell(Id("het_yeu"),[IntLiteral(0)]))]])),CallStmt(Id("phep_mau"),[BooleanLiteral(True)]),Return(BinaryOp("+",CallExpr(Id("dua_ta_ve"),[]),CallExpr(Id("thang_nam"),[BinaryOp("&&",Id("bat"),BinaryOp("*",Id("dau"),Id("yeu")))])))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,381))

    def test_82(self):
        input = """
                    Var: loi_noi;
                    Var: chia,  kho = "cwijv";
                    Function: vi_con_yeu
                    Parameter: gio, heo[46][84][32316], may[13]
                    Body:
                        em_bat_khox = dung_lo(nguoi + xxx);
                        For (phai_chang=la_vi()[12], dieu, do) Do
                        EndFor.
                        phep_mau(True);
                        Return dua_ta_ve() + thang_nam(bat && dau * yeu);
                        Break;
                    EndBody.
                    Function: bo_lai
                    Parameter: manh, ghep[56]
                    Body:
                        Var: tat =0, ca=1;
                        vun_vo=minh()[foo()];
                        Continue;
                        Return thuc || tai;
                    EndBody.
                """
        expect = Program([VarDecl(Id("loi_noi"),[],None),VarDecl(Id("chia"),[],None),VarDecl(Id("kho"),[],StringLiteral("cwijv")),FuncDecl(Id("vi_con_yeu"),[VarDecl(Id("gio"),[],None),VarDecl(Id("heo"),[46,84,32316],None),VarDecl(Id("may"),[13],None)],tuple([[],[Assign(Id("em_bat_khox"),CallExpr(Id("dung_lo"),[BinaryOp("+",Id("nguoi"),Id("xxx"))])),For(Id("phai_chang"),ArrayCell(CallExpr(Id("la_vi"),[]),[IntLiteral(12)]),Id("dieu"),Id("do"),tuple([[],[]])),CallStmt(Id("phep_mau"),[BooleanLiteral(True)]),Return(BinaryOp("+",CallExpr(Id("dua_ta_ve"),[]),CallExpr(Id("thang_nam"),[BinaryOp("&&",Id("bat"),BinaryOp("*",Id("dau"),Id("yeu")))]))),Break()]])),FuncDecl(Id("bo_lai"),[VarDecl(Id("manh"),[],None),VarDecl(Id("ghep"),[56],None)],tuple([[VarDecl(Id("tat"),[],IntLiteral(0)),VarDecl(Id("ca"),[],IntLiteral(1))],[Assign(Id("vun_vo"),ArrayCell(CallExpr(Id("minh"),[]),[CallExpr(Id("foo"),[])])),Continue(),Return(BinaryOp("||",Id("thuc"),Id("tai")))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test_83(self):
        input = """
                    Var: mau_trang;
                    Var: tran, le, quynh;
                    Function: cha
                    Body:EndBody.
                    Function: me
                    Body:EndBody.

                    Function: tinh_yeu
                    Parameter: chuyen, co[10][10], tich[100]
                    Body:
                        cha = cha();
                        me = me();
                        xem(cha, lau_lam);
                        gap(me, ban_cu);
                        o_cua(trang || den);
                        Return co_be(giau, giot, le);
                    EndBody.
                """
        expect = Program([VarDecl(Id("mau_trang"),[],None),VarDecl(Id("tran"),[],None),VarDecl(Id("le"),[],None),VarDecl(Id("quynh"),[],None),FuncDecl(Id("cha"),[],tuple([[],[]])),FuncDecl(Id("me"),[],tuple([[],[]])),FuncDecl(Id("tinh_yeu"),[VarDecl(Id("chuyen"),[],None),VarDecl(Id("co"),[10,10],None),VarDecl(Id("tich"),[100],None)],tuple([[],[Assign(Id("cha"),CallExpr(Id("cha"),[])),Assign(Id("me"),CallExpr(Id("me"),[])),CallStmt(Id("xem"),[Id("cha"),Id("lau_lam")]),CallStmt(Id("gap"),[Id("me"),Id("ban_cu")]),CallStmt(Id("o_cua"),[BinaryOp("||",Id("trang"),Id("den"))]),Return(CallExpr(Id("co_be"),[Id("giau"),Id("giot"),Id("le")]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,383))

    def test_84(self):
        input = """
                    Var: mau_trang;
                    Var: tran, le, quynh;

                    Function: tinh_yeu
                    Parameter: chuyen, co[10][10], tich[100]
                    Body:
                        cha = cha();
                        me = me();
                        xem(cha, lau_lam);
                        gap(me, ban_cu);
                        o_cua(trang || den);
                        Return co_be(giau, giot, le);
                        While nhung + vi || sao Do
                        Var: ngoi_sao;
                        roi = ngoai == (song) + {{"mot"}, "dem", {"lap", "lanh"}};
                        anh_tran();EndWhile.
                    EndBody.
                """
        expect = Program([VarDecl(Id("mau_trang"),[],None),VarDecl(Id("tran"),[],None),VarDecl(Id("le"),[],None),VarDecl(Id("quynh"),[],None),FuncDecl(Id("tinh_yeu"),[VarDecl(Id("chuyen"),[],None),VarDecl(Id("co"),[10,10],None),VarDecl(Id("tich"),[100],None)],tuple([[],[Assign(Id("cha"),CallExpr(Id("cha"),[])),Assign(Id("me"),CallExpr(Id("me"),[])),CallStmt(Id("xem"),[Id("cha"),Id("lau_lam")]),CallStmt(Id("gap"),[Id("me"),Id("ban_cu")]),CallStmt(Id("o_cua"),[BinaryOp("||",Id("trang"),Id("den"))]),Return(CallExpr(Id("co_be"),[Id("giau"),Id("giot"),Id("le")])),While(BinaryOp("||",BinaryOp("+",Id("nhung"),Id("vi")),Id("sao")),tuple([[VarDecl(Id("ngoi_sao"),[],None)],[Assign(Id("roi"),BinaryOp("==",Id("ngoai"),BinaryOp("+",Id("song"),ArrayLiteral([ArrayLiteral([StringLiteral("mot")]),StringLiteral("dem"),ArrayLiteral([StringLiteral("lap"),StringLiteral("lanh")])])))),CallStmt(Id("anh_tran"),[])]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test_85(self):
        input = """
                    Var: mau_trang;
                    Var: tran, le, quynh;

                    Function: tinh_yeu
                    Parameter: chuyen, co[10][10], tich[100]
                    Body:

                        Return co_be(giau, giot, le);
                        While nhung + vi || sao Do
                        Var: ngoi_sao;
                        roi = ngoai == (song) + {{"mot"}, "dem", {"lap", "lanh"}};
                        anh_tran();EndWhile.
                    EndBody.
                    Function: loi_ho_hung
                    Parameter: dang, sau
                    Body:
                        tinh_yeu();
                        For (thang=0,nam,qua_Di) Do
                        nu_cuoi(hanh * phuc);
                        tieng_khox = khong_gnuooi[as[ wef]] - a();
                        EndFor.
                    EndBody.
                """
        expect = Program([VarDecl(Id("mau_trang"),[],None),VarDecl(Id("tran"),[],None),VarDecl(Id("le"),[],None),VarDecl(Id("quynh"),[],None),FuncDecl(Id("tinh_yeu"),[VarDecl(Id("chuyen"),[],None),VarDecl(Id("co"),[10,10],None),VarDecl(Id("tich"),[100],None)],tuple([[],[Return(CallExpr(Id("co_be"),[Id("giau"),Id("giot"),Id("le")])),While(BinaryOp("||",BinaryOp("+",Id("nhung"),Id("vi")),Id("sao")),tuple([[VarDecl(Id("ngoi_sao"),[],None)],[Assign(Id("roi"),BinaryOp("==",Id("ngoai"),BinaryOp("+",Id("song"),ArrayLiteral([ArrayLiteral([StringLiteral("mot")]),StringLiteral("dem"),ArrayLiteral([StringLiteral("lap"),StringLiteral("lanh")])])))),CallStmt(Id("anh_tran"),[])]]))]])),FuncDecl(Id("loi_ho_hung"),[VarDecl(Id("dang"),[],None),VarDecl(Id("sau"),[],None)],tuple([[],[CallStmt(Id("tinh_yeu"),[]),For(Id("thang"),IntLiteral(0),Id("nam"),Id("qua_Di"),tuple([[],[CallStmt(Id("nu_cuoi"),[BinaryOp("*",Id("hanh"),Id("phuc"))]),Assign(Id("tieng_khox"),BinaryOp("-",ArrayCell(Id("khong_gnuooi"),[ArrayCell(Id("as"),[Id("wef")])]),CallExpr(Id("a"),[])))]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,385))

    def test_86(self):
        input = """
                    Var: mau_trang;
                    Var: tran, le, quynh;

                    Function: tinh_yeu
                    Parameter: chuyen, co[10][10], tich[100]
                    Body:

                        Return co_be(giau, giot, le);
                        While nhung + vi || sao Do
                        Var: ngoi_sao;
                        anh_tran();EndWhile.
                        For (thang=0,nam,qua_Di) Do
                        nu_cuoi(hanh * phuc);
                        tieng_khox = khong_gnuooi[as[ wef]] - a();
                        If (ngoi - nha + vang) Then
                        do_dem_trang = noi_buon()[dem[mua[dong]]];
                        ElseIf mau && hoa Then
                        While !xuan_sang Do thuc(day); EndWhile.
                        EndIf.
                        EndFor.
                    EndBody.
                """
        expect = Program([VarDecl(Id("mau_trang"),[],None),VarDecl(Id("tran"),[],None),VarDecl(Id("le"),[],None),VarDecl(Id("quynh"),[],None),FuncDecl(Id("tinh_yeu"),[VarDecl(Id("chuyen"),[],None),VarDecl(Id("co"),[10,10],None),VarDecl(Id("tich"),[100],None)],tuple([[],[Return(CallExpr(Id("co_be"),[Id("giau"),Id("giot"),Id("le")])),While(BinaryOp("||",BinaryOp("+",Id("nhung"),Id("vi")),Id("sao")),tuple([[VarDecl(Id("ngoi_sao"),[],None)],[CallStmt(Id("anh_tran"),[])]])),For(Id("thang"),IntLiteral(0),Id("nam"),Id("qua_Di"),tuple([[],[CallStmt(Id("nu_cuoi"),[BinaryOp("*",Id("hanh"),Id("phuc"))]),Assign(Id("tieng_khox"),BinaryOp("-",ArrayCell(Id("khong_gnuooi"),[ArrayCell(Id("as"),[Id("wef")])]),CallExpr(Id("a"),[]))),If([tuple([BinaryOp("+",BinaryOp("-",Id("ngoi"),Id("nha")),Id("vang")),[],[Assign(Id("do_dem_trang"),ArrayCell(CallExpr(Id("noi_buon"),[]),[ArrayCell(Id("dem"),[ArrayCell(Id("mua"),[Id("dong")])])]))]]),tuple([BinaryOp("&&",Id("mau"),Id("hoa")),[],[While(UnaryOp("!",Id("xuan_sang")),tuple([[],[CallStmt(Id("thuc"),[Id("day")])]]))]])],tuple([[],[]]))]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_87(self):
        input = """
                Function: tinh_yeu
                Parameter: chuyen, co[10][10], tich[100]
                Body:

                    For (thang=0,nam,qua_Di) Do
                    nu_cuoi(hanh * phuc);
                    If (ngoi - nha + vang) Then
                    do_dem_trang = noi_buon()[dem[mua[dong]]];
                    ElseIf mau && hoa Then Else If (giac - ngu) Then
                    While !xuan_sang Do thuc(day); EndWhile.
                    EndIf.
                    den();
                    EndIf.
                    EndFor.
                    If a Then
                    While st Do If x Then EndIf.EndWhile.
                    con_en(bay);
                    Return suong()[mo];
                    EndIf.
                EndBody.
                """
        expect = Program([FuncDecl(Id("tinh_yeu"),[VarDecl(Id("chuyen"),[],None),VarDecl(Id("co"),[10,10],None),VarDecl(Id("tich"),[100],None)],tuple([[],[For(Id("thang"),IntLiteral(0),Id("nam"),Id("qua_Di"),tuple([[],[CallStmt(Id("nu_cuoi"),[BinaryOp("*",Id("hanh"),Id("phuc"))]),If([tuple([BinaryOp("+",BinaryOp("-",Id("ngoi"),Id("nha")),Id("vang")),[],[Assign(Id("do_dem_trang"),ArrayCell(CallExpr(Id("noi_buon"),[]),[ArrayCell(Id("dem"),[ArrayCell(Id("mua"),[Id("dong")])])]))]]),tuple([BinaryOp("&&",Id("mau"),Id("hoa")),[],[]])],tuple([[],[If([tuple([BinaryOp("-",Id("giac"),Id("ngu")),[],[While(UnaryOp("!",Id("xuan_sang")),tuple([[],[CallStmt(Id("thuc"),[Id("day")])]]))]])],tuple([[],[]])),CallStmt(Id("den"),[])]]))]])),If([tuple([Id("a"),[],[While(Id("st"),tuple([[],[If([tuple([Id("x"),[],[]])],tuple([[],[]]))]])),CallStmt(Id("con_en"),[Id("bay")]),Return(ArrayCell(CallExpr(Id("suong"),[]),[Id("mo")]))]])],tuple([[],[]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_88(self):
        input = """
                    Function: tinh_yeu
                    Parameter: chuyen, co[10][10], tich[100]
                    Body:

                        a="**vvok **" ** ajw
                        swg
                        se
                        ges
                        g
                        es g
                        est
                        hrd
                        jidtriurs e563w4667
                        66
                        34
                         5yui 5
                         **
                         ;While abcd Do If oop_qua(chan) Then EndIf.EndWhile.
                         bang_qua = dai + duong;
                         bay(den(nhuwng(thien(ha(xa(lam()[0]))))));
                    EndBody.
                """
        expect = Program([FuncDecl(Id("tinh_yeu"),[VarDecl(Id("chuyen"),[],None),VarDecl(Id("co"),[10,10],None),VarDecl(Id("tich"),[100],None)],tuple([[],[Assign(Id("a"),StringLiteral("**vvok **")),While(Id("abcd"),tuple([[],[If([tuple([CallExpr(Id("oop_qua"),[Id("chan")]),[],[]])],tuple([[],[]]))]])),Assign(Id("bang_qua"),BinaryOp("+",Id("dai"),Id("duong"))),CallStmt(Id("bay"),[CallExpr(Id("den"),[CallExpr(Id("nhuwng"),[CallExpr(Id("thien"),[CallExpr(Id("ha"),[CallExpr(Id("xa"),[ArrayCell(CallExpr(Id("lam"),[]),[IntLiteral(0)])])])])])])])]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_89(self):
        input = """
                    Function: tinh_yeu
                    Parameter: chuyen, co[10][10], tich[100]
                    Body:
                        Var: mau_trang;
                         While abcd Do If oop_qua(chan) ThenEndIf. EndWhile.
                         bang_qua = dai + duong;
                         bay(den(nhuwng(thien(ha(xa(lam()[0]))))));
                    EndBody.
                    Function: giac_mo
                    Parameter: diu, dang[267789]
                    Body:
                        Var: tim, o, lai;
                        mai(nha + den(chim[en(xxx)]));
                        cung = mua(xuan[{1,2,3}]);
                    EndBody.
                """
        expect = Program([FuncDecl(Id("tinh_yeu"),[VarDecl(Id("chuyen"),[],None),VarDecl(Id("co"),[10,10],None),VarDecl(Id("tich"),[100],None)],tuple([[VarDecl(Id("mau_trang"),[],None)],[While(Id("abcd"),tuple([[],[If([tuple([CallExpr(Id("oop_qua"),[Id("chan")]),[],[]])],tuple([[],[]]))]])),Assign(Id("bang_qua"),BinaryOp("+",Id("dai"),Id("duong"))),CallStmt(Id("bay"),[CallExpr(Id("den"),[CallExpr(Id("nhuwng"),[CallExpr(Id("thien"),[CallExpr(Id("ha"),[CallExpr(Id("xa"),[ArrayCell(CallExpr(Id("lam"),[]),[IntLiteral(0)])])])])])])])]])),FuncDecl(Id("giac_mo"),[VarDecl(Id("diu"),[],None),VarDecl(Id("dang"),[267789],None)],tuple([[VarDecl(Id("tim"),[],None),VarDecl(Id("o"),[],None),VarDecl(Id("lai"),[],None)],[CallStmt(Id("mai"),[BinaryOp("+",Id("nha"),CallExpr(Id("den"),[ArrayCell(Id("chim"),[CallExpr(Id("en"),[Id("xxx")])])]))]),Assign(Id("cung"),CallExpr(Id("mua"),[ArrayCell(Id("xuan"),[ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])])]))]]))])
        
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_90(self):
        input = """
                    Var: cuoc_song, dieu_gi[0] = {1,2,3};
                    Var: tinh_yeu;
                    Function: den_roi_di
                    Parameter: ban_tay, nhau
                    Body:
                        nam(ban_tay, lac(nhau));
                        For (ngay_nang=1e7, ngay_nang-nhat_nhoa, -.ngay_nang) Do
                            Var: doi_chan;
                            do_chan = buoc_di[0];
                            quay_lung(minh);
                            Break;
                        EndFor.
                        Do mot_lan(); While !True EndDo.
                    EndBody.
                    Function: ngay_do
                    Parameter: abcd
                    Body:
                        While ngaydo(haita(chang(thay[nhau]))) Do
                        anh(song[ra[sao]]);
                        yeu_nguoi = the_nao[xxx];
                        EndWhile.
                    EndBody.

                """
        expect = Program([VarDecl(Id("cuoc_song"),[],None),VarDecl(Id("dieu_gi"),[0],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),VarDecl(Id("tinh_yeu"),[],None),FuncDecl(Id("den_roi_di"),[VarDecl(Id("ban_tay"),[],None),VarDecl(Id("nhau"),[],None)],tuple([[],[CallStmt(Id("nam"),[Id("ban_tay"),CallExpr(Id("lac"),[Id("nhau")])]),For(Id("ngay_nang"),FloatLiteral(10000000.0),BinaryOp("-",Id("ngay_nang"),Id("nhat_nhoa")),UnaryOp("-.",Id("ngay_nang")),tuple([[VarDecl(Id("doi_chan"),[],None)],[Assign(Id("do_chan"),ArrayCell(Id("buoc_di"),[IntLiteral(0)])),CallStmt(Id("quay_lung"),[Id("minh")]),Break()]])),Dowhile(tuple([[],[CallStmt(Id("mot_lan"),[])]]),UnaryOp("!",BooleanLiteral(True)))]])),FuncDecl(Id("ngay_do"),[VarDecl(Id("abcd"),[],None)],tuple([[],[While(CallExpr(Id("ngaydo"),[CallExpr(Id("haita"),[CallExpr(Id("chang"),[ArrayCell(Id("thay"),[Id("nhau")])])])]),tuple([[],[CallStmt(Id("anh"),[ArrayCell(Id("song"),[ArrayCell(Id("ra"),[Id("sao")])])]),Assign(Id("yeu_nguoi"),ArrayCell(Id("the_nao"),[Id("xxx")]))]]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,390))

    def test_91(self):
        input = """
                    Var: cuoc_song, dieu_gi[0] = {1,2,3};
                    Function: den_roi_di
                    Body:
                        nam(ban_tay, lac(nhau));
                        Do mot_lan(); While !True EndDo.
                    EndBody.
                    Function: ngay_do
                    Parameter: abcd
                    Body:
                        While ngaydo(haita(chang(thay[nhau]))) Do
                        anh(song[ra[sao]]);
                        EndWhile.
                        den(roi, di||a);
                        Return ky_uc(van_con[nhung[gio(em[voi(anh)])]]);
                    EndBody.
                """
        expect = Program([VarDecl(Id("cuoc_song"),[],None),VarDecl(Id("dieu_gi"),[0],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("den_roi_di"),[],tuple([[],[CallStmt(Id("nam"),[Id("ban_tay"),CallExpr(Id("lac"),[Id("nhau")])]),Dowhile(tuple([[],[CallStmt(Id("mot_lan"),[])]]),UnaryOp("!",BooleanLiteral(True)))]])),FuncDecl(Id("ngay_do"),[VarDecl(Id("abcd"),[],None)],tuple([[],[While(CallExpr(Id("ngaydo"),[CallExpr(Id("haita"),[CallExpr(Id("chang"),[ArrayCell(Id("thay"),[Id("nhau")])])])]),tuple([[],[CallStmt(Id("anh"),[ArrayCell(Id("song"),[ArrayCell(Id("ra"),[Id("sao")])])])]])),CallStmt(Id("den"),[Id("roi"),BinaryOp("||",Id("di"),Id("a"))]),Return(CallExpr(Id("ky_uc"),[ArrayCell(Id("van_con"),[ArrayCell(Id("nhung"),[CallExpr(Id("gio"),[ArrayCell(Id("em"),[CallExpr(Id("voi"),[Id("anh")])])])])])]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_92(self):
        input = """
                    Var: cuoc_song, dieu_gi[0] = {1,2,3};
                    Function: den_roi_di
                    Body:
                        nam(ban_tay, lac(nhau));
                        Do mot_lan(); While !True EndDo.
                        nguoi_yeu = cu();
                        For(nam=0,thang==12.0,nhieu)Do
                            anh(tro[lai]);
                            loi_xua = em[co] + biet || khoong;
                        EndFor.
                    EndBody.
                    Function: ngay_do
                    Parameter: nguoi, yeu
                    Body:
                        While ngaydo(haita(chang(thay[nhau]))) Do
                        anh(song[ra[sao]]);
                        EndWhile.
                        den(roi, di||a);
                        Return ky_uc(van_con[nhung[gio(em[voi(anh)])]]);
                    EndBody.

                """
        expect = Program([VarDecl(Id("cuoc_song"),[],None),VarDecl(Id("dieu_gi"),[0],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("den_roi_di"),[],tuple([[],[CallStmt(Id("nam"),[Id("ban_tay"),CallExpr(Id("lac"),[Id("nhau")])]),Dowhile(tuple([[],[CallStmt(Id("mot_lan"),[])]]),UnaryOp("!",BooleanLiteral(True))),Assign(Id("nguoi_yeu"),CallExpr(Id("cu"),[])),For(Id("nam"),IntLiteral(0),BinaryOp("==",Id("thang"),FloatLiteral(12.0)),Id("nhieu"),tuple([[],[CallStmt(Id("anh"),[ArrayCell(Id("tro"),[Id("lai")])]),Assign(Id("loi_xua"),BinaryOp("||",BinaryOp("+",ArrayCell(Id("em"),[Id("co")]),Id("biet")),Id("khoong")))]]))]])),FuncDecl(Id("ngay_do"),[VarDecl(Id("nguoi"),[],None),VarDecl(Id("yeu"),[],None)],tuple([[],[While(CallExpr(Id("ngaydo"),[CallExpr(Id("haita"),[CallExpr(Id("chang"),[ArrayCell(Id("thay"),[Id("nhau")])])])]),tuple([[],[CallStmt(Id("anh"),[ArrayCell(Id("song"),[ArrayCell(Id("ra"),[Id("sao")])])])]])),CallStmt(Id("den"),[Id("roi"),BinaryOp("||",Id("di"),Id("a"))]),Return(CallExpr(Id("ky_uc"),[ArrayCell(Id("van_con"),[ArrayCell(Id("nhung"),[CallExpr(Id("gio"),[ArrayCell(Id("em"),[CallExpr(Id("voi"),[Id("anh")])])])])])]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_93(self):
        input = """
                    Var: cuoc_song, dieu_gi[0] = {1,2,3};
                    Function: den_roi_di
                    Body:
                        mua_thu = ay_dang()[con_duong[la_roi()]];
                        ngay_nam[123654] = giot_le(roi);
                        While nguoi_dan > ong Do
                            Var: em, nho = {};
                            For (ngan=0, lan, hon) Do
                        EndFor.EndWhile.
                    EndBody.
                    Function: ngay_do
                    Parameter: nguoi, yeu
                    Body:
                        chot_nhu_giac_mo = nhu_khong - 1.e78 + 9;
                        yeu = lai - nguoi || hom (qua()[10]);
                    EndBody.
                """
        expect = Program([VarDecl(Id("cuoc_song"),[],None),VarDecl(Id("dieu_gi"),[0],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("den_roi_di"),[],tuple([[],[Assign(Id("mua_thu"),ArrayCell(CallExpr(Id("ay_dang"),[]),[ArrayCell(Id("con_duong"),[CallExpr(Id("la_roi"),[])])])),Assign(ArrayCell(Id("ngay_nam"),[IntLiteral(123654)]),CallExpr(Id("giot_le"),[Id("roi")])),While(BinaryOp(">",Id("nguoi_dan"),Id("ong")),tuple([[VarDecl(Id("em"),[],None),VarDecl(Id("nho"),[],ArrayLiteral([]))],[For(Id("ngan"),IntLiteral(0),Id("lan"),Id("hon"),tuple([[],[]]))]]))]])),FuncDecl(Id("ngay_do"),[VarDecl(Id("nguoi"),[],None),VarDecl(Id("yeu"),[],None)],tuple([[],[Assign(Id("chot_nhu_giac_mo"),BinaryOp("+",BinaryOp("-",Id("nhu_khong"),FloatLiteral(1e+78)),IntLiteral(9))),Assign(Id("yeu"),BinaryOp("||",BinaryOp("-",Id("lai"),Id("nguoi")),CallExpr(Id("hom"),[ArrayCell(CallExpr(Id("qua"),[]),[IntLiteral(10)])])))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,393))

    def test_94(self):
        input = """
                    Var: cuoc_song, dieu_gi[0] = {1,2,3};
                    Function: den_roi_di
                    Body:
                        mua_thu = ay_dang()[con_duong[la_roi()]];
                        ngay_nam[123654] = giot_le(roi);
                        While nguoi_dan > ong Do
                            Var: em, nho = {};
                            For (ngan=0, lan, hon) Do
                        EndFor.EndWhile.
                    EndBody.
                    Function: ngay_do
                    Parameter: nguoi, yeu
                    Body:
                        chot_nhu_giac_mo = nhu_khong - 1.e78 + 9;
                        yeu = lai - nguoi || hom (qua()[10]);
                        Do
                        Var: em;
                        noi_buon = su() + (co() - don()[nguoi_hom(qua)]);
                        yeu_het = tuoi - 8 * xuan;
                        While nguoi_co * con && yeu \\ em EndDo.
                    EndBody.
                """
        expect = Program([VarDecl(Id("cuoc_song"),[],None),VarDecl(Id("dieu_gi"),[0],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("den_roi_di"),[],tuple([[],[Assign(Id("mua_thu"),ArrayCell(CallExpr(Id("ay_dang"),[]),[ArrayCell(Id("con_duong"),[CallExpr(Id("la_roi"),[])])])),Assign(ArrayCell(Id("ngay_nam"),[IntLiteral(123654)]),CallExpr(Id("giot_le"),[Id("roi")])),While(BinaryOp(">",Id("nguoi_dan"),Id("ong")),tuple([[VarDecl(Id("em"),[],None),VarDecl(Id("nho"),[],ArrayLiteral([]))],[For(Id("ngan"),IntLiteral(0),Id("lan"),Id("hon"),tuple([[],[]]))]]))]])),FuncDecl(Id("ngay_do"),[VarDecl(Id("nguoi"),[],None),VarDecl(Id("yeu"),[],None)],tuple([[],[Assign(Id("chot_nhu_giac_mo"),BinaryOp("+",BinaryOp("-",Id("nhu_khong"),FloatLiteral(1e+78)),IntLiteral(9))),Assign(Id("yeu"),BinaryOp("||",BinaryOp("-",Id("lai"),Id("nguoi")),CallExpr(Id("hom"),[ArrayCell(CallExpr(Id("qua"),[]),[IntLiteral(10)])]))),Dowhile(tuple([[VarDecl(Id("em"),[],None)],[Assign(Id("noi_buon"),BinaryOp("+",CallExpr(Id("su"),[]),BinaryOp("-",CallExpr(Id("co"),[]),ArrayCell(CallExpr(Id("don"),[]),[CallExpr(Id("nguoi_hom"),[Id("qua")])])))),Assign(Id("yeu_het"),BinaryOp("-",Id("tuoi"),BinaryOp("*",IntLiteral(8),Id("xuan"))))]]),BinaryOp("&&",BinaryOp("*",Id("nguoi_co"),Id("con")),BinaryOp("\\",Id("yeu"),Id("em"))))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_95(self):
        input = """
                    Var: cuoc_song, dieu_gi[0] = {1,2,3};
                    Function: den_roi_di
                    Body:
                        mua_thu = ay_dang()[con_duong[la_roi()]];
                        Break;
                        chang_muon = mot_minh - di(khap[the(gian)]);
                        yeu(); vi_em_thuong_mot_nguoi();
                        Continue;di_tim();
                        Return chang(con[gi(trong==vang) - nguoi_giong(nhu &&vay)]);
                    EndBody.
                    Function: ngay_do
                    Parameter: nguoi, yeu
                    Body:
                        yeu = lai - nguoi || hom (qua()[10]);
                        Do
                        Var: em;
                        While nguoi_co * con && yeu \\ em EndDo.
                    EndBody.
                """
        expect = Program([VarDecl(Id("cuoc_song"),[],None),VarDecl(Id("dieu_gi"),[0],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("den_roi_di"),[],tuple([[],[Assign(Id("mua_thu"),ArrayCell(CallExpr(Id("ay_dang"),[]),[ArrayCell(Id("con_duong"),[CallExpr(Id("la_roi"),[])])])),Break(),Assign(Id("chang_muon"),BinaryOp("-",Id("mot_minh"),CallExpr(Id("di"),[ArrayCell(Id("khap"),[CallExpr(Id("the"),[Id("gian")])])]))),CallStmt(Id("yeu"),[]),CallStmt(Id("vi_em_thuong_mot_nguoi"),[]),Continue(),CallStmt(Id("di_tim"),[]),Return(CallExpr(Id("chang"),[ArrayCell(Id("con"),[BinaryOp("-",CallExpr(Id("gi"),[BinaryOp("==",Id("trong"),Id("vang"))]),CallExpr(Id("nguoi_giong"),[BinaryOp("&&",Id("nhu"),Id("vay"))]))])]))]])),FuncDecl(Id("ngay_do"),[VarDecl(Id("nguoi"),[],None),VarDecl(Id("yeu"),[],None)],tuple([[],[Assign(Id("yeu"),BinaryOp("||",BinaryOp("-",Id("lai"),Id("nguoi")),CallExpr(Id("hom"),[ArrayCell(CallExpr(Id("qua"),[]),[IntLiteral(10)])]))),Dowhile(tuple([[VarDecl(Id("em"),[],None)],[]]),BinaryOp("&&",BinaryOp("*",Id("nguoi_co"),Id("con")),BinaryOp("\\",Id("yeu"),Id("em"))))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test_96(self):
        input = """
                    Var: cuoc_song, dieu_gi[0] = {1,2,3};
                    Function: den_roi_di
                    Body:
                    EndBody.
                    Function: ngay_do
                    Parameter: nguoi, yeu
                    Body:
                    EndBody.
                    Function: den_roi_di
                    Body:
                    EndBody.
                    Function: ngay_do
                    Parameter: nguoi, yeu
                    Body:
                    EndBody.
                    Function: den_roi_di
                    Body:
                    EndBody.
                    Function: ngay_do
                    Parameter: nguoi, yeu
                    Body:
                    EndBody.
                    Function: den_roi_di
                    Body:
                    EndBody.
                    Function: ngay_do
                    Parameter: nguoi, yeu
                    Body:
                    EndBody.
                    Function: den_roi_di
                    Body:
                    EndBody.
                    Function: ngay_do
                    Parameter: nguoi, yeu
                    Body:
                    EndBody.
                    Function: den_roi_di
                    Body:
                    EndBody.
                    Function: ngay_do
                    Parameter: nguoi, yeu
                    Body:
                    EndBody.
                    Function: den_roi_di
                    Body:
                    EndBody.
                    Function: ngay_do
                    Parameter: nguoi, yeu
                    Body:
                    EndBody.

                """
        expect = Program([VarDecl(Id("cuoc_song"),[],None),VarDecl(Id("dieu_gi"),[0],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),FuncDecl(Id("den_roi_di"),[],tuple([[],[]])),FuncDecl(Id("ngay_do"),[VarDecl(Id("nguoi"),[],None),VarDecl(Id("yeu"),[],None)],tuple([[],[]])),FuncDecl(Id("den_roi_di"),[],tuple([[],[]])),FuncDecl(Id("ngay_do"),[VarDecl(Id("nguoi"),[],None),VarDecl(Id("yeu"),[],None)],tuple([[],[]])),FuncDecl(Id("den_roi_di"),[],tuple([[],[]])),FuncDecl(Id("ngay_do"),[VarDecl(Id("nguoi"),[],None),VarDecl(Id("yeu"),[],None)],tuple([[],[]])),FuncDecl(Id("den_roi_di"),[],tuple([[],[]])),FuncDecl(Id("ngay_do"),[VarDecl(Id("nguoi"),[],None),VarDecl(Id("yeu"),[],None)],tuple([[],[]])),FuncDecl(Id("den_roi_di"),[],tuple([[],[]])),FuncDecl(Id("ngay_do"),[VarDecl(Id("nguoi"),[],None),VarDecl(Id("yeu"),[],None)],tuple([[],[]])),FuncDecl(Id("den_roi_di"),[],tuple([[],[]])),FuncDecl(Id("ngay_do"),[VarDecl(Id("nguoi"),[],None),VarDecl(Id("yeu"),[],None)],tuple([[],[]])),FuncDecl(Id("den_roi_di"),[],tuple([[],[]])),FuncDecl(Id("ngay_do"),[VarDecl(Id("nguoi"),[],None),VarDecl(Id("yeu"),[],None)],tuple([[],[]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test_97(self):
        input = """
                    Var: x[0x7] = 10;
                    Function: den_roi_di
                    Body:
                        hanh_phuc = nguoi - con + gai == danh * mat % False;
                        For(tiec_nhung = 7.3, ngam_ngui(), buong_canh_tay[cho_em(123)]) Do
                            em_chang(mang - chang_dau(vi_anh));
                            den_khi_nao_nguoi();
                            di_tim_noi_ngu(3e67);
                            While hapinesss(4 + (girl)) Do danh_mat(smile); EndWhile.
                            Continue;
                        EndFor.
                    EndBody.
                    Function: ngay_do
                    Parameter: nguoi, yeu
                    Body:
                        Var: tam_biet = {10, "46wf", 0x7, 1.e5};
                        Return chi_con(la[ban(thoi[ai(do)])]) || {"mot_nua", "lam", "bang"} && mo;
                    EndBody.
                """
        expect = Program([VarDecl(Id("x"),[7],IntLiteral(10)),FuncDecl(Id("den_roi_di"),[],tuple([[],[Assign(Id("hanh_phuc"),BinaryOp("==",BinaryOp("+",BinaryOp("-",Id("nguoi"),Id("con")),Id("gai")),BinaryOp("%",BinaryOp("*",Id("danh"),Id("mat")),BooleanLiteral(False)))),For(Id("tiec_nhung"),FloatLiteral(7.3),CallExpr(Id("ngam_ngui"),[]),ArrayCell(Id("buong_canh_tay"),[CallExpr(Id("cho_em"),[IntLiteral(123)])]),tuple([[],[CallStmt(Id("em_chang"),[BinaryOp("-",Id("mang"),CallExpr(Id("chang_dau"),[Id("vi_anh")]))]),CallStmt(Id("den_khi_nao_nguoi"),[]),CallStmt(Id("di_tim_noi_ngu"),[FloatLiteral(3e+67)]),While(CallExpr(Id("hapinesss"),[BinaryOp("+",IntLiteral(4),Id("girl"))]),tuple([[],[CallStmt(Id("danh_mat"),[Id("smile")])]])),Continue()]]))]])),FuncDecl(Id("ngay_do"),[VarDecl(Id("nguoi"),[],None),VarDecl(Id("yeu"),[],None)],tuple([[VarDecl(Id("tam_biet"),[],ArrayLiteral([IntLiteral(10),StringLiteral("46wf"),IntLiteral(7),FloatLiteral(100000.0)]))],[Return(BinaryOp("&&",BinaryOp("||",CallExpr(Id("chi_con"),[ArrayCell(Id("la"),[CallExpr(Id("ban"),[ArrayCell(Id("thoi"),[CallExpr(Id("ai"),[Id("do")])])])])]),ArrayLiteral([StringLiteral("mot_nua"),StringLiteral("lam"),StringLiteral("bang")])),Id("mo")))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_98(self):
        input = """
                    Var: x[0x7] = 10;
                    Var: em_qua_yeu[0O325] = {0x4,0o3,1.e4};
                    Function: den_roi_di
                    Body:
                        hanh_phuc = nguoi - con + gai == danh * mat % False;
                        For(tiec_nhung = 7.3, ngam_ngui(tan_di), buong_canh_tay[cho_em(123)]) Do
                        Var: vai = 3, nguoi, mim[10] = {"cuoi"};
                            em_chang(mang - chang_dau(vi_anh));
                            While hapinesss(4 + (girl)) Do
                            rot_nuoc_mat = dau_buot(con_tim) ;
                            danh_mat(smile); EndWhile.
                            Continue;
                        EndFor.
                        Return dem_tha_troi();
                    EndBody.
                """
        expect = Program([VarDecl(Id("x"),[7],IntLiteral(10)),VarDecl(Id("em_qua_yeu"),[213],ArrayLiteral([IntLiteral(4),IntLiteral(3),FloatLiteral(10000.0)])),FuncDecl(Id("den_roi_di"),[],tuple([[],[Assign(Id("hanh_phuc"),BinaryOp("==",BinaryOp("+",BinaryOp("-",Id("nguoi"),Id("con")),Id("gai")),BinaryOp("%",BinaryOp("*",Id("danh"),Id("mat")),BooleanLiteral(False)))),For(Id("tiec_nhung"),FloatLiteral(7.3),CallExpr(Id("ngam_ngui"),[Id("tan_di")]),ArrayCell(Id("buong_canh_tay"),[CallExpr(Id("cho_em"),[IntLiteral(123)])]),tuple([[VarDecl(Id("vai"),[],IntLiteral(3)),VarDecl(Id("nguoi"),[],None),VarDecl(Id("mim"),[10],ArrayLiteral([StringLiteral("cuoi")]))],[CallStmt(Id("em_chang"),[BinaryOp("-",Id("mang"),CallExpr(Id("chang_dau"),[Id("vi_anh")]))]),While(CallExpr(Id("hapinesss"),[BinaryOp("+",IntLiteral(4),Id("girl"))]),tuple([[],[Assign(Id("rot_nuoc_mat"),CallExpr(Id("dau_buot"),[Id("con_tim")])),CallStmt(Id("danh_mat"),[Id("smile")])]])),Continue()]])),Return(CallExpr(Id("dem_tha_troi"),[]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_99(self):
        input = """
                    Var: x[0x7] = 10;
                    Var: em_qua_yeu[0O325] = {0x4,0o3,1.e4};
                    Function: den_roi_di
                    Body:
                        hanh_phuc = nguoi - con + gai == danh * mat % False;
                        For(tiec_nhung = 7.3, ngam_ngui(tan_di), buong_canh_tay[cho_em(123)]) Do
                        Var: vai = 3, nguoi, mim[10] = {"cuoi"};
                            em_chang(mang - chang_dau(vi_anh));
                            danh_mat(smile);
                            Continue;
                        EndFor.
                        Return dem_tha_troi();
                        om_lay(cha[tua(0, vao, vai+cua || cha)]);
                        Do con = nho(lam) + luc[hai(cha&&cha)];
                        ha_ha_how_how = khong_con(ai) + hoi(con[da + !ve -. chua]);
                        quan = nhung_ky_niem * dong - day == yen || binh && nhat;
                        While chi(vi == con) EndDo.
                    EndBody.
                """
        expect = Program([VarDecl(Id("x"),[7],IntLiteral(10)),VarDecl(Id("em_qua_yeu"),[213],ArrayLiteral([IntLiteral(4),IntLiteral(3),FloatLiteral(10000.0)])),FuncDecl(Id("den_roi_di"),[],tuple([[],[Assign(Id("hanh_phuc"),BinaryOp("==",BinaryOp("+",BinaryOp("-",Id("nguoi"),Id("con")),Id("gai")),BinaryOp("%",BinaryOp("*",Id("danh"),Id("mat")),BooleanLiteral(False)))),For(Id("tiec_nhung"),FloatLiteral(7.3),CallExpr(Id("ngam_ngui"),[Id("tan_di")]),ArrayCell(Id("buong_canh_tay"),[CallExpr(Id("cho_em"),[IntLiteral(123)])]),tuple([[VarDecl(Id("vai"),[],IntLiteral(3)),VarDecl(Id("nguoi"),[],None),VarDecl(Id("mim"),[10],ArrayLiteral([StringLiteral("cuoi")]))],[CallStmt(Id("em_chang"),[BinaryOp("-",Id("mang"),CallExpr(Id("chang_dau"),[Id("vi_anh")]))]),CallStmt(Id("danh_mat"),[Id("smile")]),Continue()]])),Return(CallExpr(Id("dem_tha_troi"),[])),CallStmt(Id("om_lay"),[ArrayCell(Id("cha"),[CallExpr(Id("tua"),[IntLiteral(0),Id("vao"),BinaryOp("||",BinaryOp("+",Id("vai"),Id("cua")),Id("cha"))])])]),Dowhile(tuple([[],[Assign(Id("con"),BinaryOp("+",CallExpr(Id("nho"),[Id("lam")]),ArrayCell(Id("luc"),[CallExpr(Id("hai"),[BinaryOp("&&",Id("cha"),Id("cha"))])]))),Assign(Id("ha_ha_how_how"),BinaryOp("+",CallExpr(Id("khong_con"),[Id("ai")]),CallExpr(Id("hoi"),[ArrayCell(Id("con"),[BinaryOp("-.",BinaryOp("+",Id("da"),UnaryOp("!",Id("ve"))),Id("chua"))])]))),Assign(Id("quan"),BinaryOp("==",BinaryOp("-",BinaryOp("*",Id("nhung_ky_niem"),Id("dong")),Id("day")),BinaryOp("&&",BinaryOp("||",Id("yen"),Id("binh")),Id("nhat"))))]]),CallExpr(Id("chi"),[BinaryOp("==",Id("vi"),Id("con"))]))]]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,399))

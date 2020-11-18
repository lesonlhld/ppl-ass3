def test_349(self):
        input = r"""
        Var: x = 0, a[10][10];
        Function: complicated_function
        Parameter: m, n
        Body: 
            If n == 0 Then
                Return 1;
            ElseIf n != 0 Then
                Return n * fact (n - 1);
            ElseIf True Then
                n = 1;
                If (a[n][n] \ 2 == m) Then
                    For (x = 10, 1 == (True || False), 0x13) Do
                        a[n][n] = a[n][n] + 1;
                        m = m * 2;
                        While (m != 1000) Do
                            Do 
                                print("Hahaha!");
                            While (m != 500)
                            EndDo.
                        EndWhile.
                    EndFor.
                Else
                    Var: y = 0; c[0] = {{1,2}, 3, {4, {5, 6}}};
                    Continue;
                EndIf.
            Else
                Return True;
            EndIf.
        EndBody.""" 
        expect_output = Program([VarDecl(Id("x"),[],IntLiteral(0)),VarDecl(Id("a"),[10,10],None),FuncDecl(Id("complicated_function"),[VarDecl(Id("m"),[],None),VarDecl(Id("n"),[],None)],([],[If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],[Return(IntLiteral(1))]),(BinaryOp("!=",Id("n"),IntLiteral(0)),[],[Return(BinaryOp("*",Id("n"),CallExpr(Id("fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))]),(BooleanLiteral(True),[],[Assign(Id("n"),IntLiteral(1)),If([(BinaryOp("==",BinaryOp("\\",ArrayCell(Id("a"),[Id("n"),Id("n")]),IntLiteral(2)),Id("m")),[],[For(Id("x"),IntLiteral(10),BinaryOp("==",IntLiteral(1),BinaryOp("||",BooleanLiteral(True),BooleanLiteral(False))),IntLiteral(19),([],[Assign(ArrayCell(Id("a"),[Id("n"),Id("n")]),BinaryOp("+",ArrayCell(Id("a"),[Id("n"),Id("n")]),IntLiteral(1))),Assign(Id("m"),BinaryOp("*",Id("m"),IntLiteral(2))),While(BinaryOp("!=",Id("m"),IntLiteral(1000)),([],[Dowhile(([],[CallStmt(Id("print"),[StringLiteral("Hahaha!")])]),BinaryOp("!=",Id("m"),IntLiteral(500)))]))]))])],([VarDecl(Id("y"),[],IntLiteral(0))],[Assign(ArrayCell(Id("c"),[IntLiteral(0)]),ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)]),IntLiteral(3),ArrayLiteral([IntLiteral(4),ArrayLiteral([IntLiteral(5),IntLiteral(6)])])])),Continue()]))])],([],[Return(BooleanLiteral(True))]))]))])
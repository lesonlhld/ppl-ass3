import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):
    def test_401(self):
        """Created automatically"""
        input = r"""
                    Var: a, b, c, d;
                    Function: main
                    Parameter: a, e
                    Body:
                        Var: o;
                        a = d;
                        Return 6.6;
                    EndBody.
                """
        expect = str(TypeCannotBeInferred(Assign(Id("a"),Id("d"))))
        self.assertTrue(TestChecker.test(input,expect,401))
        
    def test_402(self):
        """Created automatically"""
        input = r"""Var: a = 2;
                    Function: main
                    Parameter: b, c
                    Body:
                        b = foo();
                        Return a;
                    EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,402))
        
    def test_403(self):
        """Created automatically"""
        input = r"""Var: a = 2;
                    Function: main
                    Parameter: b, c
                    Body:
                        f = 5; 
                        Return a;
                    EndBody."""
        expect = str(Undeclared(Identifier(),"f"))
        self.assertTrue(TestChecker.test(input,expect,403))
        
    def test_404(self):
        """Created automatically"""
        input = r"""Var: a = 2;
                    Function: main1
                    Parameter: b, c
                    Body:
                        Return a;
                    EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,404))
        
    def test_405(self):
        """Created automatically"""
        input = r"""Function: main
                    Parameter: b, c
                    Body:
                        Return a;
                    EndBody."""
        expect = str(Undeclared(Identifier(),"a"))
        self.assertTrue(TestChecker.test(input,expect,405))
        
    def test_406(self):
        """Created automatically"""
        input = r"""Function: main
                    Parameter: b, c
                    Body:
                        b = a;
                    EndBody."""
        expect = str(Undeclared(Identifier(),"a"))
        self.assertTrue(TestChecker.test(input,expect,406))
        
    def test_407(self):
        """Created automatically"""
        input = r"""Var: a = 2;
                    Function: main
                    Parameter: b, c
                    Body:
                        b = 2.2;
                        a = 3.3;
                        Return a;
                    EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("a"),FloatLiteral(3.3))))
        self.assertTrue(TestChecker.test(input,expect,407))
        
    def test_408(self):
        """Created automatically"""
        input = r"""Var: a = 2;
                    Function: main
                    Parameter: b, c
                    Body:
                        b = 2.2;
                        a = 2.2*a;
                        Return a;
                    EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("*",FloatLiteral(2.2),Id("a"))))
        self.assertTrue(TestChecker.test(input,expect,408))
        
    def test_409(self):
        """Created automatically"""
        input = r"""Var: a = 2;
                    Function: main
                    Parameter: b, c
                    Body:
                        b = 2.2;
                        a = 2.2*.a;
                        Return a;
                    EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("*.",FloatLiteral(2.2),Id("a"))))
        self.assertTrue(TestChecker.test(input,expect,409))
        
    def test_410(self):
        """Created automatically"""
        input = r"""Var: a;
                    Function: main
                    Parameter: b, c
                    Body:
                        b = 2;
                        a = c*.a;
                        a = b;
                        Return a;
                    EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("a"),Id("b"))))
        self.assertTrue(TestChecker.test(input,expect,410))
        
    def test_411(self):
        """Created automatically"""
        input = r"""Var: a;
                    Function: main
                    Parameter: b, c
                    Body:
                        b = 2;
                        a = c*.a;
                        a = c;
                        b = a*.c;
                        Return a;
                    EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("b"),BinaryOp("*.",Id("a"),Id("c")))))
        self.assertTrue(TestChecker.test(input,expect,411))
        
    def test_412(self):
        """Created automatically"""
        input = r"""Var: a;
                    Function: main
                    Parameter: b
                    Body:
                        Var: i;
                        For (i = 2, i == b, 6) Do
                            a = 6;
                        EndFor.
                        b = a +. 2.2;          
                        Return a;
                    EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("+.",Id("a"),FloatLiteral(2.2))))
        self.assertTrue(TestChecker.test(input,expect,412))
        
    def test_413(self):
        """Created automatically"""
        input = r"""Var: a, c;
                    Function: main
                    Parameter: b
                    Body:
                        Var: i;
                        c = 2.2;
                        For (i = 2, i == b, c) Do
                            a = 6;
                        EndFor.         
                        Return a;
                    EndBody."""
        expect = str(TypeMismatchInStatement(For(Id("i"),IntLiteral(2),BinaryOp("==",Id("i"),Id("b")),Id("c"),([],[Assign(Id("a"),IntLiteral(6))]))))
        self.assertTrue(TestChecker.test(input,expect,413))
        
    def test_414(self):
        """Created automatically"""
        input = r"""Var: a, c;
                    Function: main
                    Parameter: b
                    Body:
                        Var: i;
                        c = -5;
                        For (i = 2, i < b, c) Do
                            a = 6;
                        EndFor. 
                        c = b + 2.2;       
                        Return a;
                    EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("+",Id("b"),FloatLiteral(2.2))))
        self.assertTrue(TestChecker.test(input,expect,414))
        
    def test_415(self):
        """Created automatically"""
        input = r"""Var: a, c;
                    Function: main
                    Parameter: b
                    Body:
                        Var: i;
                        c = -5;
                        For (i = 2, i < b, c) Do
                            a = 6.6;
                        EndFor. 
                        c = a +. 2.2;       
                        Return a;
                    EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("c"),BinaryOp("+.",Id("a"),FloatLiteral(2.2)))))
        self.assertTrue(TestChecker.test(input,expect,415))
        
    def test_416(self):
        """Created automatically"""
        input = r"""Function: main
                Body:
                    Var: x;
                    x = x + foo();
                EndBody.

                Function: foo
                Body:
                    Return 2.2;
                EndBody."""
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(2.2))))
        self.assertTrue(TestChecker.test(input,expect,416))
        
    def test_417(self):
        """Created automatically"""
        input = r"""Function: main
                Body:
                    Var: x;
                    x = x + foo();
                EndBody.

                Function: foo
                Parameter: a,a
                Body:
                    Return 2.2;
                EndBody."""
        expect = str(Redeclared(Parameter(),"a"))
        self.assertTrue(TestChecker.test(input,expect,417))
        
    def test_418(self):
        """Created automatically"""
        input = r"""Function: main
                Body:
                    Var: x, x;
                    x = x + foo();
                EndBody.

                Function: foo
                Parameter: a,a
                Body:
                    Return 2.2;
                EndBody."""
        expect = str(Redeclared(Parameter(),"a"))
        self.assertTrue(TestChecker.test(input,expect,418))
        
    def test_419(self):
        """Created automatically"""
        input = r"""Function: main
                Body:
                    Var: x;
                    x = x + foo();
                EndBody.

                Function: foo
                Parameter: a
                Body:
                    Var: a;
                    Return 2.2;
                EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[])))
        self.assertTrue(TestChecker.test(input,expect,419))
        
    def test_420(self):
        """Created automatically"""
        input = r"""Function: main
                Body:
                    Var: x = 2;
                    x = x + foo(x);
                EndBody.

                Function: foo
                Parameter: a
                Body:
                    Return c;
                EndBody."""
        expect = str(Undeclared(Identifier(),"c"))
        self.assertTrue(TestChecker.test(input,expect,420))
        
    def test_421(self):
        """Created automatically"""
        input = r"""Var: b;
                Function: main
                Body:
                    Var: x = 2, c, f;
                    Do
                        b = x;
                    While b > c
                    EndDo.
                    For(c = 5, c == True, 5) Do
                        f = 6;
                    EndFor.
                    Return c;
                EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("==",Id("c"),BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect,421))
        
    def test_422(self):
        """Created automatically"""
        input = r"""Var: b;
                Var: b;
                Function: main
                Body:
                    Var: x = 2, c, f;
                    Do
                        b = x;
                        c = 2.2;
                    While b > c
                    EndDo.
                    For(c = 5, c == True, 5) Do
                        f = 6;
                    EndFor.
                    Return c;
                EndBody."""
        expect = str(Redeclared(Variable(),"b"))
        self.assertTrue(TestChecker.test(input,expect,422))
        
    def test_423(self):
        """Created automatically"""
        input = r"""Var: b;
                Function: main
                Body:
                    Var: x = 2, c, f;
                    Do
                        c = 2.2;
                    While b >. c
                    EndDo.
                    For(x = 5, c =/= 2.2, 5) Do
                        f = 6;
                    EndFor.
                    c = f + 2;
                    Return c;
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("c"),BinaryOp("+",Id("f"),IntLiteral(2)))))
        self.assertTrue(TestChecker.test(input,expect,423))
        
    def test_424(self):
        """Created automatically"""
        input = r"""Var: b;
                Function: main
                Body:
                    Var: x = 2, c, f;
                    Do
                        c = 2.2;
                    While b >. c
                    EndDo.
                    For(x = 5, c =/= 2.2, 5) Do
                        f = 6;
                    EndFor.
                    c = f + 2;
                    Return c;
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("c"),BinaryOp("+",Id("f"),IntLiteral(2)))))
        self.assertTrue(TestChecker.test(input,expect,424))
        
    def test_425(self):
        """Created automatically"""
        input = r"""Var: b;
                Function: main
                Body:
                    Var: x = 5;
                    While b < 2 Do
                        x = b +. 2.2;
                    EndWhile.
                EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("+.",Id("b"),FloatLiteral(2.2))))
        self.assertTrue(TestChecker.test(input,expect,425))
        
    def test_426(self):
        """Created automatically"""
        input = r"""Var: b;
                Function: main
                Body:
                    Var: x;
                    While b < 2 Do
                        x = b + 2;
                    EndWhile.
                    x = True;
                    Return x;
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"),BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect,426))
        
    def test_427(self):
        """Created automatically"""
        input = r"""Var: b;
                Function: main
                Body:
                    Var: x;
                    While b <. 2 Do
                        x = b + 2;
                    EndWhile.
                    x = True;
                    Return x;
                EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("<.",Id("b"),IntLiteral(2))))
        self.assertTrue(TestChecker.test(input,expect,427))
        
    def test_428(self):
        """Created automatically"""
        input = r"""Var: b;
                Function: main
                Body:
                    Var: x;
                    While b <. 2.2 Do
                        x = b +. 0.0;
                    EndWhile.
                    x = 3;
                    Return x;
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"),IntLiteral(3))))
        self.assertTrue(TestChecker.test(input,expect,428))
        
    def test_429(self):
        """Created automatically"""
        input = r"""Var: b;
                Function: main
                Body:
                    Var: x;
                    While b <. 2.2 Do
                        x = b +. 0.0;
                    EndWhile.
                    b = 2 + foo(x);
                    Return x;
                EndBody.

                Function: foo
                Parameter: b
                Body:
                    Return 3;
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("b"),BinaryOp("+",IntLiteral(2),CallExpr(Id("foo"),[Id("x")])))))
        self.assertTrue(TestChecker.test(input,expect,429))
        
    def test_430(self):
        """Created automatically"""
        input = r"""Var: b;
                Function: main
                Body:
                    Var: x, c;
                    While b <. 2.2 Do
                        x = b +. 0.0;
                        For(x = 5, x <. 4.4, 2) Do
                            c = 5;
                        EndFor.
                    EndWhile.
                    b = 2 + foo(x);
                    Return x;
                EndBody.

                Function: foo
                Parameter: b
                Body:
                    Return 3;
                EndBody."""
        expect = str(TypeMismatchInStatement(For(Id("x"),IntLiteral(5),BinaryOp("<.",Id("x"),FloatLiteral(4.4)),IntLiteral(2),([],[Assign(Id("c"),IntLiteral(5))]))))
        self.assertTrue(TestChecker.test(input,expect,430))
        
    def test_431(self):
        """Created automatically"""
        input = r"""Var: b;
                Function: main
                Body:
                    Var: x, c;
                    While b <. 2.2 Do
                        x = b +. 0.0;
                        For(i = 5, x <. 4.4, 2) Do
                            c = i;
                        EndFor.
                    EndWhile.
                    c = i + foo(0.0);
                    Return x;
                EndBody.

                Function: foo
                Parameter: b
                Body:
                    Return 3;
                EndBody."""
        expect = str(Undeclared(Identifier(),"i"))
        self.assertTrue(TestChecker.test(input,expect,431))
        
    def test_432(self):
        """Created automatically"""
        input = r"""
                Var: b;
                Function: main
                Body:
                    Var: x, c;
                    While b <. 2.2 Do
                        x = b +. 0.0;
                        For(i = 5, x <. 4.4, 2) Do
                            c = i;
                        EndFor.
                    EndWhile.
                    c = c + foo(0.0) * 2.0;
                    Return x;
                EndBody.

                Function: foo
                Parameter: b
                Body:
                    Return 3;
                EndBody.
                """
        expect = str(Undeclared(Identifier(),"i"))
        self.assertTrue(TestChecker.test(input,expect,432))
        
    def test_433(self):
        """Created automatically"""
        input = r"""
                Var: b;
                Function: main
                Body:
                    foo(5);
                    b = 2.2;
                EndBody.

                Function: foo
                Parameter: c
                Body:
                    b = c;
                    Return 3;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id("b"),Id("c"))))
        self.assertTrue(TestChecker.test(input,expect,433))
        
    def test_434(self):
        """Created automatically"""
        input = r"""
                Var: b;
                Function: main
                Body:
                    Var: c;
                    If b < 5 Then
                        c = 5;
                    ElseIf c > 5 Then
                        c = b;
                    Else c = 2.2;
                    EndIf.
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id("c"),FloatLiteral(2.2))))
        self.assertTrue(TestChecker.test(input,expect,434))
        
    def test_435(self):
        """Created automatically"""
        input = r"""
                Var: b;
                Function: main
                Body:
                    Var: c = 2;
                    foo() = c;
                EndBody.

                Function: foo
                Body:
                    Return 2;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(CallExpr(Id("foo"),[]),Id("c"))))
        self.assertTrue(TestChecker.test(input,expect,435))
        
    def test_436(self):
        """Created automatically"""
        input = r"""
                Var: b;
                Function: main
                Body:
                    foo()[b + 2][3] = 3;
                    b = 5.2;
                    Return 3;
                EndBody.

                Function: foo
                Body:
                    Var: c[3];
                    Return c;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(ArrayCell(CallExpr(Id("foo"),[]),[BinaryOp("+",Id("b"),IntLiteral(2))]),[IntLiteral(3)]),IntLiteral(3))))
        self.assertTrue(TestChecker.test(input,expect,436))
        
    def test_437(self):
        """Created automatically"""
        input = r"""
                Var: x;
                Function: fact
                Parameter: n
                Body:
                    If n == 0 Then
                        Return 1;
                    Else
                        Return 4.4 *. 5.4;
                    EndIf.
                    Return 0;
                EndBody.

                Function: main
                Body:
                    x = 10;
                    x = fact(2.2);                    
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Return(BinaryOp("*.",FloatLiteral(4.4),FloatLiteral(5.4)))))
        self.assertTrue(TestChecker.test(input,expect,437))
        
    def test_438(self):
        """Created automatically"""
        input = r"""
                Var: x;
                Function: foo
                Parameter: a[5], b
                Body:
                    Var: i = 0;
                    While (i < 5) Do
                        a[i] = b +. 1.0;
                        i = i + 1;
                    EndWhile.
                    Return 2;
                EndBody.

                Function: main
                Body:
                    Var: c;
                    x = 10;
                    x = foo(c, 7);                    
                EndBody.
                """
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[Id("c"),IntLiteral(7)])))
        self.assertTrue(TestChecker.test(input,expect,438))
        
    def test_439(self):
        """Created automatically"""
        input = r"""
                Var: x;
                Function: foo
                Parameter: a[5], b
                Body:
                    Var: i = 0, f;
                    While (i < 5) Do
                        a[i] = b +. 1.0;
                        f = a[i] +. 5;
                        i = i + 1;
                    EndWhile.
                    Return 2;
                EndBody.

                Function: main
                Body:
                    Var: c;
                    x = 10;
                    x = foo(c, 7);                    
                EndBody.
                """
        expect = str(TypeMismatchInExpression(BinaryOp("+.",ArrayCell(Id("a"),[Id("i")]),IntLiteral(5))))
        self.assertTrue(TestChecker.test(input,expect,439))
        
    def test_440(self):
        """Created automatically"""
        input = r"""
                Var: x;
                Function: fact
                Parameter: n
                Body:
                    Var: a[2] ={3,4};
                    If n == 0 Then
                        Return 1;
                    Else
                        Return 2;
                    EndIf.
                    Return a;
                EndBody.
                
                Function: main
                Body:
                    Var: b[2] = {5.5};
                    x = 6.6;
                    b[2] = 5.5 +. x +. fact(4)[4];
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Return(Id("a"))))
        self.assertTrue(TestChecker.test(input,expect,440))
        
    def test_441(self):
        """Created automatically"""
        input = r"""
                Var: a[3][4], c, d=5.5;
                Function: main
                Body:
                    Var: b[2];
                    a[3 + 2.2][2][4] = d;
                    Return 1;
                EndBody.

                Function: foo
                Parameter: f[2]
                Body:
                    Return 6;
                EndBody.
                """
        expect = str(TypeMismatchInExpression(BinaryOp("+",IntLiteral(3),FloatLiteral(2.2))))
        self.assertTrue(TestChecker.test(input,expect,441))
        
    def test_442(self):
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
        expect = str(TypeMismatchInExpression(BinaryOp(">.",Id("a"),IntLiteral(2))))
        self.assertTrue(TestChecker.test(input,expect,442))
        
    def test_443(self):
        """Created automatically"""
        input = r"""
                Var: x;
                Function: main
                Body:
                    Var: a, b;
                    If bool_of_string("True") Then
                        a = int_of_string (read());
                        b = float_of_int (a) +. 2.0;
                    EndIf.
                    a = 2.2;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id("a"),FloatLiteral(2.2))))
        self.assertTrue(TestChecker.test(input,expect,443))
        
    def test_444(self):
        """Created automatically"""
        input = r"""
                Var: x;
            Function: main
            Body:
                Var: a, b;
                If bool_of_string("True") Then
                    a = int_of_string (read());
                    b = float_of_int (a) +. 2.0;
                EndIf.
                b =2 ;
            EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id("b"),IntLiteral(2))))
        self.assertTrue(TestChecker.test(input,expect,444))
        
    def test_445(self):
        """Created automatically"""
        input = r"""
                Var: x;
            Function: main
            Body:
                Var: a, b;
                x  = 3;
                If bool_of_string(x) Then
                    a = int_of_string (read());
                    b = float_of_int (a) +. 2.0;
                EndIf.
                b =2 ;
            EndBody.
                """
        expect = str(TypeMismatchInExpression(CallExpr(Id("bool_of_string"),[Id("x")])))
        self.assertTrue(TestChecker.test(input,expect,445))
        
    def test_446(self):
        """Created automatically"""
        input = r"""
                Var: x;
            Function: main
            Body:
                Var: a, b;
                x  = 3;
                If bool_of_string("True") Then
                    a = int_of_string (b);
                    b = float_of_int (a) +. 2.0;
                EndIf.
                b =2 ;
            EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id("b"),BinaryOp("+.",CallExpr(Id("float_of_int"),[Id("a")]),FloatLiteral(2.0)))))
        self.assertTrue(TestChecker.test(input,expect,446))
        
    def test_447(self):
        """Created automatically"""
        input = r"""
                Var: x;
                Function: main
                Body:
                    Var: a, b, c;
                    x  = 3;
                    If bool_of_string("True") Then
                        a = int_of_string (b);
                        c = float_of_int (a) +. 2.0;
                    EndIf.
                    b = c;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id("b"),Id("c"))))
        self.assertTrue(TestChecker.test(input,expect,447))
        
    def test_448(self):
        """Created automatically"""
        input = r"""
                Var: x;
                Function: main
                Body:
                    Var: a, b, c;
                    x  = 3;
                    If bool_of_string("True") Then
                        a = int_of_string (b);
                        c = float_of_int (a) +. 2.0;
                    EndIf.
                    b = "turong";
                    c = "sss";
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id("c"),StringLiteral("sss"))))
        self.assertTrue(TestChecker.test(input,expect,448))
        
    def test_449(self):
        """Created automatically"""
        input = r"""
                Var: x;
                Function: main
                Body:
                    Var: a, b, c;
                    x  = 3;
                    If bool_of_string("True") Then
                        a = int_of_string (b);
                        c = float_of_int (a) +. 2.0;
                    EndIf.
                    c = doo(b);
                EndBody.

                Function: doo
                Parameter: a
                Body:
                    a = "truong";
                    Return 2;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Return(IntLiteral(2))))
        self.assertTrue(TestChecker.test(input,expect,449))
        
    def test_450(self):
        """Created automatically"""
        input = r"""
                Var: x;
                Function: main
                Body:
                    Var: a, b, c;
                    x  = 3;
                    If bool_of_string("True") Then
                        a = int_of_string (b);
                        c = float_of_int (a) +. 2.0;
                    EndIf.
                    c = doo(a);
                EndBody.

                Function: doo
                Parameter: a
                Body:
                    a = "truong";
                    Return 2;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id("a"),StringLiteral("truong"))))
        self.assertTrue(TestChecker.test(input,expect,450))
        
    def test_451(self):
        """Created automatically"""
        input = r"""
                Var: x;
                Function: main
                Body:
                    Var: a, b, c;
                    x  = 3;
                    If bool_of_string("True") Then
                        a = int_of_string (b);
                        c = float_of_int (a) +. 2.0;
                    EndIf.
                    c = doo(a, b);
                EndBody.

                Function: doo
                Parameter: a
                Body:
                    a = "truong";
                    Return 2;
                EndBody.
                """
        expect = str(TypeMismatchInExpression(CallExpr(Id("doo"),[Id("a"),Id("b")])))
        self.assertTrue(TestChecker.test(input,expect,451))
        
    def test_452(self):
        """Created automatically"""
        input = r"""
                Var: x[2];
                Function: main
                Body:
                    Var: a = 3;
                    x[2 + 3*2.2] = a + foo(123)*a_2; 
                EndBody.
                """
        expect = str(TypeMismatchInExpression(BinaryOp("*",IntLiteral(3),FloatLiteral(2.2))))
        self.assertTrue(TestChecker.test(input,expect,452))
        
    def test_453(self):
        """Created automatically"""
        input = r"""
                Var: x[2];
                Function: main
                Body:
                    Var: a = 3;
                    x[2 + a] = 4;
                    x[2] = 5.5;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id("x"),[IntLiteral(2)]),FloatLiteral(5.5))))
        self.assertTrue(TestChecker.test(input,expect,453))
        
    def test_454(self):
        """Created automatically"""
        input = r"""
                Var: x[2];
                Function: main
                Body:
                    Var: a = 3;
                    x[2 + a] = 4;
                    x[2] = "true";
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id("x"),[IntLiteral(2)]),StringLiteral("true"))))
        self.assertTrue(TestChecker.test(input,expect,454))
        
    def test_455(self):
        """Created automatically"""
        input = r"""
                Var: x[2];
                Function: main
                Body:
                    Var: a = 3;
                    x[2 + a] = 4;
                    x[2] = True;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id("x"),[IntLiteral(2)]),BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect,455))
        
    def test_456(self):
        """Created automatically"""
        input = r"""
                Var: x[2];
                Function: main
                Body:
                    Var: a;
                    a = x[2] + 2;
                    x[2] = 2.2;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id("x"),[IntLiteral(2)]),FloatLiteral(2.2))))
        self.assertTrue(TestChecker.test(input,expect,456))
        
    def test_457(self):
        """Created automatically"""
        input = r"""
                Var: x[2];
                Function: main
                Body:
                    Var: a, c;
                    a = x[2] + 2;
                    x[2][c] = 5;
                    c = 5.5;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id("c"),FloatLiteral(5.5))))
        self.assertTrue(TestChecker.test(input,expect,457))
        
    def test_458(self):
        """Created automatically"""
        input = r"""
                Var: x[2];
                Function: main
                Body:
                    Var: a, c;
                    a = x[2] + 2;
                    x[2][c + 2] = 5;
                    c = 6 + int_of_float(5.5);
                    c = True;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id("c"),BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect,458))
        
    def test_459(self):
        """Created automatically"""
        input = r"""
                Var: x[2];
                Function: main
                Body:
                    Var: a, c, d;
                    a = x[2] + 2;
                    x[2][d] = 5;
                    c = 6 + int_of_float(5.5);
                    c = doo(d) + 2.3;
                EndBody.

                Function: doo
                Parameter: s
                Body:
                    Return 0;
                EndBody.
                """
        expect = str(TypeMismatchInExpression(BinaryOp("+",CallExpr(Id("doo"),[Id("d")]),FloatLiteral(2.3))))
        self.assertTrue(TestChecker.test(input,expect,459))
        
    def test_460(self):
        """Created automatically"""
        input = r"""
                Var: x[2], a[2];
                Function: main
                Body:
                    Var: b[2];
                    a[3 + foo(2)] = a[b[2][3]] + 4;
                    b[3] = 4.4;
                EndBody.

                Function: foo
                Parameter: a
                Body:
                    a = 2;
                    Return a;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id("b"),[IntLiteral(3)]),FloatLiteral(4.4))))
        self.assertTrue(TestChecker.test(input,expect,460))
        
    def test_461(self):
        """Created automatically"""
        input = r"""
                Var: x[2], a[2];
                Function: main
                Body:
                    Var: b[2];
                    a[3 + foo(2)] = b[2] + 4;
                    b[3] = 4.4;
                EndBody.

                Function: foo
                Parameter: a
                Body:
                    a = 2;
                    Return a;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id("b"),[IntLiteral(3)]),FloatLiteral(4.4))))
        self.assertTrue(TestChecker.test(input,expect,461))
        
    def test_462(self):
        """Created automatically"""
        input = r"""
                Var: x[2], a[2];
                Function: main
                Body:
                    Var: b[2];
                    a[3 + foo(2)] = b[2] + 4;
                    b[3] = foo(a[3]);
                    foo(a[3]) = 4;
                EndBody.

                Function: foo
                Parameter: a
                Body:
                    a = 2;
                    Return a;
                EndBody.
                """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,462))
        
    def test_463(self):
        """Created automatically"""
        input = r"""
                Var: x[2], a[2];
                Function: main
                Body:
                    Var: b[2];
                    a[3 + foo(2)] = b[2] + 4;
                    b[3] = foo(a[3]);
                    foo(a[3]) = 4;
                EndBody.
                """
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,463))
        
    def test_464(self):
        """Created automatically"""
        input = r"""
                Var: x[2], a[2];
                Function: main
                Body:
                    Var: b[2];
                    a[3 + foo(2)] = b[2] + 4;
                    b[3] = foo(a[3]);
                    doo();
                EndBody.

                Function: doo
                Parameter: a, b, c
                Body:
                    a = 5;
                    b = 6;
                    c = 5.5;
                    c = a + b;
                    Return;
                EndBody.
                """
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,464))
        
    def test_465(self):
        """Created automatically"""
        input = r"""
                Var: x[2], a[2];
                Function: main
                Body:
                    Var: b[2];
                    doo(1,3 ,5.5);
                EndBody.
                """
        expect = str(Undeclared(Function(),"doo"))
        self.assertTrue(TestChecker.test(input,expect,465))
        
    def test_466(self):
        """Created automatically"""
        input = r"""
                Var: x[2], a[2];
                Function: main
                Body:
                    Var: b[2];
                    doo(1,3 ,5.5);
                EndBody.

                Function: doo
                Parameter: b, c, d
                Body:
                    Var: e;
                    b = 5;
                    c = 6;
                    d = 5.5;
                    e = "5.3";
                    c = float_of_int(b) +. float_of_int(c) +. float_of_string(e);
                    Return;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id("c"),BinaryOp("+.",BinaryOp("+.",CallExpr(Id("float_of_int"),[Id("b")]),CallExpr(Id("float_of_int"),[Id("c")])),CallExpr(Id("float_of_string"),[Id("e")])))))
        self.assertTrue(TestChecker.test(input,expect,466))
        
    def test_467(self):
        """Created automatically"""
        input = r"""
                Var: x[2], a[2];
                Function: main
                Body:
                    Var: b[2], d = 4;
                    d = doo(1,3 ,5.5);
                EndBody.

                Function: doo
                Parameter: b, c, d
                Body:
                    Var: e, g;
                    b = 5;
                    c = 6;
                    d = 5.5;
                    e = "5.3";
                    g = float_of_int(b) +. float_of_int(c) +. float_of_string(e);
                    Return g;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Return(Id("g"))))
        self.assertTrue(TestChecker.test(input,expect,467))
        
    def test_468(self):
        """Created automatically"""
        input = r"""
                Var: x[2], a[2];
                Function: main
                Body:
                    Var: b[2], d = 4;
                    d = doo(1,3 ,d);
                EndBody.

                Function: doo
                Parameter: b, c, d
                Body:
                    Var: e, g;
                    b = 5;
                    c = 6;
                    d = 5.5;
                    e = "5.3";
                    g = float_of_int(b) +. float_of_int(c) +. float_of_string(e);
                    Return g;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id("d"),FloatLiteral(5.5))))
        self.assertTrue(TestChecker.test(input,expect,468))
        
    def test_469(self):
        """Created automatically"""
        input = r"""
                Var: x[2], a[2];
                Function: main
                Body:
                    Var: b[2], d = 4;
                    d = doo(1,3 ,d);
                EndBody.

                Function: doo
                Parameter: b, c, d
                Body:
                    Var: e, g;
                    b = 5;
                    c = 6;
                    d = 5.5;
                    e = "5.3";
                    g = float_of_int(b) +. float_of_int(c + 3.5) +. float_of_string(e);
                    Return g;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id("d"),FloatLiteral(5.5))))
        self.assertTrue(TestChecker.test(input,expect,469))
        
    def test_470(self):
        """Created automatically"""
        input = r"""
                Var: x[2] = {2}, a = -2;
                Function: main
                Parameter: a
                Body:
                    Var: a;
                    a = 5;
                EndBody.
                """
        expect = str(Redeclared(Variable(),"a"))
        self.assertTrue(TestChecker.test(input,expect,470))
        
    def test_471(self):
        """Created automatically"""
        input = r"""
                Var: x[2] = {2}, a = -2;
                Function: main
                Parameter: a
                Body:
                    a = True;
                    If a Then
                        Return 5;
                    Else
                        b = a;
                    EndIf.
                    Return a;
                EndBody.
                """
        expect = str(Undeclared(Identifier(),"b"))
        self.assertTrue(TestChecker.test(input,expect,471))
        
    def test_472(self):
        """Created automatically"""
        input = r"""
                Var: x[2] = {2}, a = -2;
                Function: main
                Parameter: a
                Body:
                    a = True;
                    If a Then
                        Return 5;
                    Else
                        Var: b;
                        b = a;
                    EndIf.
                    Return b;
                EndBody.
                """
        expect = str(Undeclared(Identifier(),"b"))
        self.assertTrue(TestChecker.test(input,expect,472))
        
    def test_473(self):
        """Created automatically"""
        input = r"""
                Var: x[2] = {2}, a = -2;
                Function: main
                Parameter: a
                Body:
                    a = True;
                    If a Then
                        Var: c = 5;
                        Return 5;
                    Else
                        Var: b;
                        b = a;
                    EndIf.
                    c = 5;
                    Return b;
                EndBody.
                """
        expect = str(Undeclared(Identifier(),"c"))
        self.assertTrue(TestChecker.test(input,expect,473))
        
    def test_474(self):
        """Created automatically"""
        input = r"""
                Var: x[2] = {2}, a = -2;
                Function: main
                Body:
                    a = doo(x[2], 3.3);
                EndBody.

                Function: doo
                Parameter: a, b
                Body:
                    Return a + b;
                EndBody.
                """
        expect = str(TypeMismatchInExpression(BinaryOp("+",Id("a"),Id("b"))))
        self.assertTrue(TestChecker.test(input,expect,474))
        
    def test_475(self):
        """Created automatically"""
        input = r"""
                Function: foo
                Parameter: a[5], b
                Body:
                    Var: i = 0;
                    While (i < 5) Do
                        a[i] = b +. 1.0;
                        i = i + 1;
                    EndWhile.
                    Return i;
                EndBody.

                Function: main
                Body:
                    Var: a, b[2];
                    a = foo(b[3], 3.3);
                    a = 5.5;
                    Return 5;
                EndBody.

                """
        expect = str(TypeMismatchInStatement(Assign(Id("a"),FloatLiteral(5.5))))
        self.assertTrue(TestChecker.test(input,expect,475))
        
    def test_476(self):
        """Created automatically"""
        input = r"""
                Function: foo
                Parameter: a[5], b
                Body:
                    Var: i = 0;
                    While (i < 5) Do
                        a[i] = b +. 1.0;
                        i = i + 1;
                    EndWhile.
                    Return i*foo(a[3], b);
                EndBody.

                Function: main
                Body:
                    Var: a, b[2];
                    a = foo(b[3], 3.3);
                    a = 5*foo(b[3], a);
                    Return 5;
                EndBody.
                """
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[ArrayCell(Id("b"),[IntLiteral(3)]),Id("a")])))
        self.assertTrue(TestChecker.test(input,expect,476))
        
    def test_477(self):
        """Created automatically"""
        input = r"""
                Function: foo
                Parameter: a[5], b
                Body:
                    Var: i = 0;
                    While (i < 5) Do
                        a[i] = b +. 1.0;
                        i = i + 1;
                    EndWhile.
                    Return i*foo(a[3], b);
                EndBody.

                Function: main
                Body:
                    Var: a, b[2];
                    a = foo(b[3], 3.3);
                    a = 5*.foo(b[3], 5.5);
                    Return 5;
                EndBody.
                """
        expect = str(TypeMismatchInExpression(BinaryOp("*.",IntLiteral(5),CallExpr(Id("foo"),[ArrayCell(Id("b"),[IntLiteral(3)]),FloatLiteral(5.5)]))))
        self.assertTrue(TestChecker.test(input,expect,477))
        
    def test_478(self):
        """Created automatically"""
        input = r"""
                Var: a = 5;
                Function: main
                Body:
                    Var: r = 10., v;
                    v = (4. \. 3.) *. 3.14 *. r *. r * r;
                EndBody.
                """
        expect = str(TypeMismatchInExpression(BinaryOp("*",BinaryOp("*.",BinaryOp("*.",BinaryOp("*.",BinaryOp("\.",FloatLiteral(4.0),FloatLiteral(3.0)),FloatLiteral(3.14)),Id("r")),Id("r")),Id("r"))))
        self.assertTrue(TestChecker.test(input,expect,478))
        
    def test_479(self):
        """Created automatically"""
        input = r"""
                Var: a = 5;
                Function: main
                Body:
                    Var: r = 10., v, d;
                    v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                    d = doo(r, r);
                    d = 2;
                EndBody.

                Function: doo
                Parameter: b, c
                Body:
                    b = c;
                    Return c;
                EndBody.
                """
        expect = str(TypeCannotBeInferred(Assign(Id("d"),CallExpr(Id("doo"),[Id("r"),Id("r")]))))
        self.assertTrue(TestChecker.test(input,expect,479))
        
    def test_480(self):
        """Created automatically"""
        input = r"""
                Var: a = 5;
                Function: main
                Body:
                    Var: r = 10., v, d;
                    v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                    d = doo(r*2, r);
                    d = 2;
                EndBody.

                Function: doo
                Parameter: b, c
                Body:
                    b = c;
                    Return c;
                EndBody.
                """
        expect = str(TypeMismatchInExpression(BinaryOp("*",Id("r"),IntLiteral(2))))
        self.assertTrue(TestChecker.test(input,expect,480))
        
    def test_481(self):
        """Created automatically"""
        input = r"""
                Var: a = 5;
                Function: main
                Body:
                    Var: r = 10., v, d;
                    v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                    d = doo(r, r);
                    d = 2;
                EndBody.

                Function: doo
                Parameter: b, c
                Body:
                    b = c;
                    Return f;
                EndBody.
                """
        expect = str(TypeCannotBeInferred(Assign(Id("d"),CallExpr(Id("doo"),[Id("r"),Id("r")]))))
        self.assertTrue(TestChecker.test(input,expect,481))
        
    def test_482(self):
        """Created automatically"""
        input = r"""
                Var: a = 5, f;
                Function: main
                Body:
                    Var: r = 10., v, d;
                    v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                    d = doo(r, r);
                    d = 2;
                EndBody.

                Function: doo
                Parameter: b, c
                Body:
                    b = c;
                    Return f;
                EndBody.
                """
        expect = str(TypeCannotBeInferred(Assign(Id("d"),CallExpr(Id("doo"),[Id("r"),Id("r")]))))
        self.assertTrue(TestChecker.test(input,expect,482))
        
    def test_483(self):
        """Created automatically"""
        input = r"""
                Var: a = 5, f;
                Function: main
                Body:
                    Var: r = 10., v, d;
                    v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                    For( i = 5 , True, 5) Do
                        f = read();
                    EndFor.
                    f = 5;
                EndBody.
                """
        expect = str(Undeclared(Identifier(),"i"))
        self.assertTrue(TestChecker.test(input,expect,483))
        
    def test_484(self):
        """Created automatically"""
        input = r"""
                Var: a = 5, f;
                Function: main
                Body:
                    Var: r = 10., v, d;
                    v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                    For( i = 5 , bool_of_string("True"), 5) Do
                        f = read();
                    EndFor.
                    d = 5;
                    f = string_of_float(d);
                EndBody.
                """
        expect = str(Undeclared(Identifier(),"i"))
        self.assertTrue(TestChecker.test(input,expect,484))
        
    def test_485(self):
        """Created automatically"""
        input = r"""
                Var: a = 5, f;
                Function: main
                Body:
                    Var: r = 10., v, d;
                    v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                    For( i = 5 , bool_of_string("True"), 5) Do
                        f = read();
                    EndFor.
                    d = 5;
                    f = string_of_float(v) *. 4;
                EndBody.
                """
        expect = str(Undeclared(Identifier(),"i"))
        self.assertTrue(TestChecker.test(input,expect,485))
        
    def test_486(self):
        """Created automatically"""
        input = r"""
                Var: a = 5, f;
                Function: main
                Body:
                    Var: r = 10., v, d;
                    printLn() = "truong";
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(CallExpr(Id("printLn"),[]),StringLiteral("truong"))))
        self.assertTrue(TestChecker.test(input,expect,486))
        
    def test_487(self):
        """Created automatically"""
        input = r"""
                Var: a = 5, f;
                Function: main
                Body:
                    Var: r = 10., v, d;
                    printStrLn(v);
                    v = 5;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id("v"),IntLiteral(5))))
        self.assertTrue(TestChecker.test(input,expect,487))
        
    def test_488(self):
        """Created automatically"""
        input = r"""
                Var: a = 5, f;
                Function: main
                Body:
                    Var: r = 10., v = True, d;
                    d = string_of_bool(v);
                    v = d;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id("v"),Id("d"))))
        self.assertTrue(TestChecker.test(input,expect,488))
        
    def test_489(self):
        """Created automatically"""
        input = r"""
                Var: a = 5, f;
                Function: main
                Body:
                    Var: r = 10., v = "45", d;
                    d = float_of_string(v);
                    f = (r == d);
                EndBody.
                """
        expect = str(TypeMismatchInExpression(BinaryOp("==",Id("r"),Id("d"))))
        self.assertTrue(TestChecker.test(input,expect,489))
        
    def test_490(self):
        """Created automatically"""
        input = r"""
                Var: a = 5, f;
                Function: main
                Body:
                    Var: r = 10., v = "45", d;
                    d = float_of_string(v);
                    f = (r =/= d);
                    d = string_of_bool(f);
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id("d"),CallExpr(Id("string_of_bool"),[Id("f")]))))
        self.assertTrue(TestChecker.test(input,expect,490))
        
    def test_491(self):
        """Created automatically"""
        input = r"""
                Var: a = 5, f;
                Function: main
                Body:
                    Var: r = 10., v = "45", d;
                    d = float_of_string(v);
                    f = (r != !d) ;
                    d = string_of_bool(f);
                EndBody.
                """
        expect = str(TypeMismatchInExpression(UnaryOp("!",Id("d"))))
        self.assertTrue(TestChecker.test(input,expect,491))
        
    def test_492(self):
        """Created automatically"""
        input = r"""
                Var: x,z, x[2];
                """
        expect = str(Redeclared(Variable(),"x"))
        self.assertTrue(TestChecker.test(input,expect,492))
        
    def test_493(self):
        """Created automatically"""
        input = r"""
                Var: a;
                Function: main
                Body:
                    a = 2.3;
                EndBody.

                Function: doo
                Body:
                    a = 5;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id("a"),IntLiteral(5))))
        self.assertTrue(TestChecker.test(input,expect,493))
        
    def test_494(self):
        """Created automatically"""
        input = r"""
                Var: a;
                Function: main
                Body:
                    a = True;
                EndBody.

                Function: doo
                Body:
                    a = 5;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id("a"),IntLiteral(5))))
        self.assertTrue(TestChecker.test(input,expect,494))
        
    def test_495(self):
        """Created automatically"""
        input = r"""
                Var: a;
                Function: main
                Body:
                    While a >. 2.3 Do
                        a = 2 * 2;
                    EndWhile.
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id("a"),BinaryOp("*",IntLiteral(2),IntLiteral(2)))))
        self.assertTrue(TestChecker.test(input,expect,495))
        
    def test_496(self):
        """Created automatically"""
        input = r"""
                Var: a;
                Function: main
                Body:
                    While a >. 2.3 Do
                        Return c;
                    EndWhile.
                EndBody.
                """
        expect = str(Undeclared(Identifier(),"c"))
        self.assertTrue(TestChecker.test(input,expect,496))
        
    def test_497(self):
        """Created automatically"""
        input = r"""
                Var: a;
                Function: main
                Body:
                    While a >. 2.3 Do
                        Return a*foo(2);
                    EndWhile.
                EndBody.
                """
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,497))
        
    def test_498(self):
        """Created automatically"""
        input = r"""
                Var: x;
                Function: main
                Body:
                    x = 2;
                EndBody.

                Function: doo
                Body:
                    Var: a;
                    a = doo1();
                EndBody.

                Function: doo1
                Body:
                    Return 1;
                EndBody.
                """
        expect = str(TypeCannotBeInferred(Assign(Id("a"),CallExpr(Id("doo1"),[]))))
        self.assertTrue(TestChecker.test(input,expect,498))
        
    def test_499(self):
        """Created automatically"""
        input = r"""
                Var: x;
                Function: main
                Body:
                    x = doo();
                EndBody.

                Function: doo
                Body:
                    Var: a;
                    a = doo1();
                    Return 33;
                EndBody.
                """
        expect = str(TypeCannotBeInferred(Assign(Id("x"),CallExpr(Id("doo"),[]))))
        self.assertTrue(TestChecker.test(input,expect,499))
        
    def test_500(self):
        """Created automatically"""
        input = r"""
                Var: a = "Truong", b = "Dep", c = "Trai";
                Function: main
                Body:
                    a = b + c;
                EndBody.
                """
        expect = str(TypeMismatchInExpression(BinaryOp("+",Id("b"),Id("c"))))
        self.assertTrue(TestChecker.test(input,expect,500))
        
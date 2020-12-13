import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):

    def test_401(self):
        """Created automatically"""
        input = r"""
            
            """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,401))
        
    def test_402(self):
        """Created automatically"""
        input = r"""

                Function: main
                Body:
                    x=1;
                EndBody.    
            """
        expect = str(Undeclared(Identifier(),"x"))
        self.assertTrue(TestChecker.test(input,expect,402))
        
    def test_403(self):
        """Created automatically"""
        input = r"""

                Function: main
                Parameter:x
                Body:
                    x=1;
                    x=1.6;
                EndBody.
            """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),FloatLiteral(1.6))))
        self.assertTrue(TestChecker.test(input,expect,403))
        
    def test_404(self):
        """Created automatically"""
        input = r"""
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
        self.assertTrue(TestChecker.test(input,expect,404))
        
    def test_405(self):
        """Created automatically"""
        input = r"""
                Function: foo
                Parameter: x
                Body:
                EndBody.
                Function: main
                Body:
                    Var: x, y = 0.5;
                    foo(x);
                EndBody.
            """
        expect = str(TypeCannotBeInferred(CallStmt(Id("foo"),[Id("x")])))
        self.assertTrue(TestChecker.test(input,expect,405))
        
    def test_406(self):
        """Created automatically"""
        input = r"""

                Function: main
                Body:

                EndBody.
            """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,406))
        
    def test_407(self):
        """Created automatically"""
        input = r"""
            Function: main 
            Parameter: x,y
            Body:
                x = 1; 
                main( 1.1, 0); 
            EndBody.
            """
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[FloatLiteral(1.1),IntLiteral(0)])))
        self.assertTrue(TestChecker.test(input,expect,407))
        
    def test_408(self):
        """Created automatically"""
        input = r"""
            Function: foo 
            Parameter: x,y
            Body:
            EndBody.
            Function: main
            Parameter: x,y
            Body:
                foo(1,2);  
                foo(1. , 2.); 
            EndBody.
            """
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[FloatLiteral(1.0),FloatLiteral(2.0)])))
        self.assertTrue(TestChecker.test(input,expect,408))
        
    def test_409(self):
        """Created automatically"""
        input = r"""
            Function: main
            Parameter: x,y
            Body:
                y=0.5;
                For(x=1,x==1,x+1) Do
                EndFor.
                For(y=1,y==1,y+1) Do
                EndFor.
            EndBody.    
            """
        expect = str(TypeMismatchInStatement(For(Id("y"),IntLiteral(1),BinaryOp("==",Id("y"),IntLiteral(1)),BinaryOp("+",Id("y"),IntLiteral(1)),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,409))
        
    def test_410(self):
        """Created automatically"""
        input = r"""
            Function: main 
            Parameter: x
            Body:
                Var: y = 1; 
                x = 1.0; 
                main(y); 
            EndBody.
            """
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[Id("y")])))
        self.assertTrue(TestChecker.test(input,expect,410))
        
    def test_411(self):
        """Created automatically"""
        input = r"""
            Function: main 
            Parameter: x
            Body:
                Var: y = 1; 
                main(y); 
                x = 1.0; 
            EndBody.
            """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),FloatLiteral(1.0))))
        self.assertTrue(TestChecker.test(input,expect,411))
        
    def test_412(self):
        """Created automatically"""
        input = r"""Function: main 
                    Body:
                        printStrLn(read(4));
                    EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,412))
        
    def test_413(self):
        """Created automatically"""
        input = Program([FuncDecl(Id("main"),[],([],[CallStmt(Id("printStrLn"),[CallExpr(Id("read"),[IntLiteral(4)])])]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,413))
        
    def test_414(self):
        """Created automatically"""
        input = r"""Function: main  
                   Body:
                        printStrLn();
                    EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,414))
        
    def test_415(self):
        """Created automatically"""
        input = Program([FuncDecl(Id("main"),[],([],[CallStmt(Id("printStrLn"),[])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,415))
        
    def test_416(self):
        """Created automatically"""
        input = Program([FuncDecl(Id("main"),[],([],[CallExpr(Id("foo"),[])]))])
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,416))
        
    def test_417(self):
        """Created automatically"""
        input = r"""
                
                Function: main
                Parameter: x,y,z,t,k
                Body:
                    y= x + y \ z * t;
                    x= k % t;
                    y= x == z;
                EndBody.
            """
        expect = str(TypeMismatchInStatement(Assign(Id("y"),BinaryOp("==",Id("x"),Id("z")))))
        self.assertTrue(TestChecker.test(input,expect,417))
        
    def test_418(self):
        """Created automatically"""
        input = r"""

                Function: main
                Parameter: x,y,z,t
                Body:
                    x= !y;
                    z= z && t;
                    x=z;
                EndBody.
            """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,418))
        
    def test_419(self):
        """Created automatically"""
        input = r"""
                Var: a[1][2]= {{1,2}};
                Function: main
                Parameter: x
                Body:
                    a[1][2] = x;
                EndBody.
            """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,419))
        
    def test_420(self):
        """Created automatically"""
        input = r"""                
                Function: main
                Body:
                    Var:a[5]= {1,2,3,4,5};
                    Var:b[5];
                    a=b;
                    a[5]=b;
                EndBody.
            """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id("a"),[IntLiteral(5)]),Id("b"))))
        self.assertTrue(TestChecker.test(input,expect,420))
        
    def test_421(self):
        """Created automatically"""
        input = r"""
                
                Function: main
                Body:
                    Var:a[5]= {1,2,3,4,5};
                    Var:b[5];
                    b={1.,2.,3.,4.,5.};
                    a=b;
                EndBody.
            """
        expect = str(TypeMismatchInStatement(Assign(Id("a"),Id("b"))))
        self.assertTrue(TestChecker.test(input,expect,421))
        
    def test_422(self):
        """Created automatically"""
        input = r"""               
                Function: main
                Body:
                    Var:a[5]= {1,2,3,4,5};
                    Var:b[4]= {1,2,3,4};
                    a=b;
                EndBody.
            """
        expect = str(TypeMismatchInStatement(Assign(Id("a"),Id("b"))))
        self.assertTrue(TestChecker.test(input,expect,422))
        
    def test_423(self):
        """Created automatically"""
        input = r"""             
                Function: main
                Body:
                    Var:a[5]= {1,2,3,4,5};
                    Var:b[5];
                    Var:c;
                    c = b[5] +. 1;
                    a=b; 
                EndBody.
            """
        expect = str(TypeMismatchInExpression(BinaryOp("+.",ArrayCell(Id("b"),[IntLiteral(5)]),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,423))
        
    def test_424(self):
        """Created automatically"""
        input = r"""                
                Function: main
                Body:
                    Var:a[5],b[5];
                    a=b;
                EndBody.
            """
        expect = str(TypeCannotBeInferred(Assign(Id("a"),Id("b"))))
        self.assertTrue(TestChecker.test(input,expect,424))
        
    def test_425(self):
        """Created automatically"""
        input = r"""                
                Var: x[5]={1,2};
                Var: x=1;
                Function: main
                Body:
                EndBody.            
        """
        expect = str(Redeclared(Variable(),"x"))
        self.assertTrue(TestChecker.test(input,expect,425))
        
    def test_426(self):
        """Created automatically"""
        input = r"""
                Var:x;
                Function: main
                Body:
                    Var:x;
                    Var:main;
                    Var:x[5]={1,2,3,4,5};
                EndBody.
            """
        expect = str(Redeclared(Variable(),"x"))
        self.assertTrue(TestChecker.test(input,expect,426))
        
    def test_427(self):
        """Created automatically"""
        input = r"""
                Function: main
                Body:
                EndBody.
                Function: main
                Parameter: x
                Body:

                EndBody.
            """
        expect = str(Redeclared(Function(),"main"))
        self.assertTrue(TestChecker.test(input,expect,427))
        
    def test_428(self):
        """Created automatically"""
        input = r"""
                
                Function: main
                Parameter: x
                Body:
                    Var:x;
                EndBody.
            """
        expect = str(Redeclared(Variable(),"x"))
        self.assertTrue(TestChecker.test(input,expect,428))
        
    def test_429(self):
        """Created automatically"""
        input = r"""
                
                Function: main
                Parameter: x,x
                Body:

                EndBody.
            """
        expect = str(Redeclared(Parameter(),"x"))
        self.assertTrue(TestChecker.test(input,expect,429))
        
    def test_430(self):
        """Created automatically"""
        input = r"""
                Var:x;
                Function: main
                Parameter: x
                Body:
                    x=foo;
                EndBody.
            """
        expect = str(Undeclared(Identifier(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,430))
        
    def test_431(self):
        """Created automatically"""
        input = r"""               
                Function: main
                Body:
                    foo();
                EndBody.
            """
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,431))
        
    def test_432(self):
        """Created automatically"""
        input = r"""
                Function: main
                Parameter: x,y,a
                Body:
                    y = a +foo(x);
                EndBody.

                Function: foo
                Parameter: x
                Body:

                EndBody.
            """
        expect = str(TypeCannotBeInferred(Assign(Id("y"),BinaryOp("+",Id("a"),CallExpr(Id("foo"),[Id("x")])))))
        self.assertTrue(TestChecker.test(input,expect,432))
        
    def test_433(self):
        """Created automatically"""
        input = r"""
                
                Function: main
                Body:
                    Var: x,y;
                    x=y;
                EndBody.
            """
        expect = str(TypeCannotBeInferred(Assign(Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,433))
        
    def test_434(self):
        """Created automatically"""
        input = r"""
                
                Function: main
                Body:
                    Var:x;
                    If (foo(x)) Then
                        x=1;
                    EndIf.
                EndBody.
                Function: foo
                Parameter: x
                Body:
                EndBody.

            """
        expect = str(TypeCannotBeInferred(If([(CallExpr(Id("foo"),[Id("x")]),[],[Assign(Id("x"),IntLiteral(1))])],([],[]))))
        self.assertTrue(TestChecker.test(input,expect,434))
        
    def test_435(self):
        """Created automatically"""
        input = r"""
                Function: foo
                Parameter: x,y
                Body:
                EndBody.

                Function: main
                Body:
                    Var:x=1,y;
                    foo(x,y);
                EndBody.
            """
        expect = str(TypeCannotBeInferred(CallStmt(Id("foo"),[Id("x"),Id("y")])))
        self.assertTrue(TestChecker.test(input,expect,435))
        
    def test_436(self):
        """Created automatically"""
        input = r"""
                
                Function: main
                Body:
                    Var:x;
                    x = 1 + foo(x);
                EndBody.               
                Function: foo
                Parameter: x
                Body:

                EndBody.

            """
        expect = str(TypeCannotBeInferred(Assign(Id("x"),BinaryOp("+",IntLiteral(1),CallExpr(Id("foo"),[Id("x")])))))
        self.assertTrue(TestChecker.test(input,expect,436))
        
    def test_437(self):
        """Created automatically"""
        input = r"""
                
                Function: main
                Body:
                    Var:x;
                    If x Then
                        Var:y;
                    EndIf.
                EndBody.
            """
        expect = str(TypeCannotBeInferred(If([(Id("x"),[VarDecl(Id("y"),[],None)],[])],([],[]))))
        #self.assertTrue(TestChecker.test(input,expect,437))
        
    def test_438(self):
        """Created automatically"""
        input = r"""
                
                Function: main
                Body:
                    Var:x;
                    If x Then
                        x=1;
                    Else
                        Var:y,z;
                        y=x;
                    EndIf.
                EndBody.
            """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,438))
        
    def test_439(self):
        """Created automatically"""
        input = r"""
                Function: main
                Body:
                    Var: x;
                    For (x = 1 , 1==1 , 1) Do
                    EndFor.
                EndBody.

                Function: foo
                Parameter: x
                Body:

                EndBody.
            """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,439))
        
    def test_440(self):
        """Created automatically"""
        input = r"""                
                Function: main
                Body:
                    Var: x;
                    For (x=1, x>1 , x+1) Do
                        Var:y;
                    EndFor.
                EndBody.

            """
        expect = str(TypeCannotBeInferred(For(Id("x"),IntLiteral(1),BinaryOp(">",Id("x"),IntLiteral(1)),BinaryOp("+",Id("x"),IntLiteral(1)),([VarDecl(Id("y"),[],None)],[]))))
        #self.assertTrue(TestChecker.test(input,expect,440))
        
    def test_441(self):
        """Created automatically"""
        input = r"""
                Function: main
                Body:
                    Var: x;
                    While (foo(x))
                    Do
                        x=1;
                    EndWhile.
                EndBody.
                
                Function: foo
                Parameter: x
                Body:

                EndBody.
            """
        expect = str(TypeCannotBeInferred(While(CallExpr(Id("foo"),[Id("x")]),([],[Assign(Id("x"),IntLiteral(1))]))))
        self.assertTrue(TestChecker.test(input,expect,441))
        
    def test_442(self):
        """Created automatically"""
        input = r"""
                Function: main
                Body:
                    Var: x,y;
                    While (x)
                    Do
                        Var:z;
                        y=1;
                    EndWhile.
                EndBody.
            """
        expect = str(TypeCannotBeInferred(While(Id("x"),([VarDecl(Id("z"),[],None)],[Assign(Id("y"),IntLiteral(1))]))))
        #self.assertTrue(TestChecker.test(input,expect,442))
        
    def test_443(self):
        """Created automatically"""
        input = r"""                
                Function: main
                Parameter: x
                Body:
                    x= 1+foo(1);
                    foo(1);
                EndBody.
                Function: foo
                Parameter: x
                Body:
                EndBody.

            """
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input,expect,443))
        
    def test_444(self):
        """Created automatically"""
        input = r"""
                Function: main
                Parameter: x
                Body:
                    foo(1);
                    x= 1+foo(1);
                EndBody.
                Function: foo
                Parameter: x
                Body:
                EndBody.
            """
        expect = str(TypeMismatchInExpression(BinaryOp("+",IntLiteral(1),CallExpr(Id("foo"),[IntLiteral(1)]))))
        self.assertTrue(TestChecker.test(input,expect,444))
        
    def test_445(self):
        """Created automatically"""
        input = r"""
                Function: foo
                Parameter: x
                Body:
                EndBody.
                Function: main
                Body:
                    Var:x,y;
                    x= y + foo(1,2);
                EndBody.
            """
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[IntLiteral(1),IntLiteral(2)])))
        self.assertTrue(TestChecker.test(input,expect,445))
        
    def test_446(self):
        """Created automatically"""
        input = r"""
                
                Function: main
                Body:
                    Var:x;
                    Do
                        Var:y;
                    While x
                    EndDo.
                EndBody.
            """
        expect = str(TypeCannotBeInferred(Dowhile(([VarDecl(Id("y"),[],None)],[]),Id("x"))))
        #self.assertTrue(TestChecker.test(input,expect,446))
        
    def test_447(self):
        """Created automatically"""
        input = r"""
                
                Function: main
                Body:
                    Var:x=1;
                    If x Then
                    EndIf.
                EndBody.
            """
        expect = str(TypeMismatchInStatement(If([(Id("x"),[],[])],([],[]))))
        self.assertTrue(TestChecker.test(input,expect,447))
        
    def test_448(self):
        """Created automatically"""
        input = r"""
                Function: main
                Body:
                    Var: x=1.5;
                    For (x = !True, x>1 , 0+1) Do
                    EndFor.
                EndBody.
            """
        expect = str(TypeMismatchInStatement(For(Id("x"),UnaryOp("!",BooleanLiteral(True)),BinaryOp(">",Id("x"),IntLiteral(1)),BinaryOp("+",IntLiteral(0),IntLiteral(1)),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,448))
        
    def test_449(self):
        """Created automatically"""
        input = r"""
                Function: main
                Body:
                    Var: x,y=0.5;
                    For (x=1, x>1 , y +. 1) Do
                    EndFor.
                EndBody.
            """
        expect = str(TypeMismatchInExpression(BinaryOp("+.",Id("y"),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,449))
        
    def test_450(self):
        """Created automatically"""
        input = r"""
                Function: main
                Body:
                    Var: x;
                    For (x=1, 1+1 , x+1) Do
                    EndFor.
                EndBody.
            """
        expect = str(TypeMismatchInStatement(For(Id("x"),IntLiteral(1),BinaryOp("+",IntLiteral(1),IntLiteral(1)),BinaryOp("+",Id("x"),IntLiteral(1)),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,450))
        
    def test_451(self):
        """Created automatically"""
        input = r"""
                Function: main
                Body:
                    Var: x=1,y;
                    While (x)
                    Do
                    EndWhile.
                EndBody.
            """
        expect = str(TypeMismatchInStatement(While(Id("x"),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,451))
        
    def test_452(self):
        """Created automatically"""
        input = r"""
                Function: main
                Body:
                    Var: x=1,y;
                    Do
                    While (x)
                    EndDo.
                EndBody.
            """
        expect = str(TypeMismatchInStatement(Dowhile(([],[]),Id("x"))))
        self.assertTrue(TestChecker.test(input,expect,452))
        
    def test_453(self):
        """Created automatically"""
        input = r"""
                Function: foo
                Body:
                EndBody.
                Function: main
                Body:
                    Var:x;
                    foo();
                    foo() = x+1;
                EndBody.
            """
        expect = str(TypeMismatchInStatement(Assign(CallExpr(Id("foo"),[]),BinaryOp("+",Id("x"),IntLiteral(1)))))
        self.assertTrue(TestChecker.test(input,expect,453))
        
    def test_454(self):
        """Created automatically"""
        input = r"""
                Function: foo
                Body:
                EndBody.
                Function: main
                Body:
                    Var:x;
                    foo();
                    x = foo();
                EndBody.
            """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),CallExpr(Id("foo"),[]))))
        self.assertTrue(TestChecker.test(input,expect,454))
        
    def test_455(self):
        """Created automatically"""
        input = r"""
                Function: main
                Body:
                    foo();
                EndBody.
                Function: foo
                Body:
                    Return 1;
                EndBody.
            """
        expect = str(TypeMismatchInStatement(Return(IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,455))
        
    def test_456(self):
        """Created automatically"""
        input = r"""
                Function: main
                Body:
                    Var:x;
                    x = 1+foo();
                EndBody.
                Function: foo
                Body:
                    Return 1.5;
                EndBody.
            """
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(1.5))))
        self.assertTrue(TestChecker.test(input,expect,456))
        
    def test_457(self):
        """Created automatically"""
        input = r"""                
                Function: main
                Body:
                    Var: x;
                    If x Then
                        Return 1;
                    Else
                        Return 1.5;
                    EndIf.
                EndBody.
            """
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(1.5))))
        self.assertTrue(TestChecker.test(input,expect,457))
        
    def test_458(self):
        """Created automatically"""
        input = r"""
                Function: main
                Body:
                    foo();
                EndBody.
                Function: foo
                Body:
                    Return ;
                EndBody.
            """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,458))
        
    def test_459(self):
        """Created automatically"""
        input = r"""
                Function: main
                Body:
                    Var: x;
                    Return x;
                EndBody.

            """
        expect = str(TypeCannotBeInferred(Return(Id("x"))))
        self.assertTrue(TestChecker.test(input,expect,459))
        
    def test_460(self):
        """Created automatically"""
        input = r"""
                
                Function: main
                Body:
                    Var: a[1][2];
                    a[1+1][0.5+.1.5] = 1;
                EndBody.
            """
        expect = str(TypeMismatchInExpression(ArrayCell(Id("a"),[BinaryOp("+",IntLiteral(1),IntLiteral(1)),BinaryOp("+.",FloatLiteral(0.5),FloatLiteral(1.5))])))
        self.assertTrue(TestChecker.test(input,expect,460))
        
    def test_461(self):
        """Created automatically"""
        input = r"""
                
                Function: main
                Body:
                    Var: a[1][2];
                    a[1][2][3] = 1;
                EndBody.
            """
        expect = str(TypeMismatchInExpression(ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])))
        self.assertTrue(TestChecker.test(input,expect,461))
        
    def test_462(self):
        """Created automatically"""
        input = r"""
                Function: foo
                Body:
                   Var : x[1][2]={{1,2}} ;
                   Return x;
                EndBody.
                

                Function: main
                Body:
                    Var:x;
                    foo(x)[x+3][0.5]=1;
                EndBody.
            """
        expect = str(TypeMismatchInExpression(ArrayCell(CallExpr(Id("foo"),[Id("x")]),[BinaryOp("+",Id("x"),IntLiteral(3)),FloatLiteral(0.5)])))
        self.assertTrue(TestChecker.test(input,expect,462))
        
    def test_463(self):
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
                    fact(x);
                EndBody.
            """
        expect = str(TypeMismatchInStatement(CallStmt(Id("fact"),[Id("x")])))
        self.assertTrue(TestChecker.test(input,expect,463))
        
    def test_464(self):
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
                EndBody.
                Function: main
                Body:
                EndBody.
            """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,464))
        
    def test_465(self):
        """Created automatically"""
        input = r"""
                Function: main
                Body:
                    Var:a[5]={1,2,3,4,5};
                    Var: b[2][3]={{1,2,3},{4,5,6}};
                    a[3 + foo(2)] = a[b[2][3]] +. 4.0;
                EndBody.
            """
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,465))
        
    def test_466(self):
        """Created automatically"""
        input = r"""
                Function: foo
                Parameter: x,y
                Body:
                    foo (2 + x, 4. \. y);
                    foo(x,y);
                EndBody. 
                Function: main
                Body:
                EndBody.           
                """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,466))
        
    def test_467(self):
        """Created automatically"""
        input = r"""
                Function: main
                Body:
                    If True Then
                    ElseIf True Then
                        Var: a;
                    EndIf.
                EndBody.
            """
        expect = str(TypeCannotBeInferred(If([(BooleanLiteral(True),[],[]),(BooleanLiteral(True),[VarDecl(Id("a"),[],None)],[])],([],[]))))
        #self.assertTrue(TestChecker.test(input,expect,467))
        
    def test_468(self):
        """Created automatically"""
        input = r"""
                Function: main
                Body:
                    For (a = 1, a < 10, 1) Do
                        Var:a=1;
                    EndFor.
                EndBody.
            """
        expect = str(Undeclared(Identifier(),"a"))
        self.assertTrue(TestChecker.test(input,expect,468))
        
    def test_469(self):
        """Created automatically"""
        input = r"""
                Var: a[3]={"Mot","2","Three"};
                Function: main
                Body:
                    a[1] = a[1] + a[2];
                EndBody.
            """
        expect = str(TypeMismatchInExpression(BinaryOp("+",ArrayCell(Id("a"),[IntLiteral(1)]),ArrayCell(Id("a"),[IntLiteral(2)]))))
        self.assertTrue(TestChecker.test(input,expect,469))
        
    def test_470(self):
        """Created automatically"""
        input = r"""
                
                Function: main
                Body:
                    Var:a,b,c,d;
                    a = a + b || c - d;
                EndBody.
            """
        expect = str(TypeMismatchInExpression(BinaryOp("||",BinaryOp("+",Id("a"),Id("b")),BinaryOp("-",Id("c"),Id("d")))))
        self.assertTrue(TestChecker.test(input,expect,470))
        
    def test_471(self):
        """Created automatically"""
        input = r"""
            Function: main
            Body:
                Var: sum = 0, a = 1;
                While a < 10 Do
                    Var: b, cal = 1;
                    While b < 10 Do
                        cal = cal * b;
                        b = b + 1;
                    EndWhile.
                    sum = sum + prod;
                    a = a + 1;
                EndWhile.
            EndBody.
            """
        expect = str(Undeclared(Identifier(),"prod"))
        self.assertTrue(TestChecker.test(input,expect,471))
        
    def test_472(self):
        """Created automatically"""
        input = r"""
            Function: main 
            Body: 
                Var: a=1,x; 
                a=foo(x); 
            EndBody.             
"""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,472))
        
    def test_473(self):
        """Created automatically"""
        input = r"""
                Function: main
                Body:
                    Var:x;
                    If True Then
                        x = 3;
                    Else 
                        x = 2.0;
                    EndIf.
                EndBody.
            """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),FloatLiteral(2.0))))
        self.assertTrue(TestChecker.test(input,expect,473))
        
    def test_474(self):
        """Created automatically"""
        input = r"""
                Var:x =1;
                Function: main
                Parameter: y
                Body:
                    x = y + main(0.5) ;
                EndBody.
            """
        expect = str(TypeMismatchInExpression(CallExpr(Id("main"),[FloatLiteral(0.5)])))
        self.assertTrue(TestChecker.test(input,expect,474))
        
    def test_475(self):
        """Created automatically"""
        input = r"""
        Var:x =1;
        Function: main
        Parameter: y
        Body:
            x = main(0.5) + y;
        EndBody.            """
        expect = str(TypeMismatchInExpression(BinaryOp("+",CallExpr(Id("main"),[FloatLiteral(0.5)]),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,475))
        
    def test_476(self):
        """Created automatically"""
        input = r"""
                Function: main
                Parameter: x
                Body:
                    Var:y;
                    Do
                        x=1;
                        main(0.5);
                    While y 
                    EndDo.
                EndBody.            """
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[FloatLiteral(0.5)])))
        self.assertTrue(TestChecker.test(input,expect,476))
        
    def test_477(self):
        """Created automatically"""
        input = r"""
                Function: main
                Parameter: x, a, b, c
                Body:
                    If(x == ((False||True) && (a > b + c))) Then
                        a = b - c;
                    Else
                        a = b + c;
                        x = True;
                    EndIf.
                EndBody.
            """
        expect = str(TypeMismatchInExpression(BinaryOp("==",Id("x"),BinaryOp("&&",BinaryOp("||",BooleanLiteral(False),BooleanLiteral(True)),BinaryOp(">",Id("a"),BinaryOp("+",Id("b"),Id("c")))))))
        self.assertTrue(TestChecker.test(input,expect,477))
        
    def test_478(self):
        """Created automatically"""
        input = r"""
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
                EndBody.            """
        expect = str(TypeMismatchInExpression(ArrayCell(Id("abc"),[IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input,expect,478))
        
    def test_479(self):
        """Created automatically"""
        input = r"""
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
                EndBody.            """
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[Id("w")])))
        self.assertTrue(TestChecker.test(input,expect,479))
        
    def test_480(self):
        """Created automatically"""
        input = r"""
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
                EndBody.         """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id("abc"),[IntLiteral(1)]),FloatLiteral(1.5))))
        self.assertTrue(TestChecker.test(input,expect,480))
        
    def test_481(self):
        """Created automatically"""
        input = r"""
                Function: foo
                Parameter: x[2]
                Body:
                EndBody.
                Function: main
                Body:
                    Var: z[2] = {1,2};
                    Var: w[2] = {3,4};
                    Var: x;
                    foo(z);
                    foo(w);
                EndBody.            """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,481))
        
    def test_482(self):
        """Created automatically"""
        input = r"""
                    Function: main
                    Parameter: x
                    Body:
                        y= x + main(0.5);

                    EndBody.            """
        expect = str(Undeclared(Identifier(),"y"))
        self.assertTrue(TestChecker.test(input,expect,482))
        
    def test_483(self):
        """Created automatically"""
        input = r"""
                
                Function: main 
        Body:
            If True Then
                Var: a;
                Var: x;
                Var: y;
                x = 1;
                y = 2;
                z = 3;
            EndIf.
        EndBody.
            """
        expect = str(Undeclared(Identifier(),"z"))
        self.assertTrue(TestChecker.test(input,expect,483))
        
    def test_484(self):
        """Created automatically"""
        input = r"""
        Function: main 
        Parameter: n
        Body: 
            Var:i;
            For (i = 6*9,True, i-1) Do
                Var:x=5;
                a=3;
            EndFor.
        EndBody.
            """
        expect = str(Undeclared(Identifier(),"a"))
        self.assertTrue(TestChecker.test(input,expect,484))
        
    def test_485(self):
        """Created automatically"""
        input = r"""
        Function: main 
        Parameter: n
        Body: 
            Var: i = 0;
            While i < 5 Do
            EndWhile.
        EndBody.            """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,485))
        
    def test_486(self):
        """Created automatically"""
        input = r"""
        Function: main 
        Parameter: n
        Body: 
            Var:x;
            While x>1 Do
                If x==1 Then Return;
                EndIf.
            EndWhile.
        EndBody.
            """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,486))
        
    def test_487(self):
        """Created automatically"""
        input = r"""
        Function: main 
        Parameter: n
        Body: 
            Var:a;
            Do  
                Var:b;
                Do
                While(b!=4)
                EndDo.
            While(a!=3)                
            EndDo.
            a=1.0;
        EndBody.
            """
        expect = str(TypeMismatchInStatement(Assign(Id("a"),FloatLiteral(1.0))))
        self.assertTrue(TestChecker.test(input,expect,487))
        
    def test_488(self):
        """Created automatically"""
        input = r"""
        Function: main 
        Parameter: x,y
        Body: 
            Do  
                Return main(x,y);
            While True
            EndDo.
        EndBody.
            """
        expect = str(TypeCannotBeInferred(Return(CallExpr(Id("main"),[Id("x"),Id("y")]))))
        self.assertTrue(TestChecker.test(input,expect,488))
        
    def test_489(self):
        """Created automatically"""
        input = r"""
        Var:a;
        Function: main 
        Parameter: n
        Body: 
            Do
                Return a+3;
            While True
            EndDo.
        EndBody.
            """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,489))
        
    def test_490(self):
        """Created automatically"""
        input = r"""
        Function: main 
        Parameter: x,y
        Body: 
            Return main(x +3,y +. 10.2);
        EndBody.
            """
        expect = str(TypeCannotBeInferred(Return(CallExpr(Id("main"),[BinaryOp("+",Id("x"),IntLiteral(3)),BinaryOp("+.",Id("y"),FloatLiteral(10.2))]))))
        self.assertTrue(TestChecker.test(input,expect,490))
        
    def test_491(self):
        """Created automatically"""
        input = r"""
        Function: main 
        Parameter:a
        Body: 
            a=1;
            foo(a,3*7, a+ 5,"string",True);
        EndBody.
        Function: foo 
        Parameter: a,b,c,d,e
        Body: 
            Var:z;
            a=4;
            b=21;
            c=6;
            d="Hello";
            z= !e;
        EndBody.
            """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,491))
        
    def test_492(self):
        """Created automatically"""
        input = r"""
                Function: main 
                Parameter: a,b,c
                Body: 
                    a= (a==b)!= c +3;
                EndBody.
            """
        expect = str(TypeMismatchInExpression(BinaryOp("!=",BinaryOp("==",Id("a"),Id("b")),BinaryOp("+",Id("c"),IntLiteral(3)))))
        self.assertTrue(TestChecker.test(input,expect,492))
        
    def test_493(self):
        """Created automatically"""
        input = r"""
               Function: main 
                Parameter: n
                Body: 
                    If n == 0 Then
                        If n!=0 Then
                            If n!=0 Then
                                a=5;
                            EndIf.
                        EndIf.
                    EndIf.
                EndBody.
            """
        expect = str(Undeclared(Identifier(),"a"))
        self.assertTrue(TestChecker.test(input,expect,493))
        
    def test_494(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: main 
            Parameter: x[5]
            Body:
                x = {1.,2.,3.,4.,5.};
            EndBody.
        Function: foo
            Body:
                x = 2;
            EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_495(self):
        """Created automatically"""
        input = r"""
        Function : print
            Parameter : x
            Body:
                Return;
            EndBody.

            Function: m
            Body:
                Var : value = 12345;
                Return value;
            EndBody.

            Function: main
            Parameter : x, y
            Body: 
                print(m); 
                Return 0;
            EndBody.
            """
        expect = str(Redeclared(Function(),"print"))
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_496(self):
        """Created automatically"""
        input = r"""
Function: main 
            Parameter: x[5]
            Body:
                Var: y[5]; 
                x = {1,2,3,4,5};
                main(y);
                foo(1.2);
            EndBody.
        Function: foo
            Parameter: x
            Body:
                x = 2;
            EndBody.
            """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),IntLiteral(2))))
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_497(self):
        """Created automatically"""
        input = r"""
Function: main 
            Parameter: x[5]
            Body:
                Var: y[5]; 
                x = {1,2,3,4,5};
                main(y); 
            EndBody.
            """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_498(self):
        """Created automatically"""
        input = r"""
Function: main 
            Parameter: x[5]
            Body:
                Var: y = 1; 
                x = {1,2,3,4,5};
                main(y); 
            EndBody.
            """
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[Id("y")])))
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_499(self):
        """Created automatically"""
        input = r"""
Function: main 
Body:
    Var: a=1,x; 
    a=foo(x); 
EndBody. 
            """
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,499))

    def test_500(self):
        """Created automatically"""
        input = r"""
Function: main
        Parameter: x
        Body:
            If True Then
                Var: x = 1;
                main(1.5);
            EndIf.
            main(2);
        EndBody.
            """
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[IntLiteral(2)])))
        self.assertTrue(TestChecker.test(input,expect,500))
        
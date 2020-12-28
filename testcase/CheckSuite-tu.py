import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):
    def test_401(self):
        """Created automatically"""
        input = r"""
        


        Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10], b;
        
                Function: main
                   Body: 
                   EndBody.
                   
                   
                   
                   """
        expect = str(Redeclared(Variable(),"b"))
        self.assertTrue(TestChecker.test(input,expect,401))
        
    def test_402(self):
        """Created automatically"""
        input = r"""
        


        Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10];
        Var: d;
        
                Function: main
                   Body: 
                   EndBody.
                   
                   
                   
                   """
        expect = str(Redeclared(Variable(),"d"))
        self.assertTrue(TestChecker.test(input,expect,402))
        
    def test_403(self):
        """Created automatically"""
        input = r"""
        


        Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10];
        
                Function: foo
                   Body: 
                   EndBody.


                Function: main
                   Body: 
                   EndBody.
                   
                Function: bar
                   Body: 
                   EndBody.

                Function: main
                   Body: 
                   EndBody.
                
                   
                   
                   """
        expect = str(Redeclared(Function(),"main"))
        self.assertTrue(TestChecker.test(input,expect,403))
        
    def test_404(self):
        """Created automatically"""
        input = r"""
        


        Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10];
        
                Function: foo
                   Body: 
                   EndBody.


                Function: main
                   Body: 
                   EndBody.
                   
                Function: bar
                   Body: 
                   EndBody.

                Function: b
                   Body: 
                   EndBody.
                
                   
                   
                   """
        expect = str(Redeclared(Function(),"b"))
        self.assertTrue(TestChecker.test(input,expect,404))
        
    def test_405(self):
        """Created automatically"""
        input = r"""
        


        Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10], printStrLn;
        
                Function: foo
                   Body: 
                   EndBody.


                Function: main
                   Body: 
                   EndBody.
                   
                Function: bar
                   Body: 
                   EndBody.

                Function: int_of_string
                   Body: 
                   EndBody.
                
                   
                   
                   """
        expect = str(Redeclared(Variable(),"printStrLn"))
        self.assertTrue(TestChecker.test(input,expect,405))
        
    def test_406(self):
        """Created automatically"""
        input = r"""
        


        Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10];
        
                Function: foo
                   Body: 
                   EndBody.


                Function: main
                   Body: 
                   EndBody.
                   
                Function: bar
                   Body: 
                   EndBody.

                Function: int_of_string
                   Body: 
                   EndBody.
                
                   
                   
                   """
        expect = str(Redeclared(Function(),"int_of_string"))
        self.assertTrue(TestChecker.test(input,expect,406))
        
    def test_407(self):
        """Created automatically"""
        input = r"""
        


        Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10];
        
        Function: foo
            Body:
            EndBody.


        Function: main
            Body:
            EndBody.
                   
        Function: bar
            Parameter: bar, a, b[2][3], m, n[10], int_of_string
            Body:
                Var: c, d = 6, e, f, printStr, bar;
            EndBody.

                   
                   
                   """
        expect = str(Redeclared(Variable(),"bar"))
        self.assertTrue(TestChecker.test(input,expect,407))
        
    def test_408(self):
        """Created automatically"""
        input = r"""
        


        Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10];
        
        Function: foo
            Body:
            EndBody.


        Function: main
            Body:
            EndBody.
                   
        Function: bar
            Parameter: bar, a, b[2][3], m, n[10], int_of_string, bar
            Body:
                Var: c, d = 6, e, f, printStr;
            EndBody.

                   
                   
                   """
        expect = str(Redeclared(Parameter(),"bar"))
        self.assertTrue(TestChecker.test(input,expect,408))
        
    def test_409(self):
        """Created automatically"""
        input = r"""
        


        Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10];
        
        Function: foo
            Parameter: foo, a, b[2][3], m, n[10], int_of_string
            Body:
                Var: c, d = 6, e, f, printStr;
            EndBody.


        Function: main
            Body:
            EndBody.
                   
        Function: bar
            Parameter: bar, a, b[2][3], m, n[10], int_of_string
            Body:
                Var: c, d = 6, e, f, printStr, d;
            EndBody.

                   
                   
                   """
        expect = str(Redeclared(Variable(),"d"))
        self.assertTrue(TestChecker.test(input,expect,409))
        
    def test_410(self):
        """Created automatically"""
        input = r"""
        


        Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10];
        
        Function: foo
            Parameter: foo, a, b[2][3], m, n[10], int_of_string, x
            Body:
                Var: c, d = 6, e, f, printStr;
            EndBody.


        Function: main
            Body:
                Var: c, d = 6, e, f, printStr, x;
            EndBody.
                   
        Function: bar
            Parameter: bar, a, b[2][3], m, n[10], int_of_string
            Body:
                Var: c, d = 6, e, f, printStr;
                x = 1;
            EndBody.

                   
                   
                   """
        expect = str(Undeclared(Identifier(),"x"))
        self.assertTrue(TestChecker.test(input,expect,410))
        
    def test_411(self):
        """Created automatically"""
        input = r"""
        
        


        Function: main
            Body:
            EndBody.
                   
        Function: bar
            Parameter: n[10], int_of_string, a
            Body:
                int_of_string = a;
            EndBody.

                   
                   
                   """
        expect = str(TypeCannotBeInferred(Assign(Id("int_of_string"),Id("a"))))
        self.assertTrue(TestChecker.test(input,expect,411))
        
    def test_412(self):
        """Created automatically"""
        input = r"""
        
        
        


        Function: main
            Body:
            EndBody.
                   
        Function: bar
            Parameter: n[10], int_of_string, a
            Body:
                bar = 1;
            EndBody.

                   
                   
                   """
        expect = str(Undeclared(Identifier(),"bar"))
        self.assertTrue(TestChecker.test(input,expect,412))
        
    def test_413(self):
        """Created automatically"""
        input = r"""
        
        
        Var: a = 5;

        Function: main
            Body:
            EndBody.
                   
        Function: bar
            Parameter: n[10], int_of_string
            Body:
                a = 3.0;

            EndBody.

                   
                   
                   """
        expect = str(TypeMismatchInStatement(Assign(Id("a"),FloatLiteral(3.0))))
        self.assertTrue(TestChecker.test(input,expect,413))
        
    def test_414(self):
        """Created automatically"""
        input = r"""
        
        
        Var: a;

        Function: bar
            Parameter: n[10], int_of_string
            Body:
                a = 3.0;

            EndBody.

        Function: main
            Body:
                a = 1;
            EndBody.
                   
        

                   
                   
                   """
        expect = str(TypeMismatchInStatement(Assign(Id("a"),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,414))
        
    def test_415(self):
        """Created automatically"""
        input = r"""
        
        
        Var: a;

        Function: bar
            Parameter: n[10], int_of_string
            Body:
                a = int_of_string;

            EndBody.

        Function: main
            Body:
                a = 1;
            EndBody.
                   
        

                   
                   
                   """
        expect = str(TypeCannotBeInferred(Assign(Id("a"),Id("int_of_string"))))
        self.assertTrue(TestChecker.test(input,expect,415))
        
    def test_416(self):
        """Created automatically"""
        input = r"""
        
        
        Var: a;

        Function: bar
            Parameter: n[10], int_of_string
            Body:
                int_of_string = 3.0;
                int_of_string = a;

            EndBody.

        Function: main
            Body:
                a = 1;
            EndBody.
                   
        

                   
                   
                   """
        expect = str(TypeMismatchInStatement(Assign(Id("a"),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,416))
        
    def test_417(self):
        """Created automatically"""
        input = r"""
        
        
        Var: a;


        Function: main
            Body:
                a = 3.0;
            EndBody.

        Function: bar
            Parameter: n[10], int_of_string
            Body:
                int_of_string = 3 + a;

            EndBody.

        
                   
        

                   
                   
                   """
        expect = str(TypeMismatchInExpression(BinaryOp("+",IntLiteral(3),Id("a"))))
        self.assertTrue(TestChecker.test(input,expect,417))
        
    def test_418(self):
        """Created automatically"""
        input = r"""
        
        
        Var: a = 5;
        Var: b, c[10];
        
                

        Function: main
            Parameter: main
                   Body:
            
                   EndBody.
                   

        Function: foo
                   Body: 


                   EndBody.

        Function: bar
            Parameter: bar
            Body:
                bar = 5.0;
                a = a + bar;
            EndBody.

        
                   
        

                   
                   
                   """
        expect = str(TypeMismatchInExpression(BinaryOp("+",Id("a"),Id("bar"))))
        self.assertTrue(TestChecker.test(input,expect,418))
        
    def test_419(self):
        """Created automatically"""
        input = r"""
        
        
        Var: a = 5;
        Var: b, c[10];
        
                

        Function: main
            Parameter: main
                   Body:
            
                   EndBody.
                   

        Function: foo
                   Body: 


                   EndBody.

        Function: bar
            Parameter: bar
            Body:
                bar = 5.0;
                a = bar + bar;
            EndBody.

        
                   
        

                   
                   
                   """
        expect = str(TypeMismatchInExpression(BinaryOp("+",Id("bar"),Id("bar"))))
        self.assertTrue(TestChecker.test(input,expect,419))
        
    def test_420(self):
        """Created automatically"""
        input = r"""
        
        
        Var: a = 5;
        Var: b, c[10];
        
                

        Function: main
            Parameter: main
                   Body:
            
                   EndBody.
                   

        Function: foo
                   Body: 


                   EndBody.

        Function: bar
            Parameter: bar
            Body:
                bar = 5.0;
                a = b + bar;
            EndBody.

        
                   
        

                   
                   
                   """
        expect = str(TypeMismatchInExpression(BinaryOp("+",Id("b"),Id("bar"))))
        self.assertTrue(TestChecker.test(input,expect,420))
        
    def test_421(self):
        """Created automatically"""
        input = r"""
        
        
        Var: a = 5;
        Var: b, c[10];
        
                

        Function: main
            Parameter: main
                   Body:
            
                   EndBody.
                   

        Function: foo
                   Body: 


                   EndBody.

        Function: bar
            Parameter: bar
            Body:
                bar = 5.0;
                a = b +. bar;
            EndBody.
                   
                   """
        expect = str(TypeMismatchInStatement(Assign(Id("a"),BinaryOp("+.",Id("b"),Id("bar")))))
        self.assertTrue(TestChecker.test(input,expect,421))
        
    def test_422(self):
        """Created automatically"""
        input = r"""
        
        
        Var: a = 5;
Var: b[2][3] = {{2,3,4},{4,5,6}};
Var: c, d = 6, e, f;
Var: m, n[1];
        
                

        Function: main
            Parameter: main[1]
                   Body:
                   EndBody.
                   

        Function: foo
                   Body:
                   m = {1};
                   EndBody.

        Function: bar
            Parameter: bar[2][3]
            Body:
            EndBody.
                   
                   """
        expect = str(TypeMismatchInStatement(Assign(Id("m"),ArrayLiteral([IntLiteral(1)]))))
        self.assertTrue(TestChecker.test(input,expect,422))
        
    def test_423(self):
        """Created automatically"""
        input = r"""
        
        
        Var: a = 5;
Var: b[2][3] = {{2,3,4},{4,5,6}};
Var: c, d = 6, e, f;
Var: m, n[1];
        
                

        Function: main
            Parameter: main[1]
                   Body:
                   EndBody.
                   

        Function: foo
                   Body:
                   b = {1};
                   EndBody.

        Function: bar
            Parameter: bar[2][3]
            Body:
            EndBody.
                   
                   """
        expect = str(TypeMismatchInStatement(Assign(Id("b"),ArrayLiteral([IntLiteral(1)]))))
        self.assertTrue(TestChecker.test(input,expect,423))
        
    def test_424(self):
        """Created automatically"""
        input = r"""
        
        
        Var: a = 5;
Var: b[2][3] = {{2,3,4},{4,5,6}};
Var: c, d = 6, e, f;
Var: m, n[1];
        
                

        Function: main
            Parameter: main[1]
                   Body:
                   EndBody.
                   

        Function: foo
                   Body:
                   a = bar(n);
                   EndBody.

        Function: bar
            Parameter: bar[2][3]
            Body:
            EndBody.
                   
                   """
        expect = str(TypeMismatchInExpression(CallExpr(Id("bar"),[Id("n")])))
        self.assertTrue(TestChecker.test(input,expect,424))
        
    def test_425(self):
        """Created automatically"""
        input = r"""
        
        
        Var: a = 5;
Var: b[2][3];
Var: c, d = 6, e, f;
Var: m, n[1];
        
                

        Function: main
            Parameter: main[1]
                   Body:
                   EndBody.
                   

        Function: foo
                   Body:
                   a = bar(b);
                   EndBody.

        Function: bar
            Parameter: bar[2][3]
            Body:
            EndBody.
                   
                   """
        expect = str(TypeCannotBeInferred(Assign(Id("a"),CallExpr(Id("bar"),[Id("b")]))))
        self.assertTrue(TestChecker.test(input,expect,425))
        
    def test_426(self):
        """Created automatically"""
        input = r"""
        
        
        Var: a = 5;
Var: b[2][3] = {{2,3,4},{4,5,6}};
Var: c[2][3] , d = 6, e, f;
Var: m, n[1];
        
                

        Function: main
            Parameter: main[1]
                   Body:
                   EndBody.
                   

        Function: foo
                   Body:
                   b = bar(b);
                   a = bar(c);
                   EndBody.

        Function: bar
            Parameter: bar[2][3]
            Body:
            EndBody.
                   
                   """
        expect = str(TypeMismatchInStatement(Assign(Id("a"),CallExpr(Id("bar"),[Id("c")]))))
        self.assertTrue(TestChecker.test(input,expect,426))
        
    def test_427(self):
        """Created automatically"""
        input = r"""
        
        
        Var: a = 5;
Var: b[2][3] = {{2,3,4},{4,5,6}};
Var: c[2][3] , d = 6, e, f;
Var: m, n[1];
        
                

        Function: main
            Parameter: main[1]
                   Body:
                   EndBody.
                   

        Function: foo
                   Body:
                   b = bar(b);
                    b = bar(c);
                    c = {{2.0,3.0,4.0},{4.0,5.0,6.0}};
                   EndBody.

        Function: bar
            Parameter: bar[2][3]
            Body:
            EndBody.
                   
                   """
        expect = str(TypeMismatchInStatement(Assign(Id("c"),ArrayLiteral([ArrayLiteral([FloatLiteral(2.0),FloatLiteral(3.0),FloatLiteral(4.0)]),ArrayLiteral([FloatLiteral(4.0),FloatLiteral(5.0),FloatLiteral(6.0)])]))))
        self.assertTrue(TestChecker.test(input,expect,427))
        
    def test_428(self):
        """Created automatically"""
        input = r"""
        
        
        Var: a = 5;
Var: b[2][3] = {{2,3,4},{4,5,6}};
Var: c[2][3] , d = 6, e, f;
Var: m, n[1];
        
                

        Function: main
            Parameter: main[1]
                   Body:
                   EndBody.
                   

        Function: foo
                   Body:
                   b = bar(b);
                c = bar(b);
                    c = {{2.0,3.0,4.0},{4.0,5.0,6.0}};
                   EndBody.

        Function: bar
            Parameter: bar[2][3]
            Body:
            EndBody.
                   
                   """
        expect = str(TypeMismatchInStatement(Assign(Id("c"),ArrayLiteral([ArrayLiteral([FloatLiteral(2.0),FloatLiteral(3.0),FloatLiteral(4.0)]),ArrayLiteral([FloatLiteral(4.0),FloatLiteral(5.0),FloatLiteral(6.0)])]))))
        self.assertTrue(TestChecker.test(input,expect,428))
        
    def test_429(self):
        """Created automatically"""
        input = r"""
        
        
        Var: a = 5;
Var: b[2][3] = {{2,3,4},{4,5,6}};
Var: c[2][3] , d = 6, e, f;
Var: m, n[1];
        
                

        Function: main
            Parameter: main[1]
                   Body:
                   EndBody.
                   

        Function: foo
                   Body:
                   a = bar(d);
                    a = bar(e);
                    e = 5.0;
                   EndBody.

        Function: bar
            Parameter: bar
            Body:
            EndBody.
                   
                   """
        expect = str(TypeMismatchInStatement(Assign(Id("e"),FloatLiteral(5.0))))
        self.assertTrue(TestChecker.test(input,expect,429))
        
    def test_430(self):
        """Created automatically"""
        input = r"""
        
        
        Var: a = 5;
Var: b[2][3] = {{2,3,4},{4,5,6}};
Var: c[2][3] , d = 6, e, f;
Var: m, n[1];
        
                

        Function: main
            Parameter: main[1]
                   Body:
                   EndBody.
                   

        Function: foo
                   Body:
                   b = bar(a);
                   bar(a)[e][f] = 3.0;
                   EndBody.

        Function: bar
            Parameter: bar
            Body:
            EndBody.
                   
                   """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(CallExpr(Id("bar"),[Id("a")]),[Id("e"),Id("f")]),FloatLiteral(3.0))))
        self.assertTrue(TestChecker.test(input,expect,430))
        
    def test_431(self):
        """Created automatically"""
        input = r"""
        
        
        Var: a = 5;
Var: b[2][3] = {{2,3,4},{4,5,6}};
Var: c[2][3] , d = 6, e, f;
Var: m, n[1];
        
                

        
                   

        Function: main
                   Body:
                   b = bar(a);
                   bar(a)[e][f] = 3;
                   f = n[bar(a)[e][foo(n)]];

                   EndBody.

        Function: foo
            Parameter: foo[1]
                   Body:
                   EndBody.

        Function: bar
            Parameter: bar
            Body:
            EndBody.
                   
                   """
        expect = str(TypeCannotBeInferred(Assign(Id("f"),ArrayCell(Id("n"),[ArrayCell(CallExpr(Id("bar"),[Id("a")]),[Id("e"),CallExpr(Id("foo"),[Id("n")])])]))))
        self.assertTrue(TestChecker.test(input,expect,431))
        
    def test_432(self):
        """Created automatically"""
        input = r"""
        
        
        Var: a = 5;
Var: b[2][3] = {{2,3,4},{4,5,6}};
Var: c[2][3] , d = 6, e, f;
Var: m, n[1];
        
                

        
                   

        Function: main
                   Body:
                   b = bar(a);
                   n = {1.0};
                   bar(a)[e][f] = 3;
                   f = n[bar(a)[e][foo(n)]];

                   EndBody.

        Function: foo
            Parameter: foo[1]
                   Body:
                   EndBody.

        Function: bar
            Parameter: bar
            Body:
            EndBody.
                   
                   """
        expect = str(TypeMismatchInStatement(Assign(Id("f"),ArrayCell(Id("n"),[ArrayCell(CallExpr(Id("bar"),[Id("a")]),[Id("e"),CallExpr(Id("foo"),[Id("n")])])]))))
        self.assertTrue(TestChecker.test(input,expect,432))
        
    def test_433(self):
        """Created automatically"""
        input = r""" 
            Function : printFunc
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
                printFunc(m); 
                Return 0;
            EndBody.
            """
        expect = str(Undeclared(Identifier(),"m"))
        self.assertTrue(TestChecker.test(input,expect,433))
        
    def test_434(self):
        """Created automatically"""
        input = r""" 
            Function: main
            Parameter: x, y ,z
            Body:
            y = x || (x>z);
            EndBody.
            """
        expect = str(TypeMismatchInExpression(BinaryOp(">",Id("x"),Id("z"))))
        self.assertTrue(TestChecker.test(input,expect,434))
        
    def test_435(self):
        """Created automatically"""
        input = r""" 
            Function: foo
            Parameter: x
            Body:
            x=1.1;
            Return { True };
            EndBody.
        Function: main
            Parameter: x, y
            Body:
            foo(x)[0] = x || (x>y);
            EndBody.
            """
        expect = str(TypeMismatchInExpression(BinaryOp("||",Id("x"),BinaryOp(">",Id("x"),Id("y")))))
        self.assertTrue(TestChecker.test(input,expect,435))
        
    def test_436(self):
        """Created automatically"""
        input = r""" 
            Var: a;
        Function: main
            Body:
            a = foo();
            EndBody.
        Function: foo
        Body:
            Return 1;
        EndBody.
            """
        expect = str(TypeCannotBeInferred(Assign(Id("a"),CallExpr(Id("foo"),[]))))
        self.assertTrue(TestChecker.test(input,expect,436))
        
    def test_437(self):
        """Created automatically"""
        input = r""" 
            Var: a, b;
        Function: main
            Body:
            a = a + foo(b);
            EndBody.
        Function: foo
        Parameter: x
        Body:
            Return 1;
        EndBody.
            """
        expect = str(TypeCannotBeInferred(Assign(Id("a"),BinaryOp("+",Id("a"),CallExpr(Id("foo"),[Id("b")])))))
        self.assertTrue(TestChecker.test(input,expect,437))
        
    def test_438(self):
        """Created automatically"""
        input = r""" 
            Var: a, b;
        Function: main
            Body:
            a = a + foo(a);
            EndBody.
        Function: foo
        Parameter: x
        Body:
            Return 1.0;
        EndBody.
            """
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(1.0))))
        self.assertTrue(TestChecker.test(input,expect,438))
        
    def test_439(self):
        """Created automatically"""
        input = r""" 
            Var: a, b;
        Function: main
            Body:
            a = a + foo(a);
            EndBody.
        Function: foo
        Parameter: x
        Body:
            Return x +. b;
        EndBody.
            """
        expect = str(TypeMismatchInExpression(BinaryOp("+.",Id("x"),Id("b"))))
        self.assertTrue(TestChecker.test(input,expect,439))
        
    def test_440(self):
        """Created automatically"""
        input = r""" 
            Var: a, b;
        Function: main
            Body:
            a = b || foo(a + 1);
            EndBody.
        Function: foo
        Parameter: x
        Body:
            Return True;
        EndBody.
            """
        expect = str(TypeMismatchInStatement(Assign(Id("a"),BinaryOp("||",Id("b"),CallExpr(Id("foo"),[BinaryOp("+",Id("a"),IntLiteral(1))])))))
        self.assertTrue(TestChecker.test(input,expect,440))
        
    def test_441(self):
        """Created automatically"""
        input = r""" 
            Var: a, b;
        Function: main
            Body:
            b = b || foo(a + 1);
            EndBody.
        Function: foo
        Parameter: x
        Body:
            Return;
        EndBody.
            """
        expect = str(TypeMismatchInStatement(Return(None)))
        self.assertTrue(TestChecker.test(input,expect,441))
        
    def test_442(self):
        """Created automatically"""
        input = r""" 
            Var: a, b;
        Function: main
            Body:
            b = b || foo(a + 1);
            EndBody.
        Function: foo
        Parameter: x
        Body:
            Return x;
        EndBody.
            """
        expect = str(TypeMismatchInStatement(Return(Id("x"))))
        self.assertTrue(TestChecker.test(input,expect,442))
        
    def test_443(self):
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
        expect = str(TypeMismatchInStatement(CallStmt(Id("fact"),[Id("x")])))
        self.assertTrue(TestChecker.test(input,expect,443))
        
    def test_444(self):
        """Created automatically"""
        input = r""" 
            Var: x;
Function: fact
Parameter: n
Body:
If n == 0 Then
Var: n;
If n Then
Return 1;
Else
Var: n;
Return n * fact (n - 1);
EndIf.
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
        expect = str(TypeMismatchInStatement(CallStmt(Id("fact"),[Id("x")])))
        self.assertTrue(TestChecker.test(input,expect,444))
        
    def test_445(self):
        """Created automatically"""
        input = r"""Function: main 
                    Body:
                        printStrLn(read(4));
                    EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,445))
        
    def test_446(self):
        """Created automatically"""
        input = Program([FuncDecl(Id("main"),[],([],[CallStmt(Id("printStrLn"),[CallExpr(Id("read"),[IntLiteral(4)])])]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,446))
        
    def test_447(self):
        """Created automatically"""
        input = r"""Function: main  
                   Body:
                        printStrLn();
                    EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,447))
        
    def test_448(self):
        """Created automatically"""
        input = Program([FuncDecl(Id("main"),[],([],[CallStmt(Id("printStrLn"),[])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,448))
        
    def test_449(self):
        """Created automatically"""
        input = r"""Function: main
                   Body: 
                        foo();
                   EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,449))
        
    def test_450(self):
        """Created automatically"""
        input = Program([FuncDecl(Id("main"),[],([],[CallExpr(Id("foo"),[])]))])
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,450))
        
    def test_451(self):
        """Created automatically"""
        input = r"""
        Function: main
Parameter: a[5], b
Body:
Var: i = 0;
While (i < 5) Do
If bool_of_string ("True") Then
Var: a;
a = int_of_string (read ());
b = float_to_int (a) +. 2.0;
EndIf.
a[i] = b +. 1.0;
i = i + a[i];
EndWhile.
EndBody.
    
        """
        expect = str(TypeMismatchInExpression(BinaryOp("+",Id("i"),ArrayCell(Id("a"),[Id("i")]))))
        self.assertTrue(TestChecker.test(input,expect,451))
        
    def test_452(self):
        """Created automatically"""
        input = r"""


        Function: foo
Parameter: foo
Body:
EndBody.
        Function: main
Parameter: a[5], b
Body:
Var: i = 0;
While (i < 5) Do
If bool_of_string ("True") Then
a[3 + foo(b)] = 4;
EndIf.
i = i + a[i];
EndWhile.
EndBody.
    
        """
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(Id("a"),[BinaryOp("+",IntLiteral(3),CallExpr(Id("foo"),[Id("b")]))]),IntLiteral(4))))
        self.assertTrue(TestChecker.test(input,expect,452))
        
    def test_453(self):
        """Created automatically"""
        input = r"""


        
        Function: main
Body:

    foo();
EndBody.

Function: foo
Body:
    Return foo();
EndBody.
    
        """
        expect = str(TypeMismatchInStatement(Return(CallExpr(Id("foo"),[]))))
        self.assertTrue(TestChecker.test(input,expect,453))
        
    def test_454(self):
        """Created automatically"""
        input = r"""


        
        Function: main
Body:

    foo();
EndBody.

Function: foo
Body:
    Var: x;
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
    Var: x;
    foo() = x;
EndBody.
    
        """
        expect = str(TypeMismatchInStatement(Assign(CallExpr(Id("foo"),[]),Id("x"))))
        self.assertTrue(TestChecker.test(input,expect,455))
        
    def test_456(self):
        """Created automatically"""
        input = r"""


        
        Function: main
Body:
foo(1.1);
EndBody.

Function: foo
Parameter: x
Body:
x=1;
Return;
EndBody.
    
        """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,456))
        
    def test_457(self):
        """Created automatically"""
        input = r"""


        
        Function: foo

            Parameter: x, y

            Body:

                Var: z;

                While (True) Do

                    z = foo(1, foo(x, True));

                EndWhile.

                Return y && z;

            EndBody.
        
        Function: main
        Body:
            Var: x;
            x = foo(x, x);
        EndBody.
    
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[Id("x"),Id("x")])))
        self.assertTrue(TestChecker.test(input,expect,457))
        
    def test_458(self):
        """Created automatically"""
        input = r"""


        
        Function: foo

            Parameter: x[5], y[5]
            Body:
            x = y;
            EndBody.
        
        Function: main
        Body:
        EndBody.
    
        """
        expect = str(TypeCannotBeInferred(Assign(Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,458))
        
    def test_459(self):
        """Created automatically"""
        input = r"""


        
        Function: foo

            Parameter: x[3]
            Body:
                Var: y[3] = {1,2,3};
                x[0] = y[1];
                x[1] = 3.0;
            EndBody.
        
        Function: main
        Body:
        EndBody.
    
        """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id("x"),[IntLiteral(1)]),FloatLiteral(3.0))))
        self.assertTrue(TestChecker.test(input,expect,459))
        
    def test_460(self):
        """Created automatically"""
        input = r"""


        
        Function: foo

            Parameter: x[3]
            Body:
                Var: y[3] = {1,2,3};
                x = y;
                x[1] = 3.0;
            EndBody.
        
        Function: main
        Body:
        EndBody.
    
        """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id("x"),[IntLiteral(1)]),FloatLiteral(3.0))))
        self.assertTrue(TestChecker.test(input,expect,460))
        
    def test_461(self):
        """Created automatically"""
        input = r"""


        
        Function: foo

            Parameter: x[3]
            Body:
               If x[1] Then
               x[2] = x[1];
               x[0] = 0;
EndIf.
            EndBody.
        
        Function: main
        Body:
        EndBody.
    
        """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id("x"),[IntLiteral(0)]),IntLiteral(0))))
        self.assertTrue(TestChecker.test(input,expect,461))
        
    def test_462(self):
        """Created automatically"""
        input = r"""


        
        Function: foo
            Body:
               Return 0;
            EndBody.
        
        Function: main
        Parameter: foo
        Body:
            foo = foo + foo();
        EndBody.
    
        """
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,462))
        
    def test_463(self):
        """Created automatically"""
        input = r"""


        
        Function: foo
            Body:
               Return 0;
            EndBody.
        
        Function: main
        Body:
            Var: a;
            a = foo;
        EndBody.
    
        """
        expect = str(Undeclared(Identifier(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,463))
        
    def test_464(self):
        """Created automatically"""
        input = r"""
        
        Function: main
        Body:
            Var: a;
            a = 1 + foo(3.5);
        EndBody.
        Function: foo
            Parameter: x
            Body:
               Return x + 5;
            EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("+",Id("x"),IntLiteral(5))))
        self.assertTrue(TestChecker.test(input,expect,464))
        
    def test_465(self):
        """Created automatically"""
        input = r"""
        Function: main
    Body:
        foo()[0] = 1;
    EndBody.

Function: foo
    Body:
        Return 0;
    EndBody.
       
        """
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id("foo"),[]),[IntLiteral(0)]),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,465))
        
    def test_466(self):
        """Created automatically"""
        input = r"""
        Var: test;
        Function: main
            Parameter: x
            Body:
            x = test[0];
            EndBody.
       
        """
        expect = str(TypeMismatchInExpression(ArrayCell(Id("test"),[IntLiteral(0)])))
        self.assertTrue(TestChecker.test(input,expect,466))
        
    def test_467(self):
        """Created automatically"""
        input = r"""
        Var: a;
Function: main
Body:
a=1;
EndBody.
Function: foo
Body:
a=1.1;
EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id("a"),FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input,expect,467))
        
    def test_468(self):
        """Created automatically"""
        input = r"""
        Var: a;
Function: main
Body:
foo();
a=1;
EndBody.
Function: foo
Body:
a=1.1;
EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id("a"),FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input,expect,468))
        
    def test_469(self):
        """Created automatically"""
        input = r"""
        Function : printX
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
                printX(m); 
                Return 0;
            EndBody.
        """
        expect = str(Undeclared(Identifier(),"m"))
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
        input = r"""Function: main
        Parameter: n
        Body:
        Var:factorial=1;
        print("Enter integer: ");
        read();
        For (i=0, i<=n, 1) Do
            factorial=factorial*i;
        EndFor.
        printStrLn(string_of_int(factorial));
        Return factorial;
        EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("read"),[])))
        self.assertTrue(TestChecker.test(input,expect,483))
        
    def test_484(self):
        """Created automatically"""
        input = r"""Function: main
        Parameter: n
        Body:
            Var: t1 = 0, t2 = 1, nextTerm = 0, i;
            print("Enter the number of terms: ");
            n = int_of_string(read());
            print("Fibonacci Series: ");
            For (i = 1, i <= n, 1) Do
                If(i == 1) Then
                print(string_of_int(t1));
                Continue;
                EndIf.
            If(i == 2) Then
                print("t2");
        Continue;
        EndIf.
        nextTerm = t1 + t2;
        t1 = t2;
        t2 = nextTerm;
        
        print(string_of_int(nextTerm));
    EndFor.
    Return 0;
    EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,484))
        
    def test_485(self):
        """Created automatically"""
        input = r"""Function: main
        Parameter: octalNumber
        Body:
        Var: decimalNumber = 0, i = 0, rem;
        While (octalNumber != 0) Do
            rem = octalNumber % 10;
            octalNumber =octalNumber \ 10;
            decimalNumber =decimalNumber  + rem * pow(8,i);
            i=i+1;
        EndWhile.
    Return decimalNumber;
    EndBody.
    Function: pow
    Parameter: x,y
    Body:
    If x == 0 Then
    Return 1;
    EndIf.
    Return x * pow(x-1,y);
    EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,485))
        
    def test_486(self):
        """Created automatically"""
        input = r""" 
        Function: func2 
        Parameter: n
        Body: 
            If n == 0 Then
                Return 1;
            Else
                Return n * func2 (n - 1);
            EndIf.
        EndBody.
        Function: main
        Body:
        Var: a;
            a =func1(func2(3))+23 - foo(goo(func1(a)));
        EndBody.
        Function: goo 
        Parameter: n
        Body: ** Xin chao**
        Var: string = "Xin chao";
        Return 108;
        EndBody.
        Function: func1
        Parameter: x
        Body:
        Var: a, b, c;
            If(x == ((False||True) && (a > b + c))) Then
                a = b - c;
            Else
                a = b + c;
                x = True;
            EndIf.
        EndBody.
        Function: foo 
        Parameter: n
        Body: 
            While(1) Do
                n = True;
            EndWhile.
        EndBody.
                """
        expect = str(TypeCannotBeInferred(Assign(Id("a"),BinaryOp("-",BinaryOp("+",CallExpr(Id("func1"),[CallExpr(Id("func2"),[IntLiteral(3)])]),IntLiteral(23)),CallExpr(Id("foo"),[CallExpr(Id("goo"),[CallExpr(Id("func1"),[Id("a")])])])))))
        self.assertTrue(TestChecker.test(input,expect,486))
        
    def test_487(self):
        """Created automatically"""
        input = r"""Function: main 
        Body:
        Var: n;
            If n == 0 Then
                Break;
            EndIf.
        EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,487))
        
    def test_488(self):
        """Created automatically"""
        input = r"""Function: main 
        Body:
            If n == 0 Then
                x = 3;
            ElseIf x != 2 Then
                check = False;
            EndIf.
        EndBody."""
        expect = str(Undeclared(Identifier(),"n"))
        self.assertTrue(TestChecker.test(input,expect,488))
        
    def test_489(self):
        """Created automatically"""
        input = r"""Var: a[2] = {True,{2,3}}, str = "string",c,d;
        Function: func
        Body:
        Var: j,k=2,b=1.1234e-3,i;
            If (((a + 5) * (j-6)) !=0) || ((k*7) >=100) Then
               
                a[i] = int_of_float(b +. 1.0);
                b = float_of_int(i - int_of_float(b) * a) -. b \. c -. -.d;
            EndIf.
            Return a+func(123);
        EndBody.
        Function: main
        Body:
            func();
            Return 0;
        EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("+",Id("a"),IntLiteral(5))))
        self.assertTrue(TestChecker.test(input,expect,489))
        
    def test_490(self):
        """Created automatically"""
        input = r"""** this is a comment **
        Var: a[2] = {True,{2,3}}, str = "string";
        Function: func
        Body:
            If (a + 5) && (j-6) || (k*7) Then
                ** this is another comment **
                a[i] = b +. 1.0;
                b = i - b * a -. b \ c - -.d;
            EndIf.
            Return a+func();
        EndBody.
        Function: main
        Body:
            func();
            Return 0;
        EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("+",Id("a"),IntLiteral(5))))
        self.assertTrue(TestChecker.test(input,expect,490))
        
    def test_491(self):
        """Created automatically"""
        input = r"""Var: a = 5;

        Function: main
        Parameter: a
        Body:
        Var:b[2];
            If bool_of_string ("True") Then
                a = int_of_string (read ());
                b = float_of_int (a) +. 2.0;
            ElseIf a == 5 Then
                a = a + main(123);
            ElseIf a == 6 Then
                a = a * 2;
                Return string_of_int(a);
                Break;
            Else Continue;
            EndIf.
        EndBody."""
        expect = str(Undeclared(Function(),"float_of_int"))
        self.assertTrue(TestChecker.test(input,expect,491))
        
    def test_492(self):
        """Created automatically"""
        input = r"""Function: main
                    Parameter: x
                    Body:
                    Var: i, result;
                        For (i = 1, i <= x*x*x,i + x ) Do
                            result = i * i + i \ --1 % i--i;
                        EndFor.
                        Return result;
                    EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,492))
        
    def test_493(self):
        """Created automatically"""
        input = r"""
            Function: sqrt
            Parameter: x
            Body:
                Var: i;
            While (i*i) < x Do
                    i = i - -1;
                EndWhile.
                Return i-1;
            EndBody.
            Function: main
            Parameter: n,x
            Body:
                Var: i;
                For (i = 0, i < sqrt(n), 2) Do
                    x = i + n;
                EndFor.
            EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,493))
        
    def test_494(self):
        """Created automatically"""
        input = r"""Function: main
        Body:
            m = test2(a,b) + main (x);
        EndBody.
        Function: test2
        Body:
            Do
                If(z == 1) Then
                    x = !a;
                EndIf.
            While x
            EndDo.
        EndBody."""
        expect = str(Undeclared(Identifier(),"m"))
        self.assertTrue(TestChecker.test(input,expect,494))
        
    def test_495(self):
        """Created automatically"""
        input = r"""Function: main 
        Body:
        Var:x;
            While x>1 Do
            Var: i,a = 4;
                For (i = 100,True, i-1) Do
                    If -a<-3 Then
                        Break;
                    EndIf.
                    a = a -1;
                EndFor.
            EndWhile.
        EndBody."""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,495))
        
    def test_496(self):
        """Created automatically"""
        input = r"""
        Function: main
        Parameter: a[123], b, c[13][14][15]
        Body:
        Var: y;
            If a[12] > b Then
                Var: x;
                Do
                    a = b + 3; 
                    c[2][3] = int_of_float(c[4][2]+.10.2*.main(a,b,c))+a[2+int_of_float(main({2},a[3],a))+int_of_float(c[4])]; 
                While (x == y)  EndDo.
            EndIf.
        EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("a"),BinaryOp("+",Id("b"),IntLiteral(3)))))
        self.assertTrue(TestChecker.test(input,expect,496))
        
    def test_497(self):
        """Created automatically"""
        input = r"""Function: main
            Parameter: a,b
            Body:
                a = "string 1";
                b = "string 2";
                Return a+b;
            EndBody. """
        expect = str(TypeMismatchInExpression(BinaryOp("+",Id("a"),Id("b"))))
        self.assertTrue(TestChecker.test(input,expect,497))
        
    def test_498(self):
        """Created automatically"""
        input = r""" 
            Function: main 
            Body:
                Var: x, y[1][3]={{{12,1}, {12., 12e3}},{23}, {13,32}};
                Var: b = True, c = False,i;
                For (i = 0, i < 10, 2) Do
                    For (i = 1, i < x*x , i + 1 ) Do
                    Var: a,z;
                    Var:j;
                        If(z && False) Then
                            Break;
                        ElseIf 1 Then
                            a=a-1;
                        EndIf.
                        For( j = 1, j < x*x ,j + 1) Do
                            Do
                                a = a * 1;
                            While( 1 ) 
                            EndDo.
                        EndFor.
                    EndFor.
                EndFor.
            EndBody.
            """
        expect = str(TypeMismatchInStatement(If([(BinaryOp("&&",Id("z"),BooleanLiteral(False)),[],[Break()]),(IntLiteral(1),[],[Assign(Id("a"),BinaryOp("-",Id("a"),IntLiteral(1)))])],([],[]))))
        self.assertTrue(TestChecker.test(input,expect,498))
        
    def test_499(self):
        """Created automatically"""
        input = r""" 
            Var: b;
                Function: main
                Body:
                    Var: a = 5,x;
                    a = a + foo(x);
                    b = 5.2;
                    Return 3;
                EndBody.

                Function: foo
                Parameter: a
                Body:
                    Var: c = 5;
                    Return c;
                EndBody.
            """
        expect = str(TypeCannotBeInferred(Assign(Id("a"),BinaryOp("+",Id("a"),CallExpr(Id("foo"),[Id("x")])))))
        self.assertTrue(TestChecker.test(input,expect,499))
        
    def test_500(self):
        """Created automatically"""
        input = r""" 
            Var: x, y;
            Function: main 
            Body:
                y = 1;
                While(True) Do
                Var: z;
                Var: y;
                If (z) Then
                Var: y;
                y = 1;
                x = 3;
               
                ElseIf (z) Then
                 Var: z;
                z = 1;
                y = 3.0;
                
                Else 
                y = 1.0; 
                x = 3.0;
                EndIf.
                 EndWhile.
            EndBody.
            """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),FloatLiteral(3.0))))
        self.assertTrue(TestChecker.test(input,expect,500))
        
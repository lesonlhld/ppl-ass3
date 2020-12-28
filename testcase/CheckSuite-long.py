import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):

    # Predefined test cases
    def test_undeclared_function(self):
        """Simple program: main"""
        input = """Function: main
                   Body: 
                        foo();
                        Return;
                   EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_diff_numofparam_stmt(self):
        """Complex program"""
        input = """Function: main  
                   Body:
                        printStrLn();
                        Return;
                    EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_diff_numofparam_expr(self):
        """More complex program"""
        input = """Function: main 
                    Body:
                        printStrLn(read(4));
                        Return;
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
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,405))

    # Test entry point
    def test_no_entry_point_1(self):
        """Simple program: main"""
        input = """Var: x, y, z;"""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_no_entry_point_2(self):
        """Simple program: main"""
        input = """Var: x, main, z;"""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_no_entry_point_3(self):
        """Simple program: main"""
        input = """Var: x, main, z;
        Function: foo
            Body:
                Return;
            EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_valid_entry_point(self):
        """Simple program: main"""
        input = """Var: x, y, z;
        Function: main
            Body:
                Return;
            EndBody."""
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,409))

    # Test redeclare variable
    def test_redeclare_variable_1(self):
        """Simple program: main"""
        input = """Var: x, x, z;
        Function: main
            Body:
                Return;
            EndBody."""
        expect = str(Redeclared(Variable(), "x"))
        self.assertTrue(TestChecker.test(input,expect,410))    

    def test_redeclare_variable_2(self):
        """Simple program: main"""
        input = """Var: x, y[3] = {1,2,3}, z;
        Var: m, n[2][3], y = 1;
        Function: main
            Body:
                Return;
            EndBody."""
        expect = str(Redeclared(Variable(), "y"))
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_redeclare_variable_3(self):
        """Simple program: main"""
        input = """
        Function: main
            Parameter: x, y[4], z
            Body:
                Var: y = {1,2,3}, m, n;
                Return;
            EndBody."""
        expect = str(Redeclared(Variable(), "y"))
        #self.assertTrue(TestChecker.test(input,expect,412)) 

    # Test valid var declare
    def test_valid_declare_variable(self):
        """Simple program: main"""
        input = """
        Var: x, y, z;
        Function: main
            Body:
                Var: x, y, z, main;
                Return;
            EndBody."""
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,413)) 

    # Test redeclare parameter
    def test_redeclare_parameter(self):
        """Simple program: main"""
        input = """
        Function: main
            Parameter: x,x,y
            Body:
                Return;
            EndBody."""
        expect = str(Redeclared(Parameter(), "x"))
        self.assertTrue(TestChecker.test(input,expect,414))    

    # Test valid param declare
    def test_valid_declare_parameter(self):
        """Simple program: main"""
        input = """Var: x, y, z;
        Function: main
            Parameter: x, y, z, main
            Body:
                Return;
            EndBody."""
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,415))

    # Test redeclare function
    def test_redeclare_function_1(self):
        """Simple program: main"""
        input = """Var: x, main, y;
        Function: main
            Body:
                Return;
            EndBody."""
        expect = str(Redeclared(Function(), "main"))
        self.assertTrue(TestChecker.test(input,expect,416))    

    def test_redeclare_function_2(self):
        """Simple program: main"""
        input = """
        Function: foo
            Body:
                Return;
            EndBody.
        Function: main
            Body:
                Return;
            EndBody.
        Function: foo
            Parameter: x,y,z
            Body:
                Return;
            EndBody."""
        expect = str(Redeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input,expect,417))   

    # Test undeclare identifier
    def test_undeclare_identifier_1(self):
        """Simple program: main"""
        input = """
        Function: main
            Body:
                x = 1;
                Return;
            EndBody."""
        expect = str(Undeclared(Identifier(), "x"))
        self.assertTrue(TestChecker.test(input,expect,418))       

    def test_undeclare_identifier_2(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: main
            Body:
                x = y + 1;
                Return;
            EndBody."""
        expect = str(Undeclared(Identifier(), "y"))
        self.assertTrue(TestChecker.test(input,expect,419)) 

    def test_undeclare_identifier_3(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: foo
            Parameter: x
            Body:
                x = 1.1;
                Return x;
            EndBody.        
        Function: main
            Body:
                y = foo(x) +. 2.2;
                Return;
            EndBody."""
        expect = str(Undeclared(Identifier(), "y"))
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_undeclare_identifier_4(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: foo
            Parameter: x
            Body:
                x = 1;
                Return x;
            EndBody.        
        Function: main
            Body:
                x = foo + 1;
                Return;
            EndBody."""
        expect = str(Undeclared(Identifier(), "foo"))
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_undeclare_identifier_5(self):  # one error ???
        """Simple program: main"""
        input = """
        Var: x;
        Function: main
            Body:
                Var: y;
                x = y()[1] + 1;
                Return;
            EndBody."""
        expect = str(Undeclared(Function(), "y"))
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_undeclare_identifier_6(self):  # one error ???
        """Simple program: main"""
        input = """
        Var: x;
        Function: main
            Body:
                Var: y;
                x()[1] = y + 1;
                Return;
            EndBody."""
        expect = str(Undeclared(Function(), "x"))
        self.assertTrue(TestChecker.test(input,expect,423))

    # Test undeclare function
    def test_undeclare_function_1(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: main
            Body:
                x = foo(1);
                Return;
            EndBody."""
        expect = str(Undeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input,expect,424)) 

    def test_undeclare_function_2(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: main
            Body:
                Var: foo;
                x = foo(1);
                Return;
            EndBody."""
        expect = str(Undeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input,expect,425)) 

    def test_undeclare_function_3(self):    # ???
        """Simple program: main"""
        input = """
        Var: x;
        Function: main
            Body:
                Var: foo;
                x = 1 + 2 - foo(1);
                Return;
            EndBody.
        Function: foo
            Parameter: x
            Body:
                Return x;
            EndBody."""
        expect = str(Undeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input,expect,426)) 

    # Test unidentical array dimension
    def test_unidentical_array_dimension_1(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: main
            Parameter: x[2][3], y
            Body:
                x = {1,2,3};
                Return;
            EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"), ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))))
        self.assertTrue(TestChecker.test(input,expect,427))    

    def test_unidentical_array_dimension_2(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: main
            Body:
                Var: x[2][3];
                Var: y[3][2] = { {1,2}, {3,4}, {5,6} };
                x = y;
                Return;
            EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"), Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,428))    

    # Test identical array dimension
    def test_identical_array_dimension(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: main
            Body:
                Var: x[3][2] = { {6,5}, {4,3}, {2,1} };
                Var: y[3][2] = { {1,2}, {3,4}, {5,6} };
                x = y;
                Return;
            EndBody."""
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,429)) 

    # Test unidentical array element type
    def test_unidentical_array_eletype(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: main
            Body:
                Var: x[3][2] = { {6.6,5.5}, {4.4,3.3}, {2.2,1.1} };
                Var: y[3][2] = { {1,2}, {3,4}, {5,6} };
                x = y;
                Return;
            EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"), Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,430))

    # Test invalid array indexing
    def test_invalid_array_index_1(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: main
            Body:
                Var: x[3][2] = { {6.6,5.5}, {4.4,3.3}, {2.2,1.1} };
                x[2] = {1.1, 2.2};
                Return;
            EndBody."""
        expect = str(TypeMismatchInExpression(ArrayCell(Id("x"), [IntLiteral(2)])))
        self.assertTrue(TestChecker.test(input,expect,431))    

    def test_invalid_array_index_2(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: main
            Body:
                Var: x[3][2] = { {6.6,5.5}, {4.4,3.3}, {2.2,1.1} };
                Var: y = 5, z = 1.2;
                x[y + y*2 - 4 \\ 2 % 2][z +. z *. 2.2] = 1.1;
                Return;
            EndBody."""
        expect = str(TypeMismatchInExpression(ArrayCell(Id("x"),[BinaryOp("-",BinaryOp("+",Id("y"),BinaryOp("*",Id("y"),IntLiteral(2))),BinaryOp("%",BinaryOp("\\",IntLiteral(4),IntLiteral(2)),IntLiteral(2))),BinaryOp("+.",Id("z"),BinaryOp("*.",Id("z"),FloatLiteral(2.2)))])))
        self.assertTrue(TestChecker.test(input,expect,432))

    # Test invalid unary op
    def test_invalid_unary_op(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: main
            Body:
                Var: x, y = 1e3, z = 10;
                z = - z;
                x = !!x;
                y = -. -. -.y;
                x = !(-x);
                Return;
            EndBody."""
        expect = str(TypeMismatchInExpression(UnaryOp("-", Id("x"))))
        self.assertTrue(TestChecker.test(input,expect,433))            

    # Test invalid binary op
    def test_invalid_binary_op_1(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: main
            Body:
                Var: x,y,z;
                x = (1 + 2 *3 \\ 4 % 5) * 6;
                y = 1.1 *. 2.2 +. 3.3 -. 4.4 \\. 5.5;
                z = x + y;
                Return;
            EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("+", Id("x"), Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,434))        

    def test_invalid_binary_op_2(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: main
            Body:
                Var: x,y,z;
                Var: t;
                t = !x && y || !z;
                t = !x + 1;
                Return;
            EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("+", UnaryOp("!", Id("x")), IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,435)) 

    def test_invalid_binary_op_3(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: main
            Body:
                Var: x,y,z;
                Var: t, m, n, k = True;
                t = x * y - z * (x \\ 2 + 1);
                k = (m =/= n) && ( m >=. n) || (m <. n);
                x = t >= z;
                Return;
            EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"), BinaryOp(">=", Id("t"), Id("z")))))
        self.assertTrue(TestChecker.test(input,expect,436))

    # Test type cannot be inferred
    def test_type_cannot_be_inferred_1(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: main
            Parameter: x
            Body:
                Var: y;
                x = y;
                Return;
            EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id("x"), Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_type_cannot_be_inferred_2(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: main
            Parameter: x[2][3]
            Body:
                Var: y[2][3];
                x = y;
                Return;
            EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id("x"), Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_type_cannot_be_inferred_3(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: main
            Parameter: x
            Body:
                Var: y, a = 10;
                y = a + foo(x);
                Return;
            EndBody.
        Function: foo
            Parameter: x
            Body:
                Return 1;
            EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id("y"), BinaryOp("+", Id("a"), CallExpr(Id("foo"), [Id("x")])))))
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_type_cannot_be_inferred_4(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: main
            Parameter: x
            Body:
                Var: y, a = True;
                y = !a && !foo(x);
                Return;
            EndBody.
        Function: foo
            Parameter: x
            Body:
                Return False;
            EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id("y"), BinaryOp("&&", UnaryOp("!",Id("a")), UnaryOp("!", CallExpr(Id("foo"), [Id("x")]))))))
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_type_cannot_be_inferred_5(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: main
            Parameter: x
            Body:
                Var: y, a = True;
                y = !a && foo(x)[1];
                Return;
            EndBody.
        Function: foo
            Parameter: x
            Body:
                Return {True, False};
            EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id("y"), BinaryOp("&&", UnaryOp("!",Id("a")), ArrayCell(CallExpr(Id("foo"), [Id("x")]), [IntLiteral(1)])))))
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_type_cannot_be_inferred_6(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: main
            Body:
                foo(x);
                Return;
            EndBody.
        Function: foo
            Parameter: x
            Body:
                Return;
            EndBody."""
        expect = str(TypeCannotBeInferred(CallStmt(Id("foo"), [Id("x")])))
        self.assertTrue(TestChecker.test(input,expect,442))

    # Test voidtype
    def test_voidtype_in_assign(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: main
            Body:
                foo(1);
                x = foo(1);
                Return;
            EndBody.
        Function: foo
            Parameter: x
            Body:
                Return;
            EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"), CallExpr(Id("foo"), [IntLiteral(1)]))))
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_voidtype_in_expression(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: main
            Body:
                foo(1);
                x = foo(1) + 2;
                Return;
            EndBody.
        Function: foo
            Parameter: x
            Body:
                Return;
            EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("+", CallExpr(Id("foo"), [IntLiteral(1)]), IntLiteral(2))))
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_voidtype_in_funccall(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: main
            Body:
                foo(1);
                foo(foo(10));
                Return;
            EndBody.
        Function: foo
            Parameter: x
            Body:
                Return;
            EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"), [CallExpr(Id("foo"), [IntLiteral(10)])])))
        self.assertTrue(TestChecker.test(input,expect,445))


    # Test return type
    def test_returntype_1(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: main
            Body:
                x = foo(10) +. 1.1;
                Return;
            EndBody.
        Function: foo
            Parameter: x
            Body:
                Return 1;
            EndBody."""
        expect = str(TypeMismatchInStatement(Return(IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_returntype_2(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: foo
            Parameter: x
            Body:
                Return 1;
            EndBody.
        Function: main
            Body:
                x = foo(10) +. 1.1;
                Return;
            EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("+.", CallExpr(Id("foo"), [IntLiteral(10)]), FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_returntype_3(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: main
            Body:
                foo(10);
                Return;
            EndBody.
        Function: foo
            Parameter: x
            Body:
                Return 1;
            EndBody."""
        expect = str(TypeMismatchInStatement(Return(IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_returntype_4(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: foo
            Parameter: x[3]
            Body:
                x = {4,5,6};
                Return;
            EndBody.
        Function: main
            Body:
                foo(goo());
                Return;
            EndBody.
        Function: goo
            Body:
                Return {1,2,3,4};
            EndBody."""
        expect = str(TypeMismatchInStatement(Return(ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))))
        #self.assertTrue(TestChecker.test(input,expect,449))

    def test_returntype_5(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: foo
            Parameter: x[3]
            Body:
                x = {4,5,6};
                Return 1;
            EndBody.
        Function: main
            Body:
                x = foo(goo()) + 1;
                Return;
            EndBody.
        Function: goo
            Body:
                Return {1,2,3,4};
            EndBody."""
        expect = str(TypeMismatchInStatement(Return(ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))))
        #self.assertTrue(TestChecker.test(input,expect,450))

    def test_returntype_6(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: foo
            Parameter: x[3]
            Body:
                While (True) Do
                    x = {4,5,6};
                    Return 1;
                EndWhile.
                Return 1;
            EndBody.
        Function: main
            Body:
                x = foo(goo()) +. 1.1;
                Return;
            EndBody.
        Function: goo
            Body:
                Return {1,2,3};
            EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("+.", CallExpr(Id("foo"), [CallExpr(Id("goo"), [])]), FloatLiteral(1.1))))
        #self.assertTrue(TestChecker.test(input,expect,451))

    def test_returntype_7(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: foo
            Parameter: x[3]
            Body:
                While (True) Do
                    x = {4,5,6};
                    Return 1;
                EndWhile.
                Return 1;
            EndBody.
        Function: main
            Body:
                x = foo(goo()) + 1;
                Return;
            EndBody.
        Function: goo
            Body:
                If (1 > 2) Then Return {1,2,3};
                Else Return {1.1, 2.2, 3.3};
                EndIf.
            EndBody."""
        expect = str(TypeMismatchInStatement(Return(ArrayLiteral([FloatLiteral(1.1), FloatLiteral(2.2), FloatLiteral(3.3)]))))
        #self.assertTrue(TestChecker.test(input,expect,452))

    def test_returntype_8(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: foo
            Parameter: x[3]
            Body:
                Return;
            EndBody.
        Function: main
            Body:
                Return foo({1,2,3});
            EndBody."""
        expect = str(TypeMismatchInStatement(Return(CallExpr(Id("foo"), [ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)])]))))
        self.assertTrue(TestChecker.test(input,expect,453))

    # Test assign
    def test_assign_1(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: main
            Body:
                x = x + foo(x);
                Return;
            EndBody.
        Function: foo
            Parameter: x
            Body:
                Return 1;
            EndBody."""
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_assign_2(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: main
            Body:
                x = foo(x) + x;
                Return;
            EndBody.
        Function: foo
            Parameter: x
            Body:
                Return 1;
            EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id("x"), BinaryOp("+", CallExpr(Id("foo"), [Id("x")]), Id("x")))))
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_assign_3(self):
        """Simple program: main"""
        input = """
        Function: main
            Body:
                Var: x, y[5] = {1,2,3,4,5};
                x = y;
                Return;
            EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"), Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_assign_4(self):
        """Simple program: main"""
        input = """
        Function: main
            Body:
                Var: x[3], y[5] = {1,2,3,4,5};
                x = y;
                Return;
            EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"), Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_assign_5(self):
        """Simple program: main"""
        input = """
        Function: main
            Body:
                Var: x[5] = {1.1, 2.2, 3.3, 4.4, 5.5}, y[5] = {1,2,3,4,5};
                y = foo(1);
                foo(2)[0] = x[3];
                Return;
            EndBody.
        Function: foo
            Parameter: x
            Body:
                Return {5,4,3,2,1};
            EndBody.
            """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(CallExpr(Id("foo"), [IntLiteral(2)]), [IntLiteral(0)]), ArrayCell(Id("x"), [IntLiteral(3)]))))
        #self.assertTrue(TestChecker.test(input,expect,458))

    def test_assign_6(self):
        """Simple program: main"""
        input = """
        Var: x[5];
        Function: main
            Body:
                Var: y[5] = {1,2,3,4,5};
                x = {1.1, 2.2, 3.3, 4.4, 5.5};
                y = foo(1);
                foo(y[4] + 2)[0] = y[0] + 1;
                Return;
            EndBody.
        Function: foo
            Parameter: y
            Body:
                y = x[1];
                Return {5,4,3,2,1};
            EndBody.
            """
        expect = str(TypeMismatchInStatement(Assign(Id("y"), ArrayCell(Id("x"), [IntLiteral(1)]))))
        #self.assertTrue(TestChecker.test(input,expect,459))

    def test_assign_7(self):
        """Simple program: main"""
        input = """
        Function: goo
            Parameter: x
            Body:
                Return True;
            EndBody.
        Function: main
            Body:
                Var: a, b;
                b = goo(a < b);
                Return;
            EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("b"), CallExpr(Id("goo"), [BinaryOp("<", Id("a"), Id("b"))]))))
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_assign_8(self):
        """Simple program: main"""
        input = """
        Function: foo
            Parameter: x
            Body:
                Return {True,False};
            EndBody.
        Function: main
            Body:
                Var: a,b;
                foo(True)[0] = foo(1)[1];
                Return;
            EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"), [IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input,expect,461))

    # Test function call
    def test_function_call_1(self):
        """Simple program: main"""
        input = """
        Var: x[2][2] = {{1.1, 2.2},{3.3, 4.4}};
        Function: main
            Body:
                x = foo(x);
                Return;
            EndBody.
        Function: foo
            Parameter: y[2][2]
            Body:
                Return {{1,2},{3,4}};
            EndBody.
            """
        expect = str(TypeMismatchInStatement(Return(ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)]),ArrayLiteral([IntLiteral(3),IntLiteral(4)])]))))
        #self.assertTrue(TestChecker.test(input,expect,462))

    def test_function_call_2(self):
        """Simple program: main"""
        input = """
        Function: main
            Parameter: x, y, z[2]
            Body:
                While (x > int_of_float(z[x])) Do
                    y = z[1];
                    main(1, 1.1, {1,2});
                EndWhile.
                Return;
            EndBody.
            """
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"), [IntLiteral(1), FloatLiteral(1.1), ArrayLiteral([IntLiteral(1), IntLiteral(2)])])))
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_function_call_3(self):
        """Simple program: main"""
        input = """
        Var: t[2];
        Function: foo
            Parameter: x, y, z[2]
            Body:
                While (x > int_of_float(z[x])) Do
                    y = z[1];
                    x = foo(1, 1.1, t);
                EndWhile.
                Return 1;
            EndBody.
        Function: main
            Body:
                t = {1,2};
                Return;
            EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("t"), ArrayLiteral([IntLiteral(1), IntLiteral(2)]))))
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_function_call_4(self):
        """Simple program: main"""
        input = """
        Var: t[2];
        Function: foo
            Parameter: x, y, z[2]
            Body:
                While (x > int_of_float(z[x])) Do
                    y = z[1];
                    x = foo(1, 1.1, t);
                EndWhile.
                Return 1;
            EndBody.
        Function: main
            Body:
                t = {1.1,2.2};
                foo(1, 1.1, t);
                Return;
            EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"), [IntLiteral(1), FloatLiteral(1.1), Id("t")])))
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_function_call_5(self):
        """Simple program: main"""
        input = """
        Function: main
            Body:
                Var: x;
                x = foo(foo(1) > 1);
                Return;
            EndBody.
        Function: foo
            Parameter: x
            Body:
                Return 1;
            EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"), [BinaryOp(">", CallExpr(Id("foo"), [IntLiteral(1)]), IntLiteral(1))])))
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_function_call_6(self):
        """Simple program: main"""
        input = """
        Function: main
            Body:
                Var: x;
                x = foo(1, foo(1.1, 1));
                Return;
            EndBody.
        Function: foo
            Parameter: x, y
            Body:
                Return 1;
            EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"), [FloatLiteral(1.1), IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_function_call_7(self):
        """Simple program: main"""
        input = """
        Function: foo
            Parameter: x
            Body:
                x = 1;
                Return {1,2};
            EndBody.
        Function: main
            Body:
                foo(goo(1)[0])[0] = foo(1)[1];
                Return;
            EndBody.
        Function: goo
            Parameter: x
            Body:
                Return {0};
            EndBody."""
        expect = str(TypeCannotBeInferred(Assign(    ArrayCell(CallExpr(Id("foo"), [ArrayCell(CallExpr(Id("goo"), [IntLiteral(1)]), [IntLiteral(0)])]), [IntLiteral(0)]),      ArrayCell(CallExpr(Id("foo"), [IntLiteral(1)]), [IntLiteral(1)])     )))
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_function_call_8(self):
        """Simple program: main"""
        input = """
        Function: foo
            Parameter: x
            Body:
                x = 1;
                Return;
            EndBody.
        Function: main
            Body:
                Var: x;
                foo(goo(x));
                Return;
            EndBody.
        Function: goo
            Parameter: x
            Body:
                Return 1;
            EndBody."""
        expect = str(TypeCannotBeInferred(CallStmt(Id("foo"), [CallExpr(Id("goo"), [Id("x")])])))
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_function_call_9(self):
        """Simple program: main"""
        input = """
        Function: foo
            Parameter: x, y, z
            Body:
                Return False;
            EndBody.
        Function: main
            Body:
                Var: x, y;
                x = foo(True, 1, foo(x, y, False));
                x = y;
                Return;
            EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"), Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_function_call_10(self):
        """Simple program: main"""
        input = """
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
            Parameter: x,y,z
            Body:
                If (True) Then
                    main(1, 2.2, foo(x, y));
                EndIf.
                Return;
            EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"), [Id("x"), Id("y")])))
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_function_call_11(self):
        """Simple program: main"""
        input = """
        Function: foo
            Parameter: x, y
            Body:
                Return False;
            EndBody.
        Function: main
            Parameter: x,y,z
            Body:
                Var: a, b;
                If (True) Then
                    main(1, 2.2, foo(x, y));
                EndIf.
                a = x;
                b = y;
                main(a, b, "Hello");
                Return;
            EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"), [Id("a"), Id("b"), StringLiteral("Hello")])))
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_function_call_12(self):
        """Simple program: main"""
        input = """
        Function: foo
            Parameter: x, y
            Body:
                Var: z;
                z = foo(y+1, foo(x, 1.1));
                Return z;
            EndBody.
        Function: main
            Body:
                Return;
            EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"), [Id("x"), FloatLiteral(1.1)])))
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_function_call_13(self):
        """Simple program: main"""
        input = """
        Function: foo
            Parameter: x, y
            Body:
                Var: z;
                z = foo( float_to_int(y) +. foo(1.1, 1.1) , int_of_float(foo(x, 1)) );
                Return z;
            EndBody.
        Function: main
            Body:
                Return;
            EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"), [FloatLiteral(1.1), FloatLiteral(1.1)])))
        self.assertTrue(TestChecker.test(input,expect,474))


    # def test_function_call_8(self):   which error ???
    #     """Simple program: main"""
    #     input = """
    #     Function: foo
    #         Parameter: x
    #         Body:
    #             Return {0};
    #         EndBody.
    #     Function: main
    #     Body:
    #         foo(goo(1)[0])[0] = goo(foo(1)[0])[0];
    #         Return;
    #     EndBody.
    #     Function: goo
    #         Parameter: x
    #         Body:
    #             Return {0};
    #         EndBody."""
    #     expect = str(TypeMismatchInExpression(CallExpr(Id("foo"), [FloatLiteral(1.1), IntLiteral(1)])))
    #     self.assertTrue(TestChecker.test(input,expect,469))

    # Test if
    def test_if_1(self):
        """Simple program: main"""
        input = """
        Function: main
            Body:
                Var: x;
                If (x > 1) Then Return 1;
                ElseIf (x < 1) Then
                    Var: y;
                    y = x + 1;
                    Return 2;
                Else
                    y = x - 1;
                    Return 3;
                EndIf.
            EndBody."""
        expect = str(Undeclared(Identifier(), "y"))
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_if_2(self):
        """Simple program: main"""
        input = """
        Function: main
            Body:
                Var: x;
                If (foo(x)) Then
                EndIf.
                Return;
            EndBody.
        Function: foo
            Parameter: x
            Body:
                Return True;
            EndBody."""
        expect = str(TypeCannotBeInferred(If([(CallExpr(Id("foo"), [Id("x")]), [], [])], ([],[]))))
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_if_3(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: main
            Body:
                If (foo(1.1)) Then
                    x = 1;
                EndIf.
                Return;
            EndBody.
        Function: foo
            Parameter: y
            Body:
                y = x;
                Return True;
            EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("y"), Id("x"))))
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_if_4(self):
        """Simple program: main"""
        input = """
        Function: main
            Parameter: x,y
            Body:
                If (True) Then
                    x = True;
                    main(1, 2.2);
                EndIf.
                Return;
            EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"), [IntLiteral(1), FloatLiteral(2.2)])))
        self.assertTrue(TestChecker.test(input,expect,478))

    # Test while, dowhile
    def test_while_1(self):
        """Simple program: main"""
        input = """
        Var: x = 1.1, y;
        Function: main
            Parameter: x
            Body:
                While (y > x) Do
                    foo(x);
                EndWhile.
                Return;
            EndBody.
        Function: foo
            Parameter: z
            Body:
                z = x + y;
                Return;
            EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("+", Id("x"), Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_while_2(self):
        """Simple program: main"""
        input = """
        Var: x = 1.1, y;
        Function: main
            Parameter: x
            Body:
                While (foo(x + 1)) Do
                    While (y >. float_to_int(x)) Do
                        Return x;
                    EndWhile.
                EndWhile.
                Return int_of_float(y);
            EndBody.
        Function: foo
            Parameter: z
            Body:
                z = x +. y;
                Return True;
            EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("z"), BinaryOp("+.", Id("x"), Id("y")))))
        self.assertTrue(TestChecker.test(input,expect,480))

    # Test for
    def test_for_1(self):
        """Simple program: main"""
        input = """
        Function: main
            Body:
                For (x = 5, True, 1) Do
                EndFor.
                Return;
            EndBody."""
        expect = str(Undeclared(Identifier(), "x"))
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_for_2(self):
        """Simple program: main"""
        input = """
        Function: foo
            Body:
                Return 1;
            EndBody.
        Function: main
            Body:
                For (foo = 5, True, 1) Do
                EndFor.
                Return;
            EndBody."""
        expect = str(Undeclared(Identifier(), "foo"))
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_for_3(self):
        """Simple program: main"""
        input = """
        Function: foo
            Parameter: x
            Body:
                Return 1.1;
            EndBody.
        Function: main
            Body:
                Var: x, y;
                For (x = 5, y, foo(False && y)) Do
                EndFor.
                Return;
            EndBody."""
        expect = str(TypeMismatchInStatement(For(Id("x"), IntLiteral(5), Id("y"), CallExpr(Id("foo"), [BinaryOp("&&", BooleanLiteral(False), Id("y"))]), ([], []))))
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_for_4(self):
        """Simple program: main"""
        input = """
        Var: z;
        Function: main
            Body:
                Var: x, y;
                For (x = 5, y, foo(False && y)) Do
                    For (z = foo(y), y, x) Do
                    EndFor.
                EndFor.
                Return;
            EndBody.
        Function: foo
            Parameter: x
            Body:
                x = z;
                Return 1;
            EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"), Id("z"))))
        self.assertTrue(TestChecker.test(input,expect,484))
    
    # Test array cell
    def test_arraycell_1(self):
        """Simple program: main"""
        input = """
        Var: z;
        Function: main
            Body:
                Var: x[2][3];
                x = {1,2};
                Return;
            EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"), ArrayLiteral([IntLiteral(1), IntLiteral(2)]))))
        self.assertTrue(TestChecker.test(input,expect,485))    

    def test_arraycell_2(self):
        """Simple program: main"""
        input = """
        Var: z;
        Function: main
            Body:
                Var: x[2][3];
                x[1] = {1,2,3};
                Return;
            EndBody."""
        expect = str(TypeMismatchInExpression(ArrayCell(Id("x"), [IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input,expect,486))    

    def test_arraycell_3(self):
        """Simple program: main"""
        input = """
        Var: z;
        Function: main
            Body:
                Var: x[2][3];
                x[x[0][1]][x[1][0]] = 1.1;
                Return;
            EndBody."""
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id("x"), [ArrayCell(Id("x"), [IntLiteral(0), IntLiteral(1)]), ArrayCell(Id("x"), [IntLiteral(1), IntLiteral(0)])]), FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input,expect,487))    

    def test_arraycell_4(self):
        """Simple program: main"""
        input = """
        Function: main
            Body:
                Var: x[2][3];
                x[int_of_float(x[0][1])][foo(x[1][0])] = 1.1 +. foo(3);
                Return;
            EndBody.
        Function: foo
            Parameter: x
            Body:
                Return 1.1;
            EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"), [IntLiteral(3)])))
        self.assertTrue(TestChecker.test(input,expect,488))  

    def test_arraycell_5(self):
        """Simple program: main"""
        input = """
        Function: foo
            Parameter: x[2][3], y
            Body:
                x[x[0][y]][foo(x, foo(x, y))] = 1.1;
                Return 1;
            EndBody.
        Function: main
            Body:
                Return foo({{1,2,3},{4,5,6}});
            EndBody."""
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id("x"), [ArrayCell(Id("x"), [IntLiteral(0), Id("y")]), CallExpr(Id("foo"), [Id("x"), CallExpr(Id("foo"), [Id("x"), Id("y")])])]), FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input,expect,489)) 

    # Test valid program
    def test_valid_program_1(self):
        input = """
        Var: arr[4] = {"This", "is", "a", "testcase"};
        ** This
        * is
        * a
        * block
        * comment ** 
        Function: printSth
            Parameter: arr[4]
            Body:
                Var : count = 0;
                While count < 100 Do
                    Var: i;
                    If (count % 3 == 0) || (count % 5 == 0) Then
                        print("Skip");
                        Continue;
                    ElseIf (count % 4 == 0) Then
                        Break;
                    EndIf.
                    For (i = 0 , i < 4, 1) Do
                        print(arr[i]);
                        printLn();
                    EndFor.
                    count = count + -i + 1;
                EndWhile.
                Return;
            EndBody.

        Function: main
            Body:
                printSth(arr);
                Return;
            EndBody."""
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_valid_program_2(self):
        input = """
        ** This is a global variable **
        Var: arr[5] = {5,   7, 1,2, 6};

        ** Sort function **
        Function: sort
            Parameter: arr[5]
            Body:
                Var: i;
                For (i = 0, i < 5, 1) Do
                    Var: j;
                    For (j = i + 1, j < 5, 1) Do
                        If arr[i] < arr[j] Then
                            Var: temp;
                            temp = arr[i];
                            arr[i] = arr[j];
                            arr[j] = temp;
                        EndIf.
                    EndFor.
                EndFor.
                Return arr;
            EndBody.

        ** Entry of program **
        Function: main
            Body:
                Var: i;
                arr = sort(arr);
                For (i = 0, i < 5, 1) Do
                    print(string_of_int(arr[i]));
                    printLn();
                EndFor.
            EndBody."""
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_valid_program_3(self):
        input = """Var: string_list[4] = {"","","",""};
        Function: get_string_list
            Parameter: list[4]
                Body:
                    Var : str_input = "", i;
                    For (i = 0 , i < 4, 1) Do
                        str_input = read();
                        list[i] = str_input;
                    EndFor.
                    Return list;
                EndBody.
        Function: print_string_list
            Parameter: list[4]
                Body:
                    Var: i;
                    For (i = 0 , i < 4, 1) Do
                        printStrLn(list[i]);
                    EndFor.
                    Return;
                EndBody.
        Function: main
            Body:
                print_string_list(get_string_list(string_list));
                Return;
            EndBody."""
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_valid_program_4(self):
        input = """
        Function: sqrt
            Parameter: x
            Body:
                Return 1.1;
            EndBody.
        Function: radius
            Parameter: x, y
            Body:
                Var: radius;
                radius = sqrt(x*.x +. y*.y);
                Return radius;
            EndBody.
        Function: main
            Body:
                Var : x = 3.5e0, y = 4.6e-0;
                printStrLn(string_of_float(radius(x, y)));
                Return;
            EndBody."""
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_valid_program_5(self):
        input = """Var: x[5] = {1,2,3,4,5};
        Function: sum
            Parameter: x[5]
                Body:
                    Var: sum = 0, i;
                    For (i = 0 , i < 5, 1) Do
                        sum = sum + i;
                    EndFor.
                    Return sum;
                EndBody.
        Function: main
            Body:
                Var: y;
                y = sum(x);
                printStrLn(string_of_int(y));
                Return;
            EndBody."""
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_full_program_6(self):
        input = """Var: x;
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
                print(string_of_int(fact(x)));
                Return;
            EndBody."""
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_valid_program_7(self):
        input = """           
        Function: main
            Body:
                Var: a[3][2] = {{1,2},{3,4},{5,6}}, i = 0;
                While i < 3 Do
                    Var: j = 0;
                    If i < j Then
                        Continue;
                    EndIf.
                    While (j < 2) Do
                        printStrLn(string_of_int(a[i][j]));
                        j =  j + 1;
                        If j == 3 Then
                            Continue;
                        EndIf.
                    EndWhile.
                    i = i + 1;           
                EndWhile.
                Return;
            EndBody."""
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_valid_program_8(self):
        input = """
        Function: foo
            Parameter: a[2]
            Body:
                Var: x[3], y;
                a[y] = x[a[x[a[x[y]]]]] + foo(a);
                Return y;
            EndBody.
        Function: main
            Body:
                print(string_of_int(foo({1,2})));
                Return;
            EndBody."""
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_valid_program_9(self):
        input = """
        Function: sum
            Parameter: x,y
            Body:
                Return x + y;
            EndBody.
        Function: power
            Parameter: x,y
            Body:
                Var: result = 1, i;
                For (i = 1, i <= y, 1) Do
                    result = result * x;
                EndFor.
                Return result;
            EndBody.
        Function: sqrt
            Parameter: x
            Body:
                Return 1;
            EndBody.            
        Function: main
            Body:
                Var: a[5], x, y;
                a[x * y - sum(x,y)] = a[sum(x,y) * 2 + a[x*y] - sqrt(power(x,2))] * sqrt(power(x+y,x*y) + power(x,y));
                Return;
            EndBody."""
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_valid_program_10(self):
        input = """           
        Function: main
            Body:
                Var: a[3][2] = {{1,2}, {3,4}, {5,6}}, x, y;
                a[a[x+y][x-y]][a[x*y][x\y]] = 1;
                Return;
            EndBody."""
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,499))



    def test_extra_5(self):
        """Simple program: main"""
        input = """
        Function: main
            Body:
                Var: x;
                Do
                    x = 1;
                While x EndDo.
            EndBody."""
        expect = str(TypeMismatchInStatement(Dowhile(([],[Assign(Id("x"), IntLiteral(1))]), Id("x"))))
        self.assertTrue(TestChecker.test(input,expect,603))


    def test_extra_10(self):
        """Simple program: main"""
        input = """
        Var: x;
        Function: main
            Body:
                foo(1);
                foo(foo(10));
                Return;
            EndBody.
        Function: foo
            Parameter: x
            Body:
                Return;
            EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"), [CallExpr(Id("foo"), [IntLiteral(10)])])))
        self.assertTrue(TestChecker.test(input,expect,608))

    def test_extra_11(self):
        """Created automatically"""
        input = """Function: main 
        Parameter: varrr
        Body:
            Var: x =1;
            While x>1 Do
                Var: x =1.5;
                x= x+.1.5;
            EndWhile.
            x = 1.5;
        EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"), FloatLiteral(1.5))))
        self.assertTrue(TestChecker.test(input,expect,609))

    def test_extra_12(self):
        """Created automatically"""
        input = """Function: main 
        Parameter: varrr
        Body:
            Var: x =1;
            Do
                Var: x =1.5;
                x= x+.1.5;
            While x>1
            EndDo.
        EndBody."""
        expect = str("")
        self.assertTrue(TestChecker.test(input,expect,610))

    def test_extra_13(self):
        """Created automatically"""
        input = """Function: main 
        Parameter: varrr
        Body:
            Var: x =1, i;
            For (i = 1, i< 2, 1) Do
                Var: x =1.5;
                x= x+.1.5;
            EndFor.
            x = 1.5;
        EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"), FloatLiteral(1.5))))
        self.assertTrue(TestChecker.test(input,expect,611))

    def test_extra_14(self):
        """Created automatically"""
        input = """Function: main 
        Parameter: varrr
        Body:
            Var: x =1, i;
            If (i > 1) Then
                Var: x =1.5;
                x= x+.1.5;
            EndIf.
            x = 1.5;
        EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"), FloatLiteral(1.5))))
        self.assertTrue(TestChecker.test(input,expect,612))

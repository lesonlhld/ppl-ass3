import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_empty(self):
        """test empty program"""
        testcase = """      
        Function: main

            Body:
                print("\\n");
            EndBody.
        """
        expect = ""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 300))

    def test_global_var_decl(self):
        """test global var declarations"""
        testcase = r"""Var: x, aBc, a_i, a[1][0], x0, continue;"""
        expect = Program([VarDecl(Id('x'),[],None),VarDecl(Id('aBc'),[],None),VarDecl(Id('a_i'),[],None),VarDecl(Id('a'),[1,0],None),VarDecl(Id('x0'),[],None),VarDecl(Id('continue'),[],None)])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 301))

    def test_global_var_init(self):
        """test global var initializations"""
        testcase = r"""Var: x=0, aBc=0xF, a_i=0O1, a[1][0] = {{}}, x0 = "x", continue = True, break = False;"""
        expect = Program([VarDecl(Id('x'),[],IntLiteral(0)),VarDecl(Id('aBc'),[],IntLiteral(15)),VarDecl(Id('a_i'),[],IntLiteral(1)),VarDecl(Id('a'),[1,0],ArrayLiteral([ArrayLiteral([])])),VarDecl(Id('x0'),[],StringLiteral(r"""x""")),VarDecl(Id('continue'),[],BooleanLiteral(True)),VarDecl(Id('break'),[],BooleanLiteral(False))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 302))

    def test_many_global_var_decl(self):
        """test many global variable declarations"""
        testcase = r"""Var: x; Var: aBc, a_i;
        Var: a[1][0],   x0;     Var: continue;"""
        expect = Program([VarDecl(Id('x'),[],None),VarDecl(Id('aBc'),[],None),VarDecl(Id('a_i'),[],None),VarDecl(Id('a'),[1,0],None),VarDecl(Id('x0'),[],None),VarDecl(Id('continue'),[],None)])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 303))

    def test_many_global_var_init(self):
        """test many global variable initializations"""
        testcase = r"""Var: x=0;
        Var: aBc=0xF,   a_i=0O1,
        a[1][0] = {{}}; Var: x0 = "x", continue = True;
        Var: break = False;"""
        expect = Program([VarDecl(Id('x'),[],IntLiteral(0)),VarDecl(Id('aBc'),[],IntLiteral(15)),VarDecl(Id('a_i'),[],IntLiteral(1)),VarDecl(Id('a'),[1,0],ArrayLiteral([ArrayLiteral([])])),VarDecl(Id('x0'),[],StringLiteral(r"""x""")),VarDecl(Id('continue'),[],BooleanLiteral(True)),VarDecl(Id('break'),[],BooleanLiteral(False))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 304))

    def test_global_var_init_305(self):
        """test more global variable initialization"""
        testcase = r"""Var: o = {}, o = {{"{"}};"""
        expect = Program([VarDecl(Id('o'),[],ArrayLiteral([])),VarDecl(Id('o'),[],ArrayLiteral([ArrayLiteral([StringLiteral(r"""{""")])]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 305))

    def test_global_var_init_306(self):
        """test more global variable initialization"""
        testcase = r"""Var: a[1][3][3][0o7777][0xF] = {0};"""
        expect = Program([VarDecl(Id('a'),[1,3,3,4095,15],ArrayLiteral([IntLiteral(0)]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 306))

    def test_global_var_init_307(self):
        """test more global variable initialization"""
        testcase = r"""Var: x = 79899888882e100;"""
        expect = Program([VarDecl(Id('x'),[],FloatLiteral(7.9899888882e+110))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 307))

    def test_parameter_308(self):
        """test parameter declarations"""
        testcase = r"""Function: a Parameter: a[0] Body:EndBody.Function: a Parameter: abc, cba, abc[0] Body:EndBody.
        Function: a Parameter: a,a,a[0] Body:EndBody."""
        expect = Program([FuncDecl(Id('a'),[VarDecl(Id('a'),[0],None)],([],[])),FuncDecl(Id('a'),[VarDecl(Id('abc'),[],None),VarDecl(Id('cba'),[],None),VarDecl(Id('abc'),[0],None)],([],[])),FuncDecl(Id('a'),[VarDecl(Id('a'),[],None),VarDecl(Id('a'),[],None),VarDecl(Id('a'),[0],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 308))

    def test_parameter_309(self):
        """test more parameter declaration"""
        testcase = r"""Function: a Parameter: a[1][3][3][0o7777][0xF] Body:EndBody."""
        expect = Program([FuncDecl(Id('a'),[VarDecl(Id('a'),[1,3,3,4095,15],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 309))

    def test_parameter_310(self):
        """test more parameter declaration"""
        testcase = r"""Function: a Parameter: a,a,a[0],a[1][3][3][0o7777][0xF] Body:EndBody."""
        expect = Program([FuncDecl(Id('a'),[VarDecl(Id('a'),[],None),VarDecl(Id('a'),[],None),VarDecl(Id('a'),[0],None),VarDecl(Id('a'),[1,3,3,4095,15],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 310))

    def test_local_var_decl_1(self):
        """test local varible declarations"""
        testcase = r"""Function: a Body:
        Var:a;
        Var:var;
        EndBody."""
        expect = Program([FuncDecl(Id('a'),[],([VarDecl(Id('a'),[],None),VarDecl(Id('var'),[],None)],[]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 311))

    def test_local_var_decl_2(self):
        """test local varible declarations"""
        testcase = r"""Function: a Body:IfTrueThenVar:a;Var:var;EndIf.EndBody."""
        expect = Program([FuncDecl(Id('a'),[],([],[If([(BooleanLiteral(True),[VarDecl(Id('a'),[],None),VarDecl(Id('var'),[],None)],[])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 312))

    def test_local_var_init(self):
        """test local varible initializations"""
        testcase = r"""Function: a Body:Var:var = {"var"};IfTrueThenVar:a=0;Var:var="**meant 2 b string**";EndIf.EndBody."""
        expect = Program([FuncDecl(Id('a'),[],([VarDecl(Id('var'),[],ArrayLiteral([StringLiteral(r"""var""")]))],[If([(BooleanLiteral(True),[VarDecl(Id('a'),[],IntLiteral(0)),VarDecl(Id('var'),[],StringLiteral(r"""**meant 2 b string**"""))],[])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 313))

    def test_local_var_decl_placement(self):
        """test local variable"""
        testcase = r"""Function: a Body:Var:var = {"var"};Var:a=0;Var:var="**meant 2 b string**";EndBody."""
        expect = Program([FuncDecl(Id('a'),[],([VarDecl(Id('var'),[],ArrayLiteral([StringLiteral(r"""var""")])),VarDecl(Id('a'),[],IntLiteral(0)),VarDecl(Id('var'),[],StringLiteral(r"""**meant 2 b string**"""))],[]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 314))

    def test_common_var_decl_315(self):
        """test common"""
        testcase = r"""Var: x;"""
        expect = Program([VarDecl(Id('x'),[],None)])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 315))

    def test_common_var_decl_316(self):
        """test common"""
        testcase = r"""Function: a Body:Var:var = 0;Var:a=0;Var:var="**meant 2 b string**";Var:var;EndBody."""
        expect = Program([FuncDecl(Id('a'),[],([VarDecl(Id('var'),[],IntLiteral(0)),VarDecl(Id('a'),[],IntLiteral(0)),VarDecl(Id('var'),[],StringLiteral(r"""**meant 2 b string**""")),VarDecl(Id('var'),[],None)],[]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 316))

    def test_func_decl_1(self):
        """test function declarations"""
        testcase = r"""Function: a Body:Var:var = {"var"};IfTrueThenEndIf.EndBody."""
        expect = Program([FuncDecl(Id('a'),[],([VarDecl(Id('var'),[],ArrayLiteral([StringLiteral(r"""var""")]))],[If([(BooleanLiteral(True),[],[])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 317))

    def test_func_decl_2(self):
        """test function declaration"""
        testcase = r"""Function: a Body:Var:var = {"var"};Var:a=0;Var:var="**meant 2 b string**";EndBody.
        """
        expect = Program([FuncDecl(Id('a'),[],([VarDecl(Id('var'),[],ArrayLiteral([StringLiteral(r"""var""")])),VarDecl(Id('a'),[],IntLiteral(0)),VarDecl(Id('var'),[],StringLiteral(r"""**meant 2 b string**"""))],[]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 318))

    def test_same_name_func_1(self):
        """test function with same name as another function"""
        testcase = r"""Function: a Body:EndBody.
        Function:a Body:EndBody."""
        expect = Program([FuncDecl(Id('a'),[],([],[])),FuncDecl(Id('a'),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 319))

    def test_same_name_func_2(self):
        """test function with same name as parameter"""
        testcase = r"""Function: x
            Parameter: x
            Body:
            EndBody."""
        expect = Program([FuncDecl(Id('x'),[VarDecl(Id('x'),[],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 320))

    def test_long_func_name(self):
        """test function with long name"""
        testcase = r"""Function: helper_func_of_another_helper_func_with_______a_________looooooooooooong_namu
            Parameter: x
            Body:
            EndBody."""
        expect = Program([FuncDecl(Id('helper_func_of_another_helper_func_with_______a_________looooooooooooong_namu'),[VarDecl(Id('x'),[],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 321))

    def test_assign(self):
        """test assignment statements"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                i=-1 + int_of_float(1.);
                arr[i] = i;
                i = i ** 0 ** \ 0;
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[Assign(Id('i'),BinaryOp('+',UnaryOp('-',IntLiteral(1)),CallExpr(Id('int_of_float'),[FloatLiteral(1.0)]))),Assign(ArrayCell(Id('arr'),[Id('i')]),Id('i')),Assign(Id('i'),BinaryOp('\\',Id('i'),IntLiteral(0)))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 322))

    def test_assign_weird_lhs_323(self):
        """test assignment statements with weird left-hand side"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                (i + i)[i] = -.1.;
                (arr + i)[i == 0] = i;
                1[1] = i \. 0;
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[Assign(ArrayCell(BinaryOp('+',Id('i'),Id('i')),[Id('i')]),UnaryOp('-.',FloatLiteral(1.0))),Assign(ArrayCell(BinaryOp('+',Id('arr'),Id('i')),[BinaryOp('==',Id('i'),IntLiteral(0))]),Id('i')),Assign(ArrayCell(IntLiteral(1),[IntLiteral(1)]),BinaryOp('\\.',Id('i'),IntLiteral(0)))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 323))

    def test_assign_weird_lhs_324(self):
        """test assignment statements with weird left-hand side"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                function()[i] = -.1.;
                (arr =/= arr)["True"] = i;
                arr[i] = i;
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[Assign(ArrayCell(CallExpr(Id('function'),[]),[Id('i')]),UnaryOp('-.',FloatLiteral(1.0))),Assign(ArrayCell(BinaryOp('=/=',Id('arr'),Id('arr')),[StringLiteral(r"""True""")]),Id('i')),Assign(ArrayCell(Id('arr'),[Id('i')]),Id('i'))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 324))

    def test_assign_weird_rhs_325(self):
        """test assignment statements with weird right-hand side"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                function()[i] = -.1. != !bool_of_string("True");
                i = i***i + i***i;
                i = i == arr[i + i >=. !arr() -. !6 || {"1"}] && i[i()][i()[i][(i)--i]];
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[Assign(ArrayCell(CallExpr(Id('function'),[]),[Id('i')]),BinaryOp('!=',UnaryOp('-.',FloatLiteral(1.0)),UnaryOp('!',CallExpr(Id('bool_of_string'),[StringLiteral(r"""True""")])))),Assign(Id('i'),BinaryOp('*',Id('i'),Id('i'))),Assign(Id('i'),BinaryOp('==',Id('i'),BinaryOp('&&',ArrayCell(Id('arr'),[BinaryOp('>=.',BinaryOp('+',Id('i'),Id('i')),BinaryOp('||',BinaryOp('-.',UnaryOp('!',CallExpr(Id('arr'),[])),UnaryOp('!',IntLiteral(6))),ArrayLiteral([StringLiteral(r"""1""")])))]),ArrayCell(Id('i'),[CallExpr(Id('i'),[]),ArrayCell(CallExpr(Id('i'),[]),[Id('i'),BinaryOp('-',Id('i'),UnaryOp('-',Id('i')))])]))))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 325))

    def test_assign_weird_rhs_326(self):
        """test assignment statements with weird right-hand side"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                function()[i] = -.1. >=. !bool_of_string("True");
                i = i***i + i***i;
                i = i == arr[i + i >=. arr(0) -. !6 || {"1"}] && i[i()][i()[i][(i)]];
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[Assign(ArrayCell(CallExpr(Id('function'),[]),[Id('i')]),BinaryOp('>=.',UnaryOp('-.',FloatLiteral(1.0)),UnaryOp('!',CallExpr(Id('bool_of_string'),[StringLiteral(r"""True""")])))),Assign(Id('i'),BinaryOp('*',Id('i'),Id('i'))),Assign(Id('i'),BinaryOp('==',Id('i'),BinaryOp('&&',ArrayCell(Id('arr'),[BinaryOp('>=.',BinaryOp('+',Id('i'),Id('i')),BinaryOp('||',BinaryOp('-.',CallExpr(Id('arr'),[IntLiteral(0)]),UnaryOp('!',IntLiteral(6))),ArrayLiteral([StringLiteral(r"""1""")])))]),ArrayCell(Id('i'),[CallExpr(Id('i'),[]),ArrayCell(CallExpr(Id('i'),[]),[Id('i'),Id('i')])]))))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 326))

    def test_assign_weird_rhs_327(self):
        """test assignment statements with weird right-hand side"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                function()[i] = -.1. == !bool_of_string("True");
                i = i***i == "***i***" == i***i;
                i = i == arr[i >=. !arr() -. !6 || {"1"}] && i[i()][i({})[i][(i)--i]];
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[Assign(ArrayCell(CallExpr(Id('function'),[]),[Id('i')]),BinaryOp('==',UnaryOp('-.',FloatLiteral(1.0)),UnaryOp('!',CallExpr(Id('bool_of_string'),[StringLiteral(r"""True""")])))),Assign(Id('i'),BinaryOp('*',BinaryOp('*',Id('i'),Id('i')),Id('i'))),Assign(Id('i'),BinaryOp('==',Id('i'),BinaryOp('&&',ArrayCell(Id('arr'),[BinaryOp('>=.',Id('i'),BinaryOp('||',BinaryOp('-.',UnaryOp('!',CallExpr(Id('arr'),[])),UnaryOp('!',IntLiteral(6))),ArrayLiteral([StringLiteral(r"""1""")])))]),ArrayCell(Id('i'),[CallExpr(Id('i'),[]),ArrayCell(CallExpr(Id('i'),[ArrayLiteral([])]),[Id('i'),BinaryOp('-',Id('i'),UnaryOp('-',Id('i')))])]))))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 327))

    def test_if(self):
        """test if-then statements"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                If True || False Then EndIf.
                If False && True && "True" || bool_of_string("False" +. 1.) Thenarr=arr;EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[If([(BinaryOp('||',BooleanLiteral(True),BooleanLiteral(False)),[],[])],([],[])),If([(BinaryOp('||',BinaryOp('&&',BinaryOp('&&',BooleanLiteral(False),BooleanLiteral(True)),StringLiteral(r"""True""")),CallExpr(Id('bool_of_string'),[BinaryOp('+.',StringLiteral(r"""False"""),FloatLiteral(1.0))])),[],[Assign(Id('arr'),Id('arr'))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 328))

    def test_if_else(self):
        """test if-then-else statements"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                If True || False ThenElseEndIf.
                If False && True && "True" || bool_of_string("False" +. 1.) ThenElsearr=arr;EndIf.
                Ifarr Thenarr=arr;Elsei=i*i;EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[If([(BinaryOp('||',BooleanLiteral(True),BooleanLiteral(False)),[],[])],([],[])),If([(BinaryOp('||',BinaryOp('&&',BinaryOp('&&',BooleanLiteral(False),BooleanLiteral(True)),StringLiteral(r"""True""")),CallExpr(Id('bool_of_string'),[BinaryOp('+.',StringLiteral(r"""False"""),FloatLiteral(1.0))])),[],[])],([],[Assign(Id('arr'),Id('arr'))])),If([(Id('arr'),[],[Assign(Id('arr'),Id('arr'))])],([],[Assign(Id('i'),BinaryOp('*',Id('i'),Id('i')))]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 329))

    def test_if_else_if(self):
        """test if-then-elseif statements"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                If True || False ThenElseIf true ThenEndIf.
                If False && True && "True" || bool_of_string("False" +. 1.) ThenElseIf1ThenElsearr=arr;EndIf.
                Ifarr Thenarr=arr;ElseIfbut ThenElseIfor Theni=i*i;ElseEndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[If([(BinaryOp('||',BooleanLiteral(True),BooleanLiteral(False)),[],[]),(Id('true'),[],[])],([],[])),If([(BinaryOp('||',BinaryOp('&&',BinaryOp('&&',BooleanLiteral(False),BooleanLiteral(True)),StringLiteral(r"""True""")),CallExpr(Id('bool_of_string'),[BinaryOp('+.',StringLiteral(r"""False"""),FloatLiteral(1.0))])),[],[]),(IntLiteral(1),[],[])],([],[Assign(Id('arr'),Id('arr'))])),If([(Id('arr'),[],[Assign(Id('arr'),Id('arr'))]),(Id('but'),[],[]),(Id('or'),[],[Assign(Id('i'),BinaryOp('*',Id('i'),Id('i')))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 330))

    def test_nested_if_else_if(self):
        """test nested if statements"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                IfTrue||FalseThenIfTrueThenElseIfFalseThenElseEndIf.ElseIftrue ThenEndIf.
                If False && True && "True" || bool_of_string("False" +. 1.) ThenElseIf1ThenIf0ThenEndIf.Elsearr=arr;EndIf.
                Ifarr Thenarr=arr;ElseIfbut ThenElseIfor Theni=i*i;Else Ifi ThenElseIfarr ThenEndIf.EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[If([(BinaryOp('||',BooleanLiteral(True),BooleanLiteral(False)),[],[If([(BooleanLiteral(True),[],[]),(BooleanLiteral(False),[],[])],([],[]))]),(Id('true'),[],[])],([],[])),If([(BinaryOp('||',BinaryOp('&&',BinaryOp('&&',BooleanLiteral(False),BooleanLiteral(True)),StringLiteral(r"""True""")),CallExpr(Id('bool_of_string'),[BinaryOp('+.',StringLiteral(r"""False"""),FloatLiteral(1.0))])),[],[]),(IntLiteral(1),[],[If([(IntLiteral(0),[],[])],([],[]))])],([],[Assign(Id('arr'),Id('arr'))])),If([(Id('arr'),[],[Assign(Id('arr'),Id('arr'))]),(Id('but'),[],[]),(Id('or'),[],[Assign(Id('i'),BinaryOp('*',Id('i'),Id('i')))])],([],[If([(Id('i'),[],[]),(Id('arr'),[],[])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 331))

    def test_weird_if_332(self):
        """test weird if statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                If True
                Then
                ElseIf False
                Then
                Else If True == False
                Then
                Else
                EndIf.
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[If([(BooleanLiteral(True),[],[]),(BooleanLiteral(False),[],[])],([],[If([(BinaryOp('==',BooleanLiteral(True),BooleanLiteral(False)),[],[])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 332))

    def test_weird_if_333(self):
        """test weird if statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                If (1 == 2 || 2) == (2 || 3 == 1)
                Then
                ElseIf False
                Then
                ElseIf True == False
                Then
                Else
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[If([(BinaryOp('==',BinaryOp('==',IntLiteral(1),BinaryOp('||',IntLiteral(2),IntLiteral(2))),BinaryOp('==',BinaryOp('||',IntLiteral(2),IntLiteral(3)),IntLiteral(1))),[],[]),(BooleanLiteral(False),[],[]),(BinaryOp('==',BooleanLiteral(True),BooleanLiteral(False)),[],[])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 333))

    def test_weird_if_334(self):
        """test weird if statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                If True
                Then
                If 0 Then EndIf.
                ElseIf False
                Then
                Else If True == False
                Then
                EndIf.EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[If([(BooleanLiteral(True),[],[If([(IntLiteral(0),[],[])],([],[]))]),(BooleanLiteral(False),[],[])],([],[If([(BinaryOp('==',BooleanLiteral(True),BooleanLiteral(False)),[],[])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 334))

    def test_for(self):
        """test for statements"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                For (i=0, i < 1000, 1) Do
                    arr[i] = i;
                EndFor.
                
                For (i=1, i >= 0, -1) Do
                    print(i);
                EndFor.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(1000)),IntLiteral(1),([],[Assign(ArrayCell(Id('arr'),[Id('i')]),Id('i'))])),For(Id('i'),IntLiteral(1),BinaryOp('>=',Id('i'),IntLiteral(0)),UnaryOp('-',IntLiteral(1)),([],[CallStmt(Id('print'),[Id('i')])]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 335))

    def test_for_composite_count(self):
        """test for statement with composite count variable"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                For (arr={0}, True, {1}) Do
                    arr[i] = i;
                EndFor.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[For(Id('arr'),ArrayLiteral([IntLiteral(0)]),BooleanLiteral(True),ArrayLiteral([IntLiteral(1)]),([],[Assign(ArrayCell(Id('arr'),[Id('i')]),Id('i'))]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 336))

    def test_long_for(self):
        """test for statement with semi-colon as separator"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                For (i=0, helper_func_of_another_helper_func_with_______a_________looooooooooooong_namu(), 0) Do
                    arr[i] = i;
                EndFor.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[For(Id('i'),IntLiteral(0),CallExpr(Id('helper_func_of_another_helper_func_with_______a_________looooooooooooong_namu'),[]),IntLiteral(0),([],[Assign(ArrayCell(Id('arr'),[Id('i')]),Id('i'))]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 337))

    def test_nested_for(self):
        """test nested for statements"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                For (i=0, i < 1000, 1) Do
                    Var: j = 0;
                    For (j = 1, j < 1000, 1) Do
                        Var: k = 2;
                    EndFor.
                EndFor.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(1000)),IntLiteral(1),([VarDecl(Id('j'),[],IntLiteral(0))],[For(Id('j'),IntLiteral(1),BinaryOp('<',Id('j'),IntLiteral(1000)),IntLiteral(1),([VarDecl(Id('k'),[],IntLiteral(2))],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 338))

    def test_weird_for_339(self):
        """test weird for statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                For (brr={0}, t_t(a, b, c, ";T_T;", {{},{}}), {1}) Do
                    brr[i] = arr[i];
                    i = i + 1;
                EndFor.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[For(Id('brr'),ArrayLiteral([IntLiteral(0)]),CallExpr(Id('t_t'),[Id('a'),Id('b'),Id('c'),StringLiteral(r""";T_T;"""),ArrayLiteral([ArrayLiteral([]),ArrayLiteral([])])]),ArrayLiteral([IntLiteral(1)]),([],[Assign(ArrayCell(Id('brr'),[Id('i')]),ArrayCell(Id('arr'),[Id('i')])),Assign(Id('i'),BinaryOp('+',Id('i'),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 339))

    def test_weird_for_340(self):
        """test weird for statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                For (i = {0, ",", 0}, function(if, then, else), 1[1]) Do
                    arr[i] = i;
                    i = i + 1;
                EndFor.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[For(Id('i'),ArrayLiteral([IntLiteral(0),StringLiteral(r""","""),IntLiteral(0)]),CallExpr(Id('function'),[Id('if'),Id('then'),Id('else')]),ArrayCell(IntLiteral(1),[IntLiteral(1)]),([],[Assign(ArrayCell(Id('arr'),[Id('i')]),Id('i')),Assign(Id('i'),BinaryOp('+',Id('i'),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 340))

    def test_weird_for_341(self):
        """test weird for statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                For ( i = 0, i < i * i, arr[i] ) Do
                    For (function = 0, true(True, "True"), 0) Do
                        Continue; Break;
                    EndFor.
                EndFor.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),BinaryOp('*',Id('i'),Id('i'))),ArrayCell(Id('arr'),[Id('i')]),([],[For(Id('function'),IntLiteral(0),CallExpr(Id('true'),[BooleanLiteral(True),StringLiteral(r"""True""")]),IntLiteral(0),([],[Continue(),Break()]))]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 341))

    def test_while_1(self):
        """test while statements"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                WhileTrueDoEndWhile.
                WhileFalseDo**sth**sth();EndWhile.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[While(BooleanLiteral(True),([],[])),While(BooleanLiteral(False),([],[CallStmt(Id('sth'),[])]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 342))

    def test_while_2(self):
        """test while statements"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                While True Do
                EndWhile.
                
                While False Do
                    **sth**
                    sth();
                EndWhile.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[While(BooleanLiteral(True),([],[])),While(BooleanLiteral(False),([],[CallStmt(Id('sth'),[])]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 343))

    def test_nested_while(self):
        """test nested while statements"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                While True
                Do
                While False
                Do
                EndWhile.EndWhile.
                
                WhileFalseDoWhileFalseDoEndWhile.
                
                **sth**
                sth();
                
                EndWhile.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[While(BooleanLiteral(True),([],[While(BooleanLiteral(False),([],[]))])),While(BooleanLiteral(False),([],[While(BooleanLiteral(False),([],[])),CallStmt(Id('sth'),[])]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 344))

    def test_weird_while_345(self):
        """test weird while statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                While (True == !False) Do
                    WhileFalseDoWhileTrueDoEndWhile.
                EndWhile.EndWhile.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[While(BinaryOp('==',BooleanLiteral(True),UnaryOp('!',BooleanLiteral(False))),([],[While(BooleanLiteral(False),([],[While(BooleanLiteral(True),([],[]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 345))

    def test_weird_while_346(self):
        """test weird while statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                While True Do
                    Do
                    While True -i >= i
                    EndDo.
                EndWhile.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[While(BooleanLiteral(True),([],[Dowhile(([],[]),BinaryOp('>=',BinaryOp('-',BooleanLiteral(True),Id('i')),Id('i')))]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 346))

    def test_do(self):
        """test do-while statements"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                Do
                    arr[int_of_float(i)] = i;
                    i = i * i;
                While i <. i *. i
                EndDo.
                
                DoWhileFalseEndDo.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[Dowhile(([],[Assign(ArrayCell(Id('arr'),[CallExpr(Id('int_of_float'),[Id('i')])]),Id('i')),Assign(Id('i'),BinaryOp('*',Id('i'),Id('i')))]),BinaryOp('<.',Id('i'),BinaryOp('*.',Id('i'),Id('i')))),Dowhile(([],[]),BooleanLiteral(False))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 347))

    def test_nested_do(self):
        """test nested do-while statements"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                Do
                Var: j = 0;
                    Do
                        j = i;
                    While 0. \. j
                    EndDo.
                While 0 == 0x1-0X1
                EndDo.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[Dowhile(([VarDecl(Id('j'),[],IntLiteral(0))],[Dowhile(([],[Assign(Id('j'),Id('i'))]),BinaryOp('\\.',FloatLiteral(0.0),Id('j')))]),BinaryOp('==',IntLiteral(0),BinaryOp('-',IntLiteral(1),IntLiteral(1))))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 348))

    def test_weird_do_349(self):
        """test weird do-while statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                DoWhileTrueDoDoWhileFalseEndDo.EndWhile.WhileTrue=/=FalseEndDo.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[Dowhile(([],[While(BooleanLiteral(True),([],[Dowhile(([],[]),BooleanLiteral(False))]))]),BinaryOp('=/=',BooleanLiteral(True),BooleanLiteral(False)))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 349))

    def test_weird_do_350(self):
        """test weird do-while statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                DoWhileTrueDoWhileFalseDoEndWhile.EndWhile.WhileTrue-.FalseEndDo.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[Dowhile(([],[While(BooleanLiteral(True),([],[While(BooleanLiteral(False),([],[]))]))]),BinaryOp('-.',BooleanLiteral(True),BooleanLiteral(False)))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 350))

    def test_break(self):
        """test break statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                For (i = 0, i < 1000, 0O1) Do
                    Break;
                EndFor.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(1000)),IntLiteral(1),([],[Break()]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 351))

    def test_weird_break_352(self):
        """test weird break statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                Break;
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[Break()]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 352))

    def test_weird_break_353(self):
        """test weird break statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                For (i = 0, i < 1000, 0O1) Do
                    If True Then
                        Break;
                    Else
                        Continue;
                    EndIf.
                    
                    Break;
                EndFor.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(1000)),IntLiteral(1),([],[If([(BooleanLiteral(True),[],[Break()])],([],[Continue()])),Break()]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 353))

    def test_continue(self):
        """test continue statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                For (i = 0, i < 1000, 0O1) Do
                    Continue;
                EndFor.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(1000)),IntLiteral(1),([],[Continue()]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 354))

    def test_weird_continue_355(self):
        """test weird continue statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                Continue;
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[Continue()]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 355))

    def test_weird_continue_356(self):
        """test weird continue statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                For (i = 0, i < 1000, 0O1) Do
                    If True Then
                        Continue;
                    EndIf.
                    
                    Break;
                EndFor.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(1000)),IntLiteral(1),([],[If([(BooleanLiteral(True),[],[Continue()])],([],[])),Break()]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 356))

    def test_call(self):
        """test call statements"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                print("This is the first meaning full string");
                If True Then
                    print("isn\'t it");
                Else
                    do_sth_that_will_never_be_done(0, 0.0 + 1., False, "", {}, i);
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[CallStmt(Id('print'),[StringLiteral(r"""This is the first meaning full string""")]),If([(BooleanLiteral(True),[],[CallStmt(Id('print'),[StringLiteral(r"""isn\'t it""")])])],([],[CallStmt(Id('do_sth_that_will_never_be_done'),[IntLiteral(0),BinaryOp('+',FloatLiteral(0.0),FloatLiteral(1.0)),BooleanLiteral(False),StringLiteral(r""""""),ArrayLiteral([]),Id('i')])]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 357))

    def test_complex_call(self):
        """test complex call statements"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                do_sth_that_will_be_done(func1(0, 0., 0e0) + (2)[2] \. 0. == (i +. i * 2), {{"\\","//"}});
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[CallStmt(Id('do_sth_that_will_be_done'),[BinaryOp('==',BinaryOp('+',CallExpr(Id('func1'),[IntLiteral(0),FloatLiteral(0.0),FloatLiteral(0.0)]),BinaryOp('\\.',ArrayCell(IntLiteral(2),[IntLiteral(2)]),FloatLiteral(0.0))),BinaryOp('+.',Id('i'),BinaryOp('*',Id('i'),IntLiteral(2)))),ArrayLiteral([ArrayLiteral([StringLiteral(r"""\\"""),StringLiteral(r"""//""")])])])]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 358))

    def test_weird_call_359(self):
        """test weird call statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                do_sth_that_will_be_done(func1(0, 0., 0e0) + (2)[2] \. 0. == (i +. i * 2), {{"\\","//"}});
                f__(g__(i__(True, (id())[2][True[False > 2]], 9 == (9 == 9) * 9), z()[z]));
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[CallStmt(Id('do_sth_that_will_be_done'),[BinaryOp('==',BinaryOp('+',CallExpr(Id('func1'),[IntLiteral(0),FloatLiteral(0.0),FloatLiteral(0.0)]),BinaryOp('\\.',ArrayCell(IntLiteral(2),[IntLiteral(2)]),FloatLiteral(0.0))),BinaryOp('+.',Id('i'),BinaryOp('*',Id('i'),IntLiteral(2)))),ArrayLiteral([ArrayLiteral([StringLiteral(r"""\\"""),StringLiteral(r"""//""")])])]),CallStmt(Id('f__'),[CallExpr(Id('g__'),[CallExpr(Id('i__'),[BooleanLiteral(True),ArrayCell(CallExpr(Id('id'),[]),[IntLiteral(2),ArrayCell(BooleanLiteral(True),[BinaryOp('>',BooleanLiteral(False),IntLiteral(2))])]),BinaryOp('==',IntLiteral(9),BinaryOp('*',BinaryOp('==',IntLiteral(9),IntLiteral(9)),IntLiteral(9)))]),ArrayCell(CallExpr(Id('z'),[]),[Id('z')])])])]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 359))

    def test_weird_call_360(self):
        """test weird call statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                f(True % False);
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[CallStmt(Id('f'),[BinaryOp('%',BooleanLiteral(True),BooleanLiteral(False))])]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 360))

    def test_empty_return(self):
        """test empty return statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                Return;
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 361))

    def test_return(self):
        """test non-empty return statements"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                Return 1;
                Return {};
                Return 2. +. -.2.;
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[Return(IntLiteral(1)),Return(ArrayLiteral([])),Return(BinaryOp('+.',FloatLiteral(2.0),UnaryOp('-.',FloatLiteral(2.0))))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 362))

    def test_complex_return(self):
        """test complex return statements"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                Return f(2) \ 2 =/= 2 * !(True || False);
                Return (True == False || (arr)[i*.i][i[i]]);
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[Return(BinaryOp('=/=',BinaryOp('\\',CallExpr(Id('f'),[IntLiteral(2)]),IntLiteral(2)),BinaryOp('*',IntLiteral(2),UnaryOp('!',BinaryOp('||',BooleanLiteral(True),BooleanLiteral(False)))))),Return(BinaryOp('==',BooleanLiteral(True),BinaryOp('||',BooleanLiteral(False),ArrayCell(Id('arr'),[BinaryOp('*.',Id('i'),Id('i')),ArrayCell(Id('i'),[Id('i')])]))))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 363))

    def test_weird_return_364(self):
        """test weird return statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                Return (arr[arr]);
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[Return(ArrayCell(Id('arr'),[Id('arr')]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 364))

    def test_weird_return_365(self):
        """test weird return statement"""
        testcase = r"""Function: function
            Parameter: i, arr[1000]
            Body:
                Return tuple(2, 3);
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[Return(CallExpr(Id('tuple'),[IntLiteral(2),IntLiteral(3)]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 365))

    def test_parameter_repeat(self):
        """test parameter repeat"""
        testcase = r"""Function: function
            Parameter: i, arr[1000], i, arr[1000][1000]
            Body:
                
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None),VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000,1000],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 366))

    def test_common(self):
        """test common"""
        testcase = r"""Var: a = 0.;"""
        expect = Program([VarDecl(Id('a'),[],FloatLiteral(0.0))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 367))

    def test_func(self):
        """test function"""
        testcase = r"""Function: function1
            Parameter: i, arr[1000]
            Body:
                
            EndBody.Function: function2
                Parameter: j, brr[1000]
                Body:    
                EndBody."""
        expect = Program([FuncDecl(Id('function1'),[VarDecl(Id('i'),[],None),VarDecl(Id('arr'),[1000],None)],([],[])),FuncDecl(Id('function2'),[VarDecl(Id('j'),[],None),VarDecl(Id('brr'),[1000],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 368))

    def test_multiple_scope_var(self):
        """test variable declarations across scopes"""
        testcase = r"""Var: x;
        Function: function
            Parameter: j, brr[1000]
            Body:
                Var: x=0;
                For (i=0,0,0) Do
                    Var:x=1;
                    Do
                        Var:x=2;
                    While1
                    EndDo.
                    If0Then
                        Var:x=3;
                    ElseIf0Then
                        Var:x=4;
                    Else
                        Var:x=5;
                    EndIf.
                EndFor.
            EndBody."""
        expect = Program([VarDecl(Id('x'),[],None),FuncDecl(Id('function'),[VarDecl(Id('j'),[],None),VarDecl(Id('brr'),[1000],None)],([VarDecl(Id('x'),[],IntLiteral(0))],[For(Id('i'),IntLiteral(0),IntLiteral(0),IntLiteral(0),([VarDecl(Id('x'),[],IntLiteral(1))],[Dowhile(([VarDecl(Id('x'),[],IntLiteral(2))],[]),IntLiteral(1)),If([(IntLiteral(0),[VarDecl(Id('x'),[],IntLiteral(3))],[]),(IntLiteral(0),[VarDecl(Id('x'),[],IntLiteral(4))],[])],([VarDecl(Id('x'),[],IntLiteral(5))],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 369))

    def test_long_nested_stmt(self):
        """test nested statements"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                If True Then
                    For (i=0, i, -1) Do
                        Do While False EndDo.
                        While False DoVar: k, l; Break;  EndWhile.
                    EndFor.
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('j'),[],None),VarDecl(Id('brr'),[1000],None)],([],[If([(BooleanLiteral(True),[],[For(Id('i'),IntLiteral(0),Id('i'),UnaryOp('-',IntLiteral(1)),([],[Dowhile(([],[]),BooleanLiteral(False)),While(BooleanLiteral(False),([VarDecl(Id('k'),[],None),VarDecl(Id('l'),[],None)],[Break()]))]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 370))

    def test_complex_assign(self):
        """test complex assignment statement"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                ((a[2])[3][4])[s] = f(****) + g(o + 0o1, 0)[{2}[0]];
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('j'),[],None),VarDecl(Id('brr'),[1000],None)],([],[Assign(ArrayCell(ArrayCell(ArrayCell(Id('a'),[IntLiteral(2)]),[IntLiteral(3),IntLiteral(4)]),[Id('s')]),BinaryOp('+',CallExpr(Id('f'),[]),ArrayCell(CallExpr(Id('g'),[BinaryOp('+',Id('o'),IntLiteral(1)),IntLiteral(0)]),[ArrayCell(ArrayLiteral([IntLiteral(2)]),[IntLiteral(0)])])))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 371))

    def test_operator_precedence_372(self):
        """test operator precedence"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                j = i * i + i \ --1 % i--i;
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('j'),[],None),VarDecl(Id('brr'),[1000],None)],([],[Assign(Id('j'),BinaryOp('-',BinaryOp('+',BinaryOp('*',Id('i'),Id('i')),BinaryOp('%',BinaryOp('\\',Id('i'),UnaryOp('-',UnaryOp('-',IntLiteral(1)))),Id('i'))),UnaryOp('-',Id('i'))))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 372))

    def test_operator_precedence_373(self):
        """test operator precedence"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                j = i *. -. -. 2. +. -. i \. i -. 0.E-8;
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('j'),[],None),VarDecl(Id('brr'),[1000],None)],([],[Assign(Id('j'),BinaryOp('-.',BinaryOp('+.',BinaryOp('*.',Id('i'),UnaryOp('-.',UnaryOp('-.',FloatLiteral(2.0)))),BinaryOp('\\.',UnaryOp('-.',Id('i')),Id('i'))),FloatLiteral(0.0)))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 373))

    def test_operator_precedence_374(self):
        """test operator precedence"""
        testcase = r"""Function: main
            Parameter: j, brr[1000]
            Body:
                j = !i && i == i || !!i;
            EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('j'),[],None),VarDecl(Id('brr'),[1000],None)],([],[Assign(Id('j'),BinaryOp('==',BinaryOp('&&',UnaryOp('!',Id('i')),Id('i')),BinaryOp('||',Id('i'),UnaryOp('!',UnaryOp('!',Id('i'))))))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 374))

    def test_operator_precedence_375(self):
        """test operator precedence"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                j = -.-.i +. brrr[5];
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('j'),[],None),VarDecl(Id('brr'),[1000],None)],([],[Assign(Id('j'),BinaryOp('+.',UnaryOp('-.',UnaryOp('-.',Id('i'))),ArrayCell(Id('brrr'),[IntLiteral(5)])))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 375))

    def test_operator_precedence_376(self):
        """test operator precedence"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                j = func(1)[2];
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('j'),[],None),VarDecl(Id('brr'),[1000],None)],([],[Assign(Id('j'),ArrayCell(CallExpr(Id('func'),[IntLiteral(1)]),[IntLiteral(2)]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 376))

    def test_operator_assoc_377(self):
        """test operator associativity"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                j = i + i + i;
                j = i * i * i;
                j = i \ i \ i;
                j = i - i - i;
                j = i % i % i;
                j = i *. i *. i;
                j = i +. i +. i;
                j = i -. i -. i;
                j = i \. i \. i;
                j = i || i || i;
                j = i && i && i;
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('j'),[],None),VarDecl(Id('brr'),[1000],None)],([],[Assign(Id('j'),BinaryOp('+',BinaryOp('+',Id('i'),Id('i')),Id('i'))),Assign(Id('j'),BinaryOp('*',BinaryOp('*',Id('i'),Id('i')),Id('i'))),Assign(Id('j'),BinaryOp('\\',BinaryOp('\\',Id('i'),Id('i')),Id('i'))),Assign(Id('j'),BinaryOp('-',BinaryOp('-',Id('i'),Id('i')),Id('i'))),Assign(Id('j'),BinaryOp('%',BinaryOp('%',Id('i'),Id('i')),Id('i'))),Assign(Id('j'),BinaryOp('*.',BinaryOp('*.',Id('i'),Id('i')),Id('i'))),Assign(Id('j'),BinaryOp('+.',BinaryOp('+.',Id('i'),Id('i')),Id('i'))),Assign(Id('j'),BinaryOp('-.',BinaryOp('-.',Id('i'),Id('i')),Id('i'))),Assign(Id('j'),BinaryOp('\\.',BinaryOp('\\.',Id('i'),Id('i')),Id('i'))),Assign(Id('j'),BinaryOp('||',BinaryOp('||',Id('i'),Id('i')),Id('i'))),Assign(Id('j'),BinaryOp('&&',BinaryOp('&&',Id('i'),Id('i')),Id('i')))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 377))

    def test_operator_assoc_378(self):
        """test operator associativity"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                j = --i;
                j = -.-.i;
                j = --.i;
                j = -.-i;
                j = !!i;
                j = !-.1;
                j = !-i;
                j = !-.i;
                j = !i;
                j = !-.-i;
                j = !-i;
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('j'),[],None),VarDecl(Id('brr'),[1000],None)],([],[Assign(Id('j'),UnaryOp('-',UnaryOp('-',Id('i')))),Assign(Id('j'),UnaryOp('-.',UnaryOp('-.',Id('i')))),Assign(Id('j'),UnaryOp('-',UnaryOp('-.',Id('i')))),Assign(Id('j'),UnaryOp('-.',UnaryOp('-',Id('i')))),Assign(Id('j'),UnaryOp('!',UnaryOp('!',Id('i')))),Assign(Id('j'),UnaryOp('!',UnaryOp('-.',IntLiteral(1)))),Assign(Id('j'),UnaryOp('!',UnaryOp('-',Id('i')))),Assign(Id('j'),UnaryOp('!',UnaryOp('-.',Id('i')))),Assign(Id('j'),UnaryOp('!',Id('i'))),Assign(Id('j'),UnaryOp('!',UnaryOp('-.',UnaryOp('-',Id('i'))))),Assign(Id('j'),UnaryOp('!',UnaryOp('-',Id('i'))))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 378))

    def test_operator_assoc_379(self):
        """test operator associativity"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                j = (a()[0])[0];
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('j'),[],None),VarDecl(Id('brr'),[1000],None)],([],[Assign(Id('j'),ArrayCell(ArrayCell(CallExpr(Id('a'),[]),[IntLiteral(0)]),[IntLiteral(0)]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 379))

    def test_operator_assoc_380(self):
        """test operator associativity"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                j = (i != i) != i;
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('j'),[],None),VarDecl(Id('brr'),[1000],None)],([],[Assign(Id('j'),BinaryOp('!=',BinaryOp('!=',Id('i'),Id('i')),Id('i')))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 380))

    def test_381(self):
        """test common"""
        testcase = r"""Function: function
            Body:
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 381))

    def test_382(self):
        """test common"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                j = j == j;
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('j'),[],None),VarDecl(Id('brr'),[1000],None)],([],[Assign(Id('j'),BinaryOp('==',Id('j'),Id('j')))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 382))

    def test_383(self):
        """test common"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                For (i=0,1,0) Do
                EndFor.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('j'),[],None),VarDecl(Id('brr'),[1000],None)],([],[For(Id('i'),IntLiteral(0),IntLiteral(1),IntLiteral(0),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 383))

    def test_384(self):
        """test common"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                ** Stupid comment **
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('j'),[],None),VarDecl(Id('brr'),[1000],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 384))

    def test_385(self):
        """test common"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                i = True || False;
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('j'),[],None),VarDecl(Id('brr'),[1000],None)],([],[Assign(Id('i'),BinaryOp('||',BooleanLiteral(True),BooleanLiteral(False)))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 385))

    def test_386(self):
        """test common"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                tuple = tuple(i, j);
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('j'),[],None),VarDecl(Id('brr'),[1000],None)],([],[Assign(Id('tuple'),CallExpr(Id('tuple'),[Id('i'),Id('j')]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 386))

    def test_387(self):
        """test common"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                ** Another stupid comment **
                j = i != (i != i);
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('j'),[],None),VarDecl(Id('brr'),[1000],None)],([],[Assign(Id('j'),BinaryOp('!=',Id('i'),BinaryOp('!=',Id('i'),Id('i'))))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 387))
        
    def test_388(self):
        """test common"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                While True Do True[True] = False;
                EndWhile.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('j'),[],None),VarDecl(Id('brr'),[1000],None)],([],[While(BooleanLiteral(True),([],[Assign(ArrayCell(BooleanLiteral(True),[BooleanLiteral(True)]),BooleanLiteral(False))]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 388))

    def test_389(self):
        """test common"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                j = i;
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('j'),[],None),VarDecl(Id('brr'),[1000],None)],([],[Assign(Id('j'),Id('i'))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 389))

    def test_390(self):
        """test common"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                j = j != j * {0, 0}[0];
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('j'),[],None),VarDecl(Id('brr'),[1000],None)],([],[Assign(Id('j'),BinaryOp('!=',Id('j'),BinaryOp('*',Id('j'),ArrayCell(ArrayLiteral([IntLiteral(0),IntLiteral(0)]),[IntLiteral(0)]))))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 390))

    def test_391(self):
        """test common"""
        testcase = r"""Var: x = 0,x0 = 0,o0;"""
        expect = Program([VarDecl(Id('x'),[],IntLiteral(0)),VarDecl(Id('x0'),[],IntLiteral(0)),VarDecl(Id('o0'),[],None)])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 391))

    def test_392(self):
        """test common"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                j = true;
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('j'),[],None),VarDecl(Id('brr'),[1000],None)],([],[Assign(Id('j'),Id('true'))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 392))

    def test_393(self):
        """test common"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                Var: x_x = 0;
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('j'),[],None),VarDecl(Id('brr'),[1000],None)],([VarDecl(Id('x_x'),[],IntLiteral(0))],[]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 393))

    def test_394(self):
        """test common"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                If True Then
                Else If True Then
                EndIf.EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('j'),[],None),VarDecl(Id('brr'),[1000],None)],([],[If([(BooleanLiteral(True),[],[])],([],[If([(BooleanLiteral(True),[],[])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 394))

    def test_395(self):
        """test common"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                For (i = {}, i, i+1) Do
                EndFor.
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('j'),[],None),VarDecl(Id('brr'),[1000],None)],([],[For(Id('i'),ArrayLiteral([]),Id('i'),BinaryOp('+',Id('i'),IntLiteral(1)),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 395))

    def test_396(self):
        """test common"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                j = j * 2;
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('j'),[],None),VarDecl(Id('brr'),[1000],None)],([],[Assign(Id('j'),BinaryOp('*',Id('j'),IntLiteral(2)))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 396))

    def test_397(self):
        """test common"""
        testcase = r"""Function: function
            Parameter: j, brr[1000]
            Body:
                j = j \. 2;
            EndBody."""
        expect = Program([FuncDecl(Id('function'),[VarDecl(Id('j'),[],None),VarDecl(Id('brr'),[1000],None)],([],[Assign(Id('j'),BinaryOp('\\.',Id('j'),IntLiteral(2)))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 397))

    def test_long_program_398(self):
        """test common"""
        testcase = r"""Var: x;
        Var: y;
        Var: z;
        Function: function
            Parameter: j, brr[1000]
            Body:
                For (j = 0, j < 3, 1) Do
                    If (j == 0) && (j % 3 == 0) Then
                        x = brr[j];
                    ElseIf (j == 1) || (j % 2 == 1) Then
                        y = brr[j];
                        While (y % (j * j) != 0) Do
                            y = y + 1;
                        EndWhile.
                    Else
                        Var: k = 0xFFFFFFFF;
                        k = int_of_string(brr[j]);
                        z = k;
                    EndIf.
                EndFor.
            EndBody.
            
        Function: main
            Parameter: argv[1000], argc
            Body:
                function(argc, argv);
            EndBody."""
        expect = Program([VarDecl(Id('x'),[],None),VarDecl(Id('y'),[],None),VarDecl(Id('z'),[],None),FuncDecl(Id('function'),[VarDecl(Id('j'),[],None),VarDecl(Id('brr'),[1000],None)],([],[For(Id('j'),IntLiteral(0),BinaryOp('<',Id('j'),IntLiteral(3)),IntLiteral(1),([],[If([(BinaryOp('&&',BinaryOp('==',Id('j'),IntLiteral(0)),BinaryOp('==',BinaryOp('%',Id('j'),IntLiteral(3)),IntLiteral(0))),[],[Assign(Id('x'),ArrayCell(Id('brr'),[Id('j')]))]),(BinaryOp('||',BinaryOp('==',Id('j'),IntLiteral(1)),BinaryOp('==',BinaryOp('%',Id('j'),IntLiteral(2)),IntLiteral(1))),[],[Assign(Id('y'),ArrayCell(Id('brr'),[Id('j')])),While(BinaryOp('!=',BinaryOp('%',Id('y'),BinaryOp('*',Id('j'),Id('j'))),IntLiteral(0)),([],[Assign(Id('y'),BinaryOp('+',Id('y'),IntLiteral(1)))]))])],([VarDecl(Id('k'),[],IntLiteral(4294967295))],[Assign(Id('k'),CallExpr(Id('int_of_string'),[ArrayCell(Id('brr'),[Id('j')])])),Assign(Id('z'),Id('k'))]))]))])),FuncDecl(Id('main'),[VarDecl(Id('argv'),[1000],None),VarDecl(Id('argc'),[],None)],([],[CallStmt(Id('function'),[Id('argc'),Id('argv')])]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 398))

    def test_long_program_399(self):
        """test common"""
        testcase = r"""Var: x = 0, y = 0, z = 0;
        Function: function
            Parameter: j, brr[1000]
            Body:
                For (j = 0, j < 3, 1) Do
                    If (j == 0) && (j % 3 == 0) Then
                        x = brr[j];
                    ElseIf (j == 1) || (j % 2 == 1) Then
                        y = brr[j];
                        While (y % (j * j) != 0) Do
                            y = y + 1;
                        EndWhile.
                    Else
                        Var: k = 0xFFFFFFFF;
                        k = int_of_string(brr[j]);
                        z = k;
                    EndIf.
                EndFor.
            EndBody.
            
        Function: super_print
            Parameter: str, n
            Body:
                For (i = 0, i < n, 1) Do
                    print(str);
                EndFor.
            EndBody.
            
        Function: main
            Parameter: argv[1000], argc
            Body:
                function(argc + 1, argv);
                Do
                    print("\n\r");
                    super_print("Hello World\n");
                While True
                EndDo.
            EndBody."""
        expect = Program([VarDecl(Id('x'),[],IntLiteral(0)),VarDecl(Id('y'),[],IntLiteral(0)),VarDecl(Id('z'),[],IntLiteral(0)),FuncDecl(Id('function'),[VarDecl(Id('j'),[],None),VarDecl(Id('brr'),[1000],None)],([],[For(Id('j'),IntLiteral(0),BinaryOp('<',Id('j'),IntLiteral(3)),IntLiteral(1),([],[If([(BinaryOp('&&',BinaryOp('==',Id('j'),IntLiteral(0)),BinaryOp('==',BinaryOp('%',Id('j'),IntLiteral(3)),IntLiteral(0))),[],[Assign(Id('x'),ArrayCell(Id('brr'),[Id('j')]))]),(BinaryOp('||',BinaryOp('==',Id('j'),IntLiteral(1)),BinaryOp('==',BinaryOp('%',Id('j'),IntLiteral(2)),IntLiteral(1))),[],[Assign(Id('y'),ArrayCell(Id('brr'),[Id('j')])),While(BinaryOp('!=',BinaryOp('%',Id('y'),BinaryOp('*',Id('j'),Id('j'))),IntLiteral(0)),([],[Assign(Id('y'),BinaryOp('+',Id('y'),IntLiteral(1)))]))])],([VarDecl(Id('k'),[],IntLiteral(4294967295))],[Assign(Id('k'),CallExpr(Id('int_of_string'),[ArrayCell(Id('brr'),[Id('j')])])),Assign(Id('z'),Id('k'))]))]))])),FuncDecl(Id('super_print'),[VarDecl(Id('str'),[],None),VarDecl(Id('n'),[],None)],([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),Id('n')),IntLiteral(1),([],[CallStmt(Id('print'),[Id('str')])]))])),FuncDecl(Id('main'),[VarDecl(Id('argv'),[1000],None),VarDecl(Id('argc'),[],None)],([],[CallStmt(Id('function'),[BinaryOp('+',Id('argc'),IntLiteral(1)),Id('argv')]),Dowhile(([],[CallStmt(Id('print'),[StringLiteral(r"""\n\r""")]),CallStmt(Id('super_print'),[StringLiteral(r"""Hello World\n""")])]),BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(testcase, expect, 399))
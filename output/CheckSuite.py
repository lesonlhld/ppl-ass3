import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):
    def test_401(self):
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
                EndBody.
            """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id("abc"),[IntLiteral(1)]),FloatLiteral(1.5))))
        self.assertTrue(TestChecker.test(input,expect,401))
        
    def test_402(self):
        """Created automatically"""
        input = r"""
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
        self.assertTrue(TestChecker.test(input,expect,402))
        
    def test_403(self):
        """Created automatically"""
        input = r"""
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
        expect = str(Undeclared(Identifier(),"b"))
        self.assertTrue(TestChecker.test(input,expect,403))
        
    def test_404(self):
        """Created automatically"""
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
        self.assertTrue(TestChecker.test(input,expect,404))
        
    def test_405(self):
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
                EndBody.    
            """
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[Id("w")])))
        self.assertTrue(TestChecker.test(input,expect,405))
        
    def test_406(self):
        """Created automatically"""
        input = r"""Var: faji342F__324dADS;"""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,406))
        
    def test_407(self):
        """Created automatically"""
        input = r""" 
        Var: a = 5;
Var: b[2][3] = {{2,3,4},{4,5,6}};
Var: c, d = 6, e, f;
Var: m, n[10];
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,407))
        
    def test_408(self):
        """Created automatically"""
        input = r""" 
        Var: decimal[108], hexadecimal[0X5456A][0x205F], octdecimal[0o413215][0O123];
        Var: array[5][13456];
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,408))
        
    def test_409(self):
        """Created automatically"""
        input = r""" 
        Var: dsa[432][0X364][0o35721], b = 20.e5, c = "mot con vit xoe ra 2 \n cai canh";
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,409))
        
    def test_410(self):
        """Created automatically"""
        input = r""" 
        Var: x = {**comment trong array**{34221}, {"fsd\\h" **cmt**},2};
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,410))
        
    def test_411(self):
        """Created automatically"""
        input = r""" 
        Var **COMMENT**: ****id = 465632
        **dsfhfsdhjnc^#%#@@~!**;
    Var: sss;
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,411))
        
    def test_412(self):
        """Created automatically"""
        input = r""" 
        Function: abc 
        Parameter: global_var
        Body: 
            dayLA1_teNbIen = 25+6-.2.5%3\100 ; 
        EndBody.
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,412))
        
    def test_413(self):
        """Created automatically"""
        input = r""" Function: emptybody
        Parameter: var
        Body: 
        EndBody.
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,413))
        
    def test_414(self):
        """Created automatically"""
        input = r""" 
        Function: **comment chut da**cocomment 
        Body: 
            x=20;
                x=100.0;
        EndBody.
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,414))
        
    def test_415(self):
        """Created automatically"""
        input = r""" Function: if
        Body:
            If x==i Then Break;
            EndIf. 
        EndBody.
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,415))
        
    def test_416(self):
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
EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("fact"),[Id("x")])))
        self.assertTrue(TestChecker.test(input,expect,416))
        
    def test_417(self):
        """Created automatically"""
        input = r"""
        Function: parameter 
        Parameter: a, b,c[123] ,d[123][234][0]  ,e
        Body: 
            a=1;
        EndBody.
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,417))
        
    def test_418(self):
        """Created automatically"""
        input = r"""Function: iffull


        Parameter: themdauchamphay
        Body: 
            If n == 0 Then
                Return 1;
            ElseIf (n>0) Then
                Return n * fact (n - 1);
            Else
                Return n;
            EndIf.
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,418))
        
    def test_419(self):
        """Created automatically"""
        input = r"""Function: initvalueparam 
        Parameter: n, arr[5]
        Body: 
            Var: r = 10., v;
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,419))
        
    def test_420(self):
        """Created automatically"""
        input = r"""Function: varinstmtlist
        Body:
            Var: i = 0;
            Do
                Var: k = 10;
                i = i + 1;
            While i <= 10 
            EndDo.
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,420))
        
    def test_421(self):
        """Created automatically"""
        input = r"""**sau day la 1 ham \\ main\n**
Function:**het y r** main ** test ne;**
**cmt tum lum ~!$()>?:{}**    Body: a=**235**865;
    EndBody **Body**."""
        expect = str(Undeclared(Identifier(),"a"))
        self.assertTrue(TestChecker.test(input,expect,421))
        
    def test_422(self):
        """Created automatically"""
        input = r"""** This is a single-line comment. **
** This is a
* multi-line
* comment.
**"""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,422))
        
    def test_423(self):
        """Created automatically"""
        input = r"""**Function: while 
        Parameter: x, a
        Body: 
            While x>1 Do
                Var: a = 10;
            EndWhile.
        EndBody.**"""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,423))
        
    def test_424(self):
        """Created automatically"""
        input = r"""Function: multivscmt 
        Body: 
            Var: a = 100, b;
            b = (6\2)*8*b* **b**b*b;
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,424))
        
    def test_425(self):
        """Created automatically"""
        input = r"""Var **test comment**: **bien = "STRING"**
        ****fu={0X743A5,0o26523,321 **cmt**}****;****"""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,425))
        
    def test_426(self):
        """Created automatically"""
        input = r"""Function: cmtinbody 
        Parameter: varrr
        Body: 
            **Do
                x= x+1;
            While x>1 
            EndDo.
            **
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,426))
        
    def test_427(self):
        """Created automatically"""
        input = r"""Function: keyword 
        Body: 
            Dooo=1; While True
            EndDo.
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,427))
        
    def test_428(self):
        """Created automatically"""
        input = r"""Function:main Parameter:x Body:If!a Thenb=2; ElseWhile(x>0)DoBreak;EndWhile.EndIf.EndBody."""
        expect = str(Undeclared(Identifier(),"a"))
        self.assertTrue(TestChecker.test(input,expect,428))
        
    def test_429(self):
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
        self.assertTrue(TestChecker.test(input,expect,429))
        
    def test_430(self):
        """Created automatically"""
        input = r"""Function: ifelseif 
        Parameter: n
        Body: 
            If n <=. 1.2E-4 Then
            n=n*.3.3;
            ElseIf n>.100.2 Then
            n=n\.5;
            EndIf.
        EndBody.
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,430))
        
    def test_431(self):
        """Created automatically"""
        input = r"""Function: testop 
        Body: 
            If ((k==1)&&(i!=0))||(k==5)||!j Then
                f=f%3;
            EndIf.
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,431))
        
    def test_432(self):
        """Created automatically"""
        input = r"""Function: calculate 
        Parameter: n
        Body: 
            Var: a = {1,2,3}, b[2][3] = 5, c[2] = {{1,3},{3,5,7}};
            a[3+foo(3)] = a[b[2][3]] + 4;
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,432))
        
    def test_433(self):
        """Created automatically"""
        input = r"""Function: test_precedence___ 
        Parameter: n
        Body: 
            x = !(!(!a && b) || (c >. 3.e+3) &&!(d < 2));
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,433))
        
    def test_434(self):
        """Created automatically"""
        input = r"""
        Var: x, y[1][3]={{{12,1}, {12., 12e3}},{23}, {13,32}};
        Function: testttt 
        Body: 
            var = (x==123)!= xonxon ;
            x = (var =/= ilv) <. nvh;
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,434))
        
    def test_435(self):
        """Created automatically"""
        input = r"""Function: stmtcallinindex 
        Parameter: n
        Body: 
            a = 3*.4.5\0e-2+arr[3-function("call")];
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,435))
        
    def test_436(self):
        """Created automatically"""
        input = r"""Function: precedence 
        Body: 
            x = -(-15.e-1+(-.45.1*.2.3)*(35+108+a[4]));
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,436))
        
    def test_437(self):
        """Created automatically"""
        input = r"""Function: array 
        Parameter: i , j, arr[1001]
        Body: 
            a[i] = arr[c[2+j][b[i]*3]] + 4;
            i = i + 1;
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,437))
        
    def test_438(self):
        """Created automatically"""
        input = r"""Function: positionoflogicalop 
        Parameter: n
        Body: 
            While (True) Do
                logic=a&&var||!variable;
            EndWhile.
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,438))
        
    def test_439(self):
        """Created automatically"""
        input = r"""Function: signop
        Parameter: n
        Body:
            a = -1082000;
            b = -0X123BCD;
            c = -0o21345;
            d = -a;
            c = -call(a);
            b = -.352.4E-12 ;
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,439))
        
    def test_440(self):
        """Created automatically"""
        input = r"""Function: indexop
        Parameter: n
        Body: 
            a[a[3 + foo(2)][b||True]][b[b[1+0x369]]] = a[b[2][b[12E-9]*3]] + 4;
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,440))
        
    def test_441(self):
        """Created automatically"""
        input = r"""Function: index
        Body: 
            x=arr[a+6];
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,441))
        
    def test_442(self):
        """Created automatically"""
        input = r"""Function: op 
        Body: 
             x = (a >=. 2.3e-13 || (x =/= 2e-35));
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,442))
        
    def test_443(self):
        """Created automatically"""
        input = r"""
        Function: ifelse
        Body:
            Var: x=1;
            If x > 10 Then
                x=25+6-.2.5%3\100*x;
            Else
                x=x+2;
            EndIf.
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,443))
        
    def test_444(self):
        """Created automatically"""
        input = r"""Function: var_decl 
        Parameter: naybingeohuhu
        Body:
Var: r = 10., v;
v = (4. \. 3.) *. 3.14 *. r *. r *. r;
EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,444))
        
    def test_445(self):
        """Created automatically"""
        input = r"""Function: assign 
        Parameter: n
        Body: a = {1,2,3}; b[2][3] = 5;
        c[2] = {{1,3},{1,5,7}};
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,445))
        
    def test_446(self):
        """Created automatically"""
        input = r"""Function: ifOKE 
        Body: 
            If n == 0 Then
                Return 1;
            Else
                Return n * fact (n - 1);
            EndIf.
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,446))
        
    def test_447(self):
        """Created automatically"""
        input = r"""Function: iFmoreElseIf
        Parameter: n
        Body: 
            If bool_of_string("True") Then
                a = int_of_string (read ());
            ElseIf n =/= 1.08 Then
                b = float_of_int (a) +. 2.0;
            ElseIf False Then
                Return n;
            EndIf.
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,447))
        
    def test_448(self):
        """Created automatically"""
        input = r"""Function: fullIf 
        Body: 
            If (x == (b!=c && (a > b + c))) Then Return;
            ElseIf (x=="Chung Xon@@") Then Break;
            Else 
            x="successful";
            EndIf.
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,448))
        
    def test_449(self):
        """Created automatically"""
        input = r"""Function: ifELSEelseif
        Body: 
            If i <. 4.5 Then
                print(i);
            ElseIf n > 10 Then 
                Break;
            Else
                i=i-1;
            EndIf.
            EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,449))
        
    def test_450(self):
        """Created automatically"""
        input = r"""Function: iflongnhau
        Parameter: a, b
        Body:
        Var: id[4312][867][9856][867], stringID[108] = "day la \\ 1 chuoi !!",literal = 120000e-1,  array[2][3] = {{867,345,987},{76,12,744}};
            If n > 10 Then
                If n <. 20.5 Then Return x;
                EndIf.
                printStrLn(arg);
            Else fact(x);
            EndIf.
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,450))
        
    def test_451(self):
        """Created automatically"""
        input = r"""
        Function: foroke
        Body: 
            For (i = 0, i < 10, 2) Do
                writeln(i);
            EndFor.
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,451))
        
    def test_452(self):
        """Created automatically"""
        input = r"""
        Function: forinitfail 
        Parameter: n[5]
        Body: 
            For (i = 0, i < 10, 1) Do
                n[i]=n+i;
            EndFor.
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,452))
        
    def test_453(self):
        """Created automatically"""
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
        self.assertTrue(TestChecker.test(input,expect,453))
        
    def test_454(self):
        """Created automatically"""
        input = r"""
        Function: formissing
        Body: 
            For (i=12, i < k, i*i) Do
            goo();
            EndFor.
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,454))
        
    def test_455(self):
        """Created automatically"""
        input = r"""
        Function: fornotendfor
        Body: 
            For (i = 1, i <= x*x,i*i+.1.5)
            Do x=x+1;
            EndFor.
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,455))
        
    def test_456(self):
        """Created automatically"""
        input = r"""
        Function: forinfor
        Parameter: row,col,sum,arr[5][9]
        Body:
            Var: sum=0;
            For( i=0,i<=row,1) Do
                For(j=0,j<col,2) Do
                    sum=sum+arr[i][j];
                EndFor.
            EndFor.
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,456))
        
    def test_457(self):
        """Created automatically"""
        input = r"""Function: whileoke
        Body: 
            Var: i = 0,k=10;
            While i !=k Do
                a[i] = b + i +. 15.0;
                i = i + 1;
            EndWhile.
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,457))
        
    def test_458(self):
        """Created automatically"""
        input = r"""Function: whileandif 
        Body:
            Var: x=20;
            While True Do
                If x==0 Then Break;
                ElseIf x%2==0 Then
                    x=x\2;
                Else writeln(x);
                EndIf.
            EndWhile.
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,458))
        
    def test_459(self):
        """Created automatically"""
        input = r"""Function: whilenullstmt
        Body:
            While i < 5 Do EndWhile.
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,459))
        
    def test_460(self):
        """Created automatically"""
        input = r"""Function: whileinwhile 
        Parameter: x
        Body: 
            While (True) Do
                While (x>=0) Do
                    x = x+-1;
                EndWhile.
                If ((x<0)) Then Break; EndIf.
            EndWhile.
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,460))
        
    def test_461(self):
        """Created automatically"""
        input = r"""Function: whilenotendwhile 
        Parameter: n
        Body: 
            While True Do
                Whilen>=1 Do
                    Whilen<.69.96 Do
                        While n%3==1 Do
                            n = n \ 5;
                        EndWhile
                    .EndWhile.
                EndWhile.
            EndWhile.
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,461))
        
    def test_462(self):
        """Created automatically"""
        input = r"""
        Function: main
        Body:
            While True Do print("Hello World"); EndWhile.
        EndBody."""
        expect = str(Undeclared(Function(),"print"))
        self.assertTrue(TestChecker.test(input,expect,462))
        
    def test_463(self):
        """Created automatically"""
        input = r"""Function: whileindowhile
        Parameter: x
        Body:
            Do
                While a<100 Do
                    a=a-30;
                EndWhile.
            While (a>1)
            EndDo.
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,463))
        
    def test_464(self):
        """Created automatically"""
        input = r"""Function: testdowhile
        Parameter: x,a,b
        Body: 
            Do x = a + b;
            While(x<1000.e5)
            EndDo.
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,464))
        
    def test_465(self):
        """Created automatically"""
        input = r"""Function: notexpr 
        Parameter: n
        Body: 
            Do  
                Return 1;
            While a =/= 2.2 EndDo.
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,465))
        
    def test_466(self):
        """Created automatically"""
        input = r"""Function: breaktest 
        Parameter: x
        Body: 
            While x >= 1 Do
                If y<100 Then Break;
                EndIf.
            EndWhile.
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,466))
        
    def test_467(self):
        """Created automatically"""
        input = r"""Function: break
        Body: 
            For (i=0, i!=9, (i*.2.0)) Do
                If i>=10 Then Break;
                EndIf.
            EndFor.
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,467))
        
    def test_468(self):
        """Created automatically"""
        input = r"""Function: continue 
        Body: 
            For (i=0, i!=9, i) Do
                If i==10 Then Continue;
                EndIf.
                foo();
            EndFor.
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,468))
        
    def test_469(self):
        """Created automatically"""
        input = r"""Function: breakandcontinuealone
        Body: 
            Continue;
            Break;
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,469))
        
    def test_470(self):
        """Created automatically"""
        input = r"""Function: callstmt 
        Parameter: x,y
        Body:
            foo(2 + x, 4. \. y);
            goo();
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,470))
        
    def test_471(self):
        """Created automatically"""
        input = r"""Function: callmore
        Body: 
            call(a,876,var*.65e-1,arr[3],True,"chuoi~~\n");
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,471))
        
    def test_472(self):
        """Created automatically"""
        input = r"""Var: callnotinfunction;
        Function: a
        Body:
            goo(x,y*2,z+3.00000003);
            EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,472))
        
    def test_473(self):
        """Created automatically"""
        input = r"""Function: callwithoutsemi
        Body: 
            iden__TI_FIerOf_Function(a,b_,c+.3.e-2);
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,473))
        
    def test_474(self):
        """Created automatically"""
        input = r"""Function: testreturn 
        Parameter: n
        Body: 
            Var: t=False;
            If n<100 Then t=True;
            EndIf.
            Return t;
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,474))
        
    def test_475(self):
        """Created automatically"""
        input = r"""Function: returnnull 
        Parameter: i
        Body: 
            If i==0 Then Return;
            EndIf.
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,475))
        
    def test_476(self):
        """Created automatically"""
        input = r"""Function: returnstring
            Body:
                Return "String";
            EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,476))
        
    def test_477(self):
        """Created automatically"""
        input = r"""
            Function: returnboolean
            Body:
            If str == "Chung Xon" Then
                Return True;
            Else
                Return False;
                EndIf.
            EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,477))
        
    def test_478(self):
        """Created automatically"""
        input = r"""
        Function: funccallfail 
        Body:
        foo=a+2;
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,478))
        
    def test_479(self):
        """Created automatically"""
        input = r"""Function: array
        Parameter: x[123]
        Body:
            Var: i = 0;
            x[123]={996,712,216};
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,479))
        
    def test_480(self):
        """Created automatically"""
        input = r"""Function: arrayinarray 
                Parameter: x[2][3]
        Body:
            Var: i = 0;
            x[2][3]={{867,345,987},{76,12,744}};
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,480))
        
    def test_481(self):
        """Created automatically"""
        input = r"""
        Var: stringinarray, x[123]={"STRING","aRraY1","Array2"};"""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,481))
        
    def test_482(self):
        """Created automatically"""
        input = r"""Function: arrayhavespace
        Body: 
            Var  : x[123]={   20, 2   ,108  };
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,482))
        
    def test_483(self):
        """Created automatically"""
        input = r"""Function: complexarray
            Body: x[123]={"duwat73\r \t", "@#&\n rwFEW54",54312,10.e13, 0.123, 543.0e-6  ,{"xe mau xanh"},"xe mau do"};
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,483))
        
    def test_484(self):
        """Created automatically"""
        input = r"""Function: arraynull
        Body: 
            a[12] = {  };
            x[45]={{{{{}}}}};

        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,484))
        
    def test_485(self):
        """Created automatically"""
        input = r"""Function: multicallstmt
        Body:
            a =-((func1(a)+23) * -func2(4)+arr[3])\. 0.5;
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,485))
        
    def test_486(self):
        """Created automatically"""
        input = r"""Function: callincall
        Body:
            a =func1(foo(3))+23 - func2(goo(foo(a)));
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,486))
        
    def test_487(self):
        """Created automatically"""
        input = r"""Function: a Parameter: a Body: Var: a=False;EndBody. Function: b Body: EndBody.
Function: d**Here some too**Parameter: d Body: EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,487))
        
    def test_488(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body:
            Var: i = 0;
            While i!=423 Do
                fact (i);
                i = i + 3; **cmt**
                If i==212 Then Break;
                a = (!(b && c)||!(a&&b)); 
                EndIf.
            EndWhile.
        EndBody.
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,488))
        
    def test_489(self):
        """Created automatically"""
        input = r"""Function: mmmmm
        Body: 
            Do
                While(1) Do
                foo (2 + x, 4. \. y);goo ();
            EndWhile.
            While(1)
            EndDo.
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,489))
        
    def test_490(self):
        """Created automatically"""
        input = r"""Function: more1
        Parameter: a[5], b
        Body:
        Var: x = {{1,2,3}, **Comment here** "abc"};
        Var: i = 0;
        While (i < 5) Do
        If i == 3 ThenReturn 1;EndIf.
        i = i + 1;
        EndWhile.
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,490))
        
    def test_491(self):
        """Created automatically"""
        input = r"""Function: factorialOfNumber
        Parameter: n
        Body:
        Var:factorial=1;
        print("Enter integer: ");
        read();
        For (i=0, i<=n, 1) Do
            factorial=factorial*i;
        EndFor.
        print(factorial);
        Return factorial;
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,491))
        
    def test_492(self):
        """Created automatically"""
        input = r"""Function: fibo
        Parameter: n
        Body:
            Var: n, t1 = 0, t2 = 1, nextTerm = 0;
            print("Enter the number of terms: ");
            getline(n);
            print("Fibonacci Series: ");
            For (i = 1, i <= n, 1) Do
                If(i == 1) Then
                print(" " + t1);
                Continue;
                EndIf.
            If(i == 2) Then
                print( t2+" ");
        Continue;
        EndIf.
        nextTerm = t1 + t2;
        t1 = t2;
        t2 = nextTerm;
        
        print(nextTerm + " ");
    EndFor.
    Return 0;
    EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,492))
        
    def test_493(self):
        """Created automatically"""
        input = r"""Function: octalToDecimal
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
    EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,493))
        
    def test_494(self):
        """Created automatically"""
        input = r""" Function: foo
                        Parameter: a
                        Body:
                        Var: x = 2;
                        EndBody.
                """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,494))
        
    def test_495(self):
        """Created automatically"""
        input = r"""Function: ifOKE 
        Body: 
            If n == 0 Then
                Break;
            EndIf.
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,495))
        
    def test_496(self):
        """Created automatically"""
        input = r"""Function: ifOKE 
        Body: 
            If n == 0 Then
                x = 3;
            ElseIf x != 2 Then
                check = False;
            EndIf.
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,496))
        
    def test_497(self):
        """Created automatically"""
        input = r"""Var: a[2] = {True,{2,3}}, str = "string";
        Function: func
        Body:
            If (a + 5) && (j-6) || (k*7) Then
               
                a[i] = b +. 1.0;
                b = i - b * a -. b \ c - -.d;
            EndIf.
            Return a+func(123);
        EndBody.
        Function: main
        Body:
            func();
            Return 0;
        EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("+",Id("a"),IntLiteral(5))))
        self.assertTrue(TestChecker.test(input,expect,497))
        
    def test_498(self):
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
        self.assertTrue(TestChecker.test(input,expect,498))
        
    def test_499(self):
        """Created automatically"""
        input = r"""Var: a = 5;

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
        EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("main"),[IntLiteral(123)])))
        self.assertTrue(TestChecker.test(input,expect,499))
        
    def test_500(self):
        """Created automatically"""
        input = r"""Function: index
        Body: 
            arr(a + bbb[61.2 *. (x + y)])[2] = b[2][3];
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,500))
        
    def test_501(self):
        """Created automatically"""
        input = r"""
            Function: print
            Parameter: n,x
            Body:
                Var: i;
                For (i = 0, i < sqrt(n), 2) Do
                    x = i + n;
                    print(x\2);
                EndFor.
            EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,501))
        
    def test_502(self):
        """Created automatically"""
        input = r"""Function: test1
        Body: 
            m = test2(a,b) + test1 (x);
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
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,502))
        
    def test_503(self):
        """Created automatically"""
        input = r"""Function: mix 
        Body: 
            While x>1 Do
                For (i = 100,True, i-1) Do
                    If a<3 Then
                        Break;
                    EndIf.
                    a = a -1;
                EndFor.
            EndWhile.
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,503))
        
    def test_504(self):
        """Created automatically"""
        input = r"""Function: printchar 
        Body:
            For (a = 1, a <= len(str),1 ) Do
                writeln(str[a]);
            EndFor.
        EndBody."""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,504))
        
    def test_505(self):
        """Created automatically"""
        input = r"""Function: test
            Parameter: a,b
            Body:
                a = "string 1";
                b = "string 2";
                Return a+b;
            EndBody. """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,505))
        
    def test_506(self):
        """Created automatically"""
        input = r"""Function: tinhtoansml
            Parameter: a,b
            Body:
                a[3 +. 10e2] = (foo(x) +. 12.e3) *. 0x123 - a[b[2][3]] + 4;
            EndBody. """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,506))
        
    def test_507(self):
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
                EndBody.
            """
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[Id("x")])))
        self.assertTrue(TestChecker.test(input,expect,507))
        
    def test_508(self):
        """Created automatically"""
        input = r""" 
            Function: nhieuoilanhieu 
            Body:
                Var: x, y[1][3]={{{12,1}, {12., 12e3}},{23}, {13,32}};
                Var: b = True, c = False;
                For (i = 0, i < 10, 2) Do
                    For (i = 1, i < x*x , i + 1 ) Do
                        If(z == False) Then
                            x = haha();
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
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,508))
        
    def test_509(self):
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
        self.assertTrue(TestChecker.test(input,expect,509))
        
    def test_510(self):
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
                    y = foo(x);
                EndBody.
            """
        expect = str(TypeCannotBeInferred(CallStmt(Id("foo"),[Id("x")])))
        self.assertTrue(TestChecker.test(input,expect,510))
        
    def test_511(self):
        """Created automatically"""
        input = r"""
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
        self.assertTrue(TestChecker.test(input,expect,511))
        
    def test_512(self):
        """Created automatically"""
        input = r"""
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
        self.assertTrue(TestChecker.test(input,expect,512))
        
    def test_513(self):
        """Created automatically"""
        input = r"""
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
        self.assertTrue(TestChecker.test(input,expect,513))
        
    def test_514(self):
        """Created automatically"""
        input = r"""Function: main 
                    Body:
                        printStrLn(read(4));
                    EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,514))
        
    def test_515(self):
        """Created automatically"""
        input = Program([FuncDecl(Id("main"),[],([],[CallStmt(Id("printStrLn"),[CallExpr(Id("read"),[IntLiteral(4)])])]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,515))
        
    def test_516(self):
        """Created automatically"""
        input = r"""Function: main  
                   Body:
                        printStrLn();
                    EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,516))
        
    def test_517(self):
        """Created automatically"""
        input = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None)],([],[CallStmt(Id("printStrLn"),[])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,517))
        
    def test_518(self):
        """Created automatically"""
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
        self.assertTrue(TestChecker.test(input,expect,518))
        
    def test_519(self):
        """Created automatically"""
        input = r"""Function: main
        Parameter: n
                   Body: 
                        foo();
                   EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,519))
        
    def test_520(self):
        """Created automatically"""
        input = Program([FuncDecl(Id("main"),[],([],[CallExpr(Id("foo"),[])]))])
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,520))
        
    def test_521(self):
        """Created automatically"""
        input = Program([VarDecl(Id("main"),[],IntLiteral(5)),VarDecl(Id("b"),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[],IntLiteral(6)),VarDecl(Id("e"),[],None),VarDecl(Id("f"),[],None),VarDecl(Id("m"),[],None),VarDecl(Id("n"),[10],None)])
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,521))
        
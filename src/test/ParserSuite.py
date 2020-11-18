import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_201(self):
        """Created automatically"""
        input = r"""Var: faji342F__324dADS;""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,201))
    def test_202(self):
        """Created automatically"""
        input = r""" 
        Var: a = 5;
Var: b[2][3] = {{2,3,4},{4,5,6}};
Var: c, d = 6, e, f;
Var: m, n[10];
        """ 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,202))
    def test_203(self):
        """Created automatically"""
        input = r""" 
        Var: decimal[108], hexadecimal[0X5456A][0x205F], octdecimal[0o413215][0O123];
        Var: array[5][13456];
        """ 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,203))
    def test_204(self):
        """Created automatically"""
        input = r""" 
        Var: dsa[432][0X364][0o35721], b = 20.e5, c = "mot con vit xoe ra 2 \n cai canh";
        """ 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test_205(self):
        """Created automatically"""
        input = r""" 
        Var: x = {**comment trong array**{34221}, {"fsd\\h" **cmt**},2};
        """ 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test_206(self):
        """Created automatically"""
        input = r""" 
        Var **COMMENT**: ****id = 465632
        **dsfhfsdhjnc^#%#@@~!**;
    Var: sss;
        """ 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test_207(self):
        """Created automatically"""
        input = r""" 
        Function: abc 
        Parameter: global_var
        Body: 
            dayLA1_teNbIen = 25+6-.2.5%3\100 ; 
        EndBody.
        """ 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,207))
    def test_208(self):
        """Created automatically"""
        input = r""" Function: emptybody
        Parameter: var
        Body: 
        EndBody.
        """ 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,208))
    def test_209(self):
        """Created automatically"""
        input = r""" 
        Function: **comment chut da**cocomment 
        Body: 
            x=20;
                x=100.0;
        EndBody.
        """ 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,209))
    def test_210(self):
        """Created automatically"""
        input = r""" Function: if
        Body:
            If x==i Then Break;
            EndIf. 
        EndBody.
        """ 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,210))
    def test_211(self):
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
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,211))
    def test_212(self):
        """Created automatically"""
        input = r"""
        Function: parameter 
        Parameter: a, b,c[123] ,d[123][234][0]  ,e
        Body: 
            a=1;
        EndBody.
        """ 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,212))
    def test_213(self):
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
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,213))
    def test_214(self):
        """Created automatically"""
        input = r"""Function: initvalueparam 
        Parameter: n, arr[5]
        Body: 
            Var: r = 10., v;
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,214))
    def test_215(self):
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
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,215))
    def test_216(self):
        """Created automatically"""
        input = r"""**sau day la 1 ham \\ main\n**
Function:**het y r** main ** test ne;**
**cmt tum lum ~!$()>?:{}**    Body: a=**235**865;
    EndBody **Body**.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,216))
    def test_217(self):
        """Created automatically"""
        input = r"""** This is a single-line comment. **
** This is a
* multi-line
* comment.
**""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,217))
    def test_218(self):
        """Created automatically"""
        input = r"""**Function: while 
        Parameter: x, a
        Body: 
            While x>1 Do
                Var: a = 10;
            EndWhile.
        EndBody.**""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,218))
    def test_219(self):
        """Created automatically"""
        input = r"""Function: multivscmt 
        Body: 
            Var: a = 100, b;
            b = (6\2)*8*b* **b**b*b;
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,219))
    def test_220(self):
        """Created automatically"""
        input = r"""Var **test comment**: **bien = "STRING"**
        ****fu={0X743A5,0o26523,321 **cmt**}****;****""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,220))
    def test_221(self):
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
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,221))
    def test_222(self):
        """Created automatically"""
        input = r"""Function: keyword 
        Body: 
            Dooo=1; While True
            EndDo.
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,222))
    def test_223(self):
        """Created automatically"""
        input = r"""Function:main Parameter:x Body:If!a Thenb=2; ElseWhile(x>0)DoBreak;EndWhile.EndIf.EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,223))
    def test_224(self):
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
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,224))
    def test_225(self):
        """Created automatically"""
        input = r"""Function: testop 
        Body: 
            If ((k==1)&&(i!=0))||(k==5)||!j Then
                f=f%3;
            EndIf.
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,225))
    def test_226(self):
        """Created automatically"""
        input = r"""Function: calculate 
        Parameter: n
        Body: 
            Var: a = {1,2,3}, b[2][3] = 5, c[2] = {{1,3},{3,5,7}};
            a[3+foo(3)] = a[b[2][3]] + 4;
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,226))
    def test_227(self):
        """Created automatically"""
        input = r"""Function: test_precedence___ 
        Parameter: n
        Body: 
            x = !(!(!a && b) || (c >. 3.e+3) &&!(d < 2));
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,227))
    def test_228(self):
        """Created automatically"""
        input = r"""
        Var: x, y[1][3]={{{12,1}, {12., 12e3}},{23}, {13,32}};
        Function: testttt 
        Body: 
            var = (x==123)!= xonxon ;
            x = (var =/= ilv) <. nvh;
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,228))
    def test_229(self):
        """Created automatically"""
        input = r"""Function: stmtcallinindex 
        Parameter: n
        Body: 
            a = 3*.4.5\0e-2+arr[3-function("call")];
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,229))
    def test_230(self):
        """Created automatically"""
        input = r"""Function: precedence 
        Body: 
            x = -(-15.e-1+(-.45.1*.2.3)*(35+108+a[4]));
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,230))
    def test_231(self):
        """Created automatically"""
        input = r"""Function: array 
        Parameter: i , j, arr[1001]
        Body: 
            a[i] = arr[c[2+j][b[i]*3]] + 4;
            i = i + 1;
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,231))
    def test_232(self):
        """Created automatically"""
        input = r"""Function: positionoflogicalop 
        Parameter: n
        Body: 
            While (True) Do
                logic=a&&var||!variable;
            EndWhile.
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,232))
    def test_233(self):
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
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,233))
    def test_234(self):
        """Created automatically"""
        input = r"""Function: indexop
        Parameter: n
        Body: 
            a[a[3 + foo(2)][b||True]][b[b[1+0x369]]] = a[b[2][b[12E-9]*3]] + 4;
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,234))
    def test_235(self):
        """Created automatically"""
        input = r"""Function: index
        Body: 
            x=arr[a+6];
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,235))
    def test_236(self):
        """Created automatically"""
        input = r"""Function: op 
        Body: 
             x = (a >=. 2.3e-13 || (x =/= 2e-35));
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,236))
    def test_237(self):
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
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,237))
    def test_238(self):
        """Created automatically"""
        input = r"""Function: var_decl 
        Parameter: naybingeohuhu
        Body:
Var: r = 10., v;
v = (4. \. 3.) *. 3.14 *. r *. r *. r;
EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,238))
    def test_239(self):
        """Created automatically"""
        input = r"""Function: assign 
        Parameter: n
        Body: a = {1,2,3}; b[2][3] = 5;
        c[2] = {{1,3},{1,5,7}};
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,239))
    def test_240(self):
        """Created automatically"""
        input = r"""Function: ifOKE 
        Body: 
            If n == 0 Then
                Return 1;
            Else
                Return n * fact (n - 1);
            EndIf.
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,240))
    def test_241(self):
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
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,241))
    def test_242(self):
        """Created automatically"""
        input = r"""Function: fullIf 
        Body: 
            If (x == (b!=c && (a > b + c))) Then Return;
            ElseIf (x=="Chung Xon@@") Then Break;
            Else 
            x="successful";
            EndIf.
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,242))
    def test_243(self):
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
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,243))
    def test_244(self):
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
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,244))
    def test_245(self):
        """Created automatically"""
        input = r"""
        Function: foroke
        Body: 
            For (i = 0, i < 10, 2) Do
                writeln(i);
            EndFor.
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,245))
    def test_246(self):
        """Created automatically"""
        input = r"""
        Function: forinitfail 
        Parameter: n[5]
        Body: 
            For (i = 0, i < 10, 1) Do
                n[i]=n+i;
            EndFor.
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,246))
    def test_247(self):
        """Created automatically"""
        input = r"""
        Function: formissing
        Body: 
            For (i=12, i < k, i*i) Do
            goo();
            EndFor.
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,247))
    def test_248(self):
        """Created automatically"""
        input = r"""
        Function: fornotendfor
        Body: 
            For (i = 1, i <= x*x,i*i+.1.5)
            Do x=x+1;
            EndFor.
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,248))
    def test_249(self):
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
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,249))
    def test_250(self):
        """Created automatically"""
        input = r"""Function: whileoke
        Body: 
            Var: i = 0,k=10;
            While i !=k Do
                a[i] = b + i +. 15.0;
                i = i + 1;
            EndWhile.
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,250))
    def test_251(self):
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
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,251))
    def test_252(self):
        """Created automatically"""
        input = r"""Function: whilenullstmt
        Body:
            While i < 5 Do EndWhile.
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,252))
    def test_253(self):
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
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,253))
    def test_254(self):
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
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,254))
    def test_255(self):
        """Created automatically"""
        input = r"""
        Function: main
        Body:
            While True Do print("Hello World"); EndWhile.
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,255))
    def test_256(self):
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
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,256))
    def test_257(self):
        """Created automatically"""
        input = r"""Function: testdowhile
        Parameter: x,a,b
        Body: 
            Do x = a + b;
            While(x<1000.e5)
            EndDo.
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,257))
    def test_258(self):
        """Created automatically"""
        input = r"""Function: notexpr 
        Parameter: n
        Body: 
            Do  
                Return 1;
            While a =/= 2.2 EndDo.
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,258))
    def test_259(self):
        """Created automatically"""
        input = r"""Function: breaktest 
        Parameter: x
        Body: 
            While x >= 1 Do
                If y<100 Then Break;
                EndIf.
            EndWhile.
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,259))
    def test_260(self):
        """Created automatically"""
        input = r"""Function: break
        Body: 
            For (i=0, i!=9, (i*.2.0)) Do
                If i>=10 Then Break;
                EndIf.
            EndFor.
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,260))
    def test_261(self):
        """Created automatically"""
        input = r"""Function: continue 
        Body: 
            For (i=0, i!=9, i) Do
                If i==10 Then Continue;
                EndIf.
                foo();
            EndFor.
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,261))
    def test_262(self):
        """Created automatically"""
        input = r"""Function: breakandcontinuealone
        Body: 
            Continue;
            Break;
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,262))
    def test_263(self):
        """Created automatically"""
        input = r"""Function: callstmt 
        Parameter: x,y
        Body:
            foo(2 + x, 4. \. y);
            goo();
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,263))
    def test_264(self):
        """Created automatically"""
        input = r"""Function: callmore
        Body: 
            call(a,876,var*.65e-1,arr[3],True,"chuoi~~\n");
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,264))
    def test_265(self):
        """Created automatically"""
        input = r"""Var: callnotinfunction;
        Function: a
        Body:
            goo(x,y*2,z+3.00000003);
            EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,265))
    def test_266(self):
        """Created automatically"""
        input = r"""Function: callwithoutsemi
        Body: 
            iden__TI_FIerOf_Function(a,b_,c+.3.e-2);
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,266))
    def test_267(self):
        """Created automatically"""
        input = r"""Function: testreturn 
        Parameter: n
        Body: 
            Var: t=False;
            If n<100 Then t=True;
            EndIf.
            Return t;
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,267))
    def test_268(self):
        """Created automatically"""
        input = r"""Function: returnnull 
        Parameter: i
        Body: 
            If i==0 Then Return;
            EndIf.
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,268))
    def test_269(self):
        """Created automatically"""
        input = r"""Function: returnstring
            Body:
                Return "String";
            EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,269))
    def test_270(self):
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
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,270))
    def test_271(self):
        """Created automatically"""
        input = r"""
        Function: funccallfail 
        Body:
        foo=a+2;
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,271))
    def test_272(self):
        """Created automatically"""
        input = r"""Function: array
        Parameter: x[123]
        Body:
            Var: i = 0;
            x[123]={996,712,216};
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,272))
    def test_273(self):
        """Created automatically"""
        input = r"""Function: arrayinarray 
                Parameter: x[2][3]
        Body:
            Var: i = 0;
            x[2][3]={{867,345,987},{76,12,744}};
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,273))
    def test_274(self):
        """Created automatically"""
        input = r"""
        Var: stringinarray, x[123]={"STRING","aRraY1","Array2"};""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,274))
    def test_275(self):
        """Created automatically"""
        input = r"""Function: arrayhavespace
        Body: 
            Var  : x[123]={   20, 2   ,108  };
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,275))
    def test_276(self):
        """Created automatically"""
        input = r"""Function: complexarray
            Body: x[123]={"duwat73\r \t", "@#&\n rwFEW54",54312,10.e13, 0.123, 543.0e-6  ,{"xe mau xanh"},"xe mau do"};
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,276))
    def test_277(self):
        """Created automatically"""
        input = r"""Function: arraynull
        Body: 
            a[12] = {  };
            x[45]={{{{{}}}}};

        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,277))
    def test_278(self):
        """Created automatically"""
        input = r"""Function: multicallstmt
        Body:
            a =-((func1(a)+23) * -func2(4)+arr[3])\. 0.5;
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,278))
    def test_279(self):
        """Created automatically"""
        input = r"""Function: callincall
        Body:
            a =func1(foo(3))+23 - func2(goo(foo(a)));
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,279))
    def test_280(self):
        """Created automatically"""
        input = r"""Function: a Parameter: a Body: Var: a=False;EndBody. Function: b Body: EndBody.
Function: d**Here some too**Parameter: d Body: EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,280))
    def test_281(self):
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
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,281))
    def test_282(self):
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
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,282))
    def test_283(self):
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
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,283))
    def test_284(self):
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
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,284))
    def test_285(self):
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
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,285))
    def test_286(self):
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
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,286))
    def test_287(self):
        """Created automatically"""
        input = r""" Function: foo
                        Parameter: a
                        Body:
                        Var: x = 2;
                        EndBody.
                """ 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,287))
    def test_288(self):
        """Created automatically"""
        input = r"""Function: ifOKE 
        Body: 
            If n == 0 Then
                Break;
            EndIf.
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,288))
    def test_289(self):
        """Created automatically"""
        input = r"""Function: ifOKE 
        Body: 
            If n == 0 Then
                x = 3;
            ElseIf x != 2 Then
                check = False;
            EndIf.
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,289))
    def test_290(self):
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
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,290))
    def test_291(self):
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
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,291))
    def test_292(self):
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
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,292))
    def test_293(self):
        """Created automatically"""
        input = r"""Function: index
        Body: 
            arr(a + bbb[61.2 *. (x + y)])[2] = b[2][3];
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,293))
    def test_294(self):
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
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,294))
    def test_295(self):
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
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,295))
    def test_296(self):
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
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,296))
    def test_297(self):
        """Created automatically"""
        input = r"""Function: printchar 
        Body:
            For (a = 1, a <= len(str),1 ) Do
                writeln(str[a]);
            EndFor.
        EndBody.""" 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,297))
    def test_298(self):
        """Created automatically"""
        input = r"""Function: test
            Parameter: a,b
            Body:
                a = "string 1";
                b = "string 2";
                Return a+b;
            EndBody. """ 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,298))
    def test_299(self):
        """Created automatically"""
        input = r"""Function: tinhtoansml
            Parameter: a,b
            Body:
                a[3 +. 10e2] = (foo(x) +. 12.e3) *. 0x123 - a[b[2][3]] + 4;
            EndBody. """ 
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,299))
    def test_300(self):
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
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,300))
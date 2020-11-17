import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_201(self):
        """Simple program: int main() {} """
        input = """Var: x = True;
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_202(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_203(self):
        input = """Function: foo
    Parameter: a[5], b
    Body:
        Var: i = 0;
        While i < 5 Do
            a[i] = b +. 1.0;
            i = i + 1;
        EndWhile.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_204(self):
        input = """Function: isEven
    Parameter: x
    Body:
        If x%2==0 Then
            Return True;
        Else
            Return False;
        EndIf.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    
    def test_205(self):
        input = """Function: check
    Body:
        Var: x = 0;
        If x >= 5 Then
            x = x + 1;
            Return 1;
        ElseIf x >=2 Then
            x = x - 1;
            Return func(x);
        ElseIf x > 0 Then
            x = 0;
            Return 0;
        Else Return False;
        EndIf.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test_206(self):
        input = """Function: isValid
        Parameter: x;y
        x = x +1;
        Body:
        EndBody."""
        expect = "Error on line 2 col 20: ;"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_207(self):
        input = """Function: null
    Body:
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test_208(self):
        input = """Var: x = 5;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test_209(self):
        input = """Var: x[6][7] = {1,2};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))

    def test_210(self):
        input = """Var: y[2][2] = {{1.6,5e-2},{2.02,6.2e-1}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))

    def test_211(self):
        input = """Var: x[2][2] = {{"Huu'"",15},{1,1.5e-2}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    
    def test_212(self):
        input = """Function foo()
        Parameter: x
        Body:
            x = x + 1;
        EndBody."""
        expect = "Error on line 1 col 9: foo"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test_213(self):
        input = r"""Function:
println
Parameter: m
Body:
    print(m + "\n");
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))

    def test_214(self):
        input = """**This is my
*program**
Var: x = "this is my string\\n";
Function: check
Parameter: y
Body:
    If x == y Then
        Return True;
    Else
        Return 0;
    EndIf.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test_215(self):
        input = """**No program**"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test_216(self):
        input = """Var: x = 5"""
        expect = "Error on line 1 col 10: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test_217(self):
        input = """Function: foo
Parameter: x
Body:
    x = x + 1;
    x + 1;
EndBody."""
        expect = "Error on line 5 col 6: +"
        self.assertTrue(TestParser.checkParser(input,expect,217))

    def test_218(self):
        input = """Var: x == 5;
Function: func
Body:
EndBody."""
        expect = "Error on line 1 col 7: =="
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test_219(self):
        input = """If x == 5 Then
    x = x + 1;
    EndIf."""
        expect = "Error on line 1 col 0: If"
        self.assertTrue(TestParser.checkParser(input,expect,219))

    def test_220(self):
        input = """Var: x = 5;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))

    def test_221(self):
        input = """Function: foo
Body:
    x = x+a[5][6];
    y = -5.6e-1;
    Return x - y;
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))

    def test_222(self):
        input = """Function: helloWorld
Parameter: x, e[2][2]
Body:
    a[3 + foo(2)] = a[b[2][3]] + 4;
    writeln("Hello World\\n");
    Return 0;
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))

    def test_223(self):
        input = """Function: main
Body:
    **This is a comment
    **
    x = readln();
    writeln(x);
    Return -1;
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))

    def test_224(self):
        input = """Var: x[9][1];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))

    def test_225(self):
        input = """Function: test
Body:
    x = (foo(x+y[2][3]) && -5);
    Return 6*0X5; 
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))

    def test_226(self):
        input = """Function: feature Parameter: x"""
        expect = "Error on line 1 col 30: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,226))

    def test_227(self):
        input = """Var: ;
        Function: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,227))

    def test_228(self):
        input = """Function: error
Parameter: y
Var: x;
Body:
EndBody."""
        expect = "Error on line 3 col 0: Var"
        self.assertTrue(TestParser.checkParser(input,expect,228))

    def test_229(self):
        input = """Function: expect
Body:
    foo();
    Var: x = 5;
    Return 1;
EndBody."""
        expect = "Error on line 4 col 4: Var"
        self.assertTrue(TestParser.checkParser(input,expect,229))

    def test_230(self):
        input = """Function: sort
Parameter: x[10]
Body:
    sort(x[10]);
    Return True;
EndBody.
Var: x = 5;"""
        expect = "Error on line 7 col 0: Var"
        self.assertTrue(TestParser.checkParser(input,expect,230))

    def test_231(self):
        input = """If x == False Then Return x;"""
        expect = "Error on line 1 col 0: If"
        self.assertTrue(TestParser.checkParser(input,expect,231))

    def test_232(self):
        input = """Function:ham Parameter:x,y,z Body:x=x+1;t[foo(a)+1][5]=10;Return0;EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def test_233(self):
        input = """False"""
        expect = "Error on line 1 col 0: False"
        self.assertTrue(TestParser.checkParser(input,expect,233))

    def test_234(self):
        input = """Function:zip Parameter: Body:x=x+1;Return1;EndBody."""
        expect = "Error on line 1 col 24: Body"
        self.assertTrue(TestParser.checkParser(input,expect,234))

    def test_235(self):
        input = """Var: x = 1;Function:fibonaci Parameter:x Body:Returnfibonaci(x-1)+fibonaci(x-2);EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))

    def test_236(self):
        input = """Function:**Thisis a comment**x Parameter:**t*\n**t****Body:**hello**Return**World**0**semi**;EndBody**dot**."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))

    def test_237(self):
        input = """****Function: hello Parameter:x Body:EndBody.****"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))

    def test_238(self):
        input = """****Function: hello Parameter:x Body:EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))

    def test_239(self):
        input = """Var: x = 5;Function:xParameter:y Body:EndBody."""
        expect = "Error on line 1 col 30: :"
        self.assertTrue(TestParser.checkParser(input,expect,239))

    def test_240(self):
        input = """Var: n = 7.e1;Function: radius Parameter:r Body: If r > 0 Then Return pi*r;EndIf.EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))

    def test_241(self):
        input = """Function: area Parameter: n,m Body: If (n > 0) && (m > 0) Then Return n*m;EndIf.EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test_242(self):
        input = """Var: t = {{"hello","myfen"},{1e-5,0o45,0X2}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))

    def test_243(self):
        input = """Function: test_do Body: Do e = e + 1; While e < 5 EndDo.EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))

    def test_244(self):
        input = """Function: test_stmt Body: While n < 10 Do n=n+2;If n == 5 Then Break;EndIf.EndWhile.EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))

    def test_245(self):
        input = """Function: test_for Body: For (i = 0,i<10,2) Do write(i); If i == 6 Then Continue; EndIf.EndFor.EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test_246(self):
        input = """Function: test_stmt Body: Continue;Break;EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))

    def test_247(self):
        input = """Var [x][y];"""
        expect = "Error on line 1 col 4: ["
        self.assertTrue(TestParser.checkParser(input,expect,247))

    def test_248(self):
        input = """Var: n = 5;Function: thu Parameter: x Body: While x <.5 Do If x == 2 Then print(x);Break; EndIf.x=x+1;EndWhile.EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))

    def test_249(self):
        input = """Var: n;function: n Body:EndBody."""
        expect = "Error on line 1 col 7: function"
        self.assertTrue(TestParser.checkParser(input,expect,249))

    def test_250(self):
        input = """Var: n[1][0.2];"""
        expect = "Error on line 1 col 10: 0.2"
        self.assertTrue(TestParser.checkParser(input,expect,250))

    def test_251(self):
        input = """Var: n = 0;Function:y Body:**This is a cmt**c=1;Return False + True;EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))

    def test_252(self):
        input = """Var: n = {{{1,2,3},{5},{"string",5.e-5}}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def test_253(self):
        input = """Var: str = "escape@@string'"";Function: length Parameter: str Body: If str =/= null Then Return len(str);EndIf.EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))

    def test_254(self):
        input = """var: t = 1;"""
        expect = "Error on line 1 col 0: var"
        self.assertTrue(TestParser.checkParser(input,expect,254))

    def test_255(self):
        input = """Function: test Parameter: x0 Body:Return;EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))

    def test_256(self):
        input = """Function: frac Body: n = n + func()*2;EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))

    def test_257(self):
        input = """Function:testfor Body:For(i=0,i!=1,1) DoEndFor.EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))

    def test_258(self):
        input = """Function: o_____o Body: Break;EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))

    def test_259(self):
        input = """Function:a4_5 Body:DoWhilex==1EndDo.EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,259))

    def test_260(self):
        input = """Function: test_exp Body: x = 0;Return foo(2+x,4.2\\.y)+goo();EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))

    def test_261(self):
        input = """Function:Body:EndBody."""
        expect = "Error on line 1 col 9: Body"
        self.assertTrue(TestParser.checkParser(input,expect,261))

    def test_262(self):
        input = """Function:func Body:Var: x = 0X55E;Return 0o12;EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test_263(self):
        input = """Function: foo Body:x = -0.12;y = 1.5e-1;EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test_264(self):
        input = """Function: val Body: n = 8; Var: n;EndBody."""
        expect = "Error on line 1 col 27: Var"
        self.assertTrue(TestParser.checkParser(input,expect,264))

    def test_265(self):
        input = """Function:n Body: Var: x,y = 6,z;\nstr = "tu'"asdas";EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))

    def test_266(self):
        input = """Function: main Body: While True print("Hello World"); EndWhile.EndBody."""
        expect = "Error on line 1 col 32: print"
        self.assertTrue(TestParser.checkParser(input,expect,266))

    def test_267(self):
        input = """Function: main Body: Var: x,\ny=5,z;Return True;EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))

    def test_268(self):
        input = """Function: main Body:**This is a cmt**Var: x=0;Var: y = 5; If x <= 5 Then Return x;EndIf.EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))

    def test_269(self):
        input = """Function: foo Parameter: x = 0 Body:EndBody."""
        expect = "Error on line 1 col 27: ="
        self.assertTrue(TestParser.checkParser(input,expect,269))

    def test_270(self):
        input = """Var: v = 0.;Function: sub Body:EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))

    def test_271(self):
        input = """If x == 7 Then Return 0;"""
        expect = "Error on line 1 col 0: If"
        self.assertTrue(TestParser.checkParser(input,expect,271))

    def test_272(self):
        input = """Var: n = 9\\2;"""
        expect = "Error on line 1 col 10: \\"
        self.assertTrue(TestParser.checkParser(input,expect,272))

    def test_273(self):
        input = """Function: main Parameter: x"""
        expect = "Error on line 1 col 27: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,273))

    def test_274(self):
        input = """Var: x = {1,2,3,4};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))

    def test_275(self):
        input = """Var: x = 7.e-6; Function: super Body: x = x + 1; EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))

    def test_276(self):
        input = """Function: main Body:While x == 5 Do Var: y = 6; x = x + y; EndWhile.EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))

    def test_277(self):
        input = """Var: n = 6; Var: x = 7;Function: main Body:foo();EndBody.Function: foo Body:Var: x = 6;Return x+1;EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))

    def test_278(self):
        input = """Var: x = 7;Function: nnn BodyEndBody."""
        expect = "Error on line 1 col 29: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,278))

    def test_279(self):
        input = """Function: main Parameter:n Body:Return n*n;EndBody.Var: m = 0;"""
        expect = "Error on line 1 col 51: Var"
        self.assertTrue(TestParser.checkParser(input,expect,279))

    def test_280(self):
        input = """Function: main Var: x = 7;"""
        expect = "Error on line 1 col 15: Var"
        self.assertTrue(TestParser.checkParser(input,expect,280))

    def test_281(self):
        input = r"""
Function: main
Body:
    If x > 5 Then
        If x < 7 Then
            Return 6;
        Else
            Return 7;
        EndIf.
    ElseIf x > 0 Then
        Return 1;
    EndIf.
EndBody.   
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))

    def test_282(self):
        input = r"""
Var: x = func();
"""
        expect = "Error on line 2 col 9: func"
        self.assertTrue(TestParser.checkParser(input,expect,282))

    def test_283(self):
        input = r"""
Var: x = "BKIT\n\t";
Function: main
Parameter: n
Body:
    While Do
    EndWhile.
EndBody."""
        expect = "Error on line 6 col 10: Do"
        self.assertTrue(TestParser.checkParser(input,expect,283))

    def test_284(self):
        input = r"""Function: main
Body:
    Do
        t = t + 1;
    While t < 10 EndDo.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))

    def test_285(self):
        input = """Var: i = {{1,2},{9,8},"BKIT"};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))

    def test_286(self):
        input = r"""Function: main test
Body:
    print("hello world\n");
    Return 0;
EndBody."""
        expect = "Error on line 1 col 15: test"
        self.assertTrue(TestParser.checkParser(input,expect,286))

    def test_287(self):
        input = r"""Function: main
Body:**
This is a comment

**
    If x%5 =/= 3 Then
        Var: str = "Successful"
        print(str);
        Return True;
    Else
        Return False;
    EndIf.
EndBody."""
        expect = "Error on line 8 col 8: print"
        self.assertTrue(TestParser.checkParser(input,expect,287))

    def test_288(self):
        input = r"""Var: x = {4};
Function: main
x = x + 1;
Body:
EndBody."""
        expect = "Error on line 3 col 0: x"
        self.assertTrue(TestParser.checkParser(input,expect,288))

    def test_289(self):
        input = r"""Function: n = 0
Body:
    Return False;
EndBody."""
        expect = "Error on line 1 col 12: ="
        self.assertTrue(TestParser.checkParser(input,expect,289))

    def test_290(self):
        input = r"""Function: main
Body:
    r = "Hello\tWorld";
    If len(r) == 7 Then
        Return True;
        Break;
    Else
        Return False;
        Continue;
    EndIf.
EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,290))

    def test_291(self):
        input = """ """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,291))

    def test_292(self):
        input = r"""Function: main
Body:
    x = {1,2,3} +. 5;
    Return True;
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,292))

    def test_293(self):
        input = r"""Function: foo
Parameter: t
Body:
    t = "str" + "HelloWorld";
    Return a[foo(p)+4.5e-1];
    Break;
    **cmt**
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,293))

    def test_294(self):
        input = r"""
**

This
is
a
cmt
        **

Function: max
Parameter: a,**** b
Body:
    If a >=. b Then
        Return a;
    Else
        Return b;
    EndIf.
EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,294))

    def test_295(self):
        input = r"""
Function: r
Body:
    While x > 1 Do
        While x < 10 Do
            Break;
        EndWhile.
    EndWhile.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,295))

    def test_296(self):
        input = r"""Function: main"""
        expect = "Error on line 1 col 14: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,296))

    def test_297(self):
        input = r"""Var: """
        expect = "Error on line 1 col 5: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,297))

    def test_298(self):
        input = r"""Function: main
        
        
        Body:
If 
x == 8
Then ****
Continue;
EndIf.
EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,298))

    def test_299(self):
        input = r"""
Function: true
Body:
    If True Then
        Return True;
    Else
        Return False;
EndBody."""
        expect = "Error on line 8 col 0: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,299))

    def test_300(self):
        input = r"""Function:m Body:EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,300))

    
    
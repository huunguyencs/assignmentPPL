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
        input = """Var: x[b[foo(2)][5]] = {1,2};"""
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
        input = """ """
        expect = "Error on line 1 col 1: <EOF>"
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
        expect = "Error on line 1 col 14: <EOF>"
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
        input = """Var: x = 5 == 6;"""
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
        input = """Var: x[a+foo(12,45)][0];"""
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
Var: x = (True || False);"""
        expect = "successful"
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
        input = """Var: x = fibonaci(5);Function:fibonaci Parameter:x Body:Returnfibonaci(x-1)+fibonaci(x-2);EndBody."""
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
        input = """Var: n = -7.e1;Function: radius Parameter:r Body: If r > 0 Then Return pi*r;EndIf.EndBody."""
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
        input = """Var: n[fooo(0,5)][{0,2,3}];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))

    def test_251(self):
        input = """Var: n = 0;Function:y Body:**This is a cmt**c=1;Return False + True;EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))

    def test_252(self):
        input = """Var: n = {{{1,2,3},{5},{"string",5.e-5}}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))

    

    

    

    
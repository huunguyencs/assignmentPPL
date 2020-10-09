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
        input = """Var: x[2] = {1,2};"""
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
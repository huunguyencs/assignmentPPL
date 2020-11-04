import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_program(self):
        """Simple program: int main() {} """
        input = r"""Function: foo
    Parameter: a[5], b
    Body:
        Var: i = 0;
        While i < 5 Do
            a[i] = b +. 1.0;
            i = i + 1;
        EndWhile.
    EndBody."""
        expect = """Program([FuncDecl(Id(foo)[VarDecl(Id(a),[5]),VarDecl(Id(b))],([VarDecl(Id(i),IntLiteral(0))][While(BinaryOp(<,Id(i),IntLiteral(5)),[],[Assign(ArrayCell(a,[Id(i)]),BinaryOp(+.,Id(b),FloatLiteral(1.0))),Assign(Id(i),BinaryOp(+,Id(i),IntLiteral(1)))])])])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_program_1(self):
        """Simple program: int main() {} """
        input = """Function: test_for Body: For (i = 0,i<10,2) Do write(i);Continue;EndFor.EndBody."""
        expect = """Program([FuncDecl(Id(test_for)[],([][For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),IntLiteral(10)),IntLiteral(2),[],[CallStmt(Id(write),[Id(i)]),Continue()])])])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_program_2(self):
        """Simple program: int main() {} """
        input = """Var: n = 0;Function:y Body:**This is a cmt**c=1;Return False + True;EndBody."""
        expect = """Program([VarDecl(Id(n),IntLiteral(0)),FuncDecl(Id(y)[],([][Assign(Id(c),IntLiteral(1)),Return(BinaryOp(+,BooleanLiteral(false),BooleanLiteral(true)))])])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_program_3(self):
        """Simple program: int main() {} """
        input = """Function: area Parameter: n,m Body: If (n > 0) && (m > 0) Then Return n*m;EndIf.EndBody."""
        expect = """Program([FuncDecl(Id(area)[VarDecl(Id(n)),VarDecl(Id(m))],([][If(BinaryOp(&&,BinaryOp(>,Id(n),IntLiteral(0)),BinaryOp(>,Id(m),IntLiteral(0))),[],[Return(BinaryOp(*,Id(n),Id(m)))])])])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    
    def test_program_4(self):
        """Simple program: int main() {} """
        input = """Var: t = {{"hello","myfen"},{1e-5,45}};"""
        expect = """Program([VarDecl(Id(t),ArrayLiteral(ArrayLiteral(StringLiteral(hello),StringLiteral(myfen)),ArrayLiteral(FloatLiteral(1e-05),IntLiteral(45))))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
    
    def test_program_5(self):
        """Simple program: int main() {} """
        input = """Function:ham Parameter:x,y,z Body:x=x+1;t[foo(a)+1][5]=10;Return0;EndBody."""
        expect = """Program([FuncDecl(Id(ham)[VarDecl(Id(x)),VarDecl(Id(y)),VarDecl(Id(z))],([][Assign(Id(x),BinaryOp(+,Id(x),IntLiteral(1))),Assign(ArrayCell(t,[BinaryOp(+,CallStmt(Id(foo),[Id(a)]),IntLiteral(1)),IntLiteral(5)]),IntLiteral(10)),Return(IntLiteral(0))])])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_program_6(self):
        """Simple program: int main() {} """
        input = """"""
        expect = """Program([])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    # def test_program_7(self):
    #     """Simple program: int main() {} """
    #     input = """Var: t = {{"hello","myfen"},{1e-5,45}};"""
    #     expect = """Program([VarDecl(Id(t),ArrayLiteral(ArrayLiteral(StringLiteral(hello),StringLiteral(myfen)),ArrayLiteral(FloatLiteral(1e-05),IntLiteral(45))))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,307))

    # def test_program_8(self):
    #     """Simple program: int main() {} """
    #     input = """Var: t = {{"hello","myfen"},{1e-5,45}};"""
    #     expect = """Program([VarDecl(Id(t),ArrayLiteral(ArrayLiteral(StringLiteral(hello),StringLiteral(myfen)),ArrayLiteral(FloatLiteral(1e-05),IntLiteral(45))))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,308))

    # def test_program_9(self):
    #     """Simple program: int main() {} """
    #     input = """Var: t = {{"hello","myfen"},{1e-5,45}};"""
    #     expect = """Program([VarDecl(Id(t),ArrayLiteral(ArrayLiteral(StringLiteral(hello),StringLiteral(myfen)),ArrayLiteral(FloatLiteral(1e-05),IntLiteral(45))))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,309))

    # def test_program_10(self):
    #     """Simple program: int main() {} """
    #     input = """Var: t = {{"hello","myfen"},{1e-5,45}};"""
    #     expect = """Program([VarDecl(Id(t),ArrayLiteral(ArrayLiteral(StringLiteral(hello),StringLiteral(myfen)),ArrayLiteral(FloatLiteral(1e-05),IntLiteral(45))))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,310))

    

 
   
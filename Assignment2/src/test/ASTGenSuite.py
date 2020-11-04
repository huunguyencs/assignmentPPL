import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_vardecl_1(self):
        input = """Var: x;"""
        expect = """Program([VarDecl(Id(x))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_vardecl_2(self):
        input = """Var: x,y;"""
        expect = """Program([VarDecl(Id(x)),VarDecl(Id(y))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_vardecl_3(self):
        input = """Var: x = 10;"""
        expect = """Program([VarDecl(Id(x),IntLiteral(10))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_vardecl_4(self):
        input = """Var: x = 10, y = True;"""
        expect = """Program([VarDecl(Id(x),IntLiteral(10)),VarDecl(Id(y),BooleanLiteral(true))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_vardecl_5(self):
        input = """Var: n[10];"""
        expect = """Program([VarDecl(Id(n),[10])])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_vardecl_6(self):
        input = """Var: n[10], y = "string";"""
        expect = """Program([VarDecl(Id(n),[10]),VarDecl(Id(y),StringLiteral(string))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_vardecl_7(self):
        input = """Var: n[10] = {1,2,3,4}, n = 10;"""
        expect = """Program([VarDecl(Id(n),[10],ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4))),VarDecl(Id(n),IntLiteral(10))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_vardecl_8(self):
        input = r"""Var: n = True;
Var: t,x,z;"""
        expect = """Program([VarDecl(Id(n),BooleanLiteral(true)),VarDecl(Id(t)),VarDecl(Id(x)),VarDecl(Id(z))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_vardecl_9(self):
        input = """Var: n[10][1] = {{1,2,3},{"string",True}};"""
        expect = """Program([VarDecl(Id(n),[10,1],ArrayLiteral(ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3)),ArrayLiteral(StringLiteral(string),BooleanLiteral(true))))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_vardecl_10(self):
        input = r"""Var: n[10];
Var: t = "String";
Var: m = 10;"""
        expect = """Program([VarDecl(Id(n),[10]),VarDecl(Id(t),StringLiteral(String)),VarDecl(Id(m),IntLiteral(10))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_vardecl_11(self):
        input = """Var: n = 7, t = {1,2,3};"""
        expect = """Program([VarDecl(Id(n),IntLiteral(7)),VarDecl(Id(t),ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3)))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_vardecl_12(self):
        input = """Var: t[1];
Var: m,y = 7,z;"""
        expect = """Program([VarDecl(Id(t),[1]),VarDecl(Id(m)),VarDecl(Id(y),IntLiteral(7)),VarDecl(Id(z))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    # def test_vardecl_13(self):
    #     input = """Var: n[10];"""
    #     expect = """"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,313))

    # def test_vardecl_14(self):
    #     input = """Var: n[10];"""
    #     expect = """"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,314))

    # def test_vardecl_15(self):
    #     input = """Var: n[10];"""
    #     expect = """"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,315))

    
    def test_funcdecl_1(self):
        input = r"""Function: foo
Body:
EndBody."""
        expect = """Program([FuncDecl(Id(foo)[],([][]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_funcdecl_2(self):
        input = r"""Function: hello
Body:
    Var: n = 7;
    n = n + 1;
EndBody."""
        expect = """Program([FuncDecl(Id(hello)[],([VarDecl(Id(n),IntLiteral(7))][Assign(Id(n),BinaryOp(+,Id(n),IntLiteral(1)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_funcdecl_3(self):
        input = r"""Function: foo
Parameter: x
Body:
    t = 0;
EndBody."""
        expect = """Program([FuncDecl(Id(foo)[VarDecl(Id(x))],([][Assign(Id(t),IntLiteral(0))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    # def test_funcdecl_4(self):
    #     input = r""" """
    #     expect = """"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,319))

    # def test_funcdecl_5(self):
    #     input = r""" """
    #     expect = """"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,320))

    
    
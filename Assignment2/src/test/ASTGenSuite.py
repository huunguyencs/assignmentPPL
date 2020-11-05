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
        input = """Var: n[2][1] = {{True},{"string"}};"""
        expect = """Program([VarDecl(Id(n),[2,1],ArrayLiteral(ArrayLiteral(BooleanLiteral(true)),ArrayLiteral(StringLiteral(string))))])"""
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

    def test_vardecl_13(self):
        input = """Var: n = 0x45;"""
        expect = """Program([VarDecl(Id(n),IntLiteral(69))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_vardecl_14(self):
        input = """Var: t = 0o12, n = 0O11;"""
        expect = """Program([VarDecl(Id(t),IntLiteral(10)),VarDecl(Id(n),IntLiteral(9))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_vardecl_15(self):
        input = r"""Var: n[3] = {0x14,0O78,5.e-1};
Var: t = 0X7F;"""
        expect = """Program([VarDecl(Id(n),[3],ArrayLiteral(IntLiteral(20),IntLiteral(7),FloatLiteral(0.5))),VarDecl(Id(t),IntLiteral(127))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    
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

    def test_funcdecl_4(self):
        input = r"""Function: ppl
Parameter: t[10], x
Body:
EndBody."""
        expect = """Program([FuncDecl(Id(ppl)[VarDecl(Id(t),[10]),VarDecl(Id(x))],([][]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_funcdecl_5(self):
        input = r"""Function: test
Body:
    t = 4*5;
EndBody."""
        expect = """Program([FuncDecl(Id(test)[],([][Assign(Id(t),BinaryOp(*,IntLiteral(4),IntLiteral(5)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_assign_stmt_1(self):
        input = r"""Function: foo
Body:
    t = 1 + {1,2,3};
    e = 7;
EndBody."""
        expect = """Program([FuncDecl(Id(foo)[],([][Assign(Id(t),BinaryOp(+,IntLiteral(1),ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3)))),Assign(Id(e),IntLiteral(7))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_assign_stmt_2(self):
        input = r"""Function: test
Parameter: x
Body:
    Var: x = 7;
    x =  x + 1;
EndBody."""
        expect = """Program([FuncDecl(Id(test)[VarDecl(Id(x))],([VarDecl(Id(x),IntLiteral(7))][Assign(Id(x),BinaryOp(+,Id(x),IntLiteral(1)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_assign_stmt_3(self):
        input = r"""Function: test
Body:
    m = 12 + call(x,y);
EndBody."""
        expect = """Program([FuncDecl(Id(test)[],([][Assign(Id(m),BinaryOp(+,IntLiteral(12),CallStmt(Id(call),[Id(x),Id(y)])))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_assign_stmt_4(self):
        input = r"""Function: a
Body:
    t = 7.8 + 0X7 - 3.e-4;
    m = 0;
    t = "String" + "string";
EndBody."""
        expect = """Program([FuncDecl(Id(a)[],([][Assign(Id(t),BinaryOp(-,BinaryOp(+,FloatLiteral(7.8),IntLiteral(7)),FloatLiteral(0.0003))),Assign(Id(m),IntLiteral(0)),Assign(Id(t),BinaryOp(+,StringLiteral(String),StringLiteral(string)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_if_stmt_1(self):
        input = r"""Function: test_if
Parameter: a
Body:
    If a > 0 Then
        a = a + 1;
    EndIf.
EndBody."""
        expect = """Program([FuncDecl(Id(test_if)[VarDecl(Id(a))],([][If(BinaryOp(>,Id(a),IntLiteral(0)),[],[Assign(Id(a),BinaryOp(+,Id(a),IntLiteral(1)))])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_if_stmt_2(self):
        input = r"""Function: test_if
Body:
    If a > 0 Then
        Return a;
    Else
        Return 0;
    EndIf.
EndBody."""
        expect = """Program([FuncDecl(Id(test_if)[],([][If(BinaryOp(>,Id(a),IntLiteral(0)),[],[Return(Id(a))])Else([],[Return(IntLiteral(0))])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_if_stmt_3(self):
        input = r"""Function: foo
Parameter: a,b
Body:
    If a > 0 Then
        Return 1;
    ElseIf b >= 0 Then
        Return 0
    Else
        Return -1;
    EndIf.
EndBody."""
        expect = """Program([FuncDecl(Id(foo)[VarDecl(Id(a)),VarDecl(Id(b))],([][If(BinaryOp(>,Id(a),IntLiteral(0)),[],[Return(IntLiteral(1))])ElseIf(BinaryOp(>=,Id(b),IntLiteral(0)),[],[Return(IntLiteral(0))])Else([],[Return(UnaryOp(-,IntLiteral(1)))])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_if_stmt_4(self):
        input = r"""Function: f
Body:
    If (a>0) && (b>0) Then
        Return a;
    ElseIf b > 0 Then
        Return b;
    Else
        Return -1;
    EndIf.
EndBody."""
        expect = """Program([FuncDecl(Id(f)[],([][If(BinaryOp(&&,BinaryOp(>,Id(a),IntLiteral(0)),BinaryOp(>,Id(b),IntLiteral(0))),[],[Return(Id(a))])ElseIf(BinaryOp(>,Id(b),IntLiteral(0)),[],[Return(Id(b))])Else([],[Return(UnaryOp(-,IntLiteral(1)))])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_if_stmt_5(self):
        input = r"""Function: t
Parameter: a,b
Body:
    If (a == 0) || (b < 0) Then
        b = b + 1;
        Return True;
    ElseIf b > 0 Then
        b = call();
        Return False;
    Else
        t = t + 1;
        Return False;
    EndIf.
EndBody."""
        expect = """Program([FuncDecl(Id(t)[VarDecl(Id(a)),VarDecl(Id(b))],([][If(BinaryOp(||,BinaryOp(==,Id(a),IntLiteral(0)),BinaryOp(<,Id(b),IntLiteral(0))),[],[Assign(Id(b),BinaryOp(+,Id(b),IntLiteral(1))),Return(BooleanLiteral(true))])ElseIf(BinaryOp(>,Id(b),IntLiteral(0)),[],[Assign(Id(b),CallStmt(Id(call),[])),Return(BooleanLiteral(false))])Else([],[Assign(Id(t),BinaryOp(+,Id(t),IntLiteral(1))),Return(BooleanLiteral(false))])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_if_stmt_6(self):
        input = r"""Function: y
Body:
    If i == 0 Then
        i = i + 1;
        Break;
        Return 1;
    ElseIf (i > 0) && (y == 6) Then
        y = y + 7;
    ElseIf y > 7 Then
    Else
        Return False;
    EndIf.
EndBody."""
        expect = """Program([FuncDecl(Id(y)[],([][If(BinaryOp(==,Id(i),IntLiteral(0)),[],[Assign(Id(i),BinaryOp(+,Id(i),IntLiteral(1))),Break(),Return(IntLiteral(1))])ElseIf(BinaryOp(&&,BinaryOp(>,Id(i),IntLiteral(0)),BinaryOp(==,Id(y),IntLiteral(6))),[],[Assign(Id(y),BinaryOp(+,Id(y),IntLiteral(7)))])ElseIf(BinaryOp(>,Id(y),IntLiteral(7)),[],[])Else([],[Return(BooleanLiteral(false))])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    # def test_for_stmt_1(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,331))
    
    # def test_for_stmt_2(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,332))
    
    # def test_for_stmt_3(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,333))
    
    # def test_for_stmt_4(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,334))
    
    # def test_for_stmt_5(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,335))
    
    # def test_for_stmt_6(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,336))
    
    # def test_while_stmt_1(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,337))
    
    # def test_while_stmt_2(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,338))
    
    # def test_while_stmt_3(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,339))
    
    # def test_while_stmt_4(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,340))
    
    # def test_while_stmt_5(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,341))
    
    # def test_while_stmt_6(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,342))
    
    # def test_do_stmt_1(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,343))
    
    # def test_do_stmt_2(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,344))
    
    # def test_do_stmt_3(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,345))
    
    # def test_do_stmt_4(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,346))
    
    # def test_do_stmt_5(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,347))
    
    # def test_do_stmt_6(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,348))
    
    # def test_break_stmt_1(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,349))
    
    # def test_break_stmt_2(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,350))
    
    # def test_break_stmt_3(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,351))
    
    # def test_continue_stmt_1(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,352))
    
    # def test_continue_stmt_2(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,353))
    
    # def test_continue_stmt_3(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,354))
    
    # def test_call_stmt_1(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,355))
    
    # def test_call_stmt_2(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,355))
    
    # def test_call_stmt_3(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,356))
    
    # def test_call_stmt_4(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,357))
    
    # def test_call_stmt_5(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,358))
    
    # def test_return_stmt_1(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,359))
    
    # def test_return_stmt_2(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,360))
    
    # def test_return_stmt_3(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,361))
    
    # def test_exp_stmt_1(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,362))
    
    # def test_exp_stmt_2(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,363))
    
    # def test_exp_stmt_3(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,364))
    
    # def test_exp_stmt_4(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,365))
    
    # def test_exp_stmt_5(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,366))
    
    # def test_exp_stmt_6(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,367))
    
    # def test_exp_stmt_7(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,368))
    
    # def test_exp_stmt_8(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,369))
    
    # def test_exp_stmt_9(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,370))
    
    # def test_exp_stmt_10(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,371))
    
    # def test_exp_stmt_11(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,372))
    
    # def test_exp_stmt_12(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,373))
    
    # def test_exp_stmt_13(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,374))
    
    # def test_exp_stmt_14(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,375))
    
    # def test_exp_stmt_15(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,376))
    
    # def test_exp_stmt_16(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,377))
    
    # def test_exp_stmt_17(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,378))
    
    # def test_exp_stmt_18(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,379))
    
    # def test_exp_stmt_19(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,380))
    
    # def test_exp_stmt_20(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,381))
    
    # def test_free_1(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,382))

    # def test_free_2(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,383))

    # def test_free_3(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,384))

    # def test_free_4(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,385))

    # def test_free_5(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,386))

    # def test_free_6(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,387))

    # def test_free_7(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,388))

    # def test_free_8(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,389))

    # def test_free_9(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,390))

    # def test_free_10(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,391))

    # def test_free_11(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,392))

    # def test_free_12(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,393))

    # def test_free_13(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,394))

    # def test_free_14(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,395))

    # def test_free_15(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,396))

    # def test_free_16(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,397))

    # def test_free_17(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,398))

    # def test_free_18(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,399))

    # def test_free_19(self):
    #     input = r""" """
    #     expect = """ """
    #     self.assertTrue(TestAST.checkASTGen(input,expect,400))

    
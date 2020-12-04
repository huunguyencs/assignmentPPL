import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):

    # def test_undeclared_function(self):
    #     """Simple program: main"""
    #     input = """
    #             Var: x;
    #             Function: main
    #                Body: 
    #                     foo();
    #                EndBody."""
    #     expect = str(Undeclared(Function(),"foo"))
    #     self.assertTrue(TestChecker.test(input,expect,400))


    # def test_diff_numofparam_stmt_use_ast(self):
    #     """Complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],([],[
    #                 CallStmt(Id("printStrLn"),[])]))])
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
    #     self.assertTrue(TestChecker.test(input,expect,405))

    def test_400(self):
        input = r"""Var: x, y;
Function: main
Body:
    x = z*y + 1;
    Return 0;
EndBody."""
        expect = str(Undeclared(Identifier(),"z"))
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_401(self):
        input = r"""Function: main
Body:
    Var: m = 5, z;
    m = z +. m;
    Return;
EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("+.",Id("z"),Id("m"))))
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_402(self):
        input = r"""Function: main
Parameter: m
Body:
    m = m + 1;
    main("str");
    Return;
EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[StringLiteral("str")])))
        self.assertTrue(TestChecker.test(input,expect,402))
    
    def test_403(self):
        input = r"""Var: main;
Function: foo
Body:
    Return;
EndBody.
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_404(self):
        input = r"""Function: main
Parameter: m, x
Body:
    m = 5;
    m = m * (x \. 2.2);
    Return;
EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("*",Id("m"),BinaryOp("\.",Id("x"),FloatLiteral(2.2)))))
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_405(self):
        input = r"""Var: x, x;
        """
        expect = str(Redeclared(Variable(),"x"))
        self.assertTrue(TestChecker.test(input,expect,405))
    
    def test_406(self):
        input = r"""Function: main
Body:
    Var: m, arr[5];
    arr = {1,2,5,4,7};
    m = m + 1;
    m = m + 1.2;
    Return;
EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("+",Id("m"),FloatLiteral(1.2))))
        self.assertTrue(TestChecker.test(input,expect,406))
    def test_407(self):
        input = r"""
Function: main
Body:
    Var: x;
    If x Then
        Return 1;
    Else
        Return x;
    EndIf.
EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(Id("x"))))
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_408(self):
        input = r"""
Function: foo
Body:
    Var: x[3] = {1,2,3};
    Return x[1][3];
EndBody.
Function: main
Parameter: m
Body:
    Var: x;
    Return 0;
EndBody.
        """
        expect = str(TypeMismatchInExpression(ArrayCell(Id("x"),[IntLiteral(1),IntLiteral(3)])))
        self.assertTrue(TestChecker.test(input,expect,408))
    
    def test_409(self):
        input = r"""Function: main
Parameter: x
Body:
    Var: m;
    Return m;
EndBody.
        """
        expect = str(TypeCannotBeInferred(Return(Id("m"))))
        self.assertTrue(TestChecker.test(input,expect,409))
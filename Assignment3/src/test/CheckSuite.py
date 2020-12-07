import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):


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
        input = r"""Function: foo
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

    def test_410(self):
        input = r"""Var: a,b;
Function: foo
Body:
    main(5);
EndBody.
Function: main
Parameter: x
Body:
    If x Then
    EndIf.
    Return;
EndBody.
        """
        expect = str(TypeMismatchInStatement(If([(Id("x"),[],[])],([],[]))))
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_411(self):
        input = r"""Var: m;
Function: main
Body:
    For(m = 1,main(),1) Do
    EndFor.
    Return;
EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(None)))
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_412(self):
        input = r"""Function: main
Parameter: i
Body:
    While i Do
        i = i + 1;
    EndWhile.
    Return 0;
EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("+",Id("i"),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_413(self):
        input = r"""Function: main
Body:
    Var: m;
    float_of_int(string_of_int(m));
    Return 0;
EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id("float_of_int"),[CallExpr(Id("string_of_int"),[Id("m")])])))
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_414(self):
        input = r"""Function: main
Parameter: x[5], y
Body:
    x[6][7] = 7;
    Return;
EndBody.
        """
        expect = str(TypeMismatchInExpression(ArrayCell(Id("x"),[IntLiteral(6),IntLiteral(7)])))
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_415(self):
        input = r"""Function: foo
Body:
    Return;
EndBody.
Function: main
Body:
    Var: x;
    x = foo();
    Return 0;
EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),CallExpr(Id("foo"),[]))))
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_416(self):
        input = r"""Var: y[3] = {1};
Function: main
Parameter: x[5]
Body:
    main({1}); **Cmt**
    Return 5;
EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(IntLiteral(5))))
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_417(self):
        input = r"""Var: x = 5;
Function: main
Body:
    Var: x = True;
    If x Then
        x = main();
    EndIf.
    Return 1;
EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_418(self):
        input = r"""Var: x[7];
Function: foo
Body:
    Return {1,2,3,4};
EndBody.
Function: main
Body:
    Var: m;
    m = foo()[2];
    x[1] = m + 7;
    While x[5] Do
    EndWhile.
    Return;
EndBody.
        """
        expect = str(TypeMismatchInStatement(While(ArrayCell(Id("x"),[IntLiteral(5)]),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_419(self):
        input = r"""Function: main
Body:
    Var: main;
    main();
EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[])))
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_420(self):
        input = r"""Function: main
Parameter: main
Body:
    foo(5);
EndBody.
Function: foo
Parameter: x
Body:
    Var: m = 7;
    Return 5;
EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(IntLiteral(5))))
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_421(self):
        input = r"""Var: println;
Function: printStr
Body:
    Var: m;
    Return 0;
EndBody.
Function: main
Body:
    Return 0;
EndBody.
        """
        expect = str(Redeclared(Function(),"printStr"))
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_422(self):
        input = r"""Var: x;
Function: main
Parameter: a, a
Body:
    Return 2;
EndBody.
        """
        expect = str(Redeclared(Parameter(),"a"))
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_423(self):
        input = r"""Function: main
Body:
    Var: x;
    Do
        printLn(x);
    While x EndDo.
EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id("printLn"),[Id("x")])))
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_424(self):
        input = r"""Var: main;
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_425(self):
        input = r"""Var: x[2][2][2] = {{{1,2},{3,4}},{{5,6},{7,8}}};
Function: main
Body:
    Var: m;
    m = x[1][1][1];
    m = 5.1 +. m;
    Return 0;
EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("+.",FloatLiteral(5.1),Id("m"))))
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_426(self):
        input = r"""Var: x;
        Var: x;
        """
        expect = str(Redeclared(Variable(),"x"))
        self.assertTrue(TestChecker.test(input,expect,426))
    def test_427(self):
        input = r"""Var: func;
Function: func
Body:
    Return;
EndBody.
Function: main
Body:
    Return;
EndBody.
        """
        expect = str(Redeclared(Function(),"func"))
        self.assertTrue(TestChecker.test(input,expect,427))
    def test_428(self):
        input = r"""Var: x[2];
Function: main
Body:
    If x[1] Then
        **Var: x = 1;
        x = 5 + x;**
    EndIf.
    x[0] = 1;
    Return;
EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id("x"),[IntLiteral(0)]),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,428))
    def test_429(self):
        input = r"""Function: main
Body:
    Var: m = 7;
    Var: is = False;
    Do
        m = m + 1;
    While is EndDo.
    Return True;
EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,429))
    def test_430(self):
        input = r"""Var: x;
Function: main
Body:
    Var: m;
    m = float_of_int(int_of_float(m));
    m = 7;
    Return 0;
EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id("m"),IntLiteral(7))))
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_431(self):
        input = r"""Var: test;
Function: main
Parameter: x
Body:
    x = test[0];
EndBody.
        """
        expect = str(TypeMismatchInExpression(ArrayCell(Id("test"),[IntLiteral(0)])))
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_432(self):
        input = r"""Var: x;
Function: main
Parameter: par
Body:
    Var: x = 2;
    main(t);
    Return;
EndBody.
        """
        expect = str(Undeclared(Identifier(),"t"))
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_433(self):
        input = r"""Var: x;
Function: main
Parameter: y,z
Body:
    If True Then
        z = 0.0;
    EndIf.
    main(3,x);
    main(x,0.0);
    Return;
EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[Id("x"),FloatLiteral(0.0)])))
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_434(self):
        input = r"""Function: main
Parameter: a,b,c
Body:
    Var: d, e;
    e = main(main(d, c, a), b , a + d);
    Return 3;
EndBody.
        """
        expect = str(TypeCannotBeInferred(CallExpr(Id("main"),[Id("d"),Id("c"),Id("a")])))
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_435(self):
        input = r"""Function: main
Parameter: x, y ,z
Body:
    y = x || (x>z);
    Return;
EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp("||",Id("x"),BinaryOp(">",Id("x"),Id("z")))))
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_436(self):
        input = r"""Var: m;
Function: main
Parameter: m
Body:
    For(x = 1,True,1) Do
        main(1);
    EndFor.
    Return;
EndBody.
        """
        expect = str(Undeclared(Identifier(),"x"))
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_437(self):
        input = r"""Function: main
Body:
    foo(1,2);
    Return;
EndBody.
Function: foo
Parameter: n
Body:
    Return;
EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[IntLiteral(1),IntLiteral(2)])))
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_438(self):
        input = r"""Var: a;
Function: main
Body:
    a = foo();
EndBody.
Function: foo
Body:
    Return 5;
EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id("a"),CallExpr(Id("foo"),[]))))
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_439(self):
        input = r"""Var: a;
Function: main
Body:
    a = 1;
    a = foo();
EndBody.
Function: foo
Body:
    Return 1.1;
EndBody."""
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_440(self):
        input = r"""Function: main
Parameter: x[5]
Body:
    Var: m[5];
    x = m;
    Return;
EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id("x"),Id("m"))))
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_441(self):
        input = r"""Function: main
Parameter: x[5]
Body:
    Var: m[5];
    If m[1] Then
    EndIf.
    x = m;
    x[3] = 5;
    Return;
EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id("x"),[IntLiteral(3)]),IntLiteral(5))))
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_442(self):
        input = r"""Var: x[2][3];
Function: main
Body:
    While x[1][0] Do
        Var: x[2][2];
        x[1][1] = 5;
    EndWhile.
    x[0][0] = 7;
    Return x;
EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id("x"),[IntLiteral(0),IntLiteral(0)]),IntLiteral(7))))
        self.assertTrue(TestChecker.test(input,expect,442))
    
    def test_443(self):
        input = r"""Function: foo
Body:
    Var: x[2] = {1,2};
    Return x;
EndBody.
Function: main
Body:
    Var: m;
    m = foo();
    m[1] = 1;
    Return;
EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id("m"),CallExpr(Id("foo"),[]))))
        self.assertTrue(TestChecker.test(input,expect,443))
    
    def test_444(self):
        input = r"""Var: x[2] = {"my","string"};
Function: main
Body:
    Var: x;
    x = float_of_string(x[0]);
    x = 5 + 10;
    Return;
EndBody.
        """
        expect = str(TypeMismatchInExpression(ArrayCell(Id("x"),[IntLiteral(0)])))
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_445(self):
        input = r"""Function: print
Parameter: x
Body:
    Return;
EndBody.
Function: m
Body:
    Var: value = 12345;
    Return value;
EndBody.
Function: main
Parameter: x, y
Body:
    print(m);
    Return 0;
EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id("print"),[Id("m")])))
        self.assertTrue(TestChecker.test(input,expect,445))
    
    def test_446(self):
        input = r"""Function: main
Body:
    foo(1,2,3);
    Return 0;
EndBody.
Function: foo
Parameter: x, y
Body:
    Return;
EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])))
        self.assertTrue(TestChecker.test(input,expect,446))
    
    def test_447(self):
        input = r"""Var: cond = 1;
Function: main
Body:
    While cond Do
    EndWhile.
    Return 1;
EndBody.
        """
        expect = str(TypeMismatchInStatement(While(Id("cond"),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,447))
    
    def test_448(self):
        input = r"""Var: cond = False;
Function: main
Body:
    While cond Do
        Var: cond = 1;
        cond = 7 + 3;
        Return 1;
    EndWhile.
    Return 1.1;
EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input,expect,448))
    
    def test_449(self):
        input = r"""Function: foo
Parameter: n,m
Body:
    Var: a, b;
    b = 7;
    a = b + 9;
    foo(a,"string");
    Return;
EndBody.
Function: main
Body:
    Var: x = 7, y = 5.1;
    foo(x,y);
EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[Id("x"),Id("y")])))
        self.assertTrue(TestChecker.test(input,expect,449))
    
    

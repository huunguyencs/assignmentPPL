
"""
 * @author nhphung
"""
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import * 
from Visitor import *
from StaticError import *
from functools import *

class Type(ABC):
    __metaclass__ = ABCMeta
    pass
class Prim(Type):
    __metaclass__ = ABCMeta
    pass
class IntType(Prim):
    pass
class FloatType(Prim):
    pass
class StringType(Prim):
    pass
class BoolType(Prim):
    pass
class VoidType(Type):
    pass
class Unknown(Type):
    pass

@dataclass
class ArrayType(Type):
    dimen:List[int]
    eletype: Type

@dataclass
class MType:
    intype:List[Type]
    restype:Type

@dataclass
class Symbol:
    name: str
    mtype:Type

    @staticmethod
    def setPrimType(id, type, c, ast):
        """
        id: str
        type: Type
        """
        for var in c:
            if var.name == id:
                if type(var.mtype) != Unknown and type(var.mtype) != type(type):
                    raise TypeMismatchInExpression(ast)
                var.mtype = type

    @staticmethod
    def setArrayType(id,dimen,eType,c, ast):
        """
        id: str
        dimen: List[int]
        eType: Type
        """
        for var in c:
            if var.name ==id:
                if type(var.mtype) != Unknown and type(var.mtype) != type(type):
                    raise TypeMismatchInExpression(ast)
                var.mtype.dimen = dimen
                var.mtype.eletype = eType

    @staticmethod
    def setFuncType(id, param, returnType, c, ast):
        """
        id: str
        param: List[Type]
        returnType: Type    # None for VoidType()
        """
        for f in c:
            if f.name == id:
                if returnType is None:
                    returnType = Unknown()
                if (mtype.intype and mtype.intype != param) or (type(returnType) is not Unknown and type(mtype.restype) != type(returnType)):
                    if isinstance(ast,Expr):
                        raise TypeMismatchInExpression(ast)
                    else:
                        raise TypeMismatchInStatement(ast)
                f.mtype = MType(param,returnType)

    @staticmethod
    def setVarTypeWithOp(id, op, c):
        """
        """
        if op in ['-','+','*','\\','%','==','!=','<','>','<=','>=']:
            Symbol.setPrimType(id,IntType(),c)
        elif op in ['-.','+.','\\.','=/=','<.','>.','<=.','>=.']:
            Symbol.setPrimType(id,FloatType(),c)
        elif op in ['&&','||','!']:
            Symbol.setPrimType(id,BoolType(),c)

    @staticmethod
    def isExisten(listSymbols, symbol):
        return len([x for x in listSymbols if x.name == symbol.name]) > 0

    @staticmethod
    def mergeScope(currentScope,comingScope):
        return list(reduce(lambda lst, sym: lst if Symbol.isExisten(lst, sym) else lst+[sym], currentScope, comingScope))


class Checker:
    @staticmethod
    def checkRedeclared(currentScope, symbol, typeVar):
        """
        currentScope: List[Symbol]
        symbol: str
        """
        for sym in currentScope:
            if sym.name == symbol:
                raise Redeclared(typeVar,symbol)
            

    @staticmethod
    def checkEntryPoint(listDecl):
        """
        listDecl: List[decl]
        """
        for sym in listDecl:
            if sym.name.name == "main":
                return True
        raise NoEntryPoint()

    @staticmethod
    def checkUndeclared(currentScope,symbol):
        """
        currentScope: List[Symbol]
        symbol: str
        """
        for sym in currentScope:
            if sym.name == symbol:
                return True
        raise Undeclared(symbol)



class StaticChecker(BaseVisitor):
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [
Symbol("int_of_float",MType([FloatType()],IntType())),
Symbol("float_of_int",MType([IntType()],FloatType())),
Symbol("int_of_string",MType([StringType()],IntType())),
Symbol("string_of_int",MType([IntType()],StringType())),
Symbol("float_of_string",MType([StringType()],FloatType())),
Symbol("string_of_float",MType([FloatType()],StringType())),
Symbol("bool_of_string",MType([StringType()],BoolType())),
Symbol("string_of_bool",MType([BoolType()],StringType())),
Symbol("read",MType([],StringType())),
Symbol("printLn",MType([],VoidType())),
Symbol("printStr",MType([StringType()],VoidType())),
Symbol("printStrLn",MType([StringType()],VoidType()))]                           
   
    def check(self):
        return self.visit(self.ast,self.global_envi)

    def visitProgram(self,ast, c):
        """
        decl : List[Decl]
        """
        funcDecl = []
        for decl in ast.decl:
            if type(decl) is FuncDecl:
                funcDecl.append(decl)
                name = decl.name.name
                Checker.checkRedeclared(c,name,Function())
                c.append(Symbol(name,MType(None,Unknown())))
            else:
                self.visit(decl,(Variable(),c))
            
        Checker.checkEntryPoint(funcDecl)
        [self.visit(decl,c) for decl in funcDecl]
            


    def visitVarDecl(self, ast, c):
        """
        variable : Id
        varDimen : List[int] # empty list for scalar variable
        varInit  : Literal # null if no initial
        """
        typeVar, scope = c
        Checker.checkRedeclared(scope,ast.variable.name,typeVar)
        if ast.varDimen:
            if ast.varInit:
                type = self.visit(ast.varInit,c)
                if ast.varDimen != type.dimen:
                    raise Exception()
                scope.append(Symbol(ast.variable.name,ArrayType(ast.varDimen,type.eletype)))
            else:
                scope.append(Symbol(ast.variable.name,ArrayType(ast.varDimen,Unknown())))
        else:
            if ast.varInit:
                type = self.visit(ast.varInit,c)
                scope.append(Symbol(ast.variable.name,type))
            else:
                scope.append(Symbol(ast.variable.name,Unknown()))


    def visitFuncDecl(self, ast, c):
        """
        name: Id
        param: List[VarDecl]
        body: Tuple[List[VarDecl],List[Stmt]]
        """
        param = []
        [self.visit(para,(Parameter(),param)) for para in ast.param]
        localVar = param
        [self.visit(var,(Variable(),localVar)) for var in ast.body[0]]

        newScope = Symbol.mergeScope(c,localVar)

        returnType = None
        self.visitStmts(ast.body[1], (returnType, newScope))
                    
        Symbol.setFuncType(ast.name.name,param,returnType,newScope)        
        

    def visitArrayCell(self, ast, c):
        """
        arr:Expr
        idx:List[Expr]
        """
        pass

    def visitBinaryOp(self, ast, c):
        """
        op:str
        left:Expr
        right:Expr
        """
        varType, scope = c
        op = ast.op
        left = self.visit(ast.left,(None,scope))
        right = self.visit(ast.right,(None,scope))

        if type(left) is Unknown:
            Symbol.setVarTypeWithOp(ast.left.name,op,c)

        if type(right) is Unknown:
            Symbol.setVarTypeWithOp(ast.right.name,op,c)

        if op in ['-','+','*','\\','%']:
            if type(left) is IntType and type(right) is IntType:
                return IntType()
        elif op in ['-.','+.','\\.']:
            if type(left) is FloatType and type(right) is FloatType:
                return FloatType()
        elif op in ['==','!=','<','>','<=','>=']:
            if type(left) is IntType and type(right) is IntType:
                return BoolType()
        elif op in ['=/=','<.','>.','<=.','>=.']:
            if type(left) is FloatType and type(right) is FloatType:
                return BoolType()
        elif op in ['&&','||']:
            if type(left) is BoolType and type(right) is BoolType:
                return BoolType()
        raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self, ast, c):
        """
        op:str
        body:Expr
        """
        varType, scope = c
        op = ast.op
        typeExp = self.visit(ast.body,(None,scope))
        if type(typeExp) is Unknown:
            Symbol.setVarTypeWithOp(ast.body.name,op,c)

        if op == '-':
            if type(typeExp) is IntType:
                return IntType()
        elif op == '-.':
            if type(typeExp) is FloatType:
                return FloatType()
        elif op == '!':
            if type(typeExp) is BoolType:
                return BoolType()
        raise TypeMismatchInExpression(ast)

    def visitCallExpr(self, ast, c):
        """
        method:Id
        param:List[Expr]
        """
        varType, scope = c
        mtype = self.visit(ast.method,(Function(),scope))
        paraReal = mtype.intype
        para = [self.visit(p,(None,c)) for p in ast.param]

        if paraReal is None:
            Symbol.setFuncType(ast.method.name,para,mtype.restype,scope)
        else:
            if len(para) != len(paraReal):
                raise TypeMismatchInExpression(ast)
            for i in range(len(para)):
                if type(para[i]) != type(paraReal[i]):
                    raise TypeMismatchInExpression(ast)
        return mtype.restype

    def visitIntLiteral(self, ast, c):
        """
        value:int
        """
        return IntType()

    def visitFloatLiteral(self, ast, c):
        """
        value:float
        """
        return FloatType()

    def visitStringLiteral(self, ast, c):
        """
        value:str
        """
        return StringType()

    def visitBooleanLiteral(self, ast, c):
        """
        value:bool
        """
        return BoolType()

    def visitArrayLiteral(self, ast, c):
        """
        value:List[Literal]
        """
        pass

    def visitAssign(self, ast, c):
        """
        lhs: LHS
        rhs: Expr
        """
        returnType, scope = c
        if isinstance(ast.lhs,Id):
            left = self.visit(ast.lhs,(None,scope))
        else:
            left = self.visit(ast.lhs,scope)
        if isinstance(ast.rhs,Id):
            right = self.visit(ast.rhs,(Variable(),scope))
        else:
            right = self.visit(ast.rhs,scope)

        if type(left) is Unknown and type(right) is Unknown:
            raise TypeCannotBeInferred(ast)

        if type(left) is Unknown:
            Symbol.setPrimType(ast.lhs.name,right,scope)
        
        if type(right) is Unknown:
            Symbol.setPrimType(ast.rhs.name,left,scope)
        
        if type(right) != type(left):
            raise TypeMismatchInStatement(ast)


    def visitIf(self, ast, c):
        """
        ifthenStmt:List[Tuple[Expr,List[VarDecl],List[Stmt]]]
        elseStmt:Tuple[List[VarDecl],List[Stmt]] # for Else branch, empty list if no Else
        """
        returnType, scope = c
        for ifPart in ast.ifthenStmt:
            localVar = []
            self.visit(ifPart[0],(None, scope))
            [self.visit(var,(Variable(),localVar)) for var in ifPart[1]]
            newScope = Symbol.mergeScope(scope,localVar)
            self.visitStmts(ifPart[2],(returnType, newScope))
        
        elsePart = ast.elseStmt
        localVar = []
        [self.visit(var,(Variable(), localVar)) for var in elsePart[0]]
        newScope = Symbol.mergeScope(scope,localVar)
        self.visitStmts(elsePart[1],(returnType, newScope))
        

    def visitFor(self, ast, c):
        """
        idx1: Id
        expr1:Expr
        expr2:Expr
        expr3:Expr
        loop: Tuple[List[VarDecl],List[Stmt]]
        """
        returnType, scope = c
        idx = Symbol(ast.idx1.name,IntType())
        localVar = [idx]
        exp1 = self.visit(ast.expr1,(None,scope))
        if type(exp1) is not IntType:
            raise TypeMismatchInStatement(ast)
        exp2 = self.visit(ast.expr2,(None,scope))
        if type(exp2) is not BoolType:
            raise TypeMismatchInStatement(ast)
        exp3 = self.visit(ast.expr3,(None,scope))
        if type(exp3) is not IntType:
            raise TypeMismatchInStatement(ast)

        [self.visit(var,(Variable(),localVar)) for var in ast.loop[0]]
        newScope = Symbol.mergeScope(scope,localVar)
        self.visitStmts(ast.loop[1],(returnType,newScope))

    def visitBreak(self, ast, c):
        """
        break
        """
        return

    def visitContinue(self, ast, c):
        """
        continue
        """
        return

    def visitReturn(self, ast, c):
        """
        expr:Expr # None if no expression
        """
        returnType, scope = c
        if ast.expr:
            reType = self.visit(ast.expr,(None,scope))
            returnType = reType
        returnType = VoidType()

    def visitDoWhile(self, ast, c):
        """
        sl:Tuple[List[VarDecl],List[Stmt]]
        exp: Expr
        """
        returnType, scope = c
        localVar = []
        [self.visit(var,(Variable(), localVar)) for var in ast.sl[0]]
        newScope = Symbol.mergeScope(scope,localVar)
        self.visitStmts(ast.sl[1],(returnType,newScope))
        exp = self.visit(ast.exp,(None,scope))
        if type(exp) is not BoolType:
            raise TypeMismatchInStatement(ast)

    def visitWhile(self, ast, c):
        """
        exp: Expr
        sl:Tuple[List[VarDecl],List[Stmt]]
        """
        returnType, scope = c
        exp = self.visit(ast.exp,(None,scope))
        if type(exp) is not BoolType:
            raise TypeMismatchInStatement(ast)
        localVar = []
        [self.visit(var,(Variable(), localVar)) for var in ast.sl[0]]
        newScope = Symbol.mergeScope(scope,localVar)
        self.visitStmts(ast.sl[1],(returnType,newScope))

    def visitCallStmt(self, ast, c):
        """
        method:Id
        param: List[Expr]
        """
        returnType, scope = c
        mtype = self.visit(ast.method,(Function(),scope))
        
        paraReal = mtype.intype
        para = [self.visit(p,(None,scope)) for p in ast.param]

        if paraReal is None:
            Symbol.setFuncType(ast.method.name,para,mtype.restype,scope)
        else:
            if len(para) != len(paraReal):
                raise TypeMismatchInStatement(ast)
            for i in range(len(para)):
                if type(para[i]) != type(paraReal[i]):
                    raise TypeMismatchInStatement(ast)


    def visitId(self, ast, c):
        """
        name : str
        """
        varType, scope = c
        for i in scope:
            if i.name == ast.name:
                return i.mtype
        if varType is None:
            raise Undeclared(Variable(),ast.name)
        else:
            raise Undeclared(Function(),ast.name)

    def visitStmts(self, body, c):
        """
        body: List[Stmt]
        """
        returnType, scope = c
        for stmt in body:
            ret = None
            self.visit(stmt,(ret, scope))
            if ret:
                if returnType and type(ret) != type(returnType):
                    raise TypeMismatchInStatement(stmt)
                elif returnType is None:
                    returnType = ret
        







        

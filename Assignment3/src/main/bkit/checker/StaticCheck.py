
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
    kind: Kind

    @staticmethod
    def getType(obj):
        """
        obj: Symbol
        """
        if type(obj) is Symbol:
            if type(obj.kind) is Function:
                return obj.mtype.restype
            else:
                if type(obj.mtype) is ArrayType:
                    return obj.mtype.eletype
                return obj.mtype
        else:
            if type(obj) is ArrayType:
                return obj.eletype
            return obj

    @staticmethod
    def getTypeExpectArray(obj):
        if type(obj) is Symbol:
            if type(obj.kind) is Function:
                return obj.mtype.restype
            return obj.mtype
        return obj
    @staticmethod
    def getObjFromName(name, env):
        sym = list(filter(lambda x: x.name==name, env))
        if sym:
            return sym[0]
        else:
            return None

    @staticmethod
    def setArrayType(symbol,mType,funcInfo):
        if type(symbol.mtype.eletype) is Unknown:
            symbol.mtype.eletype = mType
    
    @staticmethod
    def setTypeFromObj(symbol,mType,funcInfo):
        """
        symbol: Symbol
        mType: Type
        funcInfo = Tuple(Symbol, List[Symbol])
        """
        result = True
        if type(Symbol.getType(symbol.mtype)) is Unknown:
            if type(symbol.kind) is Parameter:
                result = Symbol.setParaType(symbol.name,mType,funcInfo)
            if type(symbol.mtype) is ArrayType:
                symbol.mtype.eletype = mType
            else:
                symbol.mtype = mType
        elif type(symbol.mtype) is MType:
            symbol.mtype.restype = mType
        return result

    @staticmethod
    def setParaType(namePara,mType,funcInfo):
        """
        namePara: str
        mType: Type
        funcInfo: Tuple(Symbol, List[Symbol])
        """
        func, params = funcInfo
        index = 0
        for p in params:
            if p.name == namePara:
                break
            index += 1
        if type(func.mtype.intype[index]) is Unknown:
            func.mtype.intype[index] = mType
        elif type(func.mtype.intype[index]) != type(mType):
            return False
        return True

    @staticmethod
    def setVarTypeWithOp(id, op, env,funcInfo):
        """
        id: str
        op: str
        """
        sym = Symbol.getObjFromName(id,env[0] + env[1])
        if op in ['-','+','*','\\','%','==','!=','<','>','<=','>=']:
            if Symbol.setTypeFromObj(sym,IntType(),funcInfo):
                return IntType()
            else:
                return False
        elif op in ['-.','+.','\\.','=/=','<.','>.','<=.','>=.']:
            if Symbol.setTypeFromObj(sym,FloatType(),funcInfo):
                return FloatType()
            else:
                return False
        elif op in ['&&','||','!']:
            if Symbol.setTypeFromObj(sym,BoolType(),funcInfo):
                return BoolType()
            else:
                return False
                

class Checker:
    @staticmethod
    def checkEntryPoint(funcList):
        """
        funcList: List[FuncDecl]
        """
        if ([*filter(lambda x: x.name.name == "main", funcList)]):
            return True
        raise NoEntryPoint()

    @staticmethod
    def checkRedeclared(id, env, kind):
        """
        id: str
        kind: Kind
        """
        checker = Symbol.getObjFromName(id,env[0])
        if checker:
            raise Redeclared(kind,id)

    @staticmethod
    def checkUndeclared(id, env, kind):
        """
        id: str
        kind: Kind
        """
        checker = Symbol.getObjFromName(id,env[0] + env[1])
        if not checker:
            raise Undeclared(kind,id)
        return checker


class StaticChecker(BaseVisitor):
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [
            Symbol("int_of_float",MType([FloatType()],IntType()),Function()),
            Symbol("float_of_int",MType([IntType()],FloatType()),Function()),
            Symbol("int_of_string",MType([StringType()],IntType()),Function()),
            Symbol("string_of_int",MType([IntType()],StringType()),Function()),
            Symbol("float_of_string",MType([StringType()],FloatType()),Function()),
            Symbol("string_of_float",MType([FloatType()],StringType()),Function()),
            Symbol("bool_of_string",MType([StringType()],BoolType()),Function()),
            Symbol("string_of_bool",MType([BoolType()],StringType()),Function()),
            Symbol("read",MType([],StringType()),Function()),
            Symbol("printLn",MType([],VoidType()),Function()),
            Symbol("printStr",MType([StringType()],VoidType()),Function()),
            Symbol("printStrLn",MType([StringType()],VoidType()),Function())]                           
   
    def check(self):
        return self.visit(self.ast,self.global_envi)

    def visitProgram(self, ast, c):
        """
        decl : List[Decl]
        """
        env = (c,[])
        funcDecl = []
        for decl in ast.decl:
            if type(decl) is FuncDecl:
                funcDecl.append(decl)
                name = decl.name.name
                para = decl.param
                Checker.checkRedeclared(name,env,Function())
                func = Symbol(name,MType([Unknown()]*len(para),Unknown()),Function())
                env[0].append(func)
            else:
                env = self.visit(decl,(Variable(),env))
        
        Checker.checkEntryPoint(funcDecl)
        reduce(lambda s,func: self.visit(func,s),funcDecl,env)
        

    def visitVarDecl(self, ast, c):
        """
        Decl
        c : (kind, env)
        variable : Id
        varDimen : List[int] # empty list for scalar variable
        varInit  : Literal # null if no initial
        """
        kind, env = c
        Checker.checkRedeclared(ast.variable.name,env,kind)
        if ast.varDimen:
            if ast.varInit:
                mType = self.visit(ast.varInit,None)
                newSym = Symbol(ast.variable.name,mType,kind)
                return env[0] + [newSym], env[1]
            else:
                mType = ArrayType(ast.varDimen,Unknown())
                newSym = Symbol(ast.variable.name,mType,kind)
                return env[0] + [newSym], env[1]
        else:
            if ast.varInit:
                mType = self.visit(ast.varInit,None)
                newSym = Symbol(ast.variable.name,mType,kind)
                return (env[0] + [newSym], env[1])
            else:
                newSym = Symbol(ast.variable.name,Unknown(),kind)
                return (env[0] + [newSym], env[1])



    def visitFuncDecl(self, ast, c):
        """
        Decl
        c : env
        name: Id
        param: List[VarDecl]
        body: Tuple[List[VarDecl],List[Stmt]]
        """
        param = reduce(lambda s, para: self.visit(para,(Parameter(), s)),ast.param,([],[]))[0]
        newEnv = (param, c[0]+c[1])
        newEnv = reduce(lambda s, ele: self.visit(ele, (Variable(), s)), ast.body[0], newEnv)
        func = list(filter(lambda n: n.name == ast.name.name and type(n.kind) is Function,c[0]+c[1]))[0]
        funcInfo = (func, param)
        self.visitStmts(ast.body[1], (funcInfo, newEnv))
        return c


    def visitArrayCell(self, ast, c):
        """
        LHS
        c: funcInfo, kind, env
        arr:Expr
        idx:List[Expr]
        """
        funcInfo, kind, env = c
        arr = self.visit(ast.arr,(funcInfo,None,env))
        aType = Symbol.getTypeExpectArray(arr)
        if type(aType) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        if len(aType.dimen) != len(ast.idx):
            raise TypeMismatchInExpression(ast)
        if type(aType) is ArrayType:
            for e in ast.idx:
                ele = self.visit(e,(funcInfo,None,env))
                if type(Symbol.getType(ele)) is not IntType:
                    raise TypeMismatchInExpression(ast)

            return arr
                
    

    def visitBinaryOp(self, ast, c):
        """
        Expr
        c: funcInfo, kind, env
        op:str
        left:Expr
        right:Expr
        """
        funcInfo, kind, env = c
        op = ast.op
        left = self.visit(ast.left,(funcInfo, None, env))
        right = self.visit(ast.right,(funcInfo, None, env))
        typeLeft = Symbol.getType(left)
        typeRight = Symbol.getType(right)

        if type(typeLeft) is Unknown:
            typeLeft = Symbol.setVarTypeWithOp(ast.left.name,op,env,funcInfo)
            if not typeLeft:
                raise TypeMismatchInExpression(ast)

        if type(typeRight) is Unknown:
            typeRight = Symbol.setVarTypeWithOp(ast.right.name,op,env,funcInfo)
            if not typeRight:
                raise TypeMismatchInExpression(ast)

        if op in ['-','+','*','\\','%']:
            if type(typeLeft) is IntType and type(typeRight) is IntType:
                return IntType()
        elif op in ['-.','+.','\\.']:
            if type(typeLeft) is FloatType and type(typeRight) is FloatType:
                return FloatType()
        elif op in ['==','!=','<','>','<=','>=']:
            if type(typeLeft) is IntType and type(typeRight) is IntType:
                return BoolType()
        elif op in ['=/=','<.','>.','<=.','>=.']:
            if type(typeLeft) is FloatType and type(typeRight) is FloatType:
                return BoolType()
        elif op in ['&&','||']:
            if type(typeLeft) is BoolType and type(typeRight) is BoolType:
                return BoolType()
        raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self, ast, c):
        """
        Expr
        c: funcInfo, kind, env
        op:str
        body:Expr
        """
        funcInfo, kind, env = c
        op = ast.op
        exp = self.visit(ast.body,(funcInfo, None,env))
        if type(Symbol.getType(exp)) is Unknown:
            if not Symbol.setVarTypeWithOp(ast.body.name,op,env,funcInfo):
                raise TypeMismatchInExpression(ast)

        if op == '-':
            if type(Symbol.getType(exp)) is IntType:
                return IntType()
        elif op == '-.':
            if type(Symbol.getType(exp)) is FloatType:
                return FloatType()
        elif op == '!':
            if type(Symbol.getType(exp)) is BoolType:
                return BoolType()
        raise TypeMismatchInExpression(ast)

    def visitCallExpr(self, ast, c):
        """
        Expr
        c: funcInfo, kind, env
        method:Id
        param:List[Expr]
        """
        funcInfo, kind, env = c
        func = Checker.checkUndeclared(ast.method.name,env,Function())
        if type(func.kind) != Function:
            raise TypeMismatchInStatement(ast)
        if len(func.mtype.intype) != len(ast.param):
            raise TypeMismatchInExpression(ast)
        for i, (arg, typePara) in enumerate(zip(ast.param,func.mtype.intype)):
            a = self.visit(arg,(funcInfo, None,env))
            if type(Symbol.getType(a)) is Unknown:
                if type(typePara) is not Unknown:
                    if not Symbol.setTypeFromObj(a,typePara,funcInfo):
                        raise TypeMismatchInStatement(ast)
                else:
                    raise TypeCannotBeInferred(ast)
            elif type(typePara) is Unknown:
                func.mtype.intype[i] = Symbol.getType(a)
            elif type(typePara) != type(Symbol.getType(a)):
                raise TypeMismatchInExpression(ast)

        return func

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
        dimen = [len(ast.value)]
        eleType = Unknown()
        isFisrt = True
        tmp = Unknown()
        for e in ast.value:
            if isFisrt:
                isFisrt = False
                x = self.visit(e,None)
                tmp = x
                if type(Symbol.getTypeExpectArray(x)) is ArrayType:
                    dimen = dimen + x.dimen
                    eleType = x.eletype
                else:
                    eleType = x
            else:
                x = self.visit(e,None)
                if type(Symbol.getType(x)) != type(Symbol.getType(tmp)):
                    raise TypeMismatchInExpression(ast)

        return ArrayType(dimen,eleType)

    def visitAssign(self, ast, c):
        """
        Stmt
        c: funcInfo, env
        lhs: LHS
        rhs: Expr
        """
        funcInfo, env = c
        left = self.visit(ast.lhs,(funcInfo, None,env))
        right = self.visit(ast.rhs,(funcInfo, None,env))
        typeLeft = Symbol.getTypeExpectArray(left)
        typeRight = Symbol.getTypeExpectArray(right)
        if type(typeLeft) is VoidType or type(typeRight) is VoidType:
            raise TypeMismatchInStatement(ast)
        if type(typeLeft) is Unknown and type(typeRight) is Unknown:
            raise TypeCannotBeInferred(ast)
        elif type(typeLeft) is Unknown:
            if type(typeRight) is ArrayType:
                if type(typeRight.eletype) is Unknown:
                    raise TypeCannotBeInferred(ast)
                else:
                    if not Symbol.setTypeFromObj(left,typeRight.eletype,funcInfo):
                        raise TypeMismatchInStatement(ast)
            else:
                if not Symbol.setTypeFromObj(left,typeRight,funcInfo):
                    raise TypeMismatchInStatement(ast)
        elif type(typeRight) is Unknown:
            if type(typeLeft) is ArrayType:
                if type(typeLeft.eletype) is Unknown:
                    raise TypeCannotBeInferred(ast)
                else:
                    if not Symbol.setTypeFromObj((right,typeLeft.eletype,funcInfo)):
                        raise TypeMismatchInStatement(ast)
            else:
                if not Symbol.setTypeFromObj(right,typeLeft,funcInfo):
                    raise TypeMismatchInStatement(ast)
        elif type(typeLeft) not in [Unknown,ArrayType] and type(typeRight) is ArrayType:
            if type(typeRight.eletype) is Unknown:
                right.mtype.eletype = typeLeft
            else:
                if type(typeLeft) != type(typeRight.eletype):
                    raise TypeMismatchInStatement(ast)
        elif type(typeRight) not in [Unknown,ArrayType] and type(typeLeft) is ArrayType:
            if type(typeLeft.eletype) is Unknown:
                left.mtype.eletype = typeRight
            else:
                if type(typeLeft.eletype) != type(typeRight):
                    raise TypeMismatchInStatement(ast)
        else:
            if type(typeLeft) is ArrayType and type(typeRight) is ArrayType:
                if type(typeLeft.eletype) is Unknown and type(typeRight) is Unknown:
                    raise TypeCannotBeInferred(ast)
                elif type(typeLeft.eletype) is Unknown:
                    left.mtype.eletype = typeRight.eletype
                elif type(typeRight.eletype) is Unknown:
                    right.mtype.eletype = typeLeft.eletype
                else:
                    if type(typeLeft.eletype) != type(typeRight.eletype):
                        raise TypeMismatchInStatement(ast)
            elif type(typeRight) != type(typeLeft):
                raise TypeMismatchInStatement(ast)


    def visitIf(self, ast, c):
        """
        Stmt
        c: funcInfo, env
        ifthenStmt:List[Tuple[Expr,List[VarDecl],List[Stmt]]]
        elseStmt:Tuple[List[VarDecl],List[Stmt]] # for Else branch, empty list if no Else
        """
        funcInfo, env = c
        for ifPart in ast.ifthenStmt:
            cond = self.visit(ifPart[0],(funcInfo, None, env))
            if type(Symbol.getType(cond)) is not BoolType:
                if type(Symbol.getType(cond)) is Unknown:
                    if not Symbol.setTypeFromObj(cond,BoolType(),funcInfo):
                        raise TypeMismatchInStatement(ast)
                else:
                    raise TypeMismatchInStatement(ast)
            newEnv = reduce(lambda s, ele: self.visit(ele,(Variable(),s)),ifPart[1],env)
            self.visitStmts(ifPart[2],(funcInfo, newEnv))
        
        elsePart = ast.elseStmt
        newEnv = reduce(lambda s, ele: self.visit(ele,(Variable(),s)),elsePart[0],env)
        self.visitStmts(elsePart[1],(funcInfo, newEnv))


    def visitFor(self, ast, c):
        """
        Stmt
        c: funcInfo, env
        idx1: Id
        expr1:Expr
        expr2:Expr
        expr3:Expr
        loop: Tuple[List[VarDecl],List[Stmt]]
        """
        funcInfo, env = c
        idx = Checker.checkUndeclared(ast.idx1.name,env,Identifier())
        if type(Symbol.getType(idx)) is not IntType:
            if type(Symbol.getType(idx)) is Unknown:
                if not Symbol.setTypeFromObj(idx,IntType(),funcInfo):
                    raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInStatement(ast)

        exp1 = self.visit(ast.expr1,(funcInfo, None,env))
        if type(Symbol.getType(exp1)) is not IntType:
            if type(Symbol.getType(exp1)) is Unknown:
                if not Symbol.setTypeFromObj(exp1,IntType(),funcInfo):
                    raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInStatement(ast)

        exp2 = self.visit(ast.expr2,(funcInfo, None,env))
        if type(Symbol.getType(exp2)) is not BoolType:
            if type(Symbol.getType(exp2)) is Unknown:
                if not Symbol.setTypeFromObj(exp2,BoolType(),funcInfo):
                    raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInStatement(ast)

        exp3 = self.visit(ast.expr3,(None,env))
        if type(Symbol.getType(exp3)) is not IntType:
            if type(Symbol.getType(exp3)) is Unknown:
                if not Symbol.setTypeFromObj(exp3,IntType(),funcInfo):
                    raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInStatement(ast)

        newEnv = reduce(lambda s, ele: self.visit(ele,(Variable(),s)),ast.loop[0],env)
        self.visitStmts(ast.loop[1], (funcInfo, newEnv))

    def visitBreak(self, ast, c):
        """
        Stmt
        break
        """
        return

    def visitContinue(self, ast, c):
        """
        Stmt
        continue
        """
        return

    def visitReturn(self, ast, c):
        """
        Stmt
        c: funcInfo, env
        expr:Expr # None if no expression
        """
        funcInfo, env = c
        returnType = funcInfo[0].mtype.restype
        if ast.expr:
            reType = self.visit(ast.expr,(funcInfo, None, env))
            if type(returnType) is not Unknown:
                if type(Symbol.getType(reType)) is not Unknown:
                    if type(returnType) != type(Symbol.getType(reType)):
                        raise TypeMismatchInStatement(ast)
                else:
                    if not Symbol.setTypeFromObj(reType,returnType,funcInfo):
                        raise TypeMismatchInStatement(ast)
            else:
                if type(Symbol.getType(reType)) is Unknown:
                    raise TypeCannotBeInferred(ast)
            funcInfo[0].mtype.restype = reType
        else:
            if type(returnType) is Unknown: 
                funcInfo[0].mtype.restype = VoidType()
            else:
                raise TypeMismatchInStatement(ast)


    def visitDowhile(self, ast, c):
        """
        Stmt
        c: funcInfo, env
        sl:Tuple[List[VarDecl],List[Stmt]]
        exp: Expr
        """
        funcInfo, env = c
        newEnv = reduce(lambda s,ele: self.visit(ele,(Variable(),s)),ast.sl[0],env)
        self.visitStmts(ast.sl[1],(funcInfo,newEnv))
        exp = self.visit(ast.exp,(funcInfo,None,env))
        if type(Symbol.getType(exp)) is not BoolType:
            if type(Symbol.getType(exp)) is Unknown:
                if not Symbol.setTypeFromObj(exp,BoolType(),funcInfo):
                    raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInStatement(ast)

    def visitWhile(self, ast, c):
        """
        Stmt
        c: funcInfo, env
        exp: Expr
        sl:Tuple[List[VarDecl],List[Stmt]]
        """
        funcInfo, env = c
        exp = self.visit(ast.exp,(funcInfo,None,env))
        if type(Symbol.getType(exp)) is not BoolType:
            if type(Symbol.getType(exp)) is Unknown:
                if not Symbol.setTypeFromObj(exp,BoolType(),funcInfo):
                    raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInStatement(ast)
        newEnv = reduce(lambda s,ele: self.visit(ele,(Variable(),s)),ast.sl[0],env)
        self.visitStmts(ast.sl[1],(funcInfo,newEnv))
        

    def visitCallStmt(self, ast, c):
        """
        Stmt
        c: funcInfo, env
        method:Id
        param:List[Expr]
        """
        funcInfo, env = c
        func = Checker.checkUndeclared(ast.method.name,env,Function())
        if type(func.kind) != Function:
            raise TypeMismatchInStatement(ast)
        if len(func.mtype.intype) != len(ast.param):
            raise TypeMismatchInStatement(ast)
        for i, (arg, typePara) in enumerate(zip(ast.param,func.mtype.intype)):
            a = self.visit(arg,(funcInfo,None,env))
            if type(Symbol.getType(a)) is Unknown:
                if type(typePara) is not Unknown:
                    if not Symbol.setTypeFromObj(a,typePara,funcInfo):
                        raise TypeMismatchInStatement(ast)
                else:
                    raise TypeCannotBeInferred(ast)
            elif type(typePara) is Unknown:
                func.mtype.intype[i] = Symbol.getType(a)
            elif type(typePara) != type(Symbol.getType(a)):
                raise TypeMismatchInStatement(ast)
        
        if type(func.mtype.restype) is Unknown:
            func.mtype.restype = VoidType()



    def visitId(self, ast, c):
        """
        LHS
        c: funcInfo, kind, env
        name : str
        """
        funcInfo, kind, env = c
        if type(kind) is Function:
            checker = Checker.checkUndeclared(ast.name,env,kind)
            return checker
        checker = Checker.checkUndeclared(ast.name,env,Identifier())
        return checker

    def visitStmts(self, stmts, c):
        """
        stmts: List[Stmt]
        c: funcInfo, env
        """
        funcInfo, env = c
        returnType = funcInfo[0].mtype.restype
        for stmt in stmts:
            self.visit(stmt,(funcInfo,env))


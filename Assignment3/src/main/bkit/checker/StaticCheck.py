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
            return obj.mtype
        return obj

    @staticmethod
    def getObjFromName(name, env,kind):
        # sym = list(filter(lambda x: x.name==name , env))
        sym = None
        for x in env:
            if x.name == name:
                sym = x
                break
        return sym

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
            if type(mType) is ArrayType and type(Symbol.getType(symbol)) is not ArrayType:
                result = False
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
    def setVarTypeWithOp(sym, op, env,funcInfo, isArrayCell):
        """
        id: str
        op: str
        """
        if op in ['-','+','*','\\','%','==','!=','<','>','<=','>=']:
            if isArrayCell:
                sym.mtype.eletype = IntType()
            elif Symbol.setTypeFromObj(sym,IntType(),funcInfo):
                return IntType()
            else:
                return False
        elif op in ['-.','+.','\\.','=/=','<.','>.','<=.','>=.']:
            if isArrayCell:
                sym.mtype.eletype = FloatType()
            if Symbol.setTypeFromObj(sym,FloatType(),funcInfo):
                return FloatType()
            else:
                return False
        elif op in ['&&','||','!']:
            if isArrayCell:
                sym.mtype.eletype = BoolType()
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
        checker = Symbol.getObjFromName(id,env[0],kind)
        if checker:
            raise Redeclared(kind,id)

    @staticmethod
    def checkUndeclared(id, env, kind):
        """
        id: str
        kind: Kind
        """
        checker = Symbol.getObjFromName(id,env[0] + env[1], kind)
        if not checker:
            raise Undeclared(kind,id)
        return checker


class StaticChecker(BaseVisitor):
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [
            Symbol("int_of_float",MType([FloatType()],IntType()),Function()),
            Symbol("float_to_int",MType([IntType()],FloatType()),Function()),
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
        newSym = None
        if ast.varDimen:
            if ast.varInit:
                mType = self.visit(ast.varInit,None)
                newSym = Symbol(ast.variable.name,mType,kind)
            else:
                mType = ArrayType(ast.varDimen,Unknown())
                newSym = Symbol(ast.variable.name,mType,kind)
        else:
            if ast.varInit:
                mType = self.visit(ast.varInit,None)
                newSym = Symbol(ast.variable.name,mType,kind)
            else:
                newSym = Symbol(ast.variable.name,Unknown(),kind)
        return env[0] + [newSym], env[1]

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
        # func.mtype.intype = [p.mtype for p in param]
        for i,(pa,p) in enumerate(zip(func.mtype.intype,param)):
            if type(pa) is Unknown:
                func.mtype.intype[i] = p.mtype

        return c

    def visitArrayCell(self, ast, c):
        """
        LHS
        c: funcInfo, kind, env
        arr:Expr
        idx:List[Expr]
        """
        funcInfo, env = c
        arr = self.visit(ast.arr,(funcInfo,env))
        if not arr:
            raise TypeMismatchInStatement(ast)
        aType = Symbol.getType(arr)
        if type(aType) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        else:
            if len(aType.dimen) != len(ast.idx):
                raise TypeMismatchInExpression(ast)
            for e in ast.idx:
                index = self.visit(e,(funcInfo,env))
                if not index:
                    raise TypeMismatchInStatement(ast)
                iType = Symbol.getType(index)
                if type(e) is ArrayCell:
                    iType = iType.eletype
                if type(iType) is Unknown:
                    if type(e) is ArrayCell:
                        index.mtype.eletype = IntType()
                    elif not Symbol.setTypeFromObj(index,IntType(),funcInfo):
                        raise TypeMismatchInExpression(ast)
                elif type(iType) is not IntType:
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
        funcInfo, env = c
        op = ast.op
        left = self.visit(ast.left,(funcInfo, env))
        if not left:
            raise TypeMismatchInStatement(ast)
        right = self.visit(ast.right,(funcInfo, env))
        if not right:
            raise TypeMismatchInStatement(ast)
        typeLeft = Symbol.getType(left)
        isArrayCellLeft = False
        isArrayCellRight = False
        if type(ast.left) is ArrayCell:
            typeLeft = typeLeft.eletype
            isArrayCellLeft = True
        typeRight = Symbol.getType(right)
        if type(ast.right) is ArrayCell:
            typeRight = typeRight.eletype
            isArrayCellRight = True

        if type(typeLeft) is Unknown:
            typeLeft = Symbol.setVarTypeWithOp(left,op,env,funcInfo,isArrayCellLeft)
            if not typeLeft:
                raise TypeMismatchInExpression(ast)

        if type(typeRight) is Unknown:
            typeRight = Symbol.setVarTypeWithOp(right,op,env,funcInfo,isArrayCellRight)
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
        funcInfo, env = c
        op = ast.op
        exp = self.visit(ast.body,(funcInfo, env))
        if not exp:
            raise TypeMismatchInStatement(ast)
        tExp = Symbol.getType(exp)
        isArrayCell = False
        if type(ast.body) is ArrayCell:
            tExp = tExp.eletype
            isArrayCell = True
        if type(tExp) is Unknown:
            if not Symbol.setVarTypeWithOp(exp,op,env,funcInfo,isArrayCell):
                raise TypeMismatchInExpression(ast)

        if op == '-':
            if type(tExp) is IntType:
                return IntType()
        elif op == '-.':
            if type(tExp) is FloatType:
                return FloatType()
        elif op == '!':
            if type(tExp) is BoolType:
                return BoolType()
        raise TypeMismatchInExpression(ast)

    def visitCallExpr(self, ast, c):
        """
        Expr
        c: funcInfo, kind, env
        method:Id
        param:List[Expr]
        """
        funcInfo, env = c
        func = Checker.checkUndeclared(ast.method.name,env,Function())
        if type(func.kind) != Function:
            raise Undeclared(Function(),ast.method.name)
        if len(func.mtype.intype) != len(ast.param):
            raise TypeMismatchInExpression(ast)
        for i, (arg, typePara) in enumerate(zip(ast.param,func.mtype.intype)):
            a = self.visit(arg,(funcInfo,env))
            if not a:
                raise TypeMismatchInExpression(ast)
            tArg = Symbol.getType(a)
            if type(arg) is ArrayCell:
                tArg = tArg.eletype
            if type(tArg) is Unknown:
                if type(typePara) is not Unknown:
                    if not Symbol.setTypeFromObj(a,typePara,funcInfo):
                        raise TypeMismatchInExpression(ast)
                else:
                    raise TypeCannotBeInferred(ast)
            elif type(typePara) is Unknown:
                func.mtype.intype[i] = tArg
            elif type(typePara) != type(tArg):
                raise TypeMismatchInExpression(ast)
            else:
                if type(typePara) is ArrayType and type(tArg) is ArrayType:
                    if typePara.dimen != tArg.dimen:
                        raise TypeMismatchInExpression(ast)
                    if type(tArg.eletype) is Unknown and type(typePara.eletype) is Unknown:
                        raise TypeCannotBeInferred(ast)
                    elif type(tArg.eletype) is Unknown:
                        a.mtype.eletype = typePara.eletype
                    elif type(typePara.eletype) is Unknown:
                        typePara.eletype = a.mtype.eletype
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
                if type(Symbol.getType(x)) is ArrayType:
                    dimen = dimen + x.dimen
                    eleType = x.eletype
                else:
                    eleType = x
            else:
                x = self.visit(e,None)
                if type(Symbol.getType(x)) != type(Symbol.getType(tmp)):
                    raise TypeMismatchInExpression(ast)
                if type(Symbol.getType(x)) is ArrayType:
                    if x.dimen != tmp.dimen or type(x.eletype) != type(tmp.eletype):
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
        left = self.visit(ast.lhs,(funcInfo,env))
        if not left:
            raise TypeMismatchInStatement(ast)
        right = self.visit(ast.rhs,(funcInfo,env))
        if not right:
            raise TypeMismatchInStatement(ast)
        typeLeft = Symbol.getType(left)
        typeRight = Symbol.getType(right)
        isArrayCellLeft = False
        isArrayCellRight = False
        if type(ast.lhs) is ArrayCell:
            typeLeft = typeLeft.eletype
            isArrayCellLeft = True
        if type(ast.rhs) is ArrayCell:
            typeRight = typeRight.eletype
            isArrayCellRight = True

        if type(typeLeft) is VoidType or type(typeRight) is VoidType:
            raise TypeMismatchInStatement(ast)

        if type(typeLeft) is Unknown and type(typeRight) is Unknown:
            raise TypeCannotBeInferred(ast)
        elif type(typeLeft) is Unknown:
            if isArrayCellLeft:
                left.mtype.eletype = typeRight
            elif not Symbol.setTypeFromObj(left,typeRight,funcInfo):
                raise TypeMismatchInStatement(ast)
        elif type(typeRight) is Unknown:
            if isArrayCellRight:
                right.mtype.eletype = typeLeft
            elif not Symbol.setTypeFromObj(right,typeLeft,funcInfo):
                raise TypeMismatchInStatement(ast)
        elif isArrayCellRight and not isArrayCellLeft:
            if type(typeRight) is Unknown:
                right.mtype.eletype = typeLeft
            else:
                if type(typeLeft) != type(typeRight):
                    raise TypeMismatchInStatement(ast)
        elif isArrayCellLeft and not isArrayCellRight:
            if type(typeLeft) is Unknown:
                left.mtype.eletype = typeRight
            else:
                if type(typeLeft) != type(typeRight):
                    raise TypeMismatchInStatement(ast)
        else:
            if type(typeRight) is ArrayType and type(typeLeft) is ArrayType:
                if len(typeLeft.dimen) != len(typeRight.dimen):
                    raise TypeMismatchInStatement(ast)
                if type(typeLeft.eletype) is Unknown and type(typeRight.eletype) is Unknown:
                    raise TypeCannotBeInferred(ast)
                elif type(typeLeft.eletype) is Unknown:
                    left.mtype.eletype = typeRight.eletype
                elif type(typeRight.eletype) is Unknown:
                    right.mtype.eletype = typeLeft.eletype
                elif type(typeLeft.eletype) != type(typeRight.eletype):
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
            cond = self.visit(ifPart[0],(funcInfo, env))
            if not cond:
                raise TypeMismatchInStatement(ast)
            conType = Symbol.getType(cond)
            isArrayCell = False
            if type(ifPart[0]) is ArrayCell:
                conType = conType.eletype
                isArrayCell = True
            if type(conType) is not BoolType:
                if type(conType) is Unknown:
                    if isArrayCell:
                        cond.mtype.eletype = BoolType()
                    elif not Symbol.setTypeFromObj(cond,BoolType(),funcInfo):
                        raise TypeMismatchInStatement(ast)
                else:
                    raise TypeMismatchInStatement(ast)
            newEnv = ([],env[0]+env[1])
            newEnv = reduce(lambda s, ele: self.visit(ele,(Variable(),s)),ifPart[1],newEnv)
            self.visitStmts(ifPart[2],(funcInfo, newEnv))
        
        elsePart = ast.elseStmt
        newEnv = ([],env[0]+env[1])
        newEnv = reduce(lambda s, ele: self.visit(ele,(Variable(),s)),elsePart[0],newEnv)
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
        idx = self.visit(ast.idx1,(funcInfo,env))
        if not idx:
            raise TypeMismatchInStatement(ast)
        iType = Symbol.getType(idx)
        if type(ast.idx1) is ArrayCell:
            iType = iType.eletype
        if type(iType) is not IntType:
            if type(iType) is Unknown:
                if type(ast.idx1) is ArrayCell:
                    idx.mtype.eletype = IntType()
                elif not Symbol.setTypeFromObj(idx,IntType(),funcInfo):
                    raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInStatement(ast)

        exp1 = self.visit(ast.expr1,(funcInfo,env))
        if not exp1:
            raise TypeMismatchInStatement(ast)
        tExp1 = Symbol.getType(exp1)
        if type(ast.expr1) is ArrayCell:
            tExp1 = tExp1.eletype
        if type(tExp1) is not IntType:
            if type(tExp1) is Unknown:
                if type(ast.expr1) is ArrayCell:
                    exp1.mtype.eletype = IntType()
                elif not Symbol.setTypeFromObj(exp1,IntType(),funcInfo):
                    raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInStatement(ast)

        exp2 = self.visit(ast.expr2,(funcInfo,env))
        if not exp2:
            raise TypeMismatchInStatement(ast)
        tExp2 = Symbol.getType(exp2)
        if type(ast.expr2) is ArrayCell:
            tExp2 = tExp2.eletype
        if type(tExp2) is not BoolType:
            if type(tExp2) is Unknown:
                if type(ast.expr2) is ArrayCell:
                    exp2.mtype.eletype = BoolType()
                elif not Symbol.setTypeFromObj(exp2,BoolType(),funcInfo):
                    raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInStatement(ast)

        exp3 = self.visit(ast.expr3,(funcInfo,env))
        if not exp3:
            raise TypeMismatchInStatement(ast)
        tExp3 = Symbol.getType(exp3)
        if type(ast.expr3) is ArrayCell:
            tExp3 = tExp3.eletype
        if type(tExp3) is not IntType:
            if type(tExp3) is Unknown:
                if type(ast.expr3) is ArrayCell:
                    exp3.mtype.eletype = IntType()
                elif not Symbol.setTypeFromObj(exp3,IntType(),funcInfo):
                    raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInStatement(ast)

        newEnv = ([],env[0]+env[1])
        newEnv = reduce(lambda s, ele: self.visit(ele,(Variable(),s)),ast.loop[0],newEnv)
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
            reType = self.visit(ast.expr,(funcInfo, env))
            if not reType:
                raise TypeMismatchInStatement(ast)
            tRe = Symbol.getType(reType)
            if type(ast.expr) is ArrayCell:
                tRe = tRe.eletype
            if type(returnType) is not Unknown:
                if type(tRe) is not Unknown:
                    if type(returnType) != type(tRe):
                        raise TypeMismatchInStatement(ast)
                else:
                    if type(ast.expr) is ArrayCell:
                        reType.mtype.eletype = returnType
                    elif not Symbol.setTypeFromObj(reType,returnType,funcInfo):
                        raise TypeMismatchInStatement(ast)
            else:
                if type(tRe) is Unknown:
                    raise TypeCannotBeInferred(ast)
            funcInfo[0].mtype.restype = tRe
        else:
            if type(returnType) is Unknown: 
                funcInfo[0].mtype.restype = VoidType()
            elif type(returnType) is not VoidType:
                raise TypeMismatchInStatement(ast)

    def visitDowhile(self, ast, c):
        """
        Stmt
        c: funcInfo, env
        sl:Tuple[List[VarDecl],List[Stmt]]
        exp: Expr
        """
        funcInfo, env = c
        newEnv = ([],env[0]+env[1])
        newEnv = reduce(lambda s,ele: self.visit(ele,(Variable(),s)),ast.sl[0],newEnv)
        self.visitStmts(ast.sl[1],(funcInfo,newEnv))
        exp = self.visit(ast.exp,(funcInfo,env))
        if not exp:
            raise TypeMismatchInStatement(ast)
        tExp = Symbol.getType(exp)
        if type(ast.exp) is ArrayCell:
            tExp = tExp.eletype
        if type(tExp) is not BoolType:
            if type(tExp) is Unknown:
                if type(ast.exp) is ArrayCell:
                    exp.mtype.eletype = BoolType()
                elif not Symbol.setTypeFromObj(exp,BoolType(),funcInfo):
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
        exp = self.visit(ast.exp,(funcInfo,env))
        if not exp:
            raise TypeMismatchInStatement(ast)
        tExp = Symbol.getType(exp)
        if type(ast.exp) is ArrayCell:
            tExp = tExp.eletype
        if type(tExp) is not BoolType:
            if type(tExp) is Unknown:
                if type(ast.exp) is ArrayCell:
                    exp.mtype.eletype = BoolType()
                elif not Symbol.setTypeFromObj(exp,BoolType(),funcInfo):
                    raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInStatement(ast)
        newEnv = ([],env[0]+env[1])
        newEnv = reduce(lambda s,ele: self.visit(ele,(Variable(),s)),ast.sl[0],newEnv)
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
            raise Undeclared(Function(),ast.method.name)
        if len(func.mtype.intype) != len(ast.param):
            raise TypeMismatchInStatement(ast)
        for i, (arg, typePara) in enumerate(zip(ast.param,func.mtype.intype)):
            a = self.visit(arg,(funcInfo,env))
            if not a:
                raise TypeMismatchInStatement(ast)
            tArg = Symbol.getType(a)
            if type(arg) is ArrayCell:
                tArg = tArg.eletype
            if type(tArg) is Unknown:
                if type(typePara) is not Unknown:
                    if type(arg) is ArrayCell:
                        a.mtype.eletype = typePara
                    elif not Symbol.setTypeFromObj(a,typePara,funcInfo):
                        raise TypeMismatchInStatement(ast)
                else:
                    raise TypeCannotBeInferred(ast)
            elif type(typePara) is Unknown:
                func.mtype.intype[i] = tArg
            elif type(typePara) != type(tArg):
                raise TypeMismatchInStatement(ast)
            else:
                if type(typePara) is ArrayType and type(tArg) is ArrayType:
                    if typePara.dimen != tArg.dimen:
                        raise TypeMismatchInStatement(ast)
                    if type(tArg.eletype) is Unknown and type(typePara.eletype) is Unknown:
                        raise TypeCannotBeInferred(ast)
                    elif type(tArg.eletype) is Unknown:
                        a.mtype.eletype = typePara.eletype
                    elif type(typePara.eletype) is Unknown:
                        typePara.eletype = a.mtype.eletype
        
        if type(func.mtype.restype) is Unknown:
            func.mtype.restype = VoidType()
        elif type(func.mtype.restype) is not VoidType:
            raise TypeMismatchInStatement(ast)
       
    def visitId(self, ast, c):
        """
        LHS
        c: funcInfo, kind, env
        name : str
        """
        funcInfo, env = c
        checker = Checker.checkUndeclared(ast.name,env,Identifier())
        if type(checker.kind) is Function:
            raise Undeclared(Identifier(),ast.name)
        return checker

    def visitStmts(self, stmts, c):
        """
        stmts: List[Stmt]
        c: funcInfo, env
        """
        for stmt in stmts:
            self.visit(stmt,c)

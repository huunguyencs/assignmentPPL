from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        """
        Visit Program - Start point
        program  : vardeclare* funcdeclare* EOF;
        """
        vardecl = []
        funcdecl = []

        if ctx.vardeclare():
            var = ctx.vardeclare()
            if isinstance(var,list):
                for v in var:
                    vardecl += self.visit(v)
            else:
                vardecl = self.visit(var)
        if ctx.funcdeclare():
            func = ctx.funcdeclare()
            if isinstance(func,list):
                for f in func:
                    funcdecl += self.visit(f)
            else:
                funcdecl = self.visit(func)
        return Program(vardecl + funcdecl)
        
    
    def visitVardeclare(self,ctx:BKITParser.VardeclareContext):
        """
        Visit vardeclare
        vardeclare: VAR CL idlistinit SM;
        """
        return self.visit(ctx.idlistinit())

    # ************************************
    def visitIdlistinit(self,ctx:BKITParser.IdlistinitContext):
        """
        Visit Id list
        idlistinit: idinit (CM idinit)*;
        """
        idlist = ctx.idinit()
        if isinstance(idlist,list):
            return [self.visit(id) for id in idlist]
        else:
            return self.visit(idlist)

    def visitIdinit(self,ctx:BKITParser.IdinitContext):
        """
        Visit Id with dimension and literal init
        idinit: iddimen (AS lit)?;
        """
        var, dim = self.visit(ctx.iddimen())
        varinit = None
        if ctx.getChildCount() == 3:
            varinit = self.visit(ctx.lit())

        return VarDecl(var,dim,varinit)

    def visitIddimen(self, ctx:BKITParser.IddimenContext):
        """
        Visit Id dimension
        iddimen: ID dimension?;
        """
        var = Id(ctx.ID().getText())
        dim = []
        if ctx.getChildCount() == 2:
            dim = self.visit(ctx.dimension())
        return var, dim


    # ***************************************
    def visitDimension(self,ctx:BKITParser.DimensionContext):
        """
        Visit dimension ([int])
        dimension: LR INTLIT RR dimension?;
        """
        if ctx.getChildCount() == 3:
            return [int(ctx.INTLIT().getText())] 
        else:
            return [int(ctx.INTLIT().getText())] + self.visit(ctx.dimension())


    def visitFuncdeclare(self,ctx: BKITParser.FuncdeclareContext):
        """
        Visit function declare
        funcdeclare: FUNCTION CL ID (PARAMETER CL paralist)? body;
        """
        name = Id(ctx.ID().getText())
        param = []
        body = self.visit(ctx.body())

        if ctx.getChildCount() > 5:
            param = self.visit(ctx.paralist())

        return [FuncDecl(name,param,body)]


    def visitParalist(self,ctx:BKITParser.ParalistContext):
        """
        Visit parameter list in function
        paralist: iddimen (CM iddimen)*;
        """
        iddimen = ctx.iddimen()
        paralist = []
        if isinstance(iddimen,list):
            for i in iddimen:
                var, dim = self.visit(i)
                paralist += [VarDecl(var,dim,None)]
        else:
            var, dim = self.visit(iddimen)
            paralist = [VarDecl(var,dim,None)]
        return paralist

    def visitBody(self,ctx:BKITParser.BodyContext):
        """
        Visit body in function
        body: BODY CL vardeclare* stmt* ENDBODY DOT;
        """
        vlist = []
        slist = []
        if ctx.getChildCount() <= 4:
            return vlist, slist
        if ctx.vardeclare():
            var = ctx.vardeclare()
            if isinstance(var,list):
                for v in var:
                    vlist += self.visit(v)
            else:
                vlist = self.visit(var)
        if ctx.stmt():
            stmt = ctx.stmt()
            if isinstance(stmt,list):
                slist = [self.visit(s) for s in stmt]
            else:
                slist = [self.visit(stmt)]
            
        return vlist, slist

    def visitStmt_list(self, ctx:BKITParser.Stmt_listContext):
        """
        Visit list of statement
        stmt_list: vardeclare* stmt*;
        """
        vlist = []
        slist = []
        if ctx.vardeclare():
            var = ctx.vardeclare()
            if isinstance(var,list):
                for v in var:
                    vlist += self.visit(v)
            else:
                vlist = self.visit(var)
        if ctx.stmt():
            stmt = ctx.stmt()
            if isinstance(stmt,list):
                slist = [self.visit(s) for s in stmt]
            else:
                slist = [self.visit(stmt)]

        return vlist, slist

    def visitStmt(self,ctx:BKITParser.StmtContext):
        """
        Visit statement in function
        stmt 
            : assign_stmt
            | break_stmt
            | call_stmt
            | continue_stmt
            | do_stmt
            | for_stmt
            | if_stmt
            | return_stmt
            | while_stmt
            ;
        """
        if ctx.assign_stmt():
            return self.visit(ctx.assign_stmt())
        elif ctx.break_stmt():
            return self.visit(ctx.break_stmt())
        elif ctx.call_stmt():
            return self.visit(ctx.call_stmt())
        elif ctx.continue_stmt():
            return self.visit(ctx.continue_stmt())
        elif ctx.do_stmt():
            return self.visit(ctx.do_stmt())
        elif ctx.for_stmt():
            return self.visit(ctx.for_stmt())
        elif ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        elif ctx.return_stmt():
            return self.visit(ctx.return_stmt())
        else:
            return self.visit(ctx.while_stmt())

    def visitAssign_stmt(self,ctx:BKITParser.Assign_stmtContext):
        """
        Visit assign statement
        assign_stmt: variable AS exp SM;
        """
        lhs = self.visit(ctx.variable())
        rhs = self.visit(ctx.exp())
        return Assign(lhs,rhs)

    def visitIf_stmt(self,ctx:BKITParser.If_stmtContext):
        """
        Visit if statement
        if_stmt: IF exp THEN stmt_list (ELSEIF exp THEN stmt_list)* (ELSE stmt_list)? ENDIF DOT;
        """
        # exp = self.visit(ctx.exp(0))
        # stmtlist = self.visit(ctx.stmt_list(0))
        # a = ((None,exp) + stmtlist)[1:]
        # print(type(a[0]))
        # print(type(a[1]))
        # print(type(a[2]))
        # return If([a],None)
        exp = ctx.exp()
        ifthenStmt = []
        elseStmt = ()
        i = 0
        if isinstance(exp,list):
            for e in exp:
                ex = self.visit(e)
                stmtlist = self.visit(ctx.stmt_list(i))
                para = ((None,ex) + stmtlist)[1:]
                ifthenStmt += [para]
                i += 1
        else:
            ex = self.visit(self.visit(ctx.exp(0)))
            stmtlist = self.visit(ctx.stmt_list(0))
            para = ((None,ex) + stmtlist)[1:]
            ifthenStmt += [para]
            i = 1
        if ctx.ELSE():
            elseStmt = self.visit(ctx.stmt_list(i))
        return If(ifthenStmt,elseStmt)

        


    def visitFor_stmt(self, ctx:BKITParser.For_stmtContext):
        """
        Visit for statement
        for_stmt: FOR LP for_loop_con RP DO stmt_list ENDFOR DOT;
        """
        idx1, expr1, expr2, expr3 = self.visit(ctx.for_loop_con())
        loop = self.visit(ctx.stmt_list())
        return For(idx1,expr1,expr2,expr3,loop)


    def visitFor_loop_con(self, ctx:BKITParser.For_loop_conContext):
        """
        Visit loop condition in for statement
        for_loop_con: ID AS exp CM exp CM exp;
        """
        idx1 = Id(ctx.ID().getText())
        expr1 = self.visit(ctx.exp(0))
        expr2 = self.visit(ctx.exp(1))
        expr3 = self.visit(ctx.exp(2))
        return idx1, expr1, expr2, expr3

    def visitWhile_stmt(self,ctx:BKITParser.While_stmtContext):
        """
        Visit while statement
        while_stmt: WHILE exp DO stmt_list ENDWHILE DOT;
        """
        exp = self.visit(ctx.exp())
        stmtlist = self.visit(ctx.stmt_list())
        return While(exp,stmtlist)
    
    def visitDo_stmt(self,ctx:BKITParser.Do_stmtContext):
        """
        Visit do statement
        do_stmt: DO stmt_list WHILE exp ENDDO DOT;
        """
        stmt_list = self.visit(ctx.stmt_list())
        exp = self.visit(ctx.exp())
        return Dowhile(stmt_list,exp)

    def visitBreak_stmt(self, ctx:BKITParser.Break_stmtContext):
        """
        Visit break statement
        break_stmt: BREAK SM;
        """
        return Break()

    def visitContinue_stmt(self, ctx:BKITParser.Continue_stmtContext):
        """
        Visit continue statement
        continue_stmt: CONTINUE SM;
        """
        return Continue()

    def visitCall_stmt(self,ctx:BKITParser.Call_stmtContext):
        """
        Visit call statement
        call_stmt: call SM;
        """
        return self.visit(ctx.call())

    def visitReturn_stmt(self,ctx:BKITParser.Return_stmtContext):
        """
        Visit return statement
        return_stmt: RETURN exp? SM;
        """
        if ctx.exp():
            exp = self.visit(ctx.exp())
            return Return(exp)
        else:
            return Return()

    def visitExp(self, ctx:BKITParser.ExpContext):
        """
        Visit expression - relational
        exp
            : exp1 relational exp1
            | exp1
            ;
        """
        if ctx.getChildCount() == 3:
            return BinaryOp(self.visit(ctx.relational()),self.visit(ctx.exp1(0)),self.visit(ctx.exp1(1)))
        else:
            return self.visit(ctx.exp1(0))

    def visitExp1(self, ctx:BKITParser.Exp1Context):
        """
        Visit expression - logical
        exp1
            : exp1 logical exp11
            | exp11
            ;
        """
        if ctx.getChildCount() == 3:
            return BinaryOp(self.visit(ctx.logical()),self.visit(ctx.exp1()),self.visit(ctx.exp11()))
        else:
            return self.visit(ctx.exp11())

    def visitExp11(self, ctx:BKITParser.Exp11Context):
        """
        Visit expression - adding
        exp11
            : exp11 adding exp12
            | exp12
            ;
        """
        if ctx.getChildCount() == 3:
            return BinaryOp(self.visit(ctx.adding()),self.visit(ctx.exp11()),self.visit(ctx.exp12()))
        else:
            return self.visit(ctx.exp12())

    def visitExp12(self, ctx:BKITParser.Exp12Context):
        """
        Visit expression - multiplying
        exp12
            : exp12 multiplying exp2
            | exp2
            ;
        """
        if ctx.getChildCount() == 3:
            return BinaryOp(self.visit(ctx.multiplying()),self.visit(ctx.exp12()),self.visit(ctx.exp2()))
        else:
            return self.visit(ctx.exp2())

    def visitExp2(self, ctx:BKITParser.Exp2Context):
        """
        Visit expression - prefix
        exp2
            : (SUB | SUBF) exp2
            | NOT exp2
            | exp3
            ;
        """
        if ctx.getChildCount() == 2:
            if ctx.SUB():
                return UnaryOp(ctx.SUB().getText(),self.visit(ctx.exp2()))
            elif ctx.SUBF():
                return UnaryOp(ctx.SUBF().getText(),self.visit(ctx.exp2()))
            elif ctx.NOT():
                return UnaryOp(ctx.NOT().getText(),self.visit(ctx.exp2()))
        else:
            return self.visit(ctx.exp3())

    def visitExp3(self, ctx:BKITParser.Exp3Context):
        """
        Visit expression - element expression (index)
        exp3
            : ele_exp
            | exp4
            ;
        """
        return self.visitChildren(ctx)

    def visitExp4(self, ctx:BKITParser.Exp4Context):
        """
        Visit expression - call expression
        exp4
            : call
            | operands
            ;
        """
        return self.visitChildren(ctx)

    def visitCall(self, ctx:BKITParser.CallContext):
        """
        Visit call expression
        call: ID LP (exp (CM exp)*)? RP;
        """
        id = Id(ctx.ID().getText())
        param = []
        if ctx.exp():
            exp = ctx.exp()
            if isinstance(exp,list):
                param = [self.visit(e) for e in exp]
            else:
                param = [self.visit(exp)]

        return CallStmt(id,param)

    def visitOperands(self,ctx:BKITParser.OperandsContext):
        """
        Visit operands in expression
        operands
            : lit
            | LP exp RP
            | ID
            ;
        """
        if ctx.getChildCount() == 3:
            return self.visit(ctx.exp())
        elif ctx.lit():
            return self.visit(ctx.lit())
        else:
            return Id(ctx.ID().getText())

    def visitVariable(self, ctx:BKITParser.VariableContext):
        """
        Visit variable include id and index
        variable
            : ID
            | ele_exp
            ;
        """
        if ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.ele_exp())
    # wait teacher fix AST
    def visitEle_exp(self, ctx:BKITParser.Ele_expContext):
        """
        Visit lement expression (index in array)
        ele_exp : (ID | call) index_op;
        """
        if ctx.ID():
            id = ctx.ID().getText()
            index_op = self.visit(ctx.index_op())
            return ArrayCell(id,index_op)

    def visitIndex_op(self, ctx:BKITParser.Index_opContext):
        """
        Visit index operator (index part)
        index_op: LR exp RR index_op?;
        """
        if ctx.getChildCount() <= 3:
            return [self.visit(ctx.exp())]
        else:
            return [self.visit(ctx.exp())] + self.visit(ctx.index_op())

    def visitRelational(self, ctx:BKITParser.RelationalContext):
        """
        Visit realational operator in expression
        relational
            : EQ
            | NEQ
            | LT
            | GT
            | LTE
            | GTE
            | LTF
            | GTF
            | LTEF
            | GTEF
            ;
        """
        return ctx.getChild(0).getText()

    def visitLogical(self, ctx:BKITParser.LogicalContext):
        """
        Visit logical operator in expression
        logical
            : AND
            | OR
            ;
        """
        return ctx.getChild(0).getText()

    def visitAdding(self, ctx:BKITParser.AddingContext):
        """
        Visit adding operator in expression
        adding
            : ADD
            | ADDF
            | SUB
            | SUBF
            ;
        """
        return ctx.getChild(0).getText()

    def visitMultiplying(self, ctx:BKITParser.MultiplyingContext):
        """
        Visit multiplying operator in expression
        multiplying
            : MUL
            | MULF
            | DIV
            | DIVF
            | MOD
            ;
        """
        return ctx.getChild(0).getText()

    def visitArraylit(self, ctx:BKITParser.ArraylitContext):
        """
        Visit array literal
        arraylit: LB (lit (CM lit)*)? RB;
        """
        litlist = []
        if ctx.lit():
            lit = ctx.lit()
            if isinstance(lit,list):
                litlist = [self.visit(l) for l in lit]
            else:
                litlist = [self.visit(lit)]
        return ArrayLiteral(litlist) 

    def visitPrimitive(self, ctx:BKITParser.PrimitiveContext):
        """
        Visit primitive type
        primitive
            : INTLIT
            | FLOATLIT
            | boollit
            | STRINGLIT
            ;
        """
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        if ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        if ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        if ctx.boollit():
            return self.visit(ctx.boollit())

    def visitLit(self, ctx:BKITParser.LitContext):
        """
        Visit literal
        lit
            : primitive
            | arraylit
            ;
        """
        if ctx.primitive():
            return self.visit(ctx.primitive())
        return self.visit(ctx.arraylit())

    def visitBoollit(self,ctx:BKITParser.BoollitContext):
        """
        Visit boolean literal
        boollit: TRUE | FALSE;
        """
        if ctx.TRUE():
            return BooleanLiteral(True)
        else:
            return BooleanLiteral(False)
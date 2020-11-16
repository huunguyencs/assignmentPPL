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
                    vardecl.extend(self.visit(v))
            else:
                vardecl = self.visit(var)
        if ctx.funcdeclare():
            func = ctx.funcdeclare()
            if isinstance(func,list):
                for f in func:
                    funcdecl.extend(self.visit(f))
            else:
                funcdecl = self.visit(func)
        return Program(vardecl + funcdecl)
        
    
    def visitVardeclare(self,ctx:BKITParser.VardeclareContext):
        """
        Visit vardeclare
        vardeclare: VAR CL idlistinit SM;
        """
        return self.visit(ctx.idlistinit())


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
        Visit var with dimension and literal init
        idinit: iddimen (AS lit)?;
        """
        var, dim = self.visit(ctx.iddimen())
        varinit = None
        if ctx.getChildCount() == 3:
            varinit = self.visit(ctx.lit())

        return VarDecl(var,dim,varinit)

    def visitIddimen(self, ctx:BKITParser.IddimenContext):
        """
        Visit var dimension
        iddimen: ID dimension?;
        """
        var = Id(ctx.ID().getText())
        dim = []
        if ctx.getChildCount() == 2:
            dim = self.visit(ctx.dimension())
        return var, dim


    def visitDimension(self,ctx:BKITParser.DimensionContext):
        """
        Visit dimension ([int]) 
        dimension: LR INTLIT RR dimension?;
        """
        if ctx.getChildCount() == 3:
            return [int(ctx.INTLIT().getText(),0)] 
        else:
            return [int(ctx.INTLIT().getText(),0)] + self.visit(ctx.dimension())


    def visitFuncdeclare(self,ctx: BKITParser.FuncdeclareContext):
        """
        Visit function declare
        funcdeclare: FUNCTION CL ID (PARAMETER CL paralist)? body;
        """
        name = Id(ctx.ID().getText())
        param = []
        body = self.visit(ctx.body())

        if ctx.getChildCount() > 4:
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
        if ctx.getChildCount() == 4:
            return vlist, slist
        if ctx.vardeclare():
            var = ctx.vardeclare()
            if isinstance(var,list):
                for v in var:
                    vlist.extend(self.visit(v))
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
                    vlist.extend(self.visit(v))
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
        return self.visitChildren(ctx)

    def visitAssign_stmt(self,ctx:BKITParser.Assign_stmtContext):
        """
        Visit assign statement
        assign_stmt: variable AS exp SM;
        """
        lhs = self.visit(ctx.variable())
        rhs = self.visit(ctx.exp())
        return Assign(lhs,rhs)

    
    # fail ***********************
    def visitIf_stmt(self,ctx:BKITParser.If_stmtContext):
        """
        Visit if statement
        if_stmt: if_part elseif_part* else_part? ENDIF DOT;
        """
        ifthenStmt = []
        elseStmt = ([],[])
        ifthenStmt += [self.visit(ctx.if_part())]
        if ctx.elseif_part():
            elseif_part = ctx.elseif_part()
            if isinstance(elseif_part,list):
                ifthenStmt += [self.visit(e) for e in elseif_part]
            else:
                ifthenStmt += [self.visit(elseif_part)]
        if ctx.else_part():
            elseStmt = self.visit(ctx.else_part())
        return If(ifthenStmt,elseStmt)
        

    def visitIf_part(self,ctx:BKITParser.If_partContext):
        """
        Visit If part in if statement
        if_part: IF exp THEN stmt_list;
        """
        exp = self.visit(ctx.exp())
        stmt_list = ([],[])
        if ctx.stmt_list():
            stmt_list = self.visit(ctx.stmt_list())
        res = ((None, exp) + stmt_list)[1:]
        return res

    def visitElseif_part(self, ctx:BKITParser.Elseif_partContext):
        """
        Visit ElseIf part in if statement
        elseif_part: ELSEIF exp THEN stmt_list;
        """
        exp = self.visit(ctx.exp())
        stmt_list = ([],[])
        if ctx.stmt_list():
            stmt_list = self.visit(ctx.stmt_list())
        res = ((None, exp) + stmt_list)[1:]
        return res

    def visitElse_part(self, ctx:BKITParser.Else_partContext):
        """
        Visit Else part in if statement
        else_part: ELSE stmt_list;
        """
        stmt_list = ([],[])
        if ctx.stmt_list():
            stmt_list = self.visit(ctx.stmt_list())
        return stmt_list

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
        stmtlist = ([],[])
        if ctx.stmt_list():
            stmtlist = self.visit(ctx.stmt_list())
        return While(exp,stmtlist)
    
    def visitDo_stmt(self,ctx:BKITParser.Do_stmtContext):
        """
        Visit do statement
        do_stmt: DO stmt_list WHILE exp ENDDO DOT;
        """
        stmtlist = ([],[])
        if ctx.stmt_list():
            stmtlist = self.visit(ctx.stmt_list())
        exp = self.visit(ctx.exp())
        return Dowhile(stmtlist,exp)

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
        id = Id(ctx.ID().getText())
        param = []
        if ctx.exp():
            exp = ctx.exp()
            if isinstance(exp,list):
                param = [self.visit(e) for e in exp]
            else:
                param = [self.visit(exp)]
        return CallStmt(id,param)

    # fail*******************************
    def visitReturn_stmt(self,ctx:BKITParser.Return_stmtContext):
        """
        Visit return statement
        return_stmt: RETURN exp? SM;
        """
        if ctx.exp():
            expr = self.visit(ctx.exp())
            return Return(expr)
        else:
            return Return(None)

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

        return CallExpr(id,param)

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
        index_op = self.visit(ctx.index_op())
        if ctx.ID():
            id = Id(ctx.ID().getText())
            return ArrayCell(id,index_op)
        else:
            call = self.visit(ctx.call())
            return ArrayCell(call,index_op)

    def visitIndex_op(self, ctx:BKITParser.Index_opContext):
        """
        Visit index operator (index part)
        index_op: LR exp RR index_op?;
        """
        if ctx.getChildCount() == 3:
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
            return IntLiteral(int(ctx.INTLIT().getText(),0))
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
        return self.visitChildren(ctx)

    def visitBoollit(self,ctx:BKITParser.BoollitContext):
        """
        Visit boolean literal
        boollit: TRUE | FALSE;
        """
        if ctx.TRUE():
            return BooleanLiteral(True)
        else:
            return BooleanLiteral(False)

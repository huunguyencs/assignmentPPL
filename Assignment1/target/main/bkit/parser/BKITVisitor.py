# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#vardeclare.
    def visitVardeclare(self, ctx:BKITParser.VardeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#idlistinit.
    def visitIdlistinit(self, ctx:BKITParser.IdlistinitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#idinit.
    def visitIdinit(self, ctx:BKITParser.IdinitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#dimension.
    def visitDimension(self, ctx:BKITParser.DimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#funcdeclare.
    def visitFuncdeclare(self, ctx:BKITParser.FuncdeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#paralist.
    def visitParalist(self, ctx:BKITParser.ParalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#body.
    def visitBody(self, ctx:BKITParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmt_list.
    def visitStmt_list(self, ctx:BKITParser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmt.
    def visitStmt(self, ctx:BKITParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmt_assign.
    def visitStmt_assign(self, ctx:BKITParser.Stmt_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmt_if.
    def visitStmt_if(self, ctx:BKITParser.Stmt_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmt_for.
    def visitStmt_for(self, ctx:BKITParser.Stmt_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_loop_con.
    def visitFor_loop_con(self, ctx:BKITParser.For_loop_conContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmt_while.
    def visitStmt_while(self, ctx:BKITParser.Stmt_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmt_do.
    def visitStmt_do(self, ctx:BKITParser.Stmt_doContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmt_break.
    def visitStmt_break(self, ctx:BKITParser.Stmt_breakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmt_con.
    def visitStmt_con(self, ctx:BKITParser.Stmt_conContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmt_call.
    def visitStmt_call(self, ctx:BKITParser.Stmt_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmt_ret.
    def visitStmt_ret(self, ctx:BKITParser.Stmt_retContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp.
    def visitExp(self, ctx:BKITParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp1.
    def visitExp1(self, ctx:BKITParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp11.
    def visitExp11(self, ctx:BKITParser.Exp11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp12.
    def visitExp12(self, ctx:BKITParser.Exp12Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp2.
    def visitExp2(self, ctx:BKITParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp3.
    def visitExp3(self, ctx:BKITParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp4.
    def visitExp4(self, ctx:BKITParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call.
    def visitCall(self, ctx:BKITParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#operands.
    def visitOperands(self, ctx:BKITParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#variable.
    def visitVariable(self, ctx:BKITParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#ele_exp.
    def visitEle_exp(self, ctx:BKITParser.Ele_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index_op.
    def visitIndex_op(self, ctx:BKITParser.Index_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#relational.
    def visitRelational(self, ctx:BKITParser.RelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#logical.
    def visitLogical(self, ctx:BKITParser.LogicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#adding.
    def visitAdding(self, ctx:BKITParser.AddingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#multiplying.
    def visitMultiplying(self, ctx:BKITParser.MultiplyingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#arraylit.
    def visitArraylit(self, ctx:BKITParser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#primitive.
    def visitPrimitive(self, ctx:BKITParser.PrimitiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#lit.
    def visitLit(self, ctx:BKITParser.LitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#boollit.
    def visitBoollit(self, ctx:BKITParser.BoollitContext):
        return self.visitChildren(ctx)



del BKITParser
# Generated from ./QLANG.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .QLANGParser import QLANGParser
else:
    from QLANGParser import QLANGParser

# This class defines a complete generic visitor for a parse tree produced by QLANGParser.

class QLANGVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by QLANGParser#block.
    def visitBlock(self, ctx:QLANGParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QLANGParser#statement.
    def visitStatement(self, ctx:QLANGParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QLANGParser#smallBlock.
    def visitSmallBlock(self, ctx:QLANGParser.SmallBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QLANGParser#literalValue.
    def visitLiteralValue(self, ctx:QLANGParser.LiteralValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QLANGParser#expression.
    def visitExpression(self, ctx:QLANGParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QLANGParser#declareVariable.
    def visitDeclareVariable(self, ctx:QLANGParser.DeclareVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QLANGParser#defineVariable.
    def visitDefineVariable(self, ctx:QLANGParser.DefineVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QLANGParser#assignVariable.
    def visitAssignVariable(self, ctx:QLANGParser.AssignVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QLANGParser#functionArgument.
    def visitFunctionArgument(self, ctx:QLANGParser.FunctionArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QLANGParser#functionHead.
    def visitFunctionHead(self, ctx:QLANGParser.FunctionHeadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QLANGParser#functionReturn.
    def visitFunctionReturn(self, ctx:QLANGParser.FunctionReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QLANGParser#defineFunction.
    def visitDefineFunction(self, ctx:QLANGParser.DefineFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QLANGParser#functionCall.
    def visitFunctionCall(self, ctx:QLANGParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QLANGParser#ifCondition.
    def visitIfCondition(self, ctx:QLANGParser.IfConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QLANGParser#elifCondition.
    def visitElifCondition(self, ctx:QLANGParser.ElifConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QLANGParser#elseCondition.
    def visitElseCondition(self, ctx:QLANGParser.ElseConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QLANGParser#fullIf.
    def visitFullIf(self, ctx:QLANGParser.FullIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QLANGParser#fullEnumerate.
    def visitFullEnumerate(self, ctx:QLANGParser.FullEnumerateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QLANGParser#caseCondition.
    def visitCaseCondition(self, ctx:QLANGParser.CaseConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QLANGParser#defaultCondition.
    def visitDefaultCondition(self, ctx:QLANGParser.DefaultConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QLANGParser#whileLoop.
    def visitWhileLoop(self, ctx:QLANGParser.WhileLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QLANGParser#defineDecorator.
    def visitDefineDecorator(self, ctx:QLANGParser.DefineDecoratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QLANGParser#callDecorator.
    def visitCallDecorator(self, ctx:QLANGParser.CallDecoratorContext):
        return self.visitChildren(ctx)



del QLANGParser
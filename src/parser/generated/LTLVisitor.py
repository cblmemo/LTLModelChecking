# Generated from LTL.g4 by ANTLR 4.13.0
from antlr4 import *

if "." in __name__:
    from .LTLParser import LTLParser
else:
    from LTLParser import LTLParser

# This class defines a complete generic visitor for a parse tree produced by LTLParser.


class LTLVisitor(ParseTreeVisitor):
    # Visit a parse tree produced by LTLParser#NegationFormula.
    def visitNegationFormula(self, ctx: LTLParser.NegationFormulaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LTLParser#AlwaysFormula.
    def visitAlwaysFormula(self, ctx: LTLParser.AlwaysFormulaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LTLParser#UntilFormula.
    def visitUntilFormula(self, ctx: LTLParser.UntilFormulaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LTLParser#EventuallyFormula.
    def visitEventuallyFormula(self, ctx: LTLParser.EventuallyFormulaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LTLParser#ParenthesisFormula.
    def visitParenthesisFormula(self, ctx: LTLParser.ParenthesisFormulaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LTLParser#AtomicFormula.
    def visitAtomicFormula(self, ctx: LTLParser.AtomicFormulaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LTLParser#DisjunctionFormula.
    def visitDisjunctionFormula(self, ctx: LTLParser.DisjunctionFormulaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LTLParser#ImplicationFormula.
    def visitImplicationFormula(self, ctx: LTLParser.ImplicationFormulaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LTLParser#NextFormula.
    def visitNextFormula(self, ctx: LTLParser.NextFormulaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LTLParser#ConjunctionFormula.
    def visitConjunctionFormula(self, ctx: LTLParser.ConjunctionFormulaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LTLParser#Identifier.
    def visitIdentifier(self, ctx: LTLParser.IdentifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LTLParser#AtomicTrue.
    def visitAtomicTrue(self, ctx: LTLParser.AtomicTrueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LTLParser#AtomicFalse.
    def visitAtomicFalse(self, ctx: LTLParser.AtomicFalseContext):
        return self.visitChildren(ctx)


del LTLParser

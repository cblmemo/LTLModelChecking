# Generated from LTL.g4 by ANTLR 4.13.0
from antlr4 import *

if "." in __name__:
    from .LTLParser import LTLParser
else:
    from LTLParser import LTLParser


# This class defines a complete listener for a parse tree produced by LTLParser.
class LTLListener(ParseTreeListener):
    # Enter a parse tree produced by LTLParser#NegationFormula.
    def enterNegationFormula(self, ctx: LTLParser.NegationFormulaContext):
        pass

    # Exit a parse tree produced by LTLParser#NegationFormula.
    def exitNegationFormula(self, ctx: LTLParser.NegationFormulaContext):
        pass

    # Enter a parse tree produced by LTLParser#AlwaysFormula.
    def enterAlwaysFormula(self, ctx: LTLParser.AlwaysFormulaContext):
        pass

    # Exit a parse tree produced by LTLParser#AlwaysFormula.
    def exitAlwaysFormula(self, ctx: LTLParser.AlwaysFormulaContext):
        pass

    # Enter a parse tree produced by LTLParser#UntilFormula.
    def enterUntilFormula(self, ctx: LTLParser.UntilFormulaContext):
        pass

    # Exit a parse tree produced by LTLParser#UntilFormula.
    def exitUntilFormula(self, ctx: LTLParser.UntilFormulaContext):
        pass

    # Enter a parse tree produced by LTLParser#EventuallyFormula.
    def enterEventuallyFormula(self, ctx: LTLParser.EventuallyFormulaContext):
        pass

    # Exit a parse tree produced by LTLParser#EventuallyFormula.
    def exitEventuallyFormula(self, ctx: LTLParser.EventuallyFormulaContext):
        pass

    # Enter a parse tree produced by LTLParser#ParenthesisFormula.
    def enterParenthesisFormula(self, ctx: LTLParser.ParenthesisFormulaContext):
        pass

    # Exit a parse tree produced by LTLParser#ParenthesisFormula.
    def exitParenthesisFormula(self, ctx: LTLParser.ParenthesisFormulaContext):
        pass

    # Enter a parse tree produced by LTLParser#AtomicFormula.
    def enterAtomicFormula(self, ctx: LTLParser.AtomicFormulaContext):
        pass

    # Exit a parse tree produced by LTLParser#AtomicFormula.
    def exitAtomicFormula(self, ctx: LTLParser.AtomicFormulaContext):
        pass

    # Enter a parse tree produced by LTLParser#DisjunctionFormula.
    def enterDisjunctionFormula(self, ctx: LTLParser.DisjunctionFormulaContext):
        pass

    # Exit a parse tree produced by LTLParser#DisjunctionFormula.
    def exitDisjunctionFormula(self, ctx: LTLParser.DisjunctionFormulaContext):
        pass

    # Enter a parse tree produced by LTLParser#ImplicationFormula.
    def enterImplicationFormula(self, ctx: LTLParser.ImplicationFormulaContext):
        pass

    # Exit a parse tree produced by LTLParser#ImplicationFormula.
    def exitImplicationFormula(self, ctx: LTLParser.ImplicationFormulaContext):
        pass

    # Enter a parse tree produced by LTLParser#NextFormula.
    def enterNextFormula(self, ctx: LTLParser.NextFormulaContext):
        pass

    # Exit a parse tree produced by LTLParser#NextFormula.
    def exitNextFormula(self, ctx: LTLParser.NextFormulaContext):
        pass

    # Enter a parse tree produced by LTLParser#ConjunctionFormula.
    def enterConjunctionFormula(self, ctx: LTLParser.ConjunctionFormulaContext):
        pass

    # Exit a parse tree produced by LTLParser#ConjunctionFormula.
    def exitConjunctionFormula(self, ctx: LTLParser.ConjunctionFormulaContext):
        pass

    # Enter a parse tree produced by LTLParser#Identifier.
    def enterIdentifier(self, ctx: LTLParser.IdentifierContext):
        pass

    # Exit a parse tree produced by LTLParser#Identifier.
    def exitIdentifier(self, ctx: LTLParser.IdentifierContext):
        pass

    # Enter a parse tree produced by LTLParser#AtomicTrue.
    def enterAtomicTrue(self, ctx: LTLParser.AtomicTrueContext):
        pass

    # Exit a parse tree produced by LTLParser#AtomicTrue.
    def exitAtomicTrue(self, ctx: LTLParser.AtomicTrueContext):
        pass

    # Enter a parse tree produced by LTLParser#AtomicFalse.
    def enterAtomicFalse(self, ctx: LTLParser.AtomicFalseContext):
        pass

    # Exit a parse tree produced by LTLParser#AtomicFalse.
    def exitAtomicFalse(self, ctx: LTLParser.AtomicFalseContext):
        pass


del LTLParser

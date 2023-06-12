from .generated import LTLVisitor
from .generated import LTLParser
from LTLComponent import Base as LTLBase
import LTLComponent

from utils import getNegation


class LTLEvalVisitor(LTLVisitor):
    """Transform Antlr parse tree into LTLComponent tree.

    This class also provides some transformation of LTL formulae. All transformation
    is done in-place.

    Supported transformations:
      - G(f) ==> !(true U !f)
      - F(f) ==> true U f
      - f0 \/ f1 ==> !( !f0 /\ !f1 )
      - f0 -> f1 <==> !(f0 /\ !f1)
    """

    def visitNegationFormula(self, ctx: LTLParser.NegationFormulaContext) -> LTLBase:
        f: LTLBase = self.visit(ctx.formula())
        return getNegation(f)

    def visitAlwaysFormula(self, ctx: LTLParser.AlwaysFormulaContext) -> LTLBase:
        f: LTLBase = self.visit(ctx.formula())
        # G(f) ==> !(true U !f)
        return getNegation(
            LTLComponent.Until(LTLComponent.Atomic.AtomicTrue(), getNegation(f))
        )

    def visitUntilFormula(self, ctx: LTLParser.UntilFormulaContext) -> LTLBase:
        f0: LTLBase = self.visit(ctx.formula(0))
        f1: LTLBase = self.visit(ctx.formula(1))
        return LTLComponent.Until(f0, f1)

    def visitEventuallyFormula(
        self, ctx: LTLParser.EventuallyFormulaContext
    ) -> LTLBase:
        f: LTLBase = self.visit(ctx.formula())
        # F(f) ==> true U f
        return LTLComponent.Until(LTLComponent.Atomic.AtomicTrue(), f)

    def visitParenthesisFormula(
        self, ctx: LTLParser.ParenthesisFormulaContext
    ) -> LTLBase:
        return self.visit(ctx.formula())

    def visitAtomicFormula(self, ctx: LTLParser.AtomicFormulaContext) -> LTLBase:
        return self.visit(ctx.atomic())

    def visitDisjunctionFormula(
        self, ctx: LTLParser.DisjunctionFormulaContext
    ) -> LTLBase:
        f0: LTLBase = self.visit(ctx.formula(0))
        f1: LTLBase = self.visit(ctx.formula(1))
        # f0 \/ f1 ==> !( !f0 /\ !f1 )
        return getNegation(LTLComponent.Conjunction(getNegation(f0), getNegation(f1)))

    def visitImplicationFormula(
        self, ctx: LTLParser.ImplicationFormulaContext
    ) -> LTLBase:
        f0: LTLBase = self.visit(ctx.formula(0))
        f1: LTLBase = self.visit(ctx.formula(1))
        # f0 -> f1 <==> !(f0 /\ !f1)
        return getNegation(LTLComponent.Conjunction(f0, getNegation(f1)))

    def visitNextFormula(self, ctx: LTLParser.NextFormulaContext) -> LTLBase:
        f = self.visit(ctx.formula())
        return LTLComponent.Next(f)

    def visitConjunctionFormula(
        self, ctx: LTLParser.ConjunctionFormulaContext
    ) -> LTLBase:
        f0: LTLBase = self.visit(ctx.formula(0))
        f1: LTLBase = self.visit(ctx.formula(1))
        return LTLComponent.Conjunction(f0, f1)

    def visitIdentifier(self, ctx: LTLParser.IdentifierContext) -> LTLBase:
        return LTLComponent.Atomic.Identifier(ctx.getText())

    def visitAtomicTrue(self, ctx: LTLParser.AtomicTrueContext) -> LTLBase:
        return LTLComponent.Atomic.AtomicTrue()

    def visitAtomicFalse(self, ctx: LTLParser.AtomicFalseContext) -> LTLBase:
        return LTLComponent.Atomic.AtomicFalse()

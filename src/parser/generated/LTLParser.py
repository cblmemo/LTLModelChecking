# Generated from LTL.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys

if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,
        1,
        14,
        43,
        2,
        0,
        7,
        0,
        2,
        1,
        7,
        1,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        3,
        0,
        19,
        8,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        5,
        0,
        33,
        8,
        0,
        10,
        0,
        12,
        0,
        36,
        9,
        0,
        1,
        1,
        1,
        1,
        1,
        1,
        3,
        1,
        41,
        8,
        1,
        1,
        1,
        0,
        1,
        0,
        2,
        0,
        2,
        0,
        0,
        51,
        0,
        18,
        1,
        0,
        0,
        0,
        2,
        40,
        1,
        0,
        0,
        0,
        4,
        5,
        6,
        0,
        -1,
        0,
        5,
        6,
        5,
        3,
        0,
        0,
        6,
        19,
        3,
        0,
        0,
        10,
        7,
        8,
        5,
        7,
        0,
        0,
        8,
        19,
        3,
        0,
        0,
        6,
        9,
        10,
        5,
        8,
        0,
        0,
        10,
        19,
        3,
        0,
        0,
        5,
        11,
        12,
        5,
        9,
        0,
        0,
        12,
        19,
        3,
        0,
        0,
        4,
        13,
        14,
        5,
        1,
        0,
        0,
        14,
        15,
        3,
        0,
        0,
        0,
        15,
        16,
        5,
        2,
        0,
        0,
        16,
        19,
        1,
        0,
        0,
        0,
        17,
        19,
        3,
        2,
        1,
        0,
        18,
        4,
        1,
        0,
        0,
        0,
        18,
        7,
        1,
        0,
        0,
        0,
        18,
        9,
        1,
        0,
        0,
        0,
        18,
        11,
        1,
        0,
        0,
        0,
        18,
        13,
        1,
        0,
        0,
        0,
        18,
        17,
        1,
        0,
        0,
        0,
        19,
        34,
        1,
        0,
        0,
        0,
        20,
        21,
        10,
        9,
        0,
        0,
        21,
        22,
        5,
        4,
        0,
        0,
        22,
        33,
        3,
        0,
        0,
        10,
        23,
        24,
        10,
        8,
        0,
        0,
        24,
        25,
        5,
        5,
        0,
        0,
        25,
        33,
        3,
        0,
        0,
        9,
        26,
        27,
        10,
        7,
        0,
        0,
        27,
        28,
        5,
        6,
        0,
        0,
        28,
        33,
        3,
        0,
        0,
        8,
        29,
        30,
        10,
        3,
        0,
        0,
        30,
        31,
        5,
        10,
        0,
        0,
        31,
        33,
        3,
        0,
        0,
        4,
        32,
        20,
        1,
        0,
        0,
        0,
        32,
        23,
        1,
        0,
        0,
        0,
        32,
        26,
        1,
        0,
        0,
        0,
        32,
        29,
        1,
        0,
        0,
        0,
        33,
        36,
        1,
        0,
        0,
        0,
        34,
        32,
        1,
        0,
        0,
        0,
        34,
        35,
        1,
        0,
        0,
        0,
        35,
        1,
        1,
        0,
        0,
        0,
        36,
        34,
        1,
        0,
        0,
        0,
        37,
        41,
        5,
        13,
        0,
        0,
        38,
        41,
        5,
        11,
        0,
        0,
        39,
        41,
        5,
        12,
        0,
        0,
        40,
        37,
        1,
        0,
        0,
        0,
        40,
        38,
        1,
        0,
        0,
        0,
        40,
        39,
        1,
        0,
        0,
        0,
        41,
        3,
        1,
        0,
        0,
        0,
        4,
        18,
        32,
        34,
        40,
    ]


class LTLParser(Parser):
    grammarFileName = "LTL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = [
        "<INVALID>",
        "'('",
        "')'",
        "'!'",
        "'/\\'",
        "'\\/'",
        "'->'",
        "'X'",
        "'G'",
        "'F'",
        "'U'",
        "'true'",
        "'false'",
    ]

    symbolicNames = [
        "<INVALID>",
        "LPAREN",
        "RPAREN",
        "NEGATION",
        "CONJUNCTION",
        "DISJUNCTION",
        "IMPLICATION",
        "NEXT",
        "ALWAYS",
        "EVENTUALLY",
        "UNTIL",
        "TRUE",
        "FALSE",
        "IDENTIFIER",
        "WS",
    ]

    RULE_formula = 0
    RULE_atomic = 1

    ruleNames = ["formula", "atomic"]

    EOF = Token.EOF
    LPAREN = 1
    RPAREN = 2
    NEGATION = 3
    CONJUNCTION = 4
    DISJUNCTION = 5
    IMPLICATION = 6
    NEXT = 7
    ALWAYS = 8
    EVENTUALLY = 9
    UNTIL = 10
    TRUE = 11
    FALSE = 12
    IDENTIFIER = 13
    WS = 14

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(
            self, self.atn, self.decisionsToDFA, self.sharedContextCache
        )
        self._predicates = None

    class FormulaContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return LTLParser.RULE_formula

        def copyFrom(self, ctx: ParserRuleContext):
            super().copyFrom(ctx)

    class NegationFormulaContext(FormulaContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a LTLParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEGATION(self):
            return self.getToken(LTLParser.NEGATION, 0)

        def formula(self):
            return self.getTypedRuleContext(LTLParser.FormulaContext, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterNegationFormula"):
                listener.enterNegationFormula(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitNegationFormula"):
                listener.exitNegationFormula(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitNegationFormula"):
                return visitor.visitNegationFormula(self)
            else:
                return visitor.visitChildren(self)

    class AlwaysFormulaContext(FormulaContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a LTLParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ALWAYS(self):
            return self.getToken(LTLParser.ALWAYS, 0)

        def formula(self):
            return self.getTypedRuleContext(LTLParser.FormulaContext, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAlwaysFormula"):
                listener.enterAlwaysFormula(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAlwaysFormula"):
                listener.exitAlwaysFormula(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAlwaysFormula"):
                return visitor.visitAlwaysFormula(self)
            else:
                return visitor.visitChildren(self)

    class UntilFormulaContext(FormulaContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a LTLParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(LTLParser.FormulaContext)
            else:
                return self.getTypedRuleContext(LTLParser.FormulaContext, i)

        def UNTIL(self):
            return self.getToken(LTLParser.UNTIL, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterUntilFormula"):
                listener.enterUntilFormula(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitUntilFormula"):
                listener.exitUntilFormula(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitUntilFormula"):
                return visitor.visitUntilFormula(self)
            else:
                return visitor.visitChildren(self)

    class EventuallyFormulaContext(FormulaContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a LTLParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EVENTUALLY(self):
            return self.getToken(LTLParser.EVENTUALLY, 0)

        def formula(self):
            return self.getTypedRuleContext(LTLParser.FormulaContext, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterEventuallyFormula"):
                listener.enterEventuallyFormula(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitEventuallyFormula"):
                listener.exitEventuallyFormula(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitEventuallyFormula"):
                return visitor.visitEventuallyFormula(self)
            else:
                return visitor.visitChildren(self)

    class ParenthesisFormulaContext(FormulaContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a LTLParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(LTLParser.LPAREN, 0)

        def formula(self):
            return self.getTypedRuleContext(LTLParser.FormulaContext, 0)

        def RPAREN(self):
            return self.getToken(LTLParser.RPAREN, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterParenthesisFormula"):
                listener.enterParenthesisFormula(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitParenthesisFormula"):
                listener.exitParenthesisFormula(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitParenthesisFormula"):
                return visitor.visitParenthesisFormula(self)
            else:
                return visitor.visitChildren(self)

    class AtomicFormulaContext(FormulaContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a LTLParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atomic(self):
            return self.getTypedRuleContext(LTLParser.AtomicContext, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAtomicFormula"):
                listener.enterAtomicFormula(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAtomicFormula"):
                listener.exitAtomicFormula(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAtomicFormula"):
                return visitor.visitAtomicFormula(self)
            else:
                return visitor.visitChildren(self)

    class DisjunctionFormulaContext(FormulaContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a LTLParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(LTLParser.FormulaContext)
            else:
                return self.getTypedRuleContext(LTLParser.FormulaContext, i)

        def DISJUNCTION(self):
            return self.getToken(LTLParser.DISJUNCTION, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterDisjunctionFormula"):
                listener.enterDisjunctionFormula(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitDisjunctionFormula"):
                listener.exitDisjunctionFormula(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitDisjunctionFormula"):
                return visitor.visitDisjunctionFormula(self)
            else:
                return visitor.visitChildren(self)

    class ImplicationFormulaContext(FormulaContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a LTLParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(LTLParser.FormulaContext)
            else:
                return self.getTypedRuleContext(LTLParser.FormulaContext, i)

        def IMPLICATION(self):
            return self.getToken(LTLParser.IMPLICATION, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterImplicationFormula"):
                listener.enterImplicationFormula(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitImplicationFormula"):
                listener.exitImplicationFormula(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitImplicationFormula"):
                return visitor.visitImplicationFormula(self)
            else:
                return visitor.visitChildren(self)

    class NextFormulaContext(FormulaContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a LTLParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEXT(self):
            return self.getToken(LTLParser.NEXT, 0)

        def formula(self):
            return self.getTypedRuleContext(LTLParser.FormulaContext, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterNextFormula"):
                listener.enterNextFormula(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitNextFormula"):
                listener.exitNextFormula(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitNextFormula"):
                return visitor.visitNextFormula(self)
            else:
                return visitor.visitChildren(self)

    class ConjunctionFormulaContext(FormulaContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a LTLParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(LTLParser.FormulaContext)
            else:
                return self.getTypedRuleContext(LTLParser.FormulaContext, i)

        def CONJUNCTION(self):
            return self.getToken(LTLParser.CONJUNCTION, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterConjunctionFormula"):
                listener.enterConjunctionFormula(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitConjunctionFormula"):
                listener.exitConjunctionFormula(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitConjunctionFormula"):
                return visitor.visitConjunctionFormula(self)
            else:
                return visitor.visitChildren(self)

    def formula(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LTLParser.FormulaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_formula, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                localctx = LTLParser.NegationFormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 5
                self.match(LTLParser.NEGATION)
                self.state = 6
                self.formula(10)
                pass
            elif token in [7]:
                localctx = LTLParser.NextFormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 7
                self.match(LTLParser.NEXT)
                self.state = 8
                self.formula(6)
                pass
            elif token in [8]:
                localctx = LTLParser.AlwaysFormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 9
                self.match(LTLParser.ALWAYS)
                self.state = 10
                self.formula(5)
                pass
            elif token in [9]:
                localctx = LTLParser.EventuallyFormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 11
                self.match(LTLParser.EVENTUALLY)
                self.state = 12
                self.formula(4)
                pass
            elif token in [1]:
                localctx = LTLParser.ParenthesisFormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 13
                self.match(LTLParser.LPAREN)
                self.state = 14
                self.formula(0)
                self.state = 15
                self.match(LTLParser.RPAREN)
                pass
            elif token in [11, 12, 13]:
                localctx = LTLParser.AtomicFormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 17
                self.atomic()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 34
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 2, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 32
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input, 1, self._ctx)
                    if la_ == 1:
                        localctx = LTLParser.ConjunctionFormulaContext(
                            self,
                            LTLParser.FormulaContext(self, _parentctx, _parentState),
                        )
                        self.pushNewRecursionContext(
                            localctx, _startState, self.RULE_formula
                        )
                        self.state = 20
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException

                            raise FailedPredicateException(
                                self, "self.precpred(self._ctx, 9)"
                            )
                        self.state = 21
                        self.match(LTLParser.CONJUNCTION)
                        self.state = 22
                        self.formula(10)
                        pass

                    elif la_ == 2:
                        localctx = LTLParser.DisjunctionFormulaContext(
                            self,
                            LTLParser.FormulaContext(self, _parentctx, _parentState),
                        )
                        self.pushNewRecursionContext(
                            localctx, _startState, self.RULE_formula
                        )
                        self.state = 23
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException

                            raise FailedPredicateException(
                                self, "self.precpred(self._ctx, 8)"
                            )
                        self.state = 24
                        self.match(LTLParser.DISJUNCTION)
                        self.state = 25
                        self.formula(9)
                        pass

                    elif la_ == 3:
                        localctx = LTLParser.ImplicationFormulaContext(
                            self,
                            LTLParser.FormulaContext(self, _parentctx, _parentState),
                        )
                        self.pushNewRecursionContext(
                            localctx, _startState, self.RULE_formula
                        )
                        self.state = 26
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException

                            raise FailedPredicateException(
                                self, "self.precpred(self._ctx, 7)"
                            )
                        self.state = 27
                        self.match(LTLParser.IMPLICATION)
                        self.state = 28
                        self.formula(8)
                        pass

                    elif la_ == 4:
                        localctx = LTLParser.UntilFormulaContext(
                            self,
                            LTLParser.FormulaContext(self, _parentctx, _parentState),
                        )
                        self.pushNewRecursionContext(
                            localctx, _startState, self.RULE_formula
                        )
                        self.state = 29
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException

                            raise FailedPredicateException(
                                self, "self.precpred(self._ctx, 3)"
                            )
                        self.state = 30
                        self.match(LTLParser.UNTIL)
                        self.state = 31
                        self.formula(4)
                        pass

                self.state = 36
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 2, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class AtomicContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return LTLParser.RULE_atomic

        def copyFrom(self, ctx: ParserRuleContext):
            super().copyFrom(ctx)

    class AtomicTrueContext(AtomicContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a LTLParser.AtomicContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(LTLParser.TRUE, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAtomicTrue"):
                listener.enterAtomicTrue(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAtomicTrue"):
                listener.exitAtomicTrue(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAtomicTrue"):
                return visitor.visitAtomicTrue(self)
            else:
                return visitor.visitChildren(self)

    class IdentifierContext(AtomicContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a LTLParser.AtomicContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(LTLParser.IDENTIFIER, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterIdentifier"):
                listener.enterIdentifier(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitIdentifier"):
                listener.exitIdentifier(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitIdentifier"):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)

    class AtomicFalseContext(AtomicContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a LTLParser.AtomicContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FALSE(self):
            return self.getToken(LTLParser.FALSE, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAtomicFalse"):
                listener.enterAtomicFalse(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAtomicFalse"):
                listener.exitAtomicFalse(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAtomicFalse"):
                return visitor.visitAtomicFalse(self)
            else:
                return visitor.visitChildren(self)

    def atomic(self):
        localctx = LTLParser.AtomicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_atomic)
        try:
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                localctx = LTLParser.IdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.match(LTLParser.IDENTIFIER)
                pass
            elif token in [11]:
                localctx = LTLParser.AtomicTrueContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.match(LTLParser.TRUE)
                pass
            elif token in [12]:
                localctx = LTLParser.AtomicFalseContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.match(LTLParser.FALSE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    def sempred(self, localctx: RuleContext, ruleIndex: int, predIndex: int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.formula_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def formula_sempred(self, localctx: FormulaContext, predIndex: int):
        if predIndex == 0:
            return self.precpred(self._ctx, 9)

        if predIndex == 1:
            return self.precpred(self._ctx, 8)

        if predIndex == 2:
            return self.precpred(self._ctx, 7)

        if predIndex == 3:
            return self.precpred(self._ctx, 3)

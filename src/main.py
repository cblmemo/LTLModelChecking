import sys
from typing import IO

from TS import TransitionSystem
from LTLComponent import Base as LTLBase
from Automata import GNBA, NBA
from utils import getNegation
import constants


logf: IO


def antlrPreprocess(ltl: str) -> LTLBase:
    from antlr4 import InputStream, CommonTokenStream
    from parser.generated import LTLLexer
    from parser.generated import LTLParser
    from parser import LTLEvalVisitor

    input_stream = InputStream(ltl)
    lexer = LTLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LTLParser(stream)
    tree = parser.formula()

    visitor = LTLEvalVisitor()
    return visitor.visit(tree)


def check(ts: TransitionSystem, ltl: str) -> bool:
    """Checks whether the given LTL formula is satisfied by the transition system.

    Returns:
        True if the LTL formula is satisfied by the transition system, False otherwise.
    """
    root: LTLBase = antlrPreprocess(ltl)
    print("Transformed LTL:", root, file=logf)
    neg_root = getNegation(root)
    gnba: GNBA = GNBA(neg_root)
    print(gnba, file=logf)
    nba: NBA = NBA(gnba)
    print(nba, file=logf)
    product_ts: TransitionSystem = TransitionSystem(ts, nba)
    print(product_ts, file=logf)
    return int(product_ts.persistenceChecking())


def main():
    ts = TransitionSystem(constants._TS_FILE_PATH)
    print(ts, file=logf)
    with open(constants._LTL_FILE_PATH, "r") as f:
        A, B = map(int, next(f).strip().split())
        for _ in range(A):
            ltl = next(f).strip()
            print(f"Checking A LTL: {ltl}", file=logf)
            print(check(ts, ltl))
        for _ in range(B):
            state, ltl = next(f).strip().split(" ", 1)
            print(f"Checking B LTL (state={state}): {ltl}", file=logf)
            ts.setInitState(state)
            print(check(ts, ltl))
        assert next(f, None) is None


if __name__ == "__main__":
    logf = open(constants._LOG_FILE_PATH, "w")
    main()
    logf.close()

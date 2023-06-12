from itertools import chain, combinations

from LTLComponent import Base as LTLBase
import LTLComponent


def powerset(iterable):
    """powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)

    This function is borrowed from https://docs.python.org/3/library/itertools.html#itertools-recipes.
    """
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def getNegation(f: LTLBase) -> LTLBase:
    if isinstance(f, LTLComponent.Negation):
        return f.getChildren()[0]
    return LTLComponent.Negation(f)

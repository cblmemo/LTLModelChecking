import typing
from typing import Union, Set

from TS import Proposition
from LTLComponent.Atomic import Identifier

if typing.TYPE_CHECKING:
    from .APSubset import APSubset


class Symbol:
    def __init__(self, subset: "APSubset"):
        self.subset = subset

    def __repr__(self) -> str:
        return str(sorted([str(s) for s in self.subset.subset]))

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

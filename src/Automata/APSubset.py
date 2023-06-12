from LTLComponent import Base as LTLBase
from .Symbol import Symbol
from typing import Set, Dict

set2symbol: Dict[str, Symbol] = dict()


class APSubset:
    def __init__(self, subset: Set[LTLBase]):
        self.subset = subset

    def setCorrespondingSymbol(self, symbol: Symbol):
        set2symbol[str(sorted(list(self.subset)))] = symbol

    def getCorrespondingSymbol(self) -> Symbol:
        key = str(sorted(list(self.subset)))
        if key not in set2symbol:
            set2symbol[key] = Symbol(self)
        return set2symbol[key]

    def __repr__(self) -> str:
        if not self.subset:
            return "{}"
        return str(self.subset)

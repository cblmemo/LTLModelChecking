from .State import State
from LTLComponent import Base as LTLBase
from typing import Set, Optional
from utils import getNegation
import LTLComponent


class ElementarySet:
    def __init__(self, B: Set[LTLBase]):
        self.B: Set[LTLBase] = B
        self.corresponding_state: Optional[State] = None

    def setCorrespondingState(self, state: State) -> None:
        assert self.corresponding_state is None
        self.corresponding_state = state

    def getCorrespondingState(self) -> State:
        assert self.corresponding_state is not None
        return self.corresponding_state

    def valid(self, closure: Set[LTLBase], has_true_in_closure: bool) -> bool:
        if has_true_in_closure and not (LTLComponent.Atomic.AtomicTrue() in self.B):
            return False
        for e in closure:
            if (e in self.B) == (getNegation(e) in self.B):
                return False
            if isinstance(e, LTLComponent.Conjunction):
                if not ((e in self.B) == all([c in self.B for c in e.getChildren()])):
                    return False
            elif isinstance(e, LTLComponent.Until):
                p1, p2 = e.getChildren()
                if p2 in self.B:
                    if e not in self.B:
                        return False
                if e in self.B and p2 not in self.B:
                    if p1 not in self.B:
                        return False
        return True

    def getAllAPs(self, APs: Set[LTLBase]) -> Set[LTLBase]:
        return self.B.intersection(APs)

    def __contains__(self, e: LTLBase) -> bool:
        return e in self.B

    def __repr__(self) -> str:
        if not self.B:
            return "{}"
        return str(self.B)

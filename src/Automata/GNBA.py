from typing import Set, Dict, List, Set

import LTLComponent
from LTLComponent import Base as LTLBase
from .BaseNBA import BaseNBA
from .Symbol import Symbol
from .State import State
from .ElementarySet import ElementarySet
from .APSubset import APSubset
from utils import powerset


class GNBA(BaseNBA):
    def __init__(self, phi: LTLBase):
        super(GNBA, self).__init__()
        self.final_state_families: List[Set[State]] = []
        self.buildAutomaton(phi)

    def addFinalStateFamily(self, family: Set[State]) -> None:
        self.final_state_families.append(family)

    def buildAutomaton(self, phi: LTLBase) -> None:
        """Build GNBA from LTL formula phi"""
        # collect elementary sets
        elementary_sets: Set[ElementarySet] = set()
        closure: Set[LTLBase] = phi.getClosure()
        has_true_in_closure = LTLComponent.Atomic.AtomicTrue() in closure
        for tuple_b in powerset(closure):
            set_b = set(tuple_b)
            B = ElementarySet(set_b)
            if B.valid(closure, has_true_in_closure):
                elementary_sets.add(B)

        # states
        State.resetCnt()
        for B in elementary_sets:
            state: State = State(str(B))
            B.setCorrespondingState(state)
            super(GNBA, self).addState(state)
            if phi in B:
                super(GNBA, self).addInitialState(state)

        # alphabet
        self.atomic_propositions = phi.getAllIdentifiers()
        for tuple_subset in powerset(self.atomic_propositions):
            subset = set(tuple_subset)
            apSubset = APSubset(subset)
            symbol = Symbol(apSubset)
            apSubset.setCorrespondingSymbol(symbol)
            super(GNBA, self).addSymbol(symbol)

        # delta
        def judgeValidDelta(
            B: ElementarySet, Bp: ElementarySet, symbol: Symbol
        ) -> bool:
            for psi in closure:
                if isinstance(psi, LTLComponent.Next):
                    p = psi.getChildren()[0]
                    if (psi in B) != (p in Bp):
                        return False
                if isinstance(psi, LTLComponent.Until):
                    p1, p2 = psi.getChildren()
                    if (psi in B) != ((p2 in B) or ((p1 in B) and (psi in Bp))):
                        return False
            return True

        for B in elementary_sets:
            A = B.getAllAPs(self.atomic_propositions)
            A = APSubset(A)
            symbol = A.getCorrespondingSymbol()
            st = B.getCorrespondingState()
            for Bp in elementary_sets:
                ed = Bp.getCorrespondingState()
                if judgeValidDelta(B, Bp, symbol):
                    super(GNBA, self).updateDelta(st, ed, symbol)

        # final state families
        for psi in filter(lambda p: isinstance(p, LTLComponent.Until), closure):
            p2 = psi.getChildren()[1]
            self.addFinalStateFamily(
                {
                    B.getCorrespondingState()
                    for B in elementary_sets
                    if (psi not in B) or (p2 in B)
                }
            )
        if len(self.final_state_families) == 0:
            self.addFinalStateFamily(
                {B.getCorrespondingState() for B in elementary_sets}
            )

    def __repr__(self) -> str:
        ret = "GNBA:\n"
        ret += super(GNBA, self).__repr__()
        ret += "\tFinal state families:\n"
        for family in self.final_state_families:
            ret += f"\t\t{family}\n"
        return ret[:-1]

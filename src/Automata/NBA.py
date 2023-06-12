import collections
from typing import Set, Dict

from TS import Proposition
from LTLComponent.Atomic import Identifier
from .BaseNBA import BaseNBA
from .GNBA import GNBA
from .State import State
from .Symbol import Symbol


class NBA(BaseNBA):
    def __init__(self, gnba: GNBA):
        super(NBA, self).__init__()
        self.final_state_family: Set[State] = set()
        self.buildAutomaton(gnba)

    def buildAutomaton(self, gnba: GNBA) -> None:
        """Build NBA from GNBA"""
        k = len(gnba.final_state_families)
        self.atomic_propositions = gnba.atomic_propositions
        # GNBA state + index --> NBA state
        state_map: Dict[State, Dict[int, State]] = collections.defaultdict(dict)

        # states
        State.resetCnt()
        for s in gnba.states:
            for i in range(k):
                state = State(f"[{s}-{i}]")
                super(NBA, self).addState(state)
                if i == 0 and s in gnba.initial_states:
                    super(NBA, self).addInitialState(state)
                state_map[s][i] = state

        # alphabet
        self.alphabet = gnba.alphabet

        # delta
        for s in gnba.states:
            for i in range(k):
                st = state_map[s][i]
                ed_idx = (i + 1) % k if s in gnba.final_state_families[i] else i
                for s0, states in gnba.delta[s].items():
                    for sp in states:
                        ed = state_map[sp][ed_idx]
                        super(NBA, self).updateDelta(st, ed, s0)

        # final state family
        for s in gnba.final_state_families[0]:
            self.final_state_family.add(state_map[s][0])

    def __repr__(self) -> str:
        ret = "NBA:\n"
        ret += super(NBA, self).__repr__()
        ret += "\tFinal State Family:\n"
        ret += f"\t\t{self.final_state_family}\n"
        return ret[:-1]

    def getEds(self, st: State, L: Set[Proposition]) -> Set[State]:
        from .APSubset import APSubset

        ap_subset = APSubset(
            {Identifier(p.name_hint) for p in L}.intersection(self.atomic_propositions)
        )
        symbol = ap_subset.getCorrespondingSymbol()
        for s in self.alphabet:
            if s == symbol:
                return self.delta[st][s]
        return self.delta[st][symbol]

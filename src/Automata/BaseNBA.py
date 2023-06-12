import collections
from typing import List, Dict, Set

from .State import State
from .Symbol import Symbol


class BaseNBA:
    def __init__(self):
        self.states: List[State] = []
        self.initial_states: List[State] = []
        self.alphabet: List[Symbol] = []
        self.delta: Dict[State, Dict[Symbol, Set[State]]] = collections.defaultdict(
            lambda: collections.defaultdict(list)
        )
        self.atomic_propositions: Set[LTLBase] = set()

    def addState(self, state: State) -> None:
        self.states.append(state)

    def addInitialState(self, state: State) -> None:
        self.initial_states.append(state)

    def addSymbol(self, symbol: Symbol) -> None:
        self.alphabet.append(symbol)

    def updateDelta(self, st: State, ed: State, symbol: Symbol) -> None:
        self.delta[st][symbol].append(ed)

    def __repr__(self) -> str:
        ret = "\tStates:\n"
        State.print_detail = True
        for state in self.states:
            ret += f"\t\t{state}" + (
                "\n" if state not in self.initial_states else " (initial)\n"
            )
        State.print_detail = False
        ret += "\tAlphabet:\n"
        for symbol in self.alphabet:
            ret += f"\t\t{symbol}\n"
        ret += "\tDelta:\n"
        for st, v in self.delta.items():
            for symbol, ed in v.items():
                ret += f"\t\t{st} -{symbol}-> {ed}\n"
        return ret

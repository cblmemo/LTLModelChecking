from typing import List, Optional, Dict, Set
import collections
import random

from Automata import NBA, State
from .TSState import TSState
from .Action import Action
from .Proposition import Proposition
import Automata


class TransitionSystem:
    def initializeVariables(self):
        self.S: int = 0
        self.T: int = 0
        self.states: List[TSState] = []
        self.initial_states: List[TSState] = []
        self.actions: Dict[int, Action] = dict()
        self.atomic_propositions: Dict[int, Proposition] = dict()
        self.transitions: Dict[
            TSState, Dict[TSState, Set[Action]]
        ] = collections.defaultdict(lambda: collections.defaultdict(set))
        self.L: Dict[TSState, Set[Proposition]] = collections.defaultdict(set)
        self.accepting_states: Set[TSState] = set()

    def __init__(self, v0, v1=None):
        self.initializeVariables()
        if v1 is None:
            self.initFromFile(v0)
        else:
            self.initFromProduct(v0, v1)

    def initFromFile(self, filename: str) -> None:
        with open(filename, "r") as f:

            def readAndSplit(expected: Optional[int] = None) -> List[str]:
                raw_text = f.readline().strip()
                ret = raw_text.split()
                if expected is not None and len(ret) != expected:
                    raise ValueError(f"Expected {expected} items, got {len(ret)}")
                return ret

            self.S, self.T = map(int, readAndSplit(expected=2))

            for i in range(self.S):
                self.states.append(TSState(f"s{i}"))

            for ist in readAndSplit():
                self.initial_states.append(self.states[int(ist)])

            for i in readAndSplit():
                self.actions[int(i)] = Action(f"a{i}")

            for i, prop in enumerate(readAndSplit()):
                self.atomic_propositions[i] = Proposition(prop)

            for _ in range(self.T):
                st, act, ed = readAndSplit(expected=3)
                self.transitions[self.states[int(st)]][self.states[int(ed)]].add(
                    self.actions[int(act)]
                )

            for i in range(self.S):
                for s in map(int, readAndSplit()):
                    assert s in self.atomic_propositions
                    self.L[self.states[i]].add(self.atomic_propositions[s])

    def initFromProduct(self, ts: "TransitionSystem", nba: NBA) -> None:
        prop_map: Dict[State, Proposition] = dict()
        for i, q in enumerate(nba.states):
            prop = Proposition(f"p{q}")
            prop_map[q] = prop
            self.atomic_propositions[i] = prop

        state_map: Dict[TSState, Dict[State, TSState]] = collections.defaultdict(dict)
        for s in ts.states:
            for q in nba.states:
                state = TSState(f"<{s}, {q}>")
                self.states.append(state)
                state_map[s][q] = state
                self.L[state].add(prop_map[q])
                if q in nba.final_state_family:
                    self.accepting_states.add(state)
                if s in ts.initial_states:
                    for q0 in filter(lambda p: p in nba.initial_states, nba.states):
                        ed = nba.getEds(q0, ts.L[s])
                        if q in ed:
                            self.initial_states.append(state)
                            break

        self.actions = ts.actions

        for s in ts.states:
            for t, acts in ts.transitions[s].items():
                for q in nba.states:
                    st = state_map[s][q]
                    eds = nba.getEds(q, ts.L[t])
                    for p in eds:
                        ed = state_map[t][p]
                        for act in acts:
                            self.transitions[st][ed].add(act)

    def __repr__(self) -> str:
        ret = "Transition System:\n"
        ret += "\tStates:\n"
        for state in self.states:
            ret += f"\t\t{state}" + (
                "\n" if state not in self.initial_states else " (initial)\n"
            )
        ret += "\tActions:\n"
        for i, act in self.actions.items():
            ret += f"\t\ta{i}: {act}\n"
        ret += "\tAtomic Propositions:\n"
        for i, prop in enumerate(self.atomic_propositions.values()):
            ret += f"\t\tap{i}: {prop}\n"
        ret += "\tTransitions:\n"
        for st, ed_act in self.transitions.items():
            for ed, acts in ed_act.items():
                ret += f"\t\t{st} -{acts}-> {ed}\n"
        ret += "\tLabels:\n"
        for state, props in self.L.items():
            ret += f"\t\t{state}: {props}\n"
        ret += "\tAccepting States:\n"
        for state in self.accepting_states:
            ret += f"\t\t{state}\n"
        return ret[:-1]

    def setInitState(self, state: str) -> None:
        self.initial_states = [self.states[int(state)]]

    def cycleCheck(self, s: TSState) -> bool:
        cycle_found = False
        self.V.append(s)
        self.T.add(s)

        while True:
            s1 = self.V[-1]
            if s1 in self.transitions and s in self.transitions[s1]:
                cycle_found = True
                self.V.append(s)
            else:
                if s1 in self.transitions:
                    p = set(self.transitions[s1].keys())
                    p -= self.T
                    if p:
                        s2 = random.choice(list(p))
                        self.V.append(s2)
                        self.T.add(s2)
                    else:
                        self.V.pop()
                else:
                    self.V.pop()
            if not self.V or cycle_found:
                break

        return cycle_found

    def reachableCycle(self, s: TSState) -> None:
        self.U.append(s)
        self.R.add(s)

        while True:
            s1 = self.U[-1]
            if s1 in self.transitions:
                p = set(self.transitions[s1].keys())
                p -= self.R
                if p:
                    s2 = random.choice(list(p))
                    self.U.append(s2)
                    self.R.add(s2)
                else:
                    self.U.pop()
                    if s1 in self.accepting_states:
                        self.cycle_found = self.cycleCheck(s1)
            else:
                self.U.pop()
                if s1 in self.accepting_states:
                    self.cycle_found = self.cycleCheck(s1)
            if not self.U or self.cycle_found:
                break

    def persistenceChecking(self) -> bool:
        self.R = set()
        self.T = set()
        self.U = []
        self.V = []
        self.cycle_found = False

        I = set(self.initial_states)
        while I and not self.cycle_found:
            cur = random.choice(list(I))
            self.reachableCycle(cur)
            I -= self.R

        return not self.cycle_found

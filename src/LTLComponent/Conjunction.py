from .Base import Base
from typing import List


class Conjunction(Base):
    """LTLComponent for (formula) /\ (formula)"""

    def __init__(self, f0: Base, f1: Base):
        self.f0 = f0
        self.f1 = f1

    def getChildren(self) -> List[Base]:
        return [self.f0, self.f1]

    def __repr__(self) -> str:
        return f"({self.f0} /\\ {self.f1})"

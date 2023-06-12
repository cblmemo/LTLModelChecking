from .Base import Base
from typing import List


class Negation(Base):
    """LTLComponent for !(formula)"""

    def __init__(self, f: Base):
        self.f = f

    def getChildren(self) -> List[Base]:
        return [self.f]

    def __repr__(self) -> str:
        return f"(!{self.f})"

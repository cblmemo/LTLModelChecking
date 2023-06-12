from .Base import Base
from typing import List


class Next(Base):
    """LTLComponent for !(formula)"""

    def __init__(self, f: Base):
        self.f = f

    def getChildren(self) -> List[Base]:
        return [self.f]

    def __repr__(self) -> str:
        return f"(X{self.f})"

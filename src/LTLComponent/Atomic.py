from .Base import Base
from typing import List, Union


class Atomic(Base):
    """LTLComponent for atomics"""

    def getChildren(self) -> List[Base]:
        return []


class AtomicTrue(Atomic):
    """LTLComponent for true"""

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return "true"


class AtomicFalse(Atomic):
    """LTLComponent for false"""

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return "false"


class Identifier(Atomic):
    """LTLComponent for identifiers"""

    def __init__(self, name: str):
        self.name = name

    def getAllIdentifiers(self) -> List["Base"]:
        return [self]

    def __repr__(self) -> str:
        return self.name

    def __lt__(self, other: "Identifier") -> bool:
        if not isinstance(other, Identifier):
            raise NotImplementedError
        return self.name < other.name

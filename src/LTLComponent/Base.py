from typing import List, Set


class Base(object):
    """Base class for all LTL Components."""

    def getChildren(self) -> List["Base"]:
        raise NotImplementedError

    def getClosure(self) -> Set["Base"]:
        from utils import getNegation

        closure: Set["Base"] = {self, getNegation(self)}
        for child in self.getChildren():
            closure.update(child.getClosure())
        return closure

    def getAllIdentifiers(self) -> Set["Base"]:
        identifiers: Set["Base"] = set()
        for child in self.getChildren():
            identifiers.update(child.getAllIdentifiers())
        return identifiers

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Base):
            raise NotImplementedError
        return self.__repr__() == other.__repr__()

    def __hash__(self) -> int:
        return hash(self.__repr__())

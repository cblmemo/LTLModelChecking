import typing


class State:
    cnt = 0
    print_detail = False

    def __init__(self, name_hint: str):
        self.name_hint = name_hint
        self.num = State.cnt
        State.cnt += 1

    @staticmethod
    def resetCnt() -> None:
        State.cnt = 0

    def __repr__(self) -> str:
        return (
            (f"S{self.num}/" + self.name_hint) if State.print_detail else f"S{self.num}"
        )

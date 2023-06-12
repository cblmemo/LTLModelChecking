class TSState:
    def __init__(self, name_hint: str):
        self.name_hint = name_hint

    def __repr__(self) -> str:
        return self.name_hint

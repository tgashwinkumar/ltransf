class Symbol:
    def __init__(self, val: str):
        self.val = val

    def __repr__(self):
        return f"<Symbol: {self.val}>"

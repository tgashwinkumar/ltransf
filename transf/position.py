class Position:
    def __init__(self, idx:int):
        self.idx = idx

    def nextPos(self):
        self.idx += 1

    def __repr__(self):
        return f"<Postion: {self.idx}>"
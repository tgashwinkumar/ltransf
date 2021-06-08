from transf.definitions.symbol import Symbol
class LaplaceOf:
    def __init__(self, expressionText: str, symbol: Symbol = Symbol('t')):
        self.expressionStr = expressionText
        self.symbol = symbol

    def evaluate(self):
        pass

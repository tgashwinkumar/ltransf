from transf.additivestack.additivestack import AdditiveStack
from transf.parser.parser import Parser
from transf.definitions.symbol import Symbol
from transf.lexer.lexer import Lexer


class LaplaceOf:
    def __init__(self, expressionText: str, symbol: Symbol = Symbol('t')):
        self.expressionStr = expressionText
        self.symbol = symbol

    def evaluate(self):
        lexer = Lexer(self.expressionStr)
        inputStack = AdditiveStack(lexer.getTokens())
        outputStack = AdditiveStack()
        for element in inputStack.getStack():
            pass
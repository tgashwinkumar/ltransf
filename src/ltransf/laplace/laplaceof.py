
from .laplacesort import LaplaceSort
from ..definitions.tokentype import TT
from ..definitions.token import LexicalToken
from ..additivestack.additivestack import AdditiveStack
from ..parser.parser import Parser
from ..definitions.symbol import Symbol
from ..lexer.lexer import Lexer


class LaplaceOf:
    def __init__(self, expressionText: str, symbol: Symbol = Symbol('t')):
        self.expressionStr = expressionText
        self.symbol = symbol

    def evaluate(self):
        lexer = Lexer(self.expressionStr)
        # print(lexer.getTokens())
        inputStack = AdditiveStack(lexer.getTokens())
        outputStack = AdditiveStack()
        for element in inputStack.getStack():
            if isinstance(element, LexicalToken) and (element.tokenType == TT.PLUS or element.tokenType == TT.MINUS):
                print(element.tokenVal)
                outputStack.add(element)
                continue
            node= Parser(element).getNodes()
            laplaceNode = LaplaceSort(node)
            outputStack.add(laplaceNode)
            print(laplaceNode)

    
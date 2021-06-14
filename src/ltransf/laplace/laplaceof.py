from ltransf.definitions.tokentype import TT
from ltransf.parser.parser import Parser
from ltransf.additivestack.additivestack import AdditiveStack
from ltransf.definitions.symbol import Symbol
from ltransf.definitions.token import LexicalToken
from ltransf.lexer.lexer import Lexer
from ltransf.laplace.laplacesort import LaplaceSort

class LaplaceOf:
    def __init__(self, expressionText: str, symbol: Symbol = Symbol('t')):
        self.expressionStr = expressionText
        self.symbol = symbol

    def evaluate(self):
        lexer = Lexer(self.expressionStr)
        # print(lexer.getTokens())
        inputStack = AdditiveStack(lexer.getTokens())
        outputStack = AdditiveStack()
        symbolToken = LexicalToken(TT.SYMBOL, tval=Symbol('s').val)
        for element in inputStack.getStack():
            if isinstance(element, LexicalToken) and (element.tokenType == TT.PLUS or element.tokenType == TT.MINUS):
                print(element.tokenVal)
                outputStack.add(element)
                continue
            node= Parser(element).getNodes()
            laplaceNode = LaplaceSort(node, symbolToken)
            outputStack.add(laplaceNode)
            print(laplaceNode)

    

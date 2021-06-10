from transf.expression_nodes.udfunc_expnode import UdFuncExpNode
from transf.expression_nodes.trigfunc_expnode import TrigFuncExpNode
from transf.definitions.tokentype import TC, TT
from transf.laplace.ltrans import LTrans
from transf.definitions.token import LexicalToken
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
        # print(lexer.getTokens())
        outputStack = AdditiveStack()
        for element in inputStack.getStack():
            if isinstance(element, LexicalToken) and (element.tokenType == TT.PLUS or element.tokenType == TT.MINUS):
                print(element.tokenVal)
                # outputStack.add(element)
                continue
            node= Parser(element).getNodes()
            if isinstance(node, TrigFuncExpNode):
                laplaceNode = LTrans.trigFunc(expNode=node)
            elif isinstance(node, UdFuncExpNode):
                laplaceNode = LTrans.udfunc(expNode=node)
            # outputStack.add(laplaceNode)
            print(laplaceNode)
from typing import List, Optional

from transf.expression import Expression
from transf.definitions.position import Position
from transf.stack import Stack, StackToken
from transf.definitions.token import LexicalToken
from transf.definitions.tokentype import TC, TT


class Parser:
    def __init__(self, lexerTokens: List[LexicalToken]):
        self.lexerTokens = lexerTokens
        self.currPos = Position(-1)
        self.currToken: Optional[LexicalToken] = None
        self.operandStack: Stack = Stack()
        self.operatorStack: Stack = Stack()

    def __advance(self):
        self.currPos.nextPos()
        if self.currPos.idx >= len(self.lexerTokens):
            self.currToken = None
        else:
            self.currToken = self.lexerTokens[self.currPos.idx]

    def __getExpression(self):
        rightToken = self.operandStack.pop()
        leftToken = self.operandStack.pop()
        operator = self.operatorStack.pop()
        return Expression(leftToken, operator, rightToken)

    def runParser(self):  
        self.__advance()
        while self.currToken:
            if self.currToken.tokenClass == TC.DIGIT or self.currToken.tokenClass == TC.CONST or self.currToken.tokenClass == TC.SYMBOL:
                self.operandStack.push(self.currToken)
            elif self.currToken.tokenClass == TC.OPER :
                if self.operatorStack.isEmpty():
                    self.operatorStack.push(self.currToken)
                else:
                    if self.currToken.getPrecedence() >= self.operatorStack.getCurrent().getPrecedence():
                        self.operatorStack.push(self.currToken)
                    else:
                        expression = self.__getExpression()
                        self.operandStack.push(expression)
            elif self.currToken.tokenClass == TC.FUNC:
                self.operatorStack.push(self.currToken)
            elif self.currToken.tokenType == TT.LPAREN:
                self.operatorStack.push(self.currToken)
            elif self.currToken.tokenType == TT.RPAREN:
                while not self.operatorStack.getCurrent().tokenType == TT.LPAREN or not self.operatorStack.getCurrent().tokenClass == TC.FUNC:
                    expression = self.__getExpression()
                    self.operandStack.push(self.currToken)
            self.__advance()    

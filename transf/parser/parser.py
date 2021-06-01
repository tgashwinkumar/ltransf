from transf.lexer.lexer import Lexer
from typing import List, Optional

from transf.definitions.expression import Expression
from transf.definitions.position import Position
from transf.stack import Stack
from transf.definitions.token import LexicalToken
from transf.definitions.tokentype import TC, TT


class Parser:
    def __init__(self, lexerTokens: List[LexicalToken]):
        self.lexerTokens = lexerTokens
        print(len(self.lexerTokens))
        self.currPos = Position(-1)
        self.currToken: Optional[LexicalToken] = None
        self.operandStack: Stack = Stack()
        self.operatorStack: Stack = Stack()

    def __advance(self):
        self.currPos.nextPos()
        if self.currPos.idx < len(self.lexerTokens):
            self.currToken = self.lexerTokens[self.currPos.idx]
        else:
            self.currToken = None
        print("Position: ", self.currPos.idx,
              "\tCurrent Token: ", self.currToken)

    def __getExpression(self):
        rightToken = self.operandStack.pop()
        leftToken = self.operandStack.pop()
        operator = self.operatorStack.pop()
        return Expression(leftToken, operator, rightToken)

    def __runParser(self):
        print("Running Parser")  
        self.__advance()
        while self.currToken:
            if self.currToken.tokenClass == TC.DIGIT or self.currToken.tokenClass == TC.CONST or self.currToken.tokenClass == TC.SYMBOL:
                self.operandStack.push(self.currToken)
                self.__advance()
            elif self.currToken.tokenClass == TC.OPER :
                if self.operatorStack.isEmpty():
                    self.operatorStack.push(self.currToken)
                    self.__advance()
                else:
                    if self.operatorStack.getCurrent().getPrecedence():
                        if self.currToken.getPrecedence() >= self.operatorStack.getCurrent().getPrecedence():
                            self.operatorStack.push(self.currToken)
                            self.__advance()
                        else:
                            expression = self.__getExpression()
                            self.operandStack.push(expression)
                    else:
                        self.operatorStack.push(self.currToken)
                        self.__advance()
            elif self.currToken.tokenClass == TC.FUNC or self.currToken.tokenType == TT.LPAREN:
                self.operatorStack.push(self.currToken)
                self.__advance()
            elif self.currToken.tokenType == TT.RPAREN:
                while not self.operatorStack.getCurrent().tokenType == TT.LPAREN:
                    expression = self.__getExpression()
                    self.operandStack.push(expression)
                if self.operatorStack.getCurrent().tokenType == TT.LPAREN:
                    self.operatorStack.pop()
                if self.operatorStack.getCurrent().tokenClass == TC.FUNC:
                    func = self.operatorStack.pop()
                    expr = self.operandStack.pop()
                    self.operandStack.push(Expression(func, expr))
                self.__advance() 
        while not self.operatorStack.isEmpty():
            expression = self.__getExpression()
            self.operandStack.push(expression)

    def printParser(self):
        self.__runParser()
        print(self.operandStack.getCurrent())

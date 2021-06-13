from typing import List, Optional
from ltransf.expression_nodes.linearpoly_expnode import LinearPolynomialExpNode
from ltransf.expression_nodes.binarynode import BinaryNode
from ltransf.expression_nodes.constevalconst_expnode import ConstEvalConstExpNode
from ltransf.expression_nodes.constmultipoly_expnode import ConstMultiPolyExpNode
from ltransf.expression_nodes.udfunc_expnode import UdFuncExpNode
from ltransf.expression_nodes.trigfunc_expnode import TrigFuncExpNode
from ltransf.expression_nodes.power1_expnode import Power1ExpNode
from ltransf.expression_nodes.powern_expnode import PowerNExpNode
from ltransf.expression_nodes.exponential_expnode import ExponentialExpNode
from ltransf.lexer.lexer import Lexer
from ltransf.definitions.position import Position
from ltransf.stack import Stack, StackToken
from ltransf.definitions.token import LexicalToken
from ltransf.definitions.tokentype import TC, TT


class Parser:
    def __init__(self, lexerTokens: List[LexicalToken]):
        self.lexerTokens = lexerTokens
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
        # print("Position: ", self.currPos.idx, "\tToken: ", self.currToken)


    def __runParser(self):
        # print("Running Parser")  
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
                    if self.operatorStack.getCurrent().tokenType == TT.LPAREN:
                        self.operatorStack.push(self.currToken)
                        self.__advance()
                    elif self.currToken.getPrecedence() >= self.operatorStack.getCurrent().getPrecedence():
                        self.operatorStack.push(self.currToken)
                        self.__advance()
                    else:
                        expression = self.__getBinaryExpression()
                        self.operandStack.push(expression)
            elif self.currToken.tokenClass == TC.FUNC or self.currToken.tokenType == TT.LPAREN:
                self.operatorStack.push(self.currToken)
                self.__advance()
            elif self.currToken.tokenType == TT.RPAREN:
                while not self.operatorStack.getCurrent().tokenType == TT.LPAREN:
                    expression = self.__getBinaryExpression()
                    self.operandStack.push(expression)
                if self.operatorStack.getCurrent().tokenType == TT.LPAREN:
                    self.operatorStack.pop()
                if self.operatorStack.getCurrent().tokenClass == TC.FUNC:
                    expression = self.__getUnaryExpression()
                    self.operandStack.push(expression)
                self.__advance() 
        while not self.operatorStack.isEmpty():
            expression = self.__getBinaryExpression()
            self.operandStack.push(expression)

    def printParser(self):
        self.__runParser()
        print(self.operandStack.getCurrent())

    def getNodes(self):
        self.__runParser()
        return self.operandStack.getCurrent()

    def __getBinaryExpression(self):
        rightToken = self.operandStack.pop()
        leftToken = self.operandStack.pop()
        operator = self.operatorStack.pop()
        if isinstance(rightToken, StackToken): 
            rightToken = rightToken.tokenValue
        if isinstance(leftToken, StackToken):
            leftToken = leftToken.tokenValue
        if isinstance(operator, StackToken):
            operator = operator.tokenValue

        if operator.tokenType == TT.POWER:
            if leftToken.tokenClass == TC.CONST or leftToken.tokenClass == TC.DIGIT:
                if rightToken.tokenClass == TC.CONST or rightToken.tokenClass == TC.DIGIT:
                    return ConstEvalConstExpNode(operator, leftToken, rightToken).evaluate()
            elif leftToken.tokenType == TT.EXP:
                if isinstance(rightToken, (LexicalToken, Power1ExpNode)):
                    return ExponentialExpNode(operator, leftToken, rightToken)
            elif leftToken.tokenType == TT.SYMBOL:
                if rightToken.tokenClass == TC.CONST or rightToken.tokenClass == TC.DIGIT:
                    return PowerNExpNode(operator, leftToken, rightToken)

        elif operator.tokenType == TT.MULTI:
            if leftToken.tokenClass == TC.CONST or leftToken.tokenClass == TC.DIGIT:
                if rightToken.tokenType == TT.SYMBOL:
                    return Power1ExpNode(operator, leftToken, rightToken)
                elif rightToken.tokenClass == TC.DIGIT or rightToken.tokenClass == TC.CONST:
                    return ConstEvalConstExpNode(operator, leftToken, rightToken).evaluate()
                else:
                    return ConstMultiPolyExpNode(operator, leftToken, rightToken)

        elif operator.tokenType == TT.MINUS:
            if rightToken.tokenClass == TC.CONST or rightToken.tokenClass == TC.DIGIT:
                if leftToken.tokenType == TT.SYMBOL:
                    return LinearPolynomialExpNode(operator, leftToken, rightToken)
                elif leftToken.tokenClass == TC.CONST or rightToken.tokenClass == TC.DIGIT:
                    return ConstEvalConstExpNode(operator, leftToken, rightToken).evaluate()
    
        elif operator.tokenType == TT.PLUS:
            if rightToken.tokenClass == TC.CONST or rightToken.tokenClass == TC.DIGIT:
                if leftToken.tokenType == TT.SYMBOL:
                    return LinearPolynomialExpNode(operator, leftToken, rightToken)
                elif leftToken.tokenClass == TC.CONST or rightToken.tokenClass == TC.DIGIT:
                    return ConstEvalConstExpNode(operator, leftToken, rightToken).evaluate()
        
    def __getUnaryExpression(self):
        leftToken = self.operandStack.pop()
        operator = self.operatorStack.pop()
        if isinstance(leftToken, StackToken):
            leftToken = leftToken.tokenValue
        if isinstance(operator, StackToken):
            operator = operator.tokenValue

        if operator.tokenType == TT.SIN or operator.tokenType == TT.COS or operator.tokenType == TT.COSH or operator.tokenType == TT.SINH:
            if isinstance(leftToken, LexicalToken) and (leftToken.tokenClass == TC.DIGIT or leftToken.tokenClass == TC.CONST):
                return ConstEvalConstExpNode(operator, leftToken).evaluate()
            return TrigFuncExpNode(operator.tokenType, operator, leftToken)
        elif operator.tokenType == TT.USTEP or operator.tokenType == TT.DDELTA:
            if isinstance(leftToken, LexicalToken) and (leftToken.tokenClass == TC.DIGIT or leftToken.tokenClass == TC.CONST):
                return ConstEvalConstExpNode(operator, leftToken).evaluate()
            return UdFuncExpNode(operator.tokenType, operator, leftToken)

from transf.definitions.expression import Expression
from transf.definitions.tokentype import ET, TC, TT
from transf.stack import StackToken
from typing import Union
from transf.definitions.token import LexicalToken



class ExpressionType:

    def __init__(self, *tokens):
        self.tokens = tokens
        self.type =  self.getType()

    def getType(self):
        if len(self.tokens) == 1:
            return self.__unaryParam(self.tokens[0])
        elif len(self.tokens) == 2:
            return self.__binaryParam(self.tokens[0], self.tokens[1])
        elif len(self.tokens) == 3:
            return self.__ternaryParam(self.tokens[0], self.tokens[1], self.tokens[2])
            
    def __unaryParam(self, token: Union[LexicalToken, StackToken]):
        if isinstance(token, StackToken):
            token = token.tokenValue
        if token.tokenType == TT.CONST or token.tokenClass == TC.DIGIT:
            return ET.CONST
        elif token.tokenType == TT.SYMBOL:
            return ET.POLY
        return ET.ERR

    def __binaryParam(self, operator: Union[LexicalToken, StackToken], operand: Union[StackToken, LexicalToken, Expression]):
        if isinstance(operator, StackToken):
            operator = operator.tokenValue
        if operator.tokenType == TT.SIN or operator.tokenType == TT.COS:
            return ET.TRIG
        elif operator.tokenType == TT.SQRT:
            return ET.SQRT
        elif operator.tokenType == TT.USTEP:
            return ET.USTEP
        elif operator.tokenType == TT.DDELTA:
            return ET.DDELTA
        return ET.ERR
    
    def __ternaryParam(self, leftoperand: Union[LexicalToken, StackToken, Expression], operator: Union[LexicalToken, StackToken], rightoperand: Union[LexicalToken, StackToken, Expression]):
        pass

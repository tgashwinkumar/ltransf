from typing import Optional
from transf.definitions.tokentype import TC, TT

class TokenClass:

    def __init__(self, tokentype: Optional[TT] = None):
        self.tokenType = tokentype
        self.__operators = [TT.PLUS, TT.MINUS, TT.MULTI, TT.DIVID, TT.POWER]
        self.__parentheses = [TT.LPAREN, TT.RPAREN]
        self.__squParentheses = [TT.LSQU, TT.RSQU]
        self.__functions = [TT.SIN, TT.COS, TT.TAN, TT.SQRT, TT.USTEP, TT.DDELTA, TT.SINH, TT.COSH]
        self.__constants = [TT.EXP, TT.PI, TT.CONST]

    def getClass(self):

        if self.tokenType in self.__operators:
            return TC.OPER

        elif self.tokenType in self.__functions:
            return TC.FUNC

        elif self.tokenType in self.__parentheses:
            return TC.PAREN

        elif self.tokenType in self.__squParentheses:
            return TC.SQUPAREN

        elif self.tokenType in self.__constants:
            return TC.CONST

        elif self.tokenType == TT.SYMBOL:
            return TC.SYMBOL

        elif self.tokenType == TT.INT or self.tokenType == TT.FLOAT:
            return TC.DIGIT
        
        else:
            return None
        

        

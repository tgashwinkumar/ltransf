from typing import Union
from .tokenclass import TokenClass
from .tokentype import TC, TT

class LexicalToken:

    def __init__(self, ttype: TT = TT.NULL, tval: Union[str, int, float, None] = None, isNeg: bool = False, isReciprocal: bool = False):
        self.tokenType: TT = ttype
        self.tokenName = ttype.name
        self.tokenVal = tval if tval else ttype.value
        if tval == 0:
            self.tokenVal = 0
            self.tokenType = TT.INT
        elif ttype == TT.INT:
            self.tokenVal = int(self.tokenVal)
        self.tokenClass: TC = TokenClass(self.tokenType).getClass()
        self.isTokenNegative = isNeg
        self.isTokenReciprocal = isReciprocal

    def __str__(self):
        return f"<LexicalToken {self.tokenType.name} : {'-' if self.isTokenNegative else ''}{self.tokenVal} >"

    def __repr__(self):
        return f"<LexicalToken {self.tokenType.name} : {'-' if self.isTokenNegative else ''}{self.tokenVal} >"

    def getPrecedence(self):
        if not self.tokenClass == TC.OPER:
            return None
        if self.tokenType == TT.PLUS or self.tokenType == TT.MINUS:
            return 0
        elif self.tokenType == TT.MULTI or self.tokenType == TT.DIVID:
            return 1
        elif self.tokenType == TT.POWER:
            return 2
        

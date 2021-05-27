from transf.definitions.tokenclass import TokenClass
from typing import Union
from transf.definitions.tokentype import TC, TT

class LexicalToken:

    def __init__(self, ttype: TT = TT.NULL, tval: Union[str, int, float, None] = None):
        self.tokenType: TT = ttype
        self.tokenName = ttype.name
        self.tokenVal = tval if tval else ttype.value
        self.tokenClass: TC = TokenClass(self.tokenType).getClass()

    def __str__(self):
        return f"<LexicalToken {self.tokenType.name} : {self.tokenVal} >"

    def __repr__(self):
        return f"<LexicalToken {self.tokenType.name} : {self.tokenVal} >"

    def getPrecedence(self):
        if not self.tokenClass == TC.OPER:
            return None
        if self.tokenType == TT.PLUS or self.tokenType == TT.MINUS:
            return 0
        elif self.tokenType == TT.MULTI or self.tokenType == TT.DIVID:
            return 1
        elif self.tokenType == TT.POWER:
            return 2
        

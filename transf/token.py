from typing import Union
from transf.tokentype import TT

class LexicalToken:

    def __init__(self, ttype: TT, tval: Union[str, int, float, None] = None):
        self.tokenType = ttype
        self.tokenName = ttype.name
        self.tokenVal = tval if tval else ttype.value

    def __str__(self):
        return f"<LexicalToken {self.tokenType.name} : {self.tokenVal}>"

    def __repr__(self):
        return f"<LexicalToken {self.tokenType.name} : {self.tokenVal}>"

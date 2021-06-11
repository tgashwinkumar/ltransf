from typing import Optional
from ..definitions.tokentype import TT
from ..errors.errors import NodeError
from ..definitions.token import LexicalToken
from .binarynode import BinaryNode
import math

class ConstEvalConstExpNode(BinaryNode):
    def __init__(self, root: LexicalToken, leftNode: LexicalToken, rightNode: Optional[LexicalToken] = None):
        super().__init__(root, leftNode=leftNode, rightNode=rightNode)

    def evaluate(self):
        if not isinstance(self.leftNode, LexicalToken):
            raise NodeError

        if self.rightNode:
            if not isinstance(self.rightNode, LexicalToken):
                raise NodeError 
        if self.rightNode:
            if self.leftNode.tokenType == TT.CONST or self.rightNode.tokenType == TT.CONST:
                return BinaryNode(self.root, self.leftNode, self.rightNode)
        else:
            if self.leftNode.tokenType == TT.CONST:
                return BinaryNode(self.root, self.leftNode, self.rightNode)

        tval = 0
        if self.root.tokenType == TT.POWER:
            tval = pow(self.leftNode.tokenVal,self.rightNode.tokenVal)
        elif self.root.tokenType == TT.PLUS:
            tval = self.leftNode.tokenVal + self.rightNode.tokenVal
        elif self.root.tokenType == TT.MINUS:
            tval = self.leftNode.tokenVal - self.rightNode.tokenVal
        elif self.root.tokenType == TT.MULTI:
            tval = self.leftNode.tokenVal * self.rightNode.tokenVal
        elif self.root.tokenType == TT.DIVID:
            tval = self.leftNode.tokenVal / self.rightNode.tokenVal
        elif self.root.tokenType == TT.SIN:
            tval = round(math.sin(self.leftNode.tokenVal), 3)
        elif self.root.tokenType == TT.COS:
            tval = round(math.cos(self.leftNode.tokenVal), 3)
        elif self.root.tokenType == TT.SINH:
            tval = round(math.sinh(self.leftNode.tokenVal), 3)
        elif self.root.tokenType == TT.COSH:
            tval = round(math.cosh(self.leftNode.tokenVal), 3)
            
        ttype = TT.INT if tval == int(tval) else TT.FLOAT
        return LexicalToken(ttype=ttype, tval=tval)

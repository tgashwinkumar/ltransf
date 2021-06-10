from typing import Optional
from transf.definitions.tokentype import TT
from transf.errors.errors import NodeError
from transf.definitions.token import LexicalToken
from transf.expression_nodes.binarynode import BinaryNode

class ConstEvalConstExpNode(BinaryNode):
    def __init__(self, root: LexicalToken, leftNode: LexicalToken, rightNode: Optional[LexicalToken]):
        super().__init__(root, leftNode=leftNode, rightNode=rightNode)

    def evaluate(self):
        if not isinstance(self.leftNode, LexicalToken) or not isinstance(self.rightNode, LexicalToken):
            raise NodeError

        if self.leftNode.tokenType == TT.CONST or self.rightNode.tokenType == TT.CONST:
            return BinaryNode(self.root, self.leftNode, self.rightNode)

        tval = 0
        if self.root.tokenType == TT.POWER:
            tval = pow(self.leftNode.tokenVal,self.rightNode.tokenVal)
        elif self.root.tokenType == TT.PLUS:
            tval = self.leftNode.tokenVal + self.rightNode.tokenVal
        elif self.root.tokenType == TT.MINUS:
            tval = self.leftNode - self.rightNode.tokenVal
        elif self.root.tokenType == TT.MULTI:
            tval = self.leftNode * self.rightNode.tokenVal
        elif self.root.tokenType == TT.DIVID:
            tval = self.leftNode / self.rightNode.tokenVal
            
        ttype = TT.INT if tval == int(tval) else TT.FLOAT
        return LexicalToken(ttype=ttype, tval=tval)
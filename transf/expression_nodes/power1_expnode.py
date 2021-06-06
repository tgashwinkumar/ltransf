from transf.errors.errors import NonPower1Error
from transf.definitions.tokentype import TC, TT
from transf.definitions.token import LexicalToken
from transf.expression_nodes.binarynode import BinaryNode


class Power1ExpNode(BinaryNode):
    def __init__(self, root: LexicalToken, leftNode:LexicalToken, rightNode: LexicalToken):
        super().__init__(root, leftNode=leftNode, rightNode=rightNode)
        if not leftNode.tokenType == TT.SYMBOL and not rightNode.tokenType == TT.SYMBOL:
            raise NonPower1Error()
        if leftNode.tokenClass == TC.CONST or leftNode.tokenClass == TC.DIGIT:
            self.coeff = leftNode
            self.symbol = rightNode
        elif rightNode.tokenClass == TC.CONST or rightNode.tokenClass == TC.DIGIT:
            self.coeff = rightNode
            self.symbol = leftNode
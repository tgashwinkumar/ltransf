from transf.definitions.tokentype import TC, TT
from transf.definitions.token import LexicalToken
from transf.expression_nodes.binarynode import BinaryNode


class LinearPolynomialExpNode(BinaryNode):
    def __init__(self, root: LexicalToken, leftNode: LexicalToken, rightNode: LexicalToken):
        super().__init__(root, leftNode=leftNode, rightNode=rightNode)
        self.sign: TT = TT.NULL
        self.const: LexicalToken = LexicalToken()
        if root.tokenType == TT.PLUS:
            self.sign = TT.PLUS
            if leftNode.tokenClass == TC.CONST or leftNode.tokenClass == TC.DIGIT:
                self.const = leftNode
            else:
                self.const = rightNode
        elif root.tokenType == TT.MINUS:
            if self.const.isTokenNegative:
                self.sign = TT.PLUS
                self.const.isTokenNegative = False
            else:
                self.sign = TT.MINUS
                self.const = rightNode
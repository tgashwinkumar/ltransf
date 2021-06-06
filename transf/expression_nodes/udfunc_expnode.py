from transf.definitions.tokentype import TT
from typing import Union
from transf.expression_nodes.linearpoly_expnode import LinearPolynomialExpNode
from transf.definitions.token import LexicalToken
from transf.expression_nodes.binarynode import BinaryNode


class UdFuncExpNode(BinaryNode):
    def __init__(self, funcType: TT, root: LexicalToken, leftNode: Union[LinearPolynomialExpNode, LexicalToken]):
        super().__init__(root, leftNode=leftNode, rightNode=None)
        self.funcType = funcType
        if isinstance(leftNode, LexicalToken) and leftNode.tokenType == TT.SYMBOL:
            self.param = LexicalToken(TT.INT, 0)
            self.sign = LexicalToken(TT.MINUS)
        elif isinstance(leftNode, LinearPolynomialExpNode):
            self.param = leftNode.const
            self.sign = leftNode.sign

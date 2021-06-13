from typing import Union
from ltransf.definitions.tokentype import TT
from ltransf.expression_nodes.linearpoly_expnode import LinearPolynomialExpNode
from ltransf.definitions.token import LexicalToken
from ltransf.expression_nodes.binarynode import BinaryNode


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

        

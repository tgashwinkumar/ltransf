from transf.expression_nodes.power1_expnode import Power1ExpNode
from typing import Union
from transf.errors.errors import NodeError
from transf.definitions.tokentype import TT
from transf.definitions.token import LexicalToken
from transf.expression_nodes.binarynode import BinaryNode


class ExponentialExpNode(BinaryNode):
    def __init__(self, root: LexicalToken, leftNode: LexicalToken, rightNode: Union[LexicalToken, Power1ExpNode]):
        super().__init__(root, leftNode=leftNode, rightNode=rightNode)
        if not (root.tokenType == TT.POWER and leftNode.tokenType == TT.EXP):
            raise NodeError()
        if isinstance(rightNode, LexicalToken) and rightNode.tokenType == TT.SYMBOL:
            self.param = LexicalToken(TT.INT, 1)
        elif isinstance(rightNode, Power1ExpNode):
            self.param = rightNode.coeff
        
        
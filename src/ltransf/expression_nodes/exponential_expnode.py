from typing import Union

from ltransf.definitions.token import LexicalToken
from ltransf.definitions.tokentype import TT
from ltransf.errors.errors import NodeError
from ltransf.expression_nodes.binarynode import BinaryNode
from ltransf.expression_nodes.power1_expnode import Power1ExpNode


class ExponentialExpNode(BinaryNode):
    def __init__(self, root: LexicalToken, leftNode: LexicalToken, rightNode: Union[LexicalToken, Power1ExpNode]):
        super().__init__(root, leftNode=leftNode, rightNode=rightNode)
        if not (root.tokenType == TT.POWER and leftNode.tokenType == TT.EXP):
            raise NodeError()
        if isinstance(rightNode, LexicalToken) and rightNode.tokenType == TT.SYMBOL:
            self.param = LexicalToken(TT.INT, 1)
        elif isinstance(rightNode, Power1ExpNode):
            self.param = rightNode.coeff
        
        
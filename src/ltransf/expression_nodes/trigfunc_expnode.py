from typing import Union
from ltransf.definitions.token import LexicalToken
from ltransf.definitions.tokentype import TT
from ltransf.expression_nodes.binarynode import BinaryNode
from ltransf.expression_nodes.power1_expnode import Power1ExpNode


class TrigFuncExpNode(BinaryNode):
    def __init__(self, funcType: TT, root: LexicalToken, leftNode: Union[Power1ExpNode, LexicalToken]):
        super().__init__(root, leftNode=leftNode, rightNode=None)
        self.funcType = funcType
        if isinstance(leftNode, LexicalToken) and leftNode.tokenType == TT.SYMBOL:
            self.param = LexicalToken(TT.INT, 1)
        elif isinstance(leftNode, Power1ExpNode):
            self.param = leftNode.coeff

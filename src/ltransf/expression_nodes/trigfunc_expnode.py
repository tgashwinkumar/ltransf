from typing import Union
from ..errors.errors import NodeError
from ..definitions.tokentype import TT
from ..definitions.token import LexicalToken
from .power1_expnode import Power1ExpNode
from .binarynode import BinaryNode


class TrigFuncExpNode(BinaryNode):
    def __init__(self, funcType: TT, root: LexicalToken, leftNode: Union[Power1ExpNode, LexicalToken]):
        super().__init__(root, leftNode=leftNode, rightNode=None)
        self.funcType = funcType
        if isinstance(leftNode, LexicalToken) and leftNode.tokenType == TT.SYMBOL:
            self.param = LexicalToken(TT.INT, 1)
        elif isinstance(leftNode, Power1ExpNode):
            self.param = leftNode.coeff

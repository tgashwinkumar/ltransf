from ..errors.errors import NodeError
from ..definitions.tokentype import TC, TT
from ..definitions.token import LexicalToken
from .binarynode import BinaryNode


class PowerNExpNode(BinaryNode):
    def __init__(self, root: LexicalToken, leftNode: LexicalToken, rightNode: LexicalToken):
        super().__init__(root, leftNode=leftNode, rightNode=rightNode)
        if not leftNode.tokenType == TT.SYMBOL:
            raise NodeError()
        if not rightNode.tokenClass == TC.DIGIT and not rightNode.tokenClass == TC.CONST:
            raise NodeError()
        self.param = rightNode
        
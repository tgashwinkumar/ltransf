
from ltransf.definitions.tokentype import TC
from ltransf.definitions.token import LexicalToken
from ltransf.errors.errors import NodeError
from ltransf.expression_nodes.binarynode import BinaryNode


class ConstMultiPolyExpNode(BinaryNode):
    def __init__(self, root: LexicalToken, leftNode: LexicalToken, rightNode):
        super().__init__(root, leftNode=leftNode, rightNode=rightNode)
        if not leftNode.tokenClass == TC.DIGIT and not leftNode.tokenClass == TC.CONST:
            raise NodeError()
        self.const = leftNode
        
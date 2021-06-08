from transf.errors.errors import NodeError
from transf.definitions.tokentype import TC
from transf.definitions.token import LexicalToken
from transf.expression_nodes.binarynode import BinaryNode


class ConstMultiPolyExpNode(BinaryNode):
    def __init__(self, root: LexicalToken, leftNode: LexicalToken, rightNode):
        super().__init__(root, leftNode=leftNode, rightNode=rightNode)
        if not leftNode.tokenClass == TC.DIGIT and not leftNode.tokenClass == TC.CONST:
            raise NodeError()
        self.const = leftNode
        
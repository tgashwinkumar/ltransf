from ltransf.definitions.tokentype import TC
from ltransf.definitions.token import LexicalToken
from ltransf.errors.errors import NodeError
from ltransf.expression_nodes.binarynode import BinaryNode


class ConstMultiPolyExpNode(BinaryNode):
    def __init__(self, root: LexicalToken, leftNode: LexicalToken, rightNode):
        super().__init__(root, leftNode=leftNode, rightNode=rightNode)
        if leftNode.tokenClass == TC.DIGIT or leftNode.tokenClass == TC.CONST:
            self.const = leftNode
            self.poly = rightNode
        elif rightNode.tokenClass == TC.DIGIT or rightNode.tokenClass == TC.CONST:
            self.const = rightNode
            self.poly = leftNode
        else:
            raise NodeError
        

from transf.definitions.token import LexicalToken
from transf.expression_nodes.binarynode import BinaryNode

class ConstEvalConstExpNode(BinaryNode):
    def __init__(self, root: LexicalToken, leftNode: LexicalToken, rightNode: LexicalToken):
        super().__init__(root, leftNode=leftNode, rightNode=rightNode)
from typing import Optional
from transf.definitions.token import LexicalToken

class BinaryNode:
    def __init__(self, root: LexicalToken, leftNode = None, rightNode = None):
        self.root = root
        self.leftNode = leftNode
        self.rightNode = rightNode
        
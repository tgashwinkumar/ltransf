from typing import Optional
from transf.definitions.token import LexicalToken

class BinaryNode:
    def __init__(self, root: LexicalToken, leftNode = None, rightNode = None):
        self.root = root
        self.leftNode = leftNode
        self.rightNode = rightNode

    def __repr__(self):
        if isinstance(self.leftNode, LexicalToken) and isinstance(self.rightNode, LexicalToken):
            return f"({self.leftNode.tokenVal} {self.root.tokenVal} {self.rightNode.tokenVal})"
        elif isinstance(self.leftNode, LexicalToken) and not isinstance(self.rightNode, LexicalToken):
            return f"({self.leftNode.tokenVal} {self.root.tokenVal} {self.rightNode})"
        elif not isinstance(self.leftNode, LexicalToken) and isinstance(self.rightNode, LexicalToken):
            return f"({self.leftNode} {self.root.tokenVal} {self.rightNode.tokenVal})"
        else:
            return f"({self.leftNode} {self.root.tokenVal} {self.rightNode})"
        

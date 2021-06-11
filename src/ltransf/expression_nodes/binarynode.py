from typing import Optional
from ..definitions.token import LexicalToken

class BinaryNode:
    def __init__(self, root: LexicalToken, leftNode = None, rightNode = None):
        self.root = root
        self.leftNode = leftNode
        self.rightNode = rightNode

    def __repr__(self):

        if isinstance(self.leftNode, LexicalToken) and isinstance(self.rightNode, LexicalToken):
            if self.leftNode.isTokenNegative:
                leftVal = '-' + str(self.leftNode.tokenVal)
            else:
                leftVal = self.leftNode.tokenVal
            if self.rightNode.isTokenNegative:
                rightVal = '-' + str(self.rightNode.tokenVal)
            else:
                rightVal = self.rightNode.tokenVal
            return f"({leftVal} {self.root.tokenVal} {rightVal})"
        elif isinstance(self.leftNode, LexicalToken) and not isinstance(self.rightNode, LexicalToken):
            if self.leftNode.isTokenNegative:
                leftVal = '-' + str(self.leftNode.tokenVal)
            else:
                leftVal = self.leftNode.tokenVal
            return f"({leftVal} {self.root.tokenVal} {self.rightNode})"
        elif not isinstance(self.leftNode, LexicalToken) and isinstance(self.rightNode, LexicalToken):
            if self.rightNode.isTokenNegative:
                rightVal = '-' + str(self.rightNode.tokenVal)
            else:
                rightVal = self.rightNode.tokenVal
            return f"({self.leftNode} {self.root.tokenVal} {rightVal})"
        else:
            return f"({self.leftNode} {self.root.tokenVal} {self.rightNode})"
        

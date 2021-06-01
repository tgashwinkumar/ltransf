from typing import Union
from transf.definitions.token import LexicalToken

class ExpressionNode:
    def __init__(self, root: LexicalToken, leftNode = None, rightNode = None):
        self.root = root
        self.leftNode = leftNode
        self.rightNode = rightNode

class Expression:

    def __init__(self, *tokens):
        self.tokens = tokens

    def getTokens(self):
        return self.tokens

    def __repr__(self):
        return  f"<Expression [{self.tokens} " + "\n]>"

    def __str__(self):
        return f"<Expression [{self.tokens} " + "\n]>"

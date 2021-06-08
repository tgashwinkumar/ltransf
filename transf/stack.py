from typing import Optional, Union
from transf.definitions.token import LexicalToken
from transf.definitions.position import Position
from transf.expression_nodes.binarynode import BinaryNode

class StackToken:
    def __init__(self, tokenValue:Union[LexicalToken, BinaryNode], prevToken: Union[LexicalToken, BinaryNode,None] = None):
        self.tokenValue = tokenValue
        self.prevToken = prevToken

    def __repr__(self):
        if isinstance(self.tokenValue, LexicalToken):
            return '\n' + f"[StackToken]{self.tokenValue}>" 
        else:
            return '\n' + f"[StackToken]{self.tokenValue}>"

    def __str__(self):
        if isinstance(self.tokenValue, LexicalToken):
            return '\n' + f"[StackToken]{self.tokenValue}>"
        else:
            return '\n' + f"[StackToken]{self.tokenValue}>"


class Stack:

    def __init__(self, currentToken: Optional[StackToken] = None):
        self.currentToken = currentToken
        self.pos: Position = Position(0) if currentToken else Position(-1)
        self.length:int = 1 if currentToken else 0

    def push(self, token: Union[StackToken,LexicalToken, BinaryNode]):
        if isinstance(token, (LexicalToken, BinaryNode)):
            token = StackToken(token)
        token.prevToken = self.currentToken
        self.currentToken = token
        self.length += 1
        return self.currentToken

    def pop(self):
        temp = self.currentToken
        self.currentToken = self.currentToken.prevToken
        self.length -= 1
        return temp

    def isEmpty(self):
        return self.length == 0

    def getCurrent(self):
        return self.currentToken.tokenValue

    def copy(self):
        return Stack(self.currentToken)


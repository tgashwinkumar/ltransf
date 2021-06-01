from transf.definitions.expression import Expression, ExpressionNode
from typing import Optional, Union
from transf.definitions.token import LexicalToken
from transf.definitions.position import Position

class StackToken:
    def __init__(self, tokenValue:Union[LexicalToken], prevToken: Union[LexicalToken, None] = None):
        self.tokenValue = tokenValue
        self.prevToken = prevToken

    def __repr__(self):
        return '\n' + f"[StackToken]{self.tokenValue}"

    def __str__(self):
        return '\n' + f"[StackToken]{self.tokenValue}"

    def isLex(self):
        return isinstance(self.tokenValue, LexicalToken)
    
    def isExpNode(self):
        return isinstance(self.tokenValue, ExpressionNode)


class Stack:

    def __init__(self, currentToken: Optional[StackToken] = None):
        self.currentToken = currentToken
        self.pos: Position = Position(0) if currentToken else Position(-1)
        self.length:int = 1 if currentToken else 0

    def push(self, token: Union[StackToken,LexicalToken,Expression]):
        if isinstance(token, (LexicalToken, Expression)):
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


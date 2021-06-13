from typing import List, Optional, Union
from ltransf.definitions.tokentype import TT
from ltransf.definitions.token import LexicalToken
from ltransf.definitions.position import Position

class AdditiveStack:

    def __init__(self, tokens: List[LexicalToken] = []):
        self.tokens = tokens
        self.currPos = Position(-1)
        self.stack = []
        self.currentToken: Optional[LexicalToken] = None
        self.addStack = []

    def __nextToken(self):
        self.currPos.nextPos()
        if self.currPos.idx < len(self.tokens):
            self.currentToken = self.tokens[self.currPos.idx]
        else:
            self.currentToken = None
    
    def __splitStack(self):
        self.__nextToken()
        parenLevel = 0
        lexStack = []
        while self.currentToken:
            if self.currentToken.tokenType == TT.LPAREN or self.currentToken.tokenType == TT.LSQU:
                parenLevel += 1
            elif self.currentToken.tokenType == TT.RPAREN or self.currentToken.tokenType == TT.RSQU:
                parenLevel -= 1
            if not parenLevel == 0:
                lexStack.append(self.currentToken)
                self.__nextToken()
            else:
                if self.currentToken.tokenType == TT.PLUS or self.currentToken.tokenType == TT.MINUS:
                    self.addStack.append(lexStack)
                    self.addStack.append(self.currentToken)
                    lexStack = []
                else:
                    lexStack.append(self.currentToken)
                self.__nextToken()
        if not lexStack == []:
            self.addStack.append(lexStack)
            lexStack = []

    def getStack(self):
        self.__splitStack()
        return self.addStack

    def printStack(self):
        print(self.getStack())

    def add(self, stackValue):
        self.addStack.append(stackValue)
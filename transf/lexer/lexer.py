from typing import Optional

from transf.definitions.position import Position
from transf.definitions.symbol import Symbol
from transf.definitions.token import LexicalToken
from transf.definitions.tokentype import TT


class Lexer:
    def __init__(self, expression: str, symbol: Symbol = Symbol('t')):
        self.expression = expression
        self.symbol = symbol
        self.currPos = Position(-1)
        self.currChar: Optional[str] = None
        self.tokens: list[LexicalToken] = []

    def __nextChar(self):
        self.currPos.nextPos()
        if self.currPos.idx < len(self.expression):
            self.currChar = self.expression[self.currPos.idx]
        else:
            self.currChar = None        

    def __runLexer(self):
        self.__nextChar()
        while self.currChar:
            if self.currChar in ' \n\t':
                self.__nextChar()

            elif self.currChar == '+':
                self.tokens.append(LexicalToken(ttype=TT.PLUS))
                self.__nextChar()
            
            elif self.currChar == '-':
                self.tokens.append(LexicalToken(ttype=TT.MINUS))
                self.__nextChar()

            elif self.currChar == '*':
                self.tokens.append(LexicalToken(ttype=TT.MULTI))
                self.__nextChar()

            elif self.currChar == '^':
                self.tokens.append(LexicalToken(ttype=TT.POWER))
                self.__nextChar()
            
            elif self.currChar == '/':
                self.tokens.append(LexicalToken(ttype=TT.DIVID))
                self.__nextChar()

            elif self.currChar == '(':
                self.tokens.append(LexicalToken(ttype=TT.LPAREN))
                self.__nextChar()

            elif self.currChar == ')':
                self.tokens.append(LexicalToken(ttype=TT.RPAREN))
                self.__nextChar()

            elif self.currChar == '[':
                self.tokens.append(LexicalToken(ttype=TT.LSQU))
                self.__nextChar()

            elif self.currChar == ']':
                self.tokens.append(LexicalToken(ttype=TT.RSQU))
                self.__nextChar()

            elif self.currChar.isdigit():
                number, ttype = self.__fetchDigits()
                self.tokens.append(LexicalToken(ttype = ttype, tval=number))

            elif self.currChar.isalpha():
                ttype, tval = self.__fetchAlpha()
                self.tokens.append(LexicalToken(ttype=ttype, tval=tval))

    def getTokens(self):
        self.__runLexer()
        return self.tokens

    def __repr__(self):
        return "\n<LexerTokens>" + '\n\t'.join(self.getToken()) + "\n</LexerTokens>"

    def __fetchDigits(self):
        number = ""
        isFloat = False
        while self.currChar:
            if self.currChar.isdigit() or (self.currChar == '.' and not isFloat):
                number += self.currChar
                if self.currChar == '.':
                    isFloat = True
                self.__nextChar()
            else:
                break
        return [float(number), TT.FLOAT] if isFloat else [int(number), TT.INT]

    def __fetchAlpha(self):
        word = ""
        while self.currChar:
            if self.currChar.isalpha():
                word += self.currChar
                self.__nextChar()
            else:
                break

        if word.lower() == 'sin':
            return [TT.SIN, None]

        elif word.lower() == 'cos':
            return [TT.COS, None]

        elif word.lower() == 'tan':
            return [TT.TAN, None]

        elif word.lower() == 'sqrt':
            return [TT.SQRT, None]

        elif word.lower() == 'u' or word.lower() == 'ustep':
            return [TT.USTEP, None]

        elif word.lower() == 'd' or word.lower() == 'ddelta':
            return [TT.DDELTA, None]

        elif word.lower() == 'e' or word.lower() == 'exp':
            return [TT.EXP, None]

        elif word.lower() == 'pi':
            return [TT.PI, None]

        elif word == self.symbol.val:
            return [TT.SYMBOL, self.symbol.val]

        elif len(word) == 1:
            return [TT.CONST, word]



            

    

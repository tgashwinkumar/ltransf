from transf.tokentype import TT
from transf.token import LexicalToken
from typing import Optional
from transf.position import Position
from transf.symbol import Symbol


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
                self.tokens.append(LexicalToken(TT.PLUS))
                self.__nextChar()
            
            elif self.currChar == '-':
                self.tokens.append(LexicalToken(TT.MINUS))
                self.__nextChar()

            elif self.currChar == '*':
                self.tokens.append(LexicalToken(TT.MULTI))
                self.__nextChar()

            elif self.currChar == '^':
                self.tokens.append(LexicalToken(TT.POWER))
                self.__nextChar()
            
            elif self.currChar == '/':
                self.tokens.append(LexicalToken(TT.DIVID))
                self.__nextChar()

            elif self.currChar == '(':
                self.tokens.append(LexicalToken(TT.LPAREN))
                self.__nextChar()

            elif self.currChar == ')':
                self.tokens.append(LexicalToken(TT.RPAREN))
                self.__nextChar()

            elif self.currChar == '[':
                self.tokens.append(LexicalToken(TT.LSQU))
                self.__nextChar()

            elif self.currChar == ']':
                self.tokens.append(LexicalToken(TT.RSQU))
                self.__nextChar()

            elif self.currChar.isdigit():
                number, ttype = self.__fetchDigits()
                self.tokens.append(LexicalToken(ttype, number))

            elif self.currChar.isalpha():
                alpha = self.__fetchAlpha()
                if isinstance(alpha, TT):
                    self.tokens.append(LexicalToken(alpha))
                else:
                    self.tokens.append(LexicalToken(TT.CONST, alpha))

    def getToken(self):
        self.__runLexer()
        return self.tokens

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
            return TT.SIN

        elif word.lower() == 'cos':
            return TT.COS

        elif word.lower() == 'tan':
            return TT.TAN

        elif word.lower() == 'sqrt':
            return TT.SQRT

        elif word.lower() == 'u' or word.lower() == 'ustep':
            return TT.USTEP

        elif word.lower() == 'd' or word.lower() == 'ddelta':
            return TT.DDELTA

        elif word.lower() == 'e' or word.lower() == 'exp':
            return TT.EXP

        elif word.lower() == 'pi':
            return TT.PI

        elif word == self.symbol.val:
            return TT.SYMBOL

        elif len(word) == 1:
            return word



            

    

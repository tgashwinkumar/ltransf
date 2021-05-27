from transf.definitions.token import LexicalToken
class Expression:

    def __init__(self, *tokens):
        self.tokens = tokens

    def getTokens(self):
        return self.tokens

    def printExpression(self):
        print(len(self.tokens), self.tokens)

    def __repr__(self):
        return f"<Expression [{self.tokens}] >"

    def __str__(self):
        return f"<Expression [{self.tokens}] >"

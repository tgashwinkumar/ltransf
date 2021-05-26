from transf.definitions.token import LexicalToken
class Expression:

    def __init__(self, *tokens):
        self.tokens = []
        for token in tokens:
            if isinstance(token, (Expression, LexicalToken)):
                self.tokens.append(token)

    def getTokens(self):
        return self.tokens

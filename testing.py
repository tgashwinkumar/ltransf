from transf.lexer.lexer import Lexer
from transf.parser.parser import Parser

lex = Lexer('sin(t+7)+4*5')
print(lex.getToken())
print('\n')

pars = Parser(lex.getToken())
pars.printParser()
from transf.lexer.lexer import Lexer
from transf.parser.parser import Parser

lex = Lexer('34+13*sin(pi)')
print(lex.getToken())
print('\n')

pars = Parser(lex.getToken())
pars.printParser()
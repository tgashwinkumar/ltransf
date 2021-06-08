from transf.additivestack.additivestack import AdditiveStack
from transf.lexer.lexer import Lexer
from transf.parser.parser import Parser

lex = Lexer('t')
print(lex.getToken())
print('\n')

pars = Parser(lex.getToken())
pars.printParser()


#In Binary TRee. 
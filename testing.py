from transf.additivestack.additivestack import AdditiveStack
from transf.lexer.lexer import Lexer
from transf.parser.parser import Parser

lex = Lexer('34+12+sin(pi)')
print(lex.getToken())
print('\n')

addiStack = AdditiveStack(lex.getToken())
addiStack.printStack()


#In Binary TRee. 
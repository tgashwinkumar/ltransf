from transf.laplace.laplaceof import LaplaceOf
from transf.additivestack.additivestack import AdditiveStack
from transf.lexer.lexer import Lexer
from transf.parser.parser import Parser

exprStr = 't + 3 + sinh(2*t)'
print("The given strings is : " , exprStr, "\nThe laplace is: ")
lapl = LaplaceOf(expressionText=exprStr)
lapl.evaluate()

# lex = Lexer('+3+4+-sin(-4)')
# print(lex.getTokens())

#In Binary Tree. 

# print(int(34.010) == 34.010)

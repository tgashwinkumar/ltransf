from ltransf.laplace.laplaceof import LaplaceOf
# from transf.additivestack.additivestack import AdditiveStack
# from transf.lexer.lexer import Lexer
# from transf.parser.parser import Parser

exprStr = 'ustep(t-3)'
print("The given strings is : " , exprStr, "\nThe laplace is: ")
lapl = LaplaceOf(expressionText=exprStr)
lapl.evaluate()

# lex = Lexer('+3+4+-sin(-4)')
# print(lex.getTokens())

#In Binary Tree. 

# print(int(34.010) == 34.010)

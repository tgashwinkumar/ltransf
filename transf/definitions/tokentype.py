from enum import Enum

class TC(Enum):
    OPER = 0
    PAREN = 1
    SQUPAREN = 2
    CONST = 3
    DIGIT = 4
    FUNC = 5
    SYMBOL = 6

class TT(Enum):

    NULL = None
    PLUS = '+'
    MINUS = '-'
    MULTI = '*'
    DIVID = '/'
    POWER = '^'
    SYMBOL = 'symbol'
    INT = 'int'
    FLOAT = 'float'
    SIN = 'sin'
    COS = 'cos'
    SINH = 'sinh'
    COSH = 'cosh'
    SQRT = 'sqrt'
    USTEP = 'ustep'
    DDELTA = 'ddelta'
    LPAREN = '('
    RPAREN = ')'
    LSQU = '['
    RSQU = ']'
    EXP = 'exp'
    PI = 'pi'
    CONST = 'const'

class ET(Enum):
    ERR = -1
    ADD = 0
    SUBT = 1
    PROD = 2
    FRAC = 3
    EXP = 4
    TRIG = 5
    USTEP = 6
    DDELTA = 7
    SQRT = 8
    POLY = 9
    CONST = 10
    


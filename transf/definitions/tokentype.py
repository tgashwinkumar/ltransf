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
    TAN = 'tan'
    SQRT = 'sqrt'
    USTEP = 'ustep'
    DDELTA = 'ddelta'

    LPAREN = '('
    RPAREN = ')'

    LSQU = '['
    RSQU = ']'

    EXP = 'e'
    PI = 'pi'
    CONST = 'const'


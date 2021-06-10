from transf.definitions.tokentype import TT
from transf.definitions.token import LexicalToken
from transf.expression_nodes.udfunc_expnode import UdFuncExpNode


def UDFuncLTrans(expNode: UdFuncExpNode):
    operator = LexicalToken(TT.POWER)
    
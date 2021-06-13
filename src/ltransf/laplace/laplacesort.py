from typing import Union
from ltransf.laplace.ltrans import LTrans
from ltransf.expression_nodes.trigfunc_expnode import TrigFuncExpNode
from ltransf.definitions.token import LexicalToken
from ltransf.expression_nodes.binarynode import BinaryNode
from ltransf.expression_nodes.udfunc_expnode import UdFuncExpNode

def LaplaceSort(node: Union[LexicalToken, BinaryNode]):
    if isinstance(node, TrigFuncExpNode):
        return LTrans.trigFunc(expNode=node)
    elif isinstance(node, UdFuncExpNode):
        return LTrans.UDFunc(expNode=node)
    elif isinstance(node, LexicalToken):
        return LTrans.lexTokenFunc(expNode=node)

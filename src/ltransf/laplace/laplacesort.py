from typing import Union
from .ltrans import LTrans
from ..expression_nodes.trigfunc_expnode import TrigFuncExpNode
from ..definitions.token import LexicalToken
from ..expression_nodes.binarynode import BinaryNode
from ..expression_nodes.udfunc_expnode import UdFuncExpNode

def LaplaceSort(node: Union[LexicalToken, BinaryNode]):
    if isinstance(node, TrigFuncExpNode):
        return LTrans.trigFunc(expNode=node)
    elif isinstance(node, UdFuncExpNode):
        return LTrans.UDFunc(expNode=node)
    elif isinstance(node, LexicalToken):
        return LTrans.lexTokenFunc(expNode=node)

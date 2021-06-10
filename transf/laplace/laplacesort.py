from typing import Union
from transf.definitions.token import LexicalToken
from transf.expression_nodes.binarynode import BinaryNode
from transf.laplace.ltrans import LTrans
from transf.expression_nodes.udfunc_expnode import UdFuncExpNode
from transf.expression_nodes.trigfunc_expnode import TrigFuncExpNode

def LaplaceSort(node: Union[LexicalToken, BinaryNode]):
    if isinstance(node, TrigFuncExpNode):
        return LTrans.trigFunc(expNode=node)
    elif isinstance(node, UdFuncExpNode):
        return LTrans.UDFunc(expNode=node)
    elif isinstance(node, LexicalToken):
        return LTrans.lexTokenFunc(expNode=node)

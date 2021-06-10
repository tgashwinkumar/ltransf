from transf.laplace.udfunc_ltrans import UDFuncLTrans
from transf.laplace.trigfunc_ltrans import trigFuncLTrans
from transf.expression_nodes.udfunc_expnode import UdFuncExpNode
from transf.expression_nodes.trigfunc_expnode import TrigFuncExpNode

class LTrans:

    @staticmethod
    def trigFunc(expNode: TrigFuncExpNode):
        return trigFuncLTrans(expNode)

    @staticmethod
    def udfunc(expNode: UdFuncExpNode):
        return UDFuncLTrans(expNode)

        

from ltransf.definitions.token import LexicalToken
from ltransf.expression_nodes.powern_expnode import PowerNExpNode
from ltransf.expression_nodes.trigfunc_expnode import TrigFuncExpNode
from ltransf.expression_nodes.udfunc_expnode import UdFuncExpNode
from ltransf.laplace.lextokenfunc_ltrans import LexTokenFuncLTrans
from ltransf.laplace.trigfunc_ltrans import trigFuncLTrans
from ltransf.laplace.udfunc_ltrans import UDFuncLTrans


class LTrans:

    @staticmethod
    def trigFunc(expNode: TrigFuncExpNode):
        return trigFuncLTrans(expNode)

    @staticmethod
    def UDFunc(expNode: UdFuncExpNode):
        return UDFuncLTrans(expNode)

    @staticmethod
    def lexTokenFunc(expNode: LexicalToken):
        return LexTokenFuncLTrans(expNode)

    @staticmethod
    def powerNFunc(expNode: PowerNExpNode):
        # return PowerNFuncLTrans(expNode)
        return

        

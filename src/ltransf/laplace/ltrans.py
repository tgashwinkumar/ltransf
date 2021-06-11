from .udfunc_ltrans import UDFuncLTrans
from .trigfunc_ltrans import trigFuncLTrans
from .lextokenfunc_ltrans import LexTokenFuncLTrans
from ..definitions.token import LexicalToken
from ..expression_nodes.powern_expnode import PowerNExpNode
from ..expression_nodes.udfunc_expnode import UdFuncExpNode
from ..expression_nodes.trigfunc_expnode import TrigFuncExpNode

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

        

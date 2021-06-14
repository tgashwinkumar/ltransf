from ltransf.definitions.token import LexicalToken
from ltransf.expression_nodes.constmultipoly_expnode import ConstMultiPolyExpNode
from ltransf.expression_nodes.powern_expnode import PowerNExpNode
from ltransf.expression_nodes.trigfunc_expnode import TrigFuncExpNode
from ltransf.expression_nodes.udfunc_expnode import UdFuncExpNode
from ltransf.laplace.constmutlipolyfunc_ltrans import ConstMultiPolyFuncLTrans
from ltransf.laplace.lextokenfunc_ltrans import LexTokenFuncLTrans
from ltransf.laplace.powernfunc_ltrans import PowerNFuncLTrans
from ltransf.laplace.trigfunc_ltrans import trigFuncLTrans
from ltransf.laplace.udfunc_ltrans import UDFuncLTrans


class LTrans:

    @staticmethod
    def trigFunc(expNode: TrigFuncExpNode, symbolToken: LexicalToken):
        return trigFuncLTrans(expNode, symbolToken)

    @staticmethod
    def UDFunc(expNode: UdFuncExpNode, symbolToken: LexicalToken):
        return UDFuncLTrans(expNode, symbolToken)

    @staticmethod
    def lexTokenFunc(expNode: LexicalToken, symbolToken: LexicalToken):
        return LexTokenFuncLTrans(expNode, symbolToken)

    @staticmethod
    def powerNFunc(expNode: PowerNExpNode, symbolToken: LexicalToken):
        return PowerNFuncLTrans(expNode, symbolToken)

    @staticmethod
    def constMultiPolyFunc(expNode: ConstMultiPolyExpNode, symbolToken: LexicalToken):
        return ConstMultiPolyFuncLTrans(expNode, symbolToken)

        

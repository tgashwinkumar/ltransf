from ltransf.definitions.symbol import Symbol
from ltransf.definitions.token import LexicalToken
from ltransf.definitions.tokentype import TC, TT
from ltransf.expression_nodes.binarynode import BinaryNode
from ltransf.expression_nodes.powern_expnode import PowerNExpNode


def LexTokenFuncLTrans(expNode: LexicalToken):
    symbolToken = LexicalToken(TT.SYMBOL, tval=Symbol('s').val)

    if expNode.tokenType == TT.SYMBOL:
        denom = PowerNExpNode(
            root=LexicalToken(TT.POWER),
            leftNode=symbolToken,
            rightNode=LexicalToken(TT.INT, 2)
        )
        return BinaryNode(
            root=LexicalToken(TT.DIVID),
            leftNode=LexicalToken(TT.INT, 1),
            rightNode=denom
        )

    elif expNode.tokenClass == TC.CONST or expNode.tokenClass == TC.DIGIT:
        if expNode.tokenVal == 0:
            return LexicalToken(TT.INT, tval=0)
        return BinaryNode(
            root=LexicalToken(TT.DIVID),
            leftNode=LexicalToken(expNode.tokenType, tval=expNode.tokenVal, isNeg=expNode.isTokenNegative),
            rightNode=symbolToken
        )
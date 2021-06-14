from typing import Union
from ltransf.definitions.tokentype import TC, TT
from ltransf.expression_nodes.constevalconst_expnode import ConstEvalConstExpNode
from ltransf.expression_nodes.constmultipoly_expnode import ConstMultiPolyExpNode
from ltransf.expression_nodes.exponential_expnode import ExponentialExpNode
from ltransf.expression_nodes.power1_expnode import Power1ExpNode
from ltransf.expression_nodes.powern_expnode import PowerNExpNode
from ltransf.expression_nodes.trigfunc_expnode import TrigFuncExpNode
from ltransf.definitions.token import LexicalToken
from ltransf.expression_nodes.binarynode import BinaryNode
from ltransf.expression_nodes.udfunc_expnode import UdFuncExpNode

def LaplaceSort(node: Union[LexicalToken, BinaryNode], symbolToken: LexicalToken):
    if isinstance(node, ConstMultiPolyExpNode):
        return ConstMultiPolyFuncLTrans(expNode=node, symbolToken=symbolToken)
    elif isinstance(node, TrigFuncExpNode):
        return trigFuncLTrans(expNode=node, symbolToken=symbolToken)
    elif isinstance(node, UdFuncExpNode):
        return UDFuncLTrans(expNode=node, symbolToken=symbolToken)
    elif isinstance(node, LexicalToken):
        return LexTokenFuncLTrans(expNode=node, symbolToken=symbolToken)
    elif isinstance(node, PowerNExpNode):
        return PowerNFuncLTrans(expNode=node, symbolToken=symbolToken)
    

def LexTokenFuncLTrans(expNode: LexicalToken, symbolToken: LexicalToken):
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
            leftNode=LexicalToken(
                expNode.tokenType, tval=expNode.tokenVal, isNeg=expNode.isTokenNegative),
            rightNode=symbolToken
        )


def trigFuncLTrans(expNode: TrigFuncExpNode, symbolToken: LexicalToken):
    param = expNode.param
    funcType = expNode.funcType

    if funcType == TT.SIN or funcType == TT.SINH:
        numer = param
    elif funcType == TT.COS or funcType == TT.COSH:
        numer = symbolToken

    if funcType == TT.SINH or funcType == TT.COSH:
        denom = BinaryNode(root=LexicalToken(TT.MINUS))
    elif funcType == TT.SIN or funcType == TT.COS:
        denom = BinaryNode(root=LexicalToken(TT.PLUS))

    denom.leftNode = PowerNExpNode(
        root=LexicalToken(TT.POWER),
        leftNode=symbolToken,
        rightNode=LexicalToken(TT.INT, 2)
    )

    denom.rightNode = ConstEvalConstExpNode(
        root=LexicalToken(TT.POWER),
        leftNode=param,
        rightNode=LexicalToken(TT.INT, 2)
    ).evaluate()

    return BinaryNode(
        root=LexicalToken(TT.DIVID),
        leftNode=numer,
        rightNode=denom
    )


def ConstMultiPolyFuncLTrans(expNode: ConstMultiPolyExpNode, symbolToken: LexicalToken):
    const = expNode.const
    poly = expNode.poly
    polyLaplace = LaplaceSort(poly, symbolToken)
    if isinstance(polyLaplace, LexicalToken):
        if polyLaplace.tokenClass == TC.DIGIT or polyLaplace.tokenClass == TC.CONST:
            return ConstEvalConstExpNode(
                root=LexicalToken(TT.MULTI),
                leftNode=const,
                rightNode=polyLaplace
            ).evaluate()
    elif isinstance(polyLaplace, BinaryNode):
        if polyLaplace.root.tokenType == TT.DIVID:
            if isinstance(polyLaplace.leftNode, LexicalToken):
                if polyLaplace.leftNode.tokenClass == TC.DIGIT or polyLaplace.leftNode.tokenClass == TC.CONST:
                    polyLaplace.leftNode = ConstEvalConstExpNode(
                        root=LexicalToken(TT.MULTI),
                        leftNode=const,
                        rightNode=polyLaplace.leftNode
                    ).evaluate()
                elif polyLaplace.leftNode.tokenType == TT.SYMBOL:
                    polyLaplace.leftNode = Power1ExpNode(
                        root=LexicalToken(TT.MULTI),
                        leftNode=const,
                        rightNode=polyLaplace.leftNode
                    )
        return polyLaplace


def UDFuncLTrans(expNode: UdFuncExpNode, symbolToken: LexicalToken):
    param = expNode.param
    funcType = expNode.funcType

    if funcType == TT.DDELTA:
        if param.tokenVal == 0:
            return LexicalToken(TT.INT, 1)
        power = Power1ExpNode(
            root=LexicalToken(TT.MULTI),
            leftNode=LexicalToken(
                param.tokenType, param.tokenVal, isNeg=param.isTokenNegative),
            rightNode=symbolToken
        )
        return ExponentialExpNode(
            root=LexicalToken(TT.POWER),
            leftNode=LexicalToken(TT.EXP),
            rightNode=power
        )

    elif funcType == TT.USTEP:
        if param.tokenVal == 0:
            return BinaryNode(
                root=LexicalToken(TT.DIVID),
                leftNode=LexicalToken(TT.INT, 1),
                rightNode=symbolToken
            )
        power = Power1ExpNode(
            root=LexicalToken(TT.MULTI),
            leftNode=LexicalToken(
                param.tokenType, param.tokenVal, isNeg=param.isTokenNegative),
            rightNode=symbolToken
        )

        numer = ExponentialExpNode(
            root=LexicalToken(TT.POWER),
            leftNode=LexicalToken(TT.EXP),
            rightNode=power
        )

        return BinaryNode(
            root=LexicalToken(TT.DIVID),
            leftNode=numer,
            rightNode=symbolToken
        )


def factorial(n: int):
    prod = 1
    while n > 0:
        prod *= n
        n -= 1
    return prod


def PowerNFuncLTrans(expNode: PowerNExpNode, symbolToken: LexicalToken):

    param = expNode.param
    numer = LexicalToken(TT.INT, factorial(param.tokenVal))
    denom = PowerNExpNode(
        root=LexicalToken(TT.POWER),
        leftNode=symbolToken,
        rightNode=LexicalToken(TT.INT, param.tokenVal + 1)
    )
    return BinaryNode(
        root=LexicalToken(TT.DIVID),
        leftNode=numer,
        rightNode=denom
    )

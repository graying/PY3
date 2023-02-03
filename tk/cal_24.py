#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 14:21:18 2019

@author: eddy

module to calculate 4 digits for 24
"""
import itertools

DIGI = 24

"""
+ -> 1
- -> 2
* -> 3
/ -> 4
"""
OP = {1: '+',
      2: '-',
      3: '*',
      4: '/'}


def print24(num, oper):
    print("((", num[0], OP[oper[0]], num[1], ')', OP[oper[1]], num[2], ')', OP[oper[2]], num[3], '=', DIGI)


def print24_bkw(num, oper):
    """
    A*(B/(C-D))
    """
    print(num[0], OP[oper[0]], '(', num[1], OP[oper[1]], '(', num[2], OP[oper[2]], num[3], "))", '=', DIGI)


def try_get_24(num, op):
    top = num[0]
    bottom = 1
    for i in range(0, len(op)):
        # num[0] () num[1]
        if op[i] == 4:
            # top = top * num[i+1]
            bottom = bottom * num[i + 1]
        elif op[i] == 3:
            top = top * num[i + 1]
        elif op[i] == 2:
            top = top - bottom * num[i + 1]
        elif op[i] == 1:
            top = top + bottom * num[i + 1]

    if (abs(top / bottom) == DIGI):
        print24(num, op)

        # backward calculate
    # format a#(b#(c#d))
    btop = num[3]
    bbottom = 1
    for i in range(len(op) - 1, -1, -1):
        if op[i] == 4:
            temp = bbottom
            bbottom = btop
            btop = num[i] * temp
        elif op[i] == 3:
            btop = num[i] * btop
        elif op[i] == 2:
            btop = num[i] * bbottom - btop
        elif op[i] == 1:
            btop = num[i] * bbottom + btop

    if bbottom == 0:
        if btop == 24:
            print24_bkw(num, op)
    elif abs(btop / bbottom) == DIGI:
        print24_bkw(num, op)

    return


def cal24(a, b, c, d):
    """
    calculate possible combination to get result of 24
    """
    # 产生各种组合
    num_all = itertools.permutations([a, b, c, d])
    # 产生各种运算符的组合，
    """
    + -> 1
    - -> 2
    * -> 3
    / -> 4
    """
    operator_all = []
    for i in range(1, 4 + 1):  # 1 to 4
        for j in range(1, 4 + 1):
            for k in range(1, 4 + 1):
                operator_all.append([i, j, k])
    for num in num_all:
        for operator in operator_all:
            #            print ("num=",num)
            #            print ("operator=",operator)
            try_get_24(num, operator)

    return


if __name__ == "__main__":
    cal24(2, 9, 3, 6)
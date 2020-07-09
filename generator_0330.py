# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/3/30 14:25
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : generator_0330.py
# @Software: PyCharm

# squares = (x**2 for x in range(3))
# print(squares)
# print(next(squares))
# print(next(squares))
# print(next(squares))
# print(list(squares))


def flatten(nested):
    try:
        # 如果是字符串，那么手动抛出TypeError。
        if isinstance(nested, str):
            raise TypeError
        for sublist in nested:
            # yield flatten(sublist)
            for element in flatten(sublist):
                # yield element
                print('got:', element)
    except TypeError:
        # print('here')
        yield nested     #生成器函数


L = ['aaadf', [1, 2, 3], 2, 4, [5, [6, [8, [9]], 'ddf'], 7]]
for num in flatten(L):
    print(num)
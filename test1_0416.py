# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/16 10:43
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : test1_0416.py
# @Software: PyCharm

import numpy

#纯python实现
def pythonsum(n):
    a = range(n)
    b = range(n)
    c = []
    for i in range(len(a)):
        a[i] = i ** 2
        b[i] = i ** 3
        c.append(a[i] + b[i])
    return c
c = pythonsum(10)
pythonsum(c[-2:])

#numpy
# def numpysum(n):
#     a = numpy.arange(n) ** 2
#     b = numpy.arange(n) ** 3
#     c = a + b
#     return c
# sum2 = numpysum(10)
# print(sum2)

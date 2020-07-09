# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/23 9:59
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : minlin_04223.py
# @Software: PyCharm

import numpy as np
from numpy import *
import sys
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

#最小二乘法
N = int(sys.argv[-1])
c = loadtxt("stocks.csv", delimiter=",", usecols=(4, ), unpack=True)
b = c[-N:]       #倒着N个数
b = b[::-1]     #颠倒顺序
print("b:",b)

A = np.zeros((N,N),float)
print("A:",A)

for i in range(N):
    A[i, ] = c[-N - 1 - i : -1 -i]
print("A:",A)

(x, residuals,rank,s) = np.linalg.lstsq(A,b)

print(x,residuals,rank,s)
print(np.dot(b,x))

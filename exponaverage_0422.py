# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/22 22:45
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : exponaverage_0422.py
# @Software: PyCharm

import numpy as np
from numpy import *
import sys
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

#指数移动平均线

x = np.arange(5)
print("Exp",np.exp(x))

print("Linspace",np.linspace(-1,0,5))
N = int(sys.argv[1])

weights = np.exp(np.linspace(-1.,0.,N))
weights /= weights.sum()
print("Weights",weights)

c = loadtxt("stocks.csv", delimiter=",", usecols=(4, ), unpack=True)
ema = np.convolve(weights, c)[N - 1:-N + 1]
t = np.arange(N - 1, len(c))
plot(t, c[N - 1:], lw=1.0)
plot(t, ema, lw=2.0)
show()

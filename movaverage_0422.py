# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/22 15:58
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : movaverage_0422.py
# @Software: PyCharm

import numpy as np
from numpy import *
import sys
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

N = int(sys.argv[1])

weights = np.ones(N) / N
print("weights:", weights)

c = loadtxt("stocks.csv", delimiter=",", usecols=(4, ), unpack=True)
sma = np.convolve(weights, c)[N - 1:-N + 1]
t = np.arange(N - 1, len(c))
plot(t, c[N - 1:], lw=1.0)
plot(t, sma, lw=2.0)
show()

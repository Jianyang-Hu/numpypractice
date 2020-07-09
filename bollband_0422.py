# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/22 23:46
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : bollband_0422.py
# @Software: PyCharm

import numpy as np
from numpy import *
import sys
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
#布林带

N = int(sys.argv[1])
weights = np.ones(N) / N
print("weights:", weights)

c = loadtxt("stocks.csv", delimiter=",", usecols=(4, ), unpack=True)
sma = np.convolve(weights, c)[N - 1:-N + 1]
deviation = []
C = len(c)

for i in range(N - 1,C):
    if i + N < C :
        dev = c[i : i+N]
    else:
        dev = c[-N:]

    averages = np.zeros(N)
    averages.fill(sma[i- N- 1])
    dev = dev - averages
    dev = dev ** 2
    dev = np.sqrt(np.mean(dev))
    deviation.append(dev)

deviation = 2 * np.array(deviation)
print(len(deviation),len(sma))
upperBB = sma + deviation
lowerBB = sma - deviation

c_slice = c[N-1:]
between_bands = np.where((c_slice < upperBB) & (c_slice > lowerBB))

print(lowerBB[between_bands])
print(c[between_bands])
print(upperBB[between_bands])

between_bands = len(np.ravel(between_bands))
print("Ration between bands",float(between_bands)/len(c_slice))

t = np.arange(N - 1, C)
plot(t,c_slice,lw=1.0)
plot(t,sma,lw=2.0)
plot(t,upperBB,lw=3.0)
plot(t,lowerBB,lw=4.0)
show()

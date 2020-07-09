# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/23 15:07
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : corrcoef_0423.py
# @Software: PyCharm

import numpy as np
from numpy import *
import sys, importlib
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

# 相关性分析
bhp = loadtxt("stocks.csv", delimiter=",", usecols=(4,), unpack=True)
bhp_returns = np.diff(bhp) / bhp[:-1]


vale = np.loadtxt("sh000001.csv", delimiter=",", usecols=(4,), unpack=True)
vale_returns = np.diff(vale) / vale[:-1]


convariance = np.cov(bhp_returns, vale_returns)
print("Convariance:", convariance)

print("Convariance diagonal:", convariance.diagonal())
print("Convariance trace:", convariance.trace())
print(convariance / (bhp_returns.std() * vale_returns.std()))
print("Correlation coefficient", np.corrcoef(bhp_returns, vale_returns))

difference = bhp - vale
avg = np.mean(difference)
dev = np.std(difference)

print("Out of sync", np.abs(difference[-1] - avg) > 2 * dev)

t = np.arange(len(bhp_returns))
plot(t, bhp_returns, lw=1)
plot(t, vale_returns, lw=2)
show()

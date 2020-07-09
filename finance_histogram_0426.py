# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/26 14:48
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : finance_histogram_0426.py
# @Software: PyCharm
#股价分布直方图
from matplotlib.finance import _quotes_historical_yahoo
import sys
from datetime import date
import matplotlib.pyplot as plt
import numpy as np
from numpy import *


today = date.today()
start = (today.year - 1, today.month, today.day)
symbol = 'DISH'
if len(sys.argv) == 2:
    symbol = sys.argv[1]
quotes = _quotes_historical_yahoo(symbol, start, today)
quotes = np.array(quotes)
close = quotes.T[4] #提取出收盘价数据,T是转置
plt.hist(close, np.sqrt(len(close)))
plt.show()

#报错TypeError: 'numpy.float64' object cannot be interpreted as an integer
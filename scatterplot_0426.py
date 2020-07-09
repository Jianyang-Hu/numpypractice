# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/26 16:24
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : scatterplot_0426.py
# @Software: PyCharm

from matplotlib.finance import _quotes_historical_yahoo
import sys
from datetime import date
import matplotlib.pyplot as plt
import numpy as np
today = date.today()
start = (today.year - 1, today.month, today.day)

symbol = 'DISH'
if len(sys.argv) == 2:
    symbol = sys.argv[1]

quotes = _quotes_historical_yahoo(symbol, start, today)
quotes = np.array(quotes)
close = quotes.T[4]
volume = quotes.T[5]

#计算股票收益率和成交量的变化值
ret = np.diff(close)/close[:-1] #out[n] = a[n+1] - a[n]
volchange = np.diff(volume)/volume[:-1]

fig = plt.figure()
ax = fig.add_subplot(111)
#数据点的颜色与股票收益率相关联，数据点的大小与成交量的变化相关联 c,color s,size
ax.scatter(ret, volchange, c=ret * 100, s=volchange * 100, alpha=0.5)
ax.set_title('Close and volume returns')
ax.grid(True)
plt.show()
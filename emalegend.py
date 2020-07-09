# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/26 16:28
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : emalegend.py
# @Software: PyCharm

from matplotlib.finance import _quotes_historical_yahoo
from matplotlib.dates import DateFormatter
from matplotlib.dates import DayLocator
from matplotlib.dates import MonthLocator
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
dates = quotes.T[0]
close = quotes.T[4]

fig = plt.figure()
ax = fig.add_subplot(111)

#计算并绘制指数移动平均线(第3章),分别使用9、12和15作为周期数计算和绘制指数移动平均线。
# 添加了一个图例，并使用注释将其中两条曲线的交点标注了出来。
# 其中两条曲线的交点标注了出来
# 其中两条曲线的交点标注了出来。示
# 方法。分别使用9、12和15作为周期数计算和绘制指数移动平均线。
emas = []
for i in range(9, 18, 3):
    weights = np.exp(np.linspace(-1., 0., i))
    weights /= weights.sum()
    ema = np.convolve(weights, close)[i-1:-i+1]
    idx = (i - 6)/3
    ax.plot(dates[i-1:], ema, lw=idx, label="EMA(%s)" % (i))
    data = np.column_stack((dates[i-1:], ema))
    emas.append(np.rec.fromrecords(data, names=["dates", "ema"]))

#找到两条指数移动平均曲线的交点。
first = emas[0]["ema"].flatten()
second = emas[1]["ema"].flatten()
bools = np.abs(first[-len(second):] - second)/second < 0.0001
xpoints = np.compress(bools, emas[1])

#将找到的交点用注释和箭头标注出来，并确保注释文本在交点的不远处。
for xpoint in xpoints:
    ax.annotate('x', xy=xpoint, textcoords='offset points',xytext=(-50, 30),arrowprops=dict(arrowstyle="->"))

#添加一个图例并由Matplotlib自动确定其摆放位置。
leg = ax.legend(loc='best', fancybox=True)

#设置alpha通道值，将图例透明化。
leg.get_frame().set_alpha(0.5)

alldays = DayLocator()
months = MonthLocator()
month_formatter = DateFormatter("%b %Y")
ax.plot(dates, close, lw=1.0, label="Close")
ax.xaxis.set_major_locator(months)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(month_formatter)
ax.grid(True)
fig.autofmt_xdate()
plt.show()
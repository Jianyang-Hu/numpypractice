# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/26 23:38
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : trend_0426.py
# @Software: PyCharm

from matplotlib.finance import _quotes_historical_yahoo
from datetime import date
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from matplotlib.dates import DayLocator
from matplotlib.dates import MonthLocator

#获取QQQ的收盘价和对应的日期数据
today = date.today()
start = (today.year - 1, today.month, today.day)
quotes = _quotes_historical_yahoo("QQQ", start, today)
quotes = np.array(quotes)
dates = quotes.T[0]
qqq = quotes.T[4]

#去除信号中的线性趋势
y = signal.detrend(qqq)

#创建月定位器和日定位器
alldays = DayLocator()
months = MonthLocator()

#创建一个日期格式化器以格式化x轴上的日期。该格式化器将创建一个字符串，包含简写的月份和年份
month_formatter = DateFormatter("%b %Y")

fig = plt.figure()
ax = fig.add_subplot(111)

#绘制股价数据以及将去除趋势后的信号从原始数据中减去所得到的潜在趋势
plt.plot(dates, qqq, 'o', dates, qqq - y, '-')

#设置定位器和格式化器
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(month_formatter)

#将x轴上的标签格式化为日期
fig.autofmt_xdate()
plt.show()
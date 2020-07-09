# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/26 0:06
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : matplotlib_finance_0426.py
# @Software: PyCharm
#matplotlib.finance从雅虎下载股票数据
from numpy import *
from matplotlib.pyplot import *
from matplotlib.dates import DateFormatter
from matplotlib.dates import DayLocator
from matplotlib.dates import MonthLocator
from matplotlib.finance import quotes_historical_yahoo_ochl
from matplotlib.finance import candlestick_ochl
import sys,pandas
from datetime import date
import matplotlib.pyplot as plt

today = date.today()
start = (today.year - 1,today.month,today.day)

alldays = DayLocator()
months = MonthLocator()
month_formatter = DateFormatter("%b %Y")

symbol = "DISH"

if len(sys.argv) == 2:
    symbol = sys.argv[1]

quotes = quotes_historical_yahoo_ochl(symbol,start,today)

fig = figure()
ax = fig.add_subplot(111)
ax.xaxis.set_major_locator(months)
ax.xaxis.set_minor_locater(alldays)
ax.xaxis.set_major_formatter(month_formatter)

candlestick_ochl(ax,quotes)
fig.autofmt_xdate()
plt.show()
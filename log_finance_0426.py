# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/26 16:14
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : log_finance_0426.py
# @Software: PyCharm

from matplotlib.finance import _quotes_historical_yahoo
from matplotlib.dates import DateFormatter
from matplotlib.dates import DayLocator
from matplotlib.dates import MonthLocator
import sys
from datetime import date
import matplotlib.pyplot as plt
import numpy as np

#对数坐标图

today = date.today()
start = (today.year - 1, today.month, today.day)

symbol = 'DISH'
if len(sys.argv) == 2:
    symbol = sys.argv[1]

quotes = _quotes_historical_yahoo(symbol, start, today)
quotes = np.array(quotes)
dates = quotes.T[0]
volume = quotes.T[5]
alldays = DayLocator()
months = MonthLocator()
month_formatter = DateFormatter("%b %Y")

fig = plt.figure()
ax = fig.add_subplot(111)
plt.semilogy(dates, volume)
ax.xaxis.set_major_locator(months)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(month_formatter)
fig.autofmt_xdate()
plt.show()
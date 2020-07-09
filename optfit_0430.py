# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/30 15:48
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : optfit_0430.py
# @Software: PyCharm

from matplotlib.finance import _quotes_historical_yahoo
import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
from scipy import signal
from matplotlib.dates import DateFormatter
from matplotlib.dates import DayLocator
from matplotlib.dates import MonthLocator
from scipy import optimize

#模拟正弦波

start = (2010, 7, 25)
end = (2011, 7, 25)

quotes = _quotes_historical_yahoo("QQQ", start, end)
quotes = np.array(quotes)

dates = quotes.T[0]
qqq = quotes.T[4]


y = signal.detrend(qqq)


alldays = DayLocator()
months = MonthLocator()
month_formatter = DateFormatter("%b %Y")

fig = plt.figure()
fig.subplots_adjust(hspace=.3)
ax = fig.add_subplot(211)

ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(month_formatter)
ax.tick_params(axis='both', which='major', labelsize='x-large')

amps = np.abs(fftpack.fftshift(fftpack.rfft(y)))
amps[amps < amps.max()] = 0

#正弦波模型
def residuals(p, y, x):
   A,k,theta,b = p
   err = y-A * np.sin(2* np.pi* k * x + theta) + b

   return err

#滤波的信号变换回时域
filtered = -fftpack.irfft(fftpack.ifftshift(amps))

#猜测参数的值
N = len(qqq)
f = np.linspace(-N/2, N/2, N)
p0 = [filtered.max(), f[amps.argmax()]/(2*N), 0, 0]
print ("P0", p0)

plsq = optimize.leastsq(residuals, p0, args=(filtered, dates))
p = plsq[0]
print ("P", p)
plt.plot(dates, y, 'o', label="detrended")
plt.plot(dates, filtered, label="filtered")
plt.plot(dates, p[0] * np.sin(2 * np.pi * dates * p[1] + p[2]) + p[3], '^', label="fit")
fig.autofmt_xdate()
plt.legend(prop={'size':'x-large'})

ax2 = fig.add_subplot(212)
ax2.tick_params(axis='both', which='major', labelsize='x-large')
plt.plot(f, amps, label="transformed")

plt.legend(prop={'size':'x-large'})
plt.show()

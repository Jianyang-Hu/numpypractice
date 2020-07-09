# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/21 15:56
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : stock_csv_0421.py
# @Software: PyCharm
import numpy
from numpy import *
from datetime import datetime

#usecols=(4,5)计数从0开始
c,v = loadtxt("stocks.csv",delimiter=",",usecols=(4,5),unpack=True)
#加权平均价格
vwap = average(c,weights=v)
print("VWAP=",vwap)

#算术平均值
print("mean=",mean(c))

#范围
print("the price span is:",ptp(c))

#价格的中位数
print("the median=",median(c))

#排序并且检查中位数
sorted_close = msort(c)
print("sorted:",sorted_close)

#中位数位置
N = len(c)
# mid = sorted()
print(N)

#求股票收益率
returns = diff(c) / c[:-1]
print("Standard deviation = ", std(returns))

#哪个交易日收益为正
posretindices = where(returns > 0)
print("indices with positive returns",posretindices)

#波动率
logreturns = diff(log(c))
annual_volatility = std(logreturns) / mean(logreturns)
annual_volatility = annual_volatility / sqrt(1./252.)
print("Annual volatility",annual_volatility)
print("Monthly volatility",annual_volatility * sqrt(1./12.))

#处理日期
# def datastr2num(s):
#     return datetime.datetime.strptime\
#             (s,"%d-%m-%Y").date().weekday()
# datas,c2 = loadtxt("stocks.csv",delimiter=",",usecols=(0,4),converters={1:datastr2num},unpack=True)
# print(datas)
#
# averages = zeros(5)
#
# for i in range(5):
#     indices = where(datas == i)
#     prices = take(c2,indices)
#     avg = mean(prices)
#     print("Day",i,"prices",prices,"averag",avg)
#     average[i] = avg

# top = max(averages)
# print("Top day of the week",argmax(averages))
#
# bottom = min(averages)
# print("Bottom day of the day",argmin(averages))

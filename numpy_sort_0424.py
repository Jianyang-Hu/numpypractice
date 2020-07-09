# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/24 21:56
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : numpy_sort_0424.py
# @Software: PyCharm

"""
Numpy排序函数：
sort返回排序后的数组
lexsort根据键值得字典序进行排序
argsort返回输入数组排序后的下标

"""

#按字典序排序
import numpy as np
import datetime

# def datestr2num(s):
#     s = str(s,'utf-8')
#     return datetime.datetime.strptime(s,"%Y-%m-%d").toordinal()
# """
# converters : dict, optional
# A dictionary mapping column number to a function that will convert that column to a float. E.g.,
# if column 0 is a date string: converters = {0: datestr2num}.
# Converters can also be used to provide a default value for missing
# data (but see also genfromtxt): converters = {3: lambda s: float(s.strip() or 0)}. Default: None.
# date.toordinal()：返回日期对应的Gregorian Calendar日期
# """
#
# dates,closes = np.loadtxt("stocks.csv",delimiter=",",usecols=(0,4),
#                           converters={0:datestr2num},unpack=True)
# indices = np.lexsort((dates,closes))
#
# print("Indices",indices)
# print(["%s %s"%(datetime.date.fromordinal(int(dates[i])),closes[i])for i in indices])

#searchsorted为指定的插入值返回一个在有序列数组中的索引位置
# a = np.arange(5)
# indices = np.searchsorted(a,[-2,7])
# print("Indices:",indices)
# print("The full array",np.insert(a,indices,[-2,7]))#用insert构建完整的数组

#extract从数组中抽取元素
a = np.arange(7)
condition = (a % 2)==0
print("Even numbers",np.extract(condition,a))
print("Non zero",np.nonzero(a))

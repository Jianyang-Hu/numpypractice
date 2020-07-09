# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2018/3/19 21:57
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : pandas_180319.py
# @Software: PyCharm

from pandas import Series,DataFrame
import pandas as np

# obj = Series([4,7,-1,9])
# print(obj)
# print(obj.values)
# print(obj.index)

# obj2 = Series([2,5,6,-3],index=['a','b','d','y'])
# print(obj2)

sdata = {'test':1,'hello':2}
statas = ['test','haha']
obj3 = Series(sdata,statas)
# print(obj3)
print(obj3.isnull)

# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2018/4/3 14:55
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : combine_first180403.py
# @Software: PyCharm
import pandas as pd
import numpy as np
from pandas import Series,DataFrame

a = Series([np.nan,2.5,np.nan,3.5,4.5,np.nan],
           index=['f','e','d','c','b','a'])
b = Series([np.arange(len(a),dtype=np.int64)],  #使用arange打印出的是列表，怎么打印出单一元素？？？
           index=['f','e','d','c','b','a'])

#合并重叠数据
# result1 = np.where(pd.isnull(a),b,a)
# print(result1)

print(a[:].combine_first(b[:]))
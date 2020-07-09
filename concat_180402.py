# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2018/4/2 21:05
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : concat_180402.py
# @Software: PyCharm
from pandas import Series,DataFrame
import pandas as pd

s1 = Series([0,1],index=['a','b'])
s2 = Series([2,3,4],index=['c','d','e'])
s3 = Series([5,6],index=['f','g'])

#s2
print(s2)

#axis=0
print(pd.concat([s1,s2,s3]))

#axis = 1,即有3列
print(pd.concat([s1,s2,s3],axis=1))

#keys
print(pd.concat([s1,s2,s3],axis=0,keys=['one','two','three']))

print(pd.concat([s1,s2,s3],axis=1,keys=['one','two','three']))



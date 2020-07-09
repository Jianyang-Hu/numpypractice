# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2018/3/29 10:38
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : merge_180329.py
# @Software: PyCharm
import pandas as pd

df1 = pd.DataFrame({'key':['b','b','a','c','a','a','b'],'data1':range(7)})

df2 = pd.DataFrame({'key':['a','b','d'],'data2':range(3)})

#默认是inner
# print(pd.merge(df1,df2))

#求取键的并集
# print(pd.merge(df1,df2,how='outer'))

#以左边数组来合并
e = pd.merge(df1,df2,on='key',how='left')
print(e)
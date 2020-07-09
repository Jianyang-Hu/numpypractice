# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2018/4/2 21:52
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : concat2_180402.py
# @Software: PyCharm

from pandas import Series,DataFrame
import pandas as pd
import numpy as np

df1 = DataFrame(np.arange(6).reshape(3,2),index=['a','b','c'],
                columns=['one','two'])

df2 = DataFrame(5 + np.arange(4).reshape(2,2),index=['a','c'],
                columns=['three','four'])

# dfconcat1 = pd.concat([df1,df2],axis=1,keys=['level1','level2'])

#names 分层级别的名称
dfconcat1 = pd.concat([df1,df2],axis=0,keys=['level1','level2'],names=['upper','lower'])


print(dfconcat1)
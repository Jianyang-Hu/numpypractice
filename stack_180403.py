# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2018/4/3 16:35
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : stack_180403.py
# @Software: PyCharm
import pandas as pd
import numpy as np
from pandas import Series,DataFrame

data = DataFrame(np.arange(6).reshape(2,3),
                 index=pd.Index(['Ohio','Coload'],name='State'),
                 columns=pd.Index(['one','two','three'],name='number'))

#
print(data)
print('................')

#stack
print(data.stack())
print('................')

#unstack
result = data.stack()

print(result.unstack())
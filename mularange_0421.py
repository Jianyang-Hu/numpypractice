# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/21 11:40
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : mularange_0421.py
# @Software: PyCharm

import numpy
from numpy import *

a = arange(9).reshape(3,3)
print(a)

#水平分割
print(hsplit(a,3))

print(split(a,3,axis=1))

#垂直分割
print(vsplit(a,3))
print(split(a,3,axis=0))

#维数ndim
print(a.ndim)
#字节数itemsize
print(a.itemsize)

#数组转列表tolist,astype可以指定类型
print(a.tolist())
print(a.astype(int))

#存储数据
i2 = eye(3)
print(i2)
savetxt("eye.txt",i2)
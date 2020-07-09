# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/17 16:47
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : mularange.py
# @Software: PyCharm
import numpy
from numpy import *

#数组
num = numpy.array([[1,2],[3,4]])
print(num)

#两个数组
b = arange(24).reshape(2,3,4)
print(b)

#提取第2个数组的1,2行的1,3列元素
print(b[1,1 : ,1: :2])

#改变维度
b.shape = (4,6)
print(b)

#转置
print(b.transpose())

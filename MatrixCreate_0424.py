# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/24 10:25
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : MatrixCreate_0424.py
# @Software: PyCharm
import numpy as np
from numpy import *
import sys, importlib
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

#创建矩阵
# A = np.mat("1,2,3;4,5,6;7,8,9")
# print("create a matrix:",A)
# print("transpose A:",A.T)
# print("Inverse A",A.I)
# print("check Inverse:",A * A.I)
# print("Creation from array:",np.mat(np.arange(12).reshape(4,3)))

#从已有矩阵创建新矩阵
# B = np.eye(2)
# print("B:",B)
#
# C = 2 * B
# print("C:",C)
#
# print("Compound matrix\n",np.bmat("C B;C B"))#复合矩阵

#通用函数
# def ultimate_answer(a):
#     result = np.zeros_like(a)
#     result.flat = 42
#     return result
#
# ufunc = np.frompyfunc(ultimate_answer,1,1)
# print("Thr answer",ufunc(np.arange(4)))
#
# print("The answer:",ufunc(np.arange(4).reshape(2,2)))

#锯齿波
t = np.linspace(-np.pi,np.pi,201)
k = np.arange(1,float(sys.argv[1]))
f = np.zeros_like(t)

for i in range(len(t)):
    f[i] = np.sum(np.sin(2 * np.pi * k * t[i]/k))
f = (-2 / np.pi ) * f
plot(t,f,lw=1.0)
plot(t,np.abs(f),lw=2.0)
show()

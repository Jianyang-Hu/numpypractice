# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/24 16:31
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : linalg_0424.py
# @Software: PyCharm
import numpy as np
from numpy import *
import sys
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
# #逆矩阵
# # A = np.mat("1,2,3;4,5,6;7,8,9")
# A = np.mat("1 -2 1;0 2 -8;-4 5 9")
# # inverse = np.linalg.inv(A)
# # print("inverse of A\n",inverse)
#
# #对形如Ax=b的线性方程组求x
# b = np.array([0,-8,9])
# x = np.linalg.solve(A,b)
# print("Solution",x)
# #dot检验
# print("Check b:\n",np.dot(A,x))
#
# #特征值  eig
# print("Eigenvalues:",np.linalg.eigvals(A))

# #奇异值分解 M=U V
# A = np.mat("4 11 14;8,7,-2")
# U,Sigma,V = np.linalg.svd(A,full_matrices=False)
# print("U:\n",U)
# print("Sigma:\n",Sigma)
# print("V:\n",V)
# print("use diag :",U*np.diag(Sigma)*V)#奇异值矩阵
#
# #计算行列式
# B = np.mat("4 11 14;8,7,-2;5,12,3")
# print("Detetminant:",np.linalg.det(B))


#超几何分布

# points = np.zeros(100)
# outcomes = np.random.hypergeometric(25,1,3,size=len(points))
#
# for i in range(len(points)):
#     if outcomes[i] == 3:
#         points[i] = points[i - 1] + 1
#     elif outcomes[i] == 2:
#         points[i] = points[i - 1]- 6
#     else:
#         print(outcomes[i])
#
# plot(np.arange(len(points)),points)
# show()


#连续分布
N = 100000
normal_values = np.random.normal(size=N)
dummy,bins,dummy = plt.hist(normal_values,np.sqrt(N),normed=True,lw=1)
sigma = 1
mu = 0
plt.plot(bins,1/(sigma*np.sqrt(2*np.pi))*np.exp(-(bins - mu)**2/(2*sigma**2)),lw=2)
plt.show()
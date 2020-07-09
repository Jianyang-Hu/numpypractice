# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/26 16:31
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : three_d_0426.py
# @Software: PyCharm
# 绘制 z = x**2 + y**2

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

fig = plt.figure()
#使用3d关键字来指定图像的三维投影。
ax = fig.add_subplot(111, projection='3d')

#使用meshgrid函数创建一个二维的坐标网格。
u = np.linspace(-1, 1, 100)
x, y = np.meshgrid(u, u)
z = x ** 2 + y ** 2 #
ax.plot_surface(x, y, z, rstride=4, cstride=4, cmap=cm.YlGnBu_r) #cmap colormap
plt.show()
# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/26 16:32
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : contour_0426.py
# @Software: PyCharm

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

#等高线图
fig = plt.figure()
ax = fig.add_subplot(111)
u = np.linspace(-2, 2, 1000)
x, y = np.meshgrid(u, u)
z = x ** 2 + y ** 2
ax.contourf(x, y, z)
plt.show()
# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/26 16:34
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : animation.py
# @Software: PyCharm

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot(111)
N = 10
x = np.random.rand(N)
y = np.random.rand(N)
z = np.random.rand(N)

#用不同颜色的圆形、小圆点和三角形来绘制三个数据集中的数据点。
circles, triangles, dots = ax.plot(x, 'ro', y, 'g^', z, 'b.')
ax.set_ylim(0, 1)
plt.axis('off')

#定期调用以更新屏幕上的内容。将随机更新两个数据集中的y坐标值。
def update(data):
    circles.set_ydata(data[0])
    triangles.set_ydata(data[1])
    return circles, triangles

#使用NumPy生成随机数。
def generated():
     while True: yield np.random.rand(2, N)

anim = animation.FuncAnimation(fig, update, generated, interval=150)
plt.show()
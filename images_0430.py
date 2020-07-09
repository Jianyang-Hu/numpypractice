# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/30 15:58
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : images_0430.py
# @Software: PyCharm
#scipy.ndimage图像处理

from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

#载入Lena图像，并使用灰度颜色表将其在子图中显示出来
image = misc.ascent().astype(np.float32)

plt.subplot(221)
plt.title("Original Image")
img = plt.imshow(image, cmap=plt.cm.gray)
plt.axis("off")

#中值滤波器扫描信号中的每一个信号，并替换为相邻数据点的中值
plt.subplot(222)
plt.title("Median Filter")
filtered = ndimage.median_filter(image, size=(42,42))
plt.imshow(filtered, cmap=plt.cm.gray)
plt.axis("off")

plt.subplot(223)
plt.title("Rotated")
rotated = ndimage.rotate(image, 90)
plt.imshow(rotated, cmap=plt.cm.gray)
plt.axis("off")

#Prewitt滤波器是基于图像强度的梯度计算
plt.subplot(224)
plt.title("Prewitt Filter")
filtered = ndimage.prewitt(image)
plt.imshow(filtered, cmap=plt.cm.gray)
plt.axis("off")
plt.show()

"""
python从网络读取图片并直接进行处理的方法:
python从网络读取图片并直接进行处理的方法。分享给大家供大家参考。具体实现方法如下：

下面的代码可以实现从网络读取一张图片，不需要保存为本地文件，直接通过Image模块对图片进行处理，
这里使用到了cStringIO库，主要是把从网络读取到的图片数据模拟成本地文件。

import urllib2
import Image
import cStringIO
def ImageScale(url,size):
  file = cStringIO.StringIO(urllib2.urlopen(url).read())
  img = Image.open(file)
  img.show()

python 读取并显示图片的两种方法:
http://www.cnblogs.com/yinxiangnan-charles/p/5928689.html
"""
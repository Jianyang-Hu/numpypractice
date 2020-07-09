# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/26 22:49
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : scipyio.py
# @Software: PyCharm
import numpy as np
from scipy import io
a = np.arange(7)
io.savemat("a.mat", {"array": a})
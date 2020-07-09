# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/25 15:07
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : finfunc_0425.py
# @Software: PyCharm
"""
fv终值
pv现值
npv净现值
pmt利息
irr内部收益率
mirr修正后neibushouyil
nper期数
rate利率
"""

import numpy as np
from numpy import *
from matplotlib.pyplot import plot,show

print("Future value",np.fv(0.03/4,5*4,-10,-1000))

fvales = []
for i in range(1,20):
    fvales.append(np.fv(0.03/4,i*4,-10,-1000))

plot(fvales,"bo")
show()

print("Present value:",np.pv(0.03/4,5*4,-10,1376.09633204))
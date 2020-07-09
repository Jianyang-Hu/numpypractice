# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/26 23:33
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : statistics_0426.py
# @Software: PyCharm

from scipy import stats
import matplotlib.pyplot as plt

generated = stats.norm.rvs(size=900)  #使用scipy.stats包按正态分布生成随机数。
print ("Mean", "Std", stats.norm.fit(generated) ) #用正态分布去拟合生成的数据，得到其均值和标准差。

#偏度（skewness）描述的是概率分布的偏斜（非对称）程度。偏度检验有两个返回值，其中第二个返回值为p-value，即观察到的数据集服从正态分布的概率，取值范围为0~1。
print ("Skewtest", "pvalue", stats.skewtest(generated))

#output
#Skewtest pvalue (-0.62120640688766893, 0.5344638245033837)
#该数据集有53%的概率服从正态分布。

#峰度（kurtosis）描述的是概率分布曲线的陡峭程度。
print ("Kurtosistest","pvalue",stats.kurtosistest(generated))

#正态性检验（normality test）可以检查数据集服从正态分布的程度。我们来做一个正态性检验。该检验同样有两个返回值，其中第二个返回值为p-value。
print ("Normaltest", "pvalue", stats.normaltest(generated))

#得到95%处的数值如下
print ("95 percentile", stats.scoreatpercentile(generated, 95))

#将前一步反过来，可以从数值1出发找到对应的百分比
print ("Percentile at 1", stats.percentileofscore(generated, 1))


plt.hist(generated)
plt.show()
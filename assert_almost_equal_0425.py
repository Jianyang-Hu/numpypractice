# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/25 17:15
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : assert_almost_equal_0425.py
# @Software: PyCharm
import numpy as np
#assert_almost_equal 指定精度，断言近似相等
print("Decimal 6:",np.testing.assert_almost_equal(0.1111234,0.1211432,decimal=2))

#assert_approx_equal指定有效数字
print("Significance 9:",np.testing.assert_approx_equal(0.1111234,0.1111432,significant=4))

#assert_array_almost_equal比较两个数组中元素的精度
print("Decimal 8:",np.testing.assert_array_almost_equal([0.,0.1111111234],[0,0.1111111111567],decimal=8))

#比较字符串
print("Pass",np.testing.assert_string_equal("NUMPY","Numpy"))
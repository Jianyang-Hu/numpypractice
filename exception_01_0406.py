# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/6 10:43
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : exception_01_0406.py
# @Software: PyCharm
"""
输出异常以及类的特殊成员str
"""

try:
    print("123")
    raise Exception("this is a exception")
except Exception as e:
    print(e)


class Foo:
    def __init__(self,arg):
        self.xo = arg

    def __str__(self):
        return self.xo

obj = Foo("THIS IS A EXCEPTION")
print(obj)
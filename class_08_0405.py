# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/5 16:16
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : class_08_0405.py
# @Software: PyCharm
"""
利用反射查看对象成员归属
"""
class Foo:

    def __init__(self,name):      #注意别写成了__int__
        self.name = name

    def show(self):
        print("show")

#对象

obj = Foo("hu")

#反射，类，只能找类里的成员
# r = hasattr(Foo,'show')
# print(r)

#反射：对象，既可以找对象，也找类的成员
r = hasattr(obj,'name')
print(r)

r = hasattr(obj,'show')
print(r)
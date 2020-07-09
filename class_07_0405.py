# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/5 15:22
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : class_07_0405.py
# @Software: PyCharm
"""
多继承之调用函数
"""
class A:
    def bar(self):
        print('Bar')
        self.f1()

class B(A):
    def f1(self):
        print('B')

class C:
    def f1(self):
        print('C')

class D(C,B):
    pass

d1 = D()
d1.bar()     #执行到self.f1()时self指的是d1，所以在D--》C--》B中找f1
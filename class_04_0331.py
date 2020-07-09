# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/3/31 22:30
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : class_04_0331.py
# @Software: PyCharm
"""
面向对象：继承多个类
http://www.cnblogs.com/suoning/p/5551173.html
F-----D------B-------E------C-------->A
"""
class A:
    def f1(self):
        print("A")


class B(A):
    def f(self):
        print("B")


class C(A):
    def f(self):
        print("C")


class D(B):
    def f(self):
        print("D")


class E(C):
    def f1(self):
        print("E")


class F(D, E):
    def f(self):
        print("F")


f1 = F()
f1.f1()
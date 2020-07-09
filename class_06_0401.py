# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/1 11:54
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : class_06_0401.py
# @Software: PyCharm
"""
一般来说，要使用某个类的方法，需要先实例化一个对象再调用方法。
而使用@staticmethod或@classmethod，就可以不需要实例化，直接类名.方法名()来调用。

"""


class Foo:
    # 静态方法
    @staticmethod
    def xo(arg1, arg2):  # 无默认参数，可不传参数，可传任意参数
        print("xo")

    # 类方法
    @classmethod
    def xxoo(cls):  # 定义类方法，至少有一个cls参数
        print(cls)

    # 普通方法，类中
    def show(self):  # 定义普通方法，至少有一个self参数
        print("show")


# 调用静态方法
Foo.xo(1, 2)

# 调用类方法
Foo.xxoo()

# 调用普通方法
obj = Foo()
obj.show()
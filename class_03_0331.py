# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/3/31 16:48
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : class_03_0331.py
# @Software: PyCharm

"""
面向对象：继承
"""


# 基类
# class Animals:
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print(self.name, "food")
#
#
# # 派生类
# class dog(Animals):
#     def tell(self):
#         print("dog wawa")
#
#
# dog = dog("Bill")
# dog.tell()
# dog.eat()

"""
继承 __init__

派生类默认不继承基类__init__，需要用super声明
"""


class A:
    def __init__(self):
        print("A")
        self.name = "nick"


class B(A):
    def __init__(self):
        print("B")
        self.age = 18
        super(B, self).__init__()  # super首先找到B的父类A，然后把类B的对象self转换为类A的对象，
                                   # 然后“被转换”的类A对象调用自己的__init__函数
        # A.__init__(self)          #指定运行A中__init__，不推荐


obj = B()
print(obj.__dict__)
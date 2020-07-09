# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/3/31 16:45
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : class_02_0331.py
# @Software: PyCharm

"""
面向对象：封装
"""


class Foo:
    def __init__(self, bk):
        """ 构造方法 """  # 析构方法在垃圾回收是解释器自己调用
        self.name = bk
        self.job = "pythoner"  # obj.job = "pythoner"
        self.age = 18  # obj.age = 18

    def fetch(self):
        print(self.name)
        print(self.age)
        print(self.job)


obj = Foo("nick")
obj.fetch()
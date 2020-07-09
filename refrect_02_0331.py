# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/3/31 11:35
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : refrect_02_0331.py
# @Software: PyCharm
"""
http://python.jobbole.com/82110/
http://www.cnblogs.com/yyyg/p/5554111.html
根据字符串的形式去对象中操作其成员
反射即想到4个内置函数分别为:getattr、hasattr、setattr、delattr  获取成员、检查成员、设置成员、删除成员
"""

class Foo(object):
    def __init__(self):
        self.name = 'abc'

    def func(self):
        return 'ok'


obj = Foo()
# 获取成员
ret = getattr(obj, 'func')  # 获取的是个对象
r = ret()
print(r)
# 检查成员
ret = hasattr(obj, 'func')  # 因为有func方法所以返回True
print(ret)
# 设置成员
print(obj.name)  # 设置之前为:abc
ret = setattr(obj, 'name', 19)
print(obj.name)  # 设置之后为:19
#删除成员
print(obj.name) #abc
delattr(obj,'name')
# print(obj.name) #报错
# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/5 17:37
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : class_09_0405.py
# @Software: PyCharm
"""
利用反射导入模块,查找类，创建对象
"""
#导入模块
m = __import__('class_08_0405',fromlist=True)

#在模块中找类
class_name = getattr(m,"Foo")

#根据类创建对象
obj = class_name('jianyang')

#在对象中找 name 对应的值
val = getattr(obj,'name')
print(val)
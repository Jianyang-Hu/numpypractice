# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/3/31 16:32
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : class_01_0331.py
# @Software: PyCharm
"""
面向对象编程是一种编程方式，此编程方式的落地需要使用 “类” 和 “对象” 来实现，所以，
面向对象编程其实就是对 “类” 和 “对象” 的使用。
类就是一个模板，模板里可以包含多个函数，函数里实现一些功能
对象则是根据模板创建的实例，通过实例对象可以执行类中的函数
"""

"""
面向对象的三大特性是指：封装、继承和多态。
一、封装

封装，顾名思义就是将内容封装到某个地方，以后再去调用被封装在某处的内容。
所以，在使用面向对象的封装特性时，需要：
将内容封装到某处
从某处调用被封装的内容

"""

#调用被封装的内容时，有两种情况：1.通过对象直接调用
class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age


obj = Foo('nick', 18)
#self 是一个形式参数，当执行 obj = Foo('nick', 18 ) 时，self 等于 obj
print (obj.name)  # 直接调用obj对象的name属性
print (obj.age)  # 直接调用obj对象的age属性

obj2 = Foo('jenny', 21)
print (obj2.name)  # 直接调用obj2对象的name属性
print (obj2.age)  # 直接调用obj2对象的age属性



#调用被封装的内容时，有两种情况：2.通过self间接调用
class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def detail(self):
        print (self.name)
        print (self.age)


obj = Foo('nick', 18)
obj.detail()  # Python默认会将obj传给self参数，即：obj.detail(obj)，
              # 所以，此时方法内部的 self ＝ obj，即：self.name 是 nick ；self.age 是 18

obj2 = Foo('jenny', 21)
obj2.detail()  # Python默认会将obj2传给self参数，即：obj1.detail(obj2)，
               # 所以，此时方法内部的 self ＝ obj2，即：self.name 是 jenny ； self.age 是 21
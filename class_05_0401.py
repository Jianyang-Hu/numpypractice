# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/1 10:24
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : class_05_0401.py
# @Software: PyCharm

"""
多态
"""


class Animal:
    def __init__(self, name):  # Constructor of the class
        self.name = name

    def talk(self):  # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class Cat(Animal):
    def talk(self):
        return 'Meow!'


class Dog(Animal):
    def talk(self):
        return 'Woof! Woof!'


animals = [Cat('Missy'),
           Dog('Lassie')]

for animal in animals:
    print (animal.name + ': ' + animal.talk())
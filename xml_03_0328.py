# -*- coding: utf-8 -*-
"""
创建xml文件的两种方法
tree= ElementTree.parse("路径")
tree = ElementTree.ElementTree(根节点（Element对象）)
"""
from xml.etree.ElementTree import Element, ElementTree
from xml.etree.ElementTree import tostring

e = Element('Data')  # 创建一个元素
e.set('name', 'abc')  # 为元素添加name属性，并指定name属性值为'abc'
e.text = '123'  # 为元素添加文本内容

print(tostring(e))  # 将xml转化为字符串文本，但是不含'\n''\t'：b'<Data name="abc">123</Data>'，导致大文本的xml可读性差

e2 = Element('Row')
e3 = Element('Open')
e3.text = '8.80'
e2.append(e3)  # 将e3添加到e2的子元素
e.append(e2)  # 将e2添加到e的子元素

print(tostring(e))

et = ElementTree(e)  # 生成ElementTree树结构，只需传入根节点即可
et.write('demo02.xml')  # 将树结构写文件即可

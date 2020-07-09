# -*- coding: utf-8 -*-

from xml.etree import ElementTree as ET

#查看文件
# root = ET.XML(open('test.xml','r',encoding='utf-8').read())
# print(root.tag)
#
# for node in root:
#     print(node.tag,node.attrib,node.find('rank').text)
#
# print(ET.__file__)

#打开并解析文件内容
tree = ET.parse("test.xml")

root = tree.getroot()    #获得根标签
for node in root.iter('year'):      #iter 查找元素
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set('name','hu')    #为当前节点 year 设置属性
    node.set('year','26')
    del node.attrib['year']    #删除当前节点 year 的属性


tree.write("test.xml")
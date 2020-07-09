# -*- coding:utf-8 -*-
"""
用于处理配置文件，查找节点。类似xml
http://www.tuicool.com/articles/EVRFjqZ
"""
import configparser
import sys

con = configparser.ConfigParser()
# 打开文件，读取内容
con.read('test.conf', encoding='utf-8')

# con对象的节点sections，内存中找所有[XXX]
result = con.sections()
print(result)

# option 键列表和 option 键值元组列表
ret = con.options('db')
print(ret)

items1 = con.items('db')
print(items1)

#读取指定的配置信息
print(con.get('db','host'))

# 按类型读取配置信息：getint、 getfloat 和 getboolean
print(con.getint('db','port'))

#判断 option 是否存在
print(con.has_option('db','host'))

"""
保存配置，set、 remove_option、 add_section
和 remove_section 等操作并不会修改配置文件，
write 方法可以将 ConfigParser 对象的配置写到文件中
"""
#删除
# con.remove_section('new_sect')
# con.write(open('test.conf','w'))
# con.write(sys.stdout)
#增加
# con.add_section('new_sect')
# con.write(open('test.conf','w',encoding='utf-8'))
# con.write(sys.stdout)


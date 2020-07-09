# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/6/10 12:06
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : mysql_connect.py
# @Software: PyCharm

import mysql.connector
conn = mysql.connector.connect(user='root', password='12345', database='test_db', use_unicode=True)
cursor = conn.cursor()

print(cursor.execute('create table user2 (id varchar(20) primary key, name varchar(20))'))

print(cursor.execute('insert into user2 (id, name) values (%s, %s)', ['1', 'Michael']))

print(cursor.rowcount)

conn.commit()

cursor.close()

# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2018/3/30 22:44
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : sqlite3_180330.py
# @Software: PyCharm

import pandas as pd
import pandas.io.sql as sql
import sqlite3

query = """
CREATE TABLE test
(a VARCHAR(20),b VARCHAR(20),
c REAL, d INTEGER );
"""
con = sqlite3.connect(':memory:')
con.execute(query)
con.commit()

data = [('Atlanta','Georgia',1.25,6),
        ('Tall','Florida',2.6,3),
        ('Sacrm','California',1.7,5)]
stmt = "INSERT INTO test VALUES(?,?,?,?)"

con.executemany(stmt,data)
con.commit()

cursor = con.execute('select * from test')
rows = cursor.fetchall()

# print(rows)

# print(cursor.description)

# pd.DataFrame(rows,columns = zip(*cursor.description)[0])

sql.read_frame('select * from test',con)




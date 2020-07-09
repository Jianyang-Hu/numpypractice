# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2018/5/20 17:07
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : tushare_mysql_20180520.py
# @Software: PyCharm

import tushare as ts
from sqlalchemy import create_engine

df = ts.get_h_data('600408')
engine = create_engine('mysql://user:passwd@127.0.0.1/db_name?charset=utf8')
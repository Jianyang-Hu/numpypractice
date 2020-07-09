# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2018/3/27 17:29
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : json_180327.py
# @Software: PyCharm

import json
import requests

url = 'http://www.yicai.com/news/5411247.html'
resp = requests.get(url)

data = json.load(resp.text)

print(data.keys())
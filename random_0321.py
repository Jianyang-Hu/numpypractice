# -*-coding:utf-8-*-
"""
生成随机验证码
"""

import random

temp = ""
for i in range(6):
    num = random.randrange(0,4)
    if num == 3 or num == 1:
        rad2 = random.randrange(0,10)
        temp = temp + str(rad2)
    else:
        rad1 = random.randrange(65,91)
        c1 = chr(rad1)
        temp = temp + c1

print(temp)



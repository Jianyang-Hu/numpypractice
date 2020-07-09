# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/3/29 22:08
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : subprocess_0329.py
# @Software: PyCharm
"""
subprocess是python创建子进程的工具.
subprocess包中有很多方法创建子进程，
这些函数创建子进程的行为不太一样，
我们可以更具需求选择不同的方式来创建子进程。
http://www.tuicool.com/articles/77JVfq
"""
import subprocess

returnCode = subprocess.call('ls -l',shell=True)

print ("returnCode:",returnCode)
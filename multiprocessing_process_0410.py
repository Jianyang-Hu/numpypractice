# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/10 14:18
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : multiprocessing_process_0410.py
# @Software: PyCharm

#进程
from multiprocessing import Process


def work(name):
    print("Hello, %s" % name)


if __name__ == "__main__":
    p = Process(target=work, args=("nick",))
    p.start()
    p.join()

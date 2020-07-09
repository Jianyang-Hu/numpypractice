# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/10 14:33
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : process_array_02_0410.py
# @Software: PyCharm

"""
                       Server process
由Manager()返回的manager提供list, dict, Namespace, Lock, RLock,
Semaphore, BoundedSemaphore, Condition, Event, Barrier, Queue, Value and Array类型的支持。
"""

from multiprocessing import Process, Manager

def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()


if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))

        p = Process(target=f, args=(d, l))
        p.start()
        p.join()

        print(d)
        print(l)

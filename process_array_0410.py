# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/10 14:22
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : process_array_0410.py
# @Software: PyCharm

"""
    不同进程间内存是不共享的，要想实现两个进程间的数据交换
    数据可以用Value或Array存储在一个共享内存地图里
"""

from multiprocessing import Process, Value, Array


def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]


if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])
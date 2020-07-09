# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/8 9:32
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : threading_Lock_0408.py
# @Software: PyCharm
"""
http://www.cnblogs.com/suoning/p/5599030.html

"""
import threading
import time

"""
     threading.Thread类的使用：

1，在自己的线程类的__init__里调用threading.Thread.__init__(self, name = threadname)

Threadname为线程的名字

2， run()，通常需要重写，编写代码实现 做需要的功能。

3，getName()，获得线程对象名称

4，setName()，设置线程对象名称

5，start()，启动线程

6，jion([timeout])，等待另 一线程结束后再运行。

7，setDaemon(bool)，设置子 线程是否随主线程一起结束，必须在start()之前调用。默认为False。

8，isDaemon()，判断线程是否随主 线程一起结束。

9，isAlive()，检查线程是否在运行中。
"""
#下列结果是随机的
# def worker(num):
#     time.sleep(1)
#     print(num)
#     return
#
# for i in range(10):
#     t = threading.Thread(target=worker, args = (i,),name = "t.%d" % i)
#     t.start()

"""
                       threading.RLock & threading.Lock
   我们使用线程对数据进行操作的时候，如果多个线程同时修改某个数据，
   可能会出现不可预料的结果，为了保证数据的准确性，引入了锁的概念。
"""

num = 0

lock = threading.RLock()  # 实例化锁类


def work():
    lock.acquire()  # 加锁
    global num
    num += 1
    time.sleep(1)
    print(num)
    lock.release()  # 解锁


for i in range(10):
    t = threading.Thread(target=work)
    t.start()



"""
                threading.RLock和threading.Lock 的区别
     RLock允许在同一线程中被多次acquire。而Lock却不允许这种情况。
     如果使用RLock，那么acquire和release必须成对出现，
     即调用了n次acquire，必须调用n次的release才能真正释放所占用的锁。
"""
# lock = threading.Lock()
# lock.acquire()
# lock.acquire()  # 产生死锁
# lock.release()
# lock.release()
# print("end1......")


rlock = threading.RLock()
rlock.acquire()
rlock.acquire()      # 在同一线程内，程序不会堵塞。
rlock.release()
rlock.release()
print("end.")
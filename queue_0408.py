# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/8 16:55
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : queue_0408.py
# @Software: PyCharm

"""
    queue 队列:
    适用于多线程编程的先进先出数据结构，可以用来安全的传递多线程信息。

queue 方法：
    先进先出  q = Queue.Queue(maxsize)

    后进先出  a = Queue.LifoQueue(maxsize)

    优先级  Queue.PriorityQueue(maxsize)
    q = queue.Queue(maxsize=0) # 构造一个先进显出队列，maxsize指定队列长度，为0 时，表示队列长度无限制。
    q.join() 　　# 等到队列为kong的时候，在执行别的操作
    q.qsize() 　 # 返回队列的大小 （不可靠）
    q.empty()    # 当队列为空的时候，返回True 否则返回False （不可靠）
    q.full()     # 当队列满的时候，返回True，否则返回False （不可靠）
    q.put(item, block=True, timeout=None) # 将item放入Queue尾部，item必须存在，可以参数block默认为True,
    表示当队列满时，会等待队列给出可用位置，为False时为非阻塞，此时如果队列已满，会引发queue.Full 异常。
    可选参数timeout，表示 会阻塞设置的时间，过后，如果队列无法给出放入item的位置，则引发 queue.Full 异常
    q.get(block=True, timeout=None) # 移除并返回队列头部的一个值，可选参数block默认为True，表示获取值的时候，
    如果队列为空，则阻塞，为False时，不阻塞，若此时队列为空，则引发 queue.Empty异常。
    可选参数timeout，表示会阻塞设置的时候，过后，如果队列为空，则引发Empty异常。
    q.put_nowait(item) # 等效于 put(item,block=False)
    q.get_nowait()     # 等效于 get(item,block=False)

"""

#生产者消费者模型
import queue
import threading

#创建一个队列（容器）先进先出,设置容器大小为10 只能添加10个数据或者元素
que = queue.Queue(10)


def s(i):
    que.put(i)
    print("size:", que.qsize())


def x(i):
    g = que.get(i)
    #print("get:", g)


for i in range(1, 13):
    t = threading.Thread(target=s, args=(i,))
    t.start()

for i in range(1, 11):
    t = threading.Thread(target=x, args=(i,))
    t.start()

print("size:", que.qsize())
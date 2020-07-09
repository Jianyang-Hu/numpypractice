# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/7 15:09
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : IO_select_0407.py
# @Software: PyCharm

"""
Python中有一个select模块，其中提供了：select、poll、epoll三个方法，
分别调用系统的 select，poll，epoll 从而实现IO多路复用。
1
2
3
4
5
6

Windows Python：
    提供： select
Mac Python：
    提供： select
Linux Python：
    提供： select、poll、epoll

注意：网络操作、文件操作、终端操作等均属于IO操作，
对于windows只支持Socket操作，其他系统支持其他IO操作，
但是无法检测 普通文件操作 自动上次读取是否已经变化。
"""

"""
对于select方法：
句柄列表11, 句柄列表22, 句柄列表33 = select.select(句柄序列1, 句柄序列2, 句柄序列3, 超时时间)

参数： 可接受四个参数（前三个必须）
返回值：三个列表

select方法用来监视文件句柄，如果句柄发生变化，则获取该句柄。
1、当 参数1 序列中的句柄发生可读时（accetp和read），则获取发生变化的句柄并添加到 返回值1 序列中
2、当 参数2 序列中含有句柄时，则将该序列中所有的句柄添加到 返回值2 序列中
3、当 参数3 序列中的句柄发生错误时，则将该发生错误的句柄添加到 返回值3 序列中
4、当 超时时间 未设置，则select会一直阻塞，直到监听的句柄发生变化
   当 超时时间 ＝ 1时，那么如果监听的句柄均无任何变化，则select会阻塞 1 秒，
   之后返回三个空列表，如果监听的句柄有变化，则直接执行。
"""

'''
 服务器的实现 采用select的方式
'''

import select
import socket
import sys
import queue

# 创建套接字并设置该套接字为非阻塞模式

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

# 绑定套接字
server_address = ('localhost', 10000)
print (sys.stderr, 'starting up on %s port %s' % server_address)
server.bind(server_address)

# 将该socket变成服务模式
# backlog等于5，表示内核已经接到了连接请求，但服务器还没有调用accept进行处理的连接个数最大为5
# 这个值不能无限大，因为要在内核中维护连接队列

server.listen(5)

# 初始化读取数据的监听列表,最开始时希望从server这个套接字上读取数据
inputs = [server]

# 初始化写入数据的监听列表，最开始并没有客户端连接进来，所以列表为空

outputs = []

# 要发往客户端的数据
message_queues = {}
while inputs:
    print (sys.stderr, 'waiting for the next event')
    # 调用select监听所有监听列表中的套接字，并将准备好的套接字加入到对应的列表中
    readable, writable, exceptional = select.select(inputs, outputs, inputs)  # 列表中的socket 套接字  如果是文件呢？
    # 监控文件句柄有某一处发生了变化 可写 可读  异常属于Linux中的网络编程
    # 属于同步I/O操作，属于I/O复用模型的一种
    # rlist--等待到准备好读
    # wlist--等待到准备好写
    # xlist--等待到一种异常
    # 处理可读取的套接字

    '''
        如果server这个套接字可读，则说明有新链接到来
        此时在server套接字上调用accept,生成一个与客户端通讯的套接字
        并将与客户端通讯的套接字加入inputs列表，下一次可以通过select检查连接是否可读
        然后在发往客户端的缓冲中加入一项，键名为:与客户端通讯的套接字，键值为空队列
        select系统调用是用来让我们的程序监视多个文件句柄(file descrīptor)的状态变化的。程序会停在select这里等待，
        直到被监视的文件句柄有某一个或多个发生了状态改变
        '''

    '''
        若可读的套接字不是server套接字,有两种情况:一种是有数据到来，另一种是链接断开
        如果有数据到来,先接收数据,然后将收到的数据填入往客户端的缓存区中的对应位置，最后
        将于客户端通讯的套接字加入到写数据的监听列表:
        如果套接字可读.但没有接收到数据，则说明客户端已经断开。这时需要关闭与客户端连接的套接字
        进行资源清理
        '''

    for s in readable:
        if s is server:
            connection, client_address = s.accept()
            print (sys.stderr, 'connection from', client_address)
            connection.setblocking(0)  # 设置非阻塞
            inputs.append(connection)
            message_queues[connection] = queue.Queue()
        else:
            data = s.recv(1024)
            if data:
                print (sys.stderr, 'received "%s" from %s' % \
                (data, s.getpeername()))
                message_queues[s].put(data)
                if s not in outputs:
                    outputs.append(s)
            else:
                print (sys.stderr, 'closing', client_address)
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
                del message_queues[s]

    # 处理可写的套接字
    '''
        在发送缓冲区中取出响应的数据，发往客户端。
        如果没有数据需要写，则将套接字从发送队列中移除，select中不再监视
        '''

    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()

        except queue.Empty:
            print (sys.stderr, '  ', s, getpeername(), 'queue empty')
            outputs.remove(s)
        else:
            print (sys.stderr, 'sending "%s" to %s' % \
            (next_msg, s.getpeername()))
            s.send(next_msg)

    # 处理异常情况

    for s in exceptional:
        for s in exceptional:
            print (sys.stderr, 'exception condition on', s.getpeername())
            inputs.remove(s)
            if s in outputs:
                outputs.remove(s)
            s.close()
            del message_queues[s]
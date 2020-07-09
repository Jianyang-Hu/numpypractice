# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/7 10:50
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : socket-server_0407.py
# @Software: PyCharm
"""
http://www.cnblogs.com/dcc001/p/5877989.html
解决粘包的问题：
1.服务端在发送数据之前，先把发送数据的长度告诉客户端，要发送多少数据，
然后客户端根据这个数据的长度循环接收就OK

传输过程：
服务端：
    1.send  #数据长度
    4.recv  #收到确认信息，开始下一步发送.data = conn.recv(1024).decode()
    send  #发送数据

客户端 :
    2.recv #获取数据长度
    3.send #发送确认信息
    recv #循环接收
"""


# 解决粘包问题


import socket,os
ip_address = '192.168.56.1'
port = 8888
bind_address = (ip_address,port)
server = socket.socket()
server.bind(bind_address)
server.listen()
while True:
    conn,addr = server.accept()
    while True:
        data = conn.recv(1024).decode()
        if not data:
            print("丢失连接")
            break
        print("这是来自",addr,data)
        cmd_res = os.popen(data).read()
        conn.send(str(len(cmd_res.encode('utf-8'))).encode('utf-8'))
        ack = conn.recv(1024).decode()
        print(ack)
        conn.send(cmd_res.encode('utf-8'))
server.close()
# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/7 11:03
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : socket-client_0407.py
# @Software: PyCharm

# 解决粘包的问题

import socket
ip_address = '192.168.56.1'
port = 8888
conn_address = (ip_address,port)
client = socket.socket()
client.connect(conn_address)
while True:
    cmd = input(":> ").encode('utf-8')
    if len(cmd) == 0:
        continue
    client.send(cmd)
    cmd_size = int(client.recv(1024).decode())
    print(cmd_size)
    client.send("收到大小".encode('utf-8'))
    recov_size = 0
    recov_data = b''
    while recov_size < cmd_size:
        data = client.recv(1024)
        #print(data)
        recov_size += len(data)
        #print(recov_size)
        recov_data += data
    else:
        print("收完了,大小",recov_size)
        print(recov_data.decode())
client.close()

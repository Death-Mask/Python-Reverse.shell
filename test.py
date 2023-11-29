import time
import socket
import os



def server():
    global s
    global conn
    global addr
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("192.168.159.128", 54321))
    s.listen(5)
    os.system("clear")
    with s.accept() :
        time_sec = 15
        for i in range(time_sec):
            mins, secs = divmod(time_sec, 60)
            timeformat = '{:02d}:{:02d}'.format(mins,secs)
            print('[%s] listening Time for incoming connections......' %timeformat,end='\r')
            time.sleep(1)
            time_sec -= 1
    print('[*] connection established from: %s' % str(addr))    
       
server()
    


time.p
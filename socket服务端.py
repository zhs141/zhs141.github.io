import socket
import sys
import time
serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()#获取本地主机名
port = 9999
#绑定端口号
serversocket.bind((host,port))
open = 1

#设置最大连接数
serversocket.listen(5)
while 1:
    if open == 0:
        sys.exit('程序关闭')
    print('服务器启动，监听中……')
    clientsocket,addr = serversocket.accept()
    puple = '连接地址：%s' % str(addr)
    print(puple)

    while True:
        try:
            data = clientsocket.recv(1024)
        except Exception:
            print('断开的客户端：',addr)
            break
        rever1 = data.decode('utf-8')
        rever3 = '客户端发送内容：' + rever1
        print(rever3)
        rever2 = input('服务端发送内容' + ':')
        print('回复：' + rever2)
        reply = rever2.strip()
        if not reply:
            open = 0
            break
        msg1 = time.strftime('%Y-%m-%d %X')#获取结构化时间戳
        msg2 = '[%s]:%s'% (msg1,reply)
        clientsocket.send(msg2.encode('utf-8'))
    clientsocket.close()
    serversocket.closel()
    print('Close!')

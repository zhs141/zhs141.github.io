#zhs141.github.io
#ZHSAN通讯
#V2.2.3.0
import os
import socket
import sys
import threading as th
import pymsgbox as msg
import easygui as eg


####
try:
    os.system('cls')
except:
    os.system('clear')
os.system('color f9')
print('~这是张三制作的 ZHSAN V2.2 应用~\n作者网页：zhs141.github.io')
input('单击<enter>开始运行\n')
HOST = socket.gethostbyname(socket.gethostname())
####


while True:
    kbs = msg.confirm('请选择服务方式：', 'Index&1', ["等待连接", "主动连接", "查本机IP", "退出"])
    if kbs == None:
        lllllllll = 1
    elif kbs == "退出":
        sys.exit('程序被退出')
    elif kbs == "查本机IP":
        while True:
            print('本机ip', HOST)
            opn = msg.confirm("本机IP" + HOST, "Index&2", ['关闭此窗', '复制IP'])
            if opn == None:
                llllllllllllllllllll = 1
            elif opn == '复制ip':
                import pyperclip
                pyperclip.copy(str(HOST))
                print('ip已被复制')
                break
            else:
                break
    elif kbs == "等待连接":
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while 1:
            PORT = msg._promptTkinter("请随便输入一个5位以下空置数字端口号：\n（对方需输入相同端口号才可连接，输入EXIT退出）", "Index&4", "")
            if PORT == None:
                ddddddddd = 1
            elif PORT == 'EXIT':
                sys.exit('退出')
            else:
                try:
                    s.bind((HOST, int(PORT)))
                    print('端口号',PORT)
                    break
                except OSError:
                    sys.exit('端口号被占用')
        print('正在等待连接...')
        s.listen(1)
        conn, addr = s.accept()
        print('已连接', addr)
        print('输入为“EXIT”时退出连接')
        print('温馨提醒：换行不影响发送哦~')
        class T1(th.Thread):
            def __init__(self):
                th.Thread.__init__(self)
            def run(self):
                while True:
                    c1 = conn.recv(1024)
                    if len(c1) > 0:
                        print('\n对方:', str(c1, encoding='utf-8'))
                        print('我：')
        t1 = T1()
        t1.start()
        while 1:
            data = input('我：')
            if data == 'EXIT':
                conn.close()
                s.close()
                import sys
                sys.exit('\n\n\n连接被单方强制关闭')
            conn.send(bytes(data, encoding='utf-8'))
    elif kbs == '主动连接':
        while True:
            HB = eg.multenterbox(msg="输入要连接的IP地址和端口号：\n(在IP那输入”EXIT“可退出)", title="Index&3", fields=['IP', '端口号'], values=[], callback=None, run=True)
            if HB[0] == None:
                llllllllll = 0
            elif HB[0] == 'EXIT':
                sys.exit('\n\n\n强制关闭')
            else:
                break
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        try:
            s.connect((HB[0], int(HB[1])))
            print('成功连接，输入为“EXIT”时自动退出连接')
            print('温馨提醒：换行不影响发送哦~')
        except:
            print('未知错误，连接失败，自动退出！')
            sys.exit('\n\n\n连接失败')
        class T2(th.Thread):
            def __init__(self):
                th.Thread.__init__(self)
            def run(self):
                while True:
                    c2 = input('我：')
                    if c2 == 'EXIT':
                        conn.close()
                        s.close()
                        import sys
                        sys.exit('\n\n\n连接被单方强制关闭')
                    s.send(bytes(c2, encoding='utf-8'))
        t2 = T2()
        t2.start()
        while 1:
            data = s.recv(1024)
            if len(data) == 0:
                s.close()
                import sys
                sys.exit('\n\n\n连接被单方强制关闭')
            print('\n对方：', str(data, encoding='utf-8'))
            print('我：')
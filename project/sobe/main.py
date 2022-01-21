import pymsgbox as box
import socket
from ybc_box import fileopenbox as fob
from ybc_box import msgbox as ms


i = 0
print('{c} 2022 zhs141.github.io,github.com')
while 1:
    op1 = box.confirm('请选择通讯类型（连接成功后效果相同）','Index1',['服务端(等待接收消息)','客户端(输入IP找到服务端并连接)'])
    if op1 == None:
        box.confirm('你没有选择哦', '查看确认', ["确定"], timeout=1000)
    else:
        break


if op1 == '服务端(等待接收消息)':
    s = socket.socket()  # 声明一个socket类型，同时创建连接（套接字）
    s.bind(('', 6969))  # 绑定要监听的ip、端口
    s.listen(5)  # 开始监听连接
    print('等待连接...')
    conn,address = s.accept()  # 连接客户端请求（筛选连接对象，在服务器端生产新的连接）
    ip_c, port_c = conn.getsockname()  # 本地IP
    ip_s, port_s = conn.getpeername()  # 远程IP
    print('{0}:{1}已连接上了。'.format(ip_s,port_s))
    while 1:
        data2 = conn.recv(1024)  # 接收信息，字符串
        data3 = data2.decode('utf-8')
        print('客户端 {0}:{1}：{2}'.format(ip_s,port_s,data3))
        while 1:
            info = input('服务器 {0}:{1}：'.format(ip_c, port_c))
            if info == 'EXIT':
                import sys
                sys.exit()
            elif len(info) == 0:
                print('不能输入空值哦！请重新输入！')
            if info == 'HELP':
                print('输入EXIT安全正常退出\n输入HELP则查看命令\n输入FILE可发送小于1024字节的文件(尚未开发)\n输入CLS则清空信息')
            elif info == 'CLS':
                import os
                os.system('cls')
                info = input('客户端 {0}:{1}：'.format(ip_c,port_c))
            else:
                break
        jk921 = info.encode('utf-8')
        conn.send(jk921)  # 发送信息，字节
    s.close()  # 关闭连接

elif op1 == '客户端(输入IP找到服务端并连接)':
    c = socket.socket()  # 定义协议类型、链接对象
    lll = box.password('请写出对方的IP(请注意数小数点时不要用中文输入法)',mask='*')
    c.connect((lll,6969))
#    except:
#        print('没有此ip或对方已被监听，请对方至局域网设置关闭代理监听')
#        i = 1
    while 1:
        if i == 1:
            break
        ip_c,port_c = c.getsockname()  # 本地IP
        ip_s,port_s = c.getpeername()  # 远程IP
        info = input('客户端 {0}:{1}：'.format(ip_c,port_c))
        if info == 'EXIT':
            import sys
            sys.exit()
        elif len(info) == 0:
            continue
        elif info == 'HELP':
            print('命令查看(不能连续输入命令)\n输入EXIT安全正常退出\n输入HELP则查看命令\n输入FILE可发送小于1024字节的文件(尚未开发)\n输入CLS则清空信息')
            info = input('客户端 {0}:{1}：'.format(ip_c,port_c))
        elif info == 'CLS':
            import os
            os.system('cls')
            info = input('客户端 {0}:{1}：'.format(ip_c,port_c))
        jk666 = info.encode('utf-8')
        c.send(jk666)
        info = input('客户端 {0}:{1}：'.format(ip_c,port_c))
        data1 = c.recv(1024)
        data2 = data1.decode('utf-8')
        print('服务器 {0}:{1}：{2}'.format(ip_s,port_s,data2))
    c.close()
box.confirm('连接已断开！', 'index3', ['确定'], timeout=1000)

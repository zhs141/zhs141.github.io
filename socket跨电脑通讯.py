import pymsgbox as box
import socket


i = 0
while 1:
    while 1:
        op1 = box.confirm('请选择通讯类型（连接成功后效果相同）','Index1',['服务端(等待接收消息)','客户端(输入IP找到服务端并连接)','查看本机IP','退出'])
        if op1 == None:
            box.confirm('你没有选择哦', '查看确认', ["确定"], timeout=1000)
        elif op1 == '查看本机IP':
            host_name1 = socket.gethostname()
            host_123 = socket.gethostbyname(host_name1)
            opn = box.confirm('你的IP是:' + host_123, 'index^ip', ["确定", '复制'])
            if opn == None:
                ilike3 = True
            elif opn == '复制':
                import pyperclip as per_q
                per_q.copy(host_123)
                box.alert('已将' + host_123 + '放入剪切板')
        elif op1 == '退出':
            break
        else:
            break
    if op1 == '退出':
        break
    ###########
    if op1 == '服务端(等待接收消息)':
        s = socket.socket()  # 声明一个socket类型，同时创建连接（套接字）
        s.bind(('', 6969))  # 绑定要监听的ip、端口
        s.listen(5)  # 开始监听连接
        print('等待连接...')
        conn,address = s.accept()  # 连接客户端请求（筛选连接对象，在服务器端生产新的连接）
        ip_c, port_c = conn.getsockname()  # 本地IP
        ip_s, port_s = conn.getpeername()  # 远程IP
        print('{0}:{1}连接上了你的服务器。'.format(ip_s,port_s))
        while 1:
            data2 = conn.recv(1024)  # 接收信息，字符串
            data3 = data2.decode('utf-8')
            print('客户端 {0}:{1}：{2}'.format(ip_s,port_s,data3))
            while 1:
                info = input('服务器 {0}:{1}：'.format(ip_c, port_c))
                if len(info) == 0:
                    print('输入不能为空哦！请重新输入！')
                else:
                    break
            jk921 = info.encode('utf-8')
            conn.send(jk921)  # 发送信息，字节
        s.close()  # 关闭连接
    ############
    elif op1 == '客户端(输入IP找到服务端并连接)':
        c = socket.socket()  # 定义协议类型、链接对象
        abc = input('请输入要连接的ip地址:')
        try:
            c.connect((abc,6969))
        except:
            print('没有此ip或对方已被监听，请对方至局域网设置关闭代理监听')
            i = 1
        while 1:
            if i == 1:
                break
            ip_c,port_c = c.getsockname()  # 本地IP
            ip_s,port_s = c.getpeername()  # 远程IP
            info = input('客户端 {0}:{1}：'.format(ip_c,port_c))
            if len(info) == 0:
                continue
            jk666 = info.encode('utf-8')
            c.send(jk666)
            data1 = c.recv(1024)
            data2 = data1.decode('utf-8')
            print('服务器 {0}:{1}：{2}'.format(ip_s,port_s,data2))
        c.close()
box.confirm('已退出！', 'index3', ['确定'], timeout=1000)

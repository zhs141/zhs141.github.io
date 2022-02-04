from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib
    
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = input('请输入你的邮箱地址: ')
password = input('请输入你邮箱的授权码（不是密码）: ')
to_addr = input('请输入收件人的邮箱地址: ')
smtp_server = input('请输入该邮箱服务器的SMTP: ')
msg = input('请输入要发送的内容')

msg = MIMEText(msg, 'plain', 'utf-8')
msg['From'] = _format_addr('小弟张三 <%s>' % from_addr)
msg['To'] = _format_addr('大哥 <%s>' % to_addr)
msg['Subject'] = Header('From Python_张三的问候', 'utf-8').encode()
    
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

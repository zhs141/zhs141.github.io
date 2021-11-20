import os,pymsgbox
os.system('pip install pypiwin32 -i https://pypi.douban.com/simple')
import ybc_box as box
import win32cilpboard

def clipboard_get():
    """获取剪贴板数据"""
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()
    return data

def clipboard_set(data):
    """设置剪贴板数据"""
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, data)
    win32clipboard.CloseClipboard()

op1 = box.buttonbox('What do you want to do?',['读取剪切板','修改剪切板'])
if op1 == None:
     box.msgbox('你未输入！自动退出！')
elif op1 == '读取剪切板':
    kbs1 = clipboard_get()
    pymsgbox.alart('剪切板内容',kbs1)
else:
    kbs2 = box.enterbox('请输入你要保存的内容：')
    if kbs2 == None:
        box.msgbox('你未输入！自动退出！')
    else:
        clipboard.set(kbs2)

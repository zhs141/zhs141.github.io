import os,pymsgbox
os.system('pip install pypiwin32 -i https://pypi.douban.com/simple')
import ybc_box as box
import win32cilpboard

def clipboard_get():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()
    return data

def clipboard_set(data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, data)
    win32clipboard.CloseClipboard()

op1 = box.buttonbox('What do you want to do?',['get','set'])
if op1 == None:
     box.msgbox('None!Break!')
elif op1 == 'get':
    kbs1 = clipboard_get()
    pymsgbox.alart('clipboard',kbs1)
else:
    kbs2 = box.enterbox('Write you want to set:')
    if kbs2 == None:
        box.msgbox('None!Break!')
    else:
        clipboard.set(kbs2)

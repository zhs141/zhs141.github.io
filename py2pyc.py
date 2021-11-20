import py_compile
import ybc_box as b


filename = b.filenamebox('选择文件')
if filename == None:
    b.msgbox('你没有输入')
py_compile.compile(filename)

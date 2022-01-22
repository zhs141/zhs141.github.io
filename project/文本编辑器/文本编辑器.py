import easygui as eg
import os

#文件路径
file_path = eg.fileopenbox(default="*.txt")

#打开文件
with open(file_path)as f:
    #把文件读取的内容放到text中
    text = f.read()
    # title 使用文件名
    title = os.path.basename(file_path)
    #窗口消息
    msg = "文件 [%s] 的内容如下:" % title
    #建立一个文本框, 读取文本内容     给他定义一个变量,是一会儿下面要调用他
    text_after = eg.textbox(msg, title, text)


#判断是否有修改,就是判断text 读取的内容是不是等于文本框text_after里的内容就行了
#因为textbox最后一行会返回\n. 所以往前取一个字符.[:-1]
if text != text_after[:-1]:
    #如果文件被修改的时候,会弹出一个框,
    choice = eg.buttonbox(msg="文件有修改", title="警告!", choices=("覆盖", "取消", "另存为"))
    if choice == "覆盖":
        #把text_after[:-1]的内容写到原文件里面,
        with open(file_path, "w") as old_file:
            old_file.write(text_after[:-1])
    if choice == "取消":
        pass
    if choice == "另存为":
        #如果点另存为,那就弹出一个file save box窗口,保存文件,
        anther_path = eg.filesavebox(default=".txt")
        #如果保存文件的时候没有后缀.txt 那就 自动添加一个后缀
        if os.path.splitext(anther_path)[1] != ".txt":
            anther_path += ".txt"
        #把文件写到新保存的文件中
        with open(anther_path, "w")as new_file:
            new_file.write(text_after[:-1])

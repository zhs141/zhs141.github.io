import os, time

import pyautogui as pag

def xy():
    try:
        while True:
            print("按下Ctrl + C 结束程序")
            # pag.position()返回鼠标的坐标
            x, y = pag.position()
            posStr = "当前鼠标位置:" + str(x).rjust(4) + ',' + str(y).rjust(4)
            # 清除屏幕
            os.system('cls')
    # 捕获异常 KeyboardInterrupt:用户中断执行(通常是输入^C)
    except KeyboardInterrupt:
        print('已退出')


try:
    while True:
        print("按下Ctrl + C 结束程序")
        # pag.position()返回鼠标的坐标
        x, y = pag.position()
        posStr = "当前鼠标位置:" + str(x).rjust(4) + ',' + str(y).rjust(4)
        # 打印当前鼠标位置坐标
        print(posStr)
        time.sleep(1)
        # 清除屏幕
        os.system('cls')
# 捕获异常 KeyboardInterrupt:用户中断执行(通常是输入^C)
except KeyboardInterrupt:
    print('已退出')

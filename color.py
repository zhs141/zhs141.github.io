import os, time
import pyautogui


def Color():
    print('按下Ctrl+C结束程序')
    
    try:
        while True:
            x,y = pyautogui.position()
            pixelColor = pyautogui.screenshot().getpixel((x,y))
            positionStr = str(pixelColor[0]).rjust(3)
            positionStr += ', ' + str(pixelColor[1]).rjust(3)
            positionStr += ', ' + str(pixelColor[2]).rjust(3)
            print(positionStr,end='')
            print('\b'*len(positionStr),end='',flush=True)
    except KeyboardInterrupt:   # 当用户按下 Ctrl-C，程序执行将转到 except 子句
        print('已退出')

Color()

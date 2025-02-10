#鼠标点击后记录所在屏幕坐标
import pyautogui
import time
import os

def get_curtime(time_format="%Y-%m-%d %H:%M:%S"):
    curTime = time.localtime()
    curTime = time.strftime(time_format, curTime)
    return curTime

def get_click_pos():
    '''
    获取鼠标点击后的坐标
    :return:tuple
    '''
    print("请点击鼠标")
    time.sleep(0.1)
    x, y = pyautogui.position()
    print("点击坐标：", x, y)
    return x, y

if __name__ == "__main__":
    while True:
        click_pos = get_click_pos()
        print("点击坐标：", click_pos)
        time.sleep(1)
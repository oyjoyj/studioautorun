import os
import time

from PIL import Image
from mouseinfo import screenshot
from pyautogui import hotkey, click, press


#imgprocess = 1: auto       2:cpu
def check(openhighquality = True, imageprocess = 1):
    hotkey('ctrl',',')
    time.sleep(0.8)
    screen = screenshot()
    screen.save("screen.jpg")
    image = Image.open("screen.jpg")
    pixel_color = image.getpixel((865, 582))
    print(pixel_color)
    if pixel_color[0] > 200 and pixel_color[1] > 200:
        if openhighquality:
            print("超高清")
        else:
            click(865, 582)
            time.sleep(0.8)
            click(1041,560)
            time.sleep(15)
            print("更改至超高清-关")
    else:
        if openhighquality:
            click(865, 582)
            time.sleep(0.8)
            click(1041, 560)
            time.sleep(15)
            print("更改至超高清-开")
        else:
            print("超高清-关")
    hotkey('ctrl',',')
    time.sleep(0.8)
    click(760,369)
    screen = screenshot()
    screen.save("screen.jpg")
    image = Image.open("screen.jpg")
    pixel_color = image.getpixel((866, 360))
    print(pixel_color)
    #如果颜色黄色的区块内

    if pixel_color[0] > 200 and pixel_color[1] > 200:
        if imageprocess == 1:
            print("自动")
        else:
            click(866, 360)
            time.sleep(0.8)
            click(1041, 560)
            time.sleep(15)
            print("更改至CPU")
    else:
        if imageprocess == 1:
            click(866, 360)
            time.sleep(0.8)
            click(1041, 560)
            time.sleep(15)
            print("更改至自动")
        else:
            print("CPU")
    os.remove("screen.jpg")
    press('esc')

if __name__ == '__main__':
    time.sleep(3)
    check(1,0)
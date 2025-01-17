import os
import time

from PIL import Image
from mouseinfo import screenshot
from pyautogui import hotkey, click, press


#imgprocess = 1: auto       2:cpu
def check(openhighquality = 1, imageprocess = 1):
    hotkey('ctrl',',')
    time.sleep(0.8)
    screen = screenshot()
    screen.save("screen.jpg")
    image = Image.open("screen.jpg")
    pixel_color = image.getpixel((865, 582))
    #print(pixel_color)
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
    #print(pixel_color)
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

#1:h264  2:h265 3:prores422LT 4:prores422
def checkencodefmt(encodefmt,ifsingle = True):
    if ifsingle:
        click(966, 595)
        time.sleep(1)
        if encodefmt == 1:
            click(954, 628)
            print("H264")
        elif encodefmt == 2:
            click(954, 658)
            print("H265")
        elif encodefmt == 3:
            click(954, 686)
            print("Prores422LT")
        elif encodefmt == 4:
            click(954, 712)
            print("Prores422")
    else:
        click(965, 624)
        time.sleep(1)
        if encodefmt == 1:
            click(954, 660)
            print("H264")
        elif encodefmt == 2:
            click(954, 697)
            print("H265")
        elif encodefmt == 3:
            click(954, 731)
            print("Prores422LT")
        elif encodefmt == 4:
            click(954, 773)
            print("Prores422")
    time.sleep(0.8)

if __name__ == '__main__':
    time.sleep(3)
    checkencodefmt(1,1)
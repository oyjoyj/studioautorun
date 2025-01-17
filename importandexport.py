import time

from PIL.Image import Image
from pyautogui import *
from pynput import mouse, keyboard

import checkconfig
import change360

#路径不能带中文
def import_file(filePath="",ifsingle=True):
    if ifsingle:
        hotkey('ctrl', 'o')
        time.sleep(1)
        press('f4')
        hotkey('ctrl', 'a')
        typewrite(filePath)
        press('enter')
        press('tab', presses=4)
        time.sleep(0.8)
        hotkey('ctrl', 'a')
        press('enter')
        time.sleep(10)
    else:
        click(1007,20)
        click(1202,366)
        change360.changeproportion(5)
        click(1105,720)
        hotkey('ctrl', 'o')
        time.sleep(1)
        press('f4')
        hotkey('ctrl', 'a')
        typewrite(filePath)
        time.sleep(2)
        press('enter', presses=2)
        press('tab', presses=4)
        time.sleep(0.8)
        hotkey('ctrl', 'a')
        press('enter')
        time.sleep(10)
        click(242,240)
        time.sleep(2)

#路径不能带中文 ex:path = r"C:\Users\Administrator\Desktop\0109sucai\photo"
def export_file(exportPath="",ifsingle=True,ifphoto=True,if360=False,encodefmt=0):
    hotkey('ctrl', 'e')
    time.sleep(1)
    if ifsingle:
        if ifphoto:
            if exportPath:
                click(1078,416)
                time.sleep(0.8)
                press('f4')
                hotkey('ctrl', 'a')
                typewrite(exportPath)
                press('enter')
                press('tab', presses=6)
                press('enter')
            click(1096,708)
        else:
            if if360:
                change360.change360()
            else:
                change360.changesquare()
            if exportPath:
                click(1085,355)
                time.sleep(0.8)
                press('f4')
                hotkey('ctrl', 'a')
                typewrite(exportPath)
                time.sleep(3)
                press('enter')
                press('tab', presses=6)
                time.sleep(0.5)
                press('tab')
                press('enter')
                checkconfig.checkencodefmt(encodefmt,ifsingle)
            click(1102,807)
    else:
        if ifphoto:
            # if exportPath:
            #     click(1142,353)
            #     press('f4')
            #     hotkey('ctrl', 'a')
            #     typewrite(exportPath)
            #     press('enter')
            #     press('tab', presses=6)
            #     press('enter')
            # if encodefmt != 0:
            #     checkconfig.checkencodefmt(encodefmt)
            # click(1166,834)
            pass
        else:
            if exportPath:
                click(1142,353)
                time.sleep(0.8)
                press('f4')
                hotkey('ctrl', 'a')
                typewrite(exportPath)
                press('enter')
                press('tab', presses=6)
                time.sleep(0.5)
                press('tab')
                press('enter')
                checkconfig.checkencodefmt(encodefmt,ifsingle)
            click(1166,834)

if __name__ == "__main__":
    time.sleep(3)
    import_file(r"C:\Users\insta360\Desktop\sucai\5.7K30fps", False)
    # export_file(r"C:\Users\insta360\Desktop\daochu", True, False, 1, 1)
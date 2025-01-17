#适用于1080p屏幕
import subprocess
import time
from pyautogui import *
from pynput import mouse, keyboard

def openstudio():
    exe_path = r"C:\Program Files\Insta360 Studio\Insta360 Studio.exe"
    subprocess.Popen(exe_path)

def closestudio():
    click(1900, 10)
    time.sleep(8)

#路径不能带中文
def import_file(filePath="",ifsingle=True):
    if ifsingle:
        hotkey('ctrl', 'o')
        press('f4')
        hotkey('ctrl', 'a')
        typewrite(filePath)
        press('enter')
        press('tab', presses=4)
        hotkey('ctrl', 'a')
        press('enter')
        time.sleep(10)
    else:
        click(1007,20)
        click(1202,366)
        click(1105,720)
        hotkey('ctrl', 'o')
        press('f4')
        hotkey('ctrl', 'a')
        typewrite(filePath)
        press('enter')
        press('tab', presses=4)
        hotkey('ctrl', 'a')
        press('enter')
        time.sleep(10)

#路径不能带中文 ex:path = r"C:\Users\Administrator\Desktop\0109sucai\photo"
def export_file(exportPath="",ifsingle=True,ifphoto=True):
    if ifsingle:
        if ifphoto:
            hotkey('ctrl', 'e')
            if exportPath:
                click(1078,416)
                press('f4')
                hotkey('ctrl', 'a')
                typewrite(exportPath)
                press('enter')
                press('tab', presses=5)
                press('enter')
            click(1096,708)
    else:
        if exportPath:
            click(1142,353)
            press('f4')
            hotkey('ctrl', 'a')
            typewrite(exportPath)
            press('enter')
            press('tab', presses=6)
            press('enter')
        click(1166,834)

def importtotimeline():
    click(210,207)
    hotkey('ctrl', 'a')



if __name__ == "__main__":
    # openstudio()
    # path = r"C:\Users\Administrator\Desktop\0109sucai\photo"
    # import_file(path,ifsingle=False)
    # export_file(path,ifsingle=False,ifphoto=True)
    openstudio()



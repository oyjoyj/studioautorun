import os
import subprocess
import time

from pyautogui import click

def openstudio(ifsingle = True):
    #删除指定目录下的文件夹，文件夹本身不删
    os.system(r"rd /s /q C:\Users\insta360\Documents\Insta360\Studio\TimelineProject")
    exe_path = r"C:\Program Files\Insta360 Studio\Insta360 Studio.exe"
    subprocess.Popen(exe_path)
    time.sleep(15)
    if ifsingle:
        click(1314,281)
    else:
        click(1007,23)
    time.sleep(2)

def closestudio(ifsingle = True):
    if ifsingle == False:
        click(1059,765)
        time.sleep(1)
    click(1900, 10)
    time.sleep(8)

if __name__ == "__main__":
    # openstudio()
    time.sleep(3)
    closestudio(0)
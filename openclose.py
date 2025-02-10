import os
import subprocess
import time

from pyautogui import click

import monitorfile

def cleancache():
    os.system(r"rd /s /q C:\Users\insta360\Documents\Insta360\Studio\Project")
    os.system(r"rd /s /q C:\Users\insta360\Documents\Insta360\Studio\TimelineProject")

def openstudio(ifsingle=True):
    #删除指定目录下的文件夹，文件夹本身不删
    cleancache()
    exe_path = r"C:\Program Files\Insta360 Studio\Insta360 Studio.exe"
    subprocess.Popen(exe_path)
    time.sleep(15)
    if ifsingle:
        click(1314,281)
    else:
        click(1007,23)
        time.sleep(0.5)
        click(1202,366)
        time.sleep(0.5)
        click(1105,720)
    time.sleep(2)

def closestudio():
    flag = monitorfile.monitorfile(r"C:\Users\insta360\AppData\Local\Insta360\Insta360 Studio\log")
    if flag:
        print("Export task completed")
    else:
        print("Export task failed")
    #找到名为Insta360 Studio.exe的进程，关闭
    os.system("taskkill /im \"Insta360 Studio.exe\"")
    time.sleep(5)

def forceclosestudio():
    os.system("taskkill /f /im \"Insta360 Studio.exe\"")
    time.sleep(5)

if __name__ == "__main__":
    #获取输入值
    print("1:open 2:close 3:cleancache 4:forceclose")
    choice = int(input())
    if choice == 1:
        openstudio(0)
    elif choice == 2:
        closestudio()
    elif choice == 3:
        cleancache()
    elif choice == 4:
        forceclosestudio()
import os
import subprocess
import time

from pyautogui import click

import monitorfile
from findplatform import find_platform

import ctypes,sys
import re

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
def runas_admin():
    if is_admin():
        return
    #提升权限
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

def getroot():
    #获取sudo权限
    os.system("sudo -v")


def cleancache():
    if find_platform() == 1:
        os.system(r"rm -rf /Users/insta360/Documents/Insta360/Studio")
    elif find_platform() == 2:
        os.system(r"rd /s /q C:\Users\insta360\Documents\Insta360\Studio")

def openstudio(ifsingle=0):
    #删除指定目录下的文件夹，文件夹本身不删
    cleancache()
    if find_platform() == 1:
        exe_path = r"/Applications/Insta360 Studio.app"
        subprocess.Popen(["open", exe_path])
    elif find_platform() == 2:
        exe_path = r"C:\Program Files\Insta360 Studio\Insta360 Studio.exe"
        subprocess.Popen(exe_path)
    time.sleep(15)
    if ifsingle == 1:
        click(1314,281)
    elif ifsingle == 2:
        click(1007,23)
        time.sleep(0.5)
        click(1202,366)
        time.sleep(0.5)
        click(1105,720)
    time.sleep(2)

def closestudio(expecttimes):
    if find_platform() == 1:
        flag = monitorfile.monitorfile(r"/Users/insta360/Library/Application Support/Insta360/Insta360 Studio/log", expecttimes)
    elif find_platform() == 2:
        flag = monitorfile.monitorfile(r"C:\Users\insta360\AppData\Local\Insta360\Insta360 Studio\log", expecttimes)
    if flag:
        print("导出任务完成")
    else:
        print("导出任务未完成")
    #找到名为Insta360 Studio.exe的进程，关闭
    if find_platform() == 1:
        os.system("pkill -9 -f \"Insta360 Studio\"")
    elif find_platform() == 2:
        os.system("taskkill /im \"Insta360 Studio.exe\"")
    time.sleep(5)

def forceclosestudio():
    if find_platform() == 1:
        os.system("pkill -9 -f \"Insta360 Studio\"")
    elif find_platform() == 2:
        os.system("taskkill /f /im \"Insta360 Studio.exe\"")
    time.sleep(5)

def changethumbnailname(choice):
    platform = find_platform()
    if platform == 1:
        path = r"/Applications/'Insta360 Studio.app'/Contents/MacOS"
        source = path + r"/insta360-thumbnail-service.app"
        dest = path + r"/111.app"
    elif platform == 2:
        path = r"C:\Program Files\Insta360 Studio"
        source = path + r"\insta360-thumbnail-service.exe"
        dest = path + r"\111.exe"
    if choice == 1:
        if platform == 1:
            os.system("sudo mv " + source + " " + dest)
        elif platform == 2:
            os.rename(source, dest)
    elif choice == 2:
        if platform == 1:
            os.system("sudo mv " + dest + " " + source)
        elif platform == 2:
            os.rename(dest, source)
        
def cloud_service_test(inipath):
    os.chdir(inipath)
    ifopen = int(input("1:打开 2:关闭\n"))
    with open("startup.ini", "r") as f:
        content = f.read()
        if 'test_environment' in content:
            if ifopen == 1:
                if 'test_environment=true' in content:
                    f.close()
                    print("测试环境已经打开")
                else:
                    content = content.replace('test_environment=false', 'test_environment=true')
                    with open("startup.ini", "w") as f:
                        f.write(content)
                    f.close()
                    print("测试环境打开")
            elif ifopen == 2:
                if 'test_environment=false' in content:
                    f.close()
                    print("测试环境已经关闭")
                else:
                    content = content.replace('test_environment=true', 'test_environment=false')
                    with open("startup.ini", "w") as f:
                        f.write(content)
                    f.close()
                    print("测试环境关闭")
        else:
            with open("startup.ini", "a") as f:
                f.write("[cloud_service]\n")
                if ifopen == 1:
                    f.write("test_environment=true\n")
                    print("测试环境已经添加-打开")
                elif ifopen == 2:
                    f.write("test_environment=false\n")
                    print("测试环境已经添加-关闭")
            f.close()

def defringechange(inipath):
    os.chdir(inipath)
    ifopen = int(input("1:打开去紫边 2:关闭去紫边\n"))
    with open("startup.ini", "r") as f:
        content = f.read()
        if 'defringe' in content:
            if ifopen == 1:
                if 'defringe=true' in content:
                    print("去紫边已经打开")
                else:
                    content = content.replace('defringe=false', 'defringe=true')
                    with open("startup.ini", "w") as f:
                        f.write(content)
                    print("去紫边打开")
            elif ifopen == 2:
                if 'defringe=false' in content:
                    print("去紫边已经关闭")
                else:
                    content = content.replace('defringe=true', 'defringe=false')
                    with open("startup.ini", "w") as f:
                        f.write(content)
                    print("去紫边关闭")
        else:
            with open("startup.ini", "a") as f:
                f.write("[filter]\n")
                if ifopen == 1:
                    f.write("defringe=true\n")
                    print("去紫边已经添加-打开")
                elif ifopen == 2:
                    f.write("defringe=false\n")
                    print("去紫边已经添加-关闭")
        f.close()

def printfps(inipath):
    os.chdir(inipath)
    with open("startup.ini", "r") as f:
        content = f.read()
        if 'print_fps' in content:
            print("fps已经添加")
        else:
            with open("startup.ini", "a") as f:
                f.write("[ui]\n")
                f.write("print_fps=true\n")
            print("fps添加")
        f.close()

def decodelog(inipath):
    os.chdir(inipath)
    with open("startup.ini", "r") as f:
        content = f.read()
        if 'decode_log' in content:
            print("解码log已经添加")
        else:
            with open("startup.ini", "a") as f:
                f.write("[preference]\n")
                f.write("do_not_crypt_log = true\n")
            print("解码log添加")
            print("fps添加")
        f.close()

def decodelog(inipath):
    os.chdir(inipath)
    with open("startup.ini", "r") as f:
        content = f.read()
        if 'decode_log' in content:
            print("解码log已经添加")
        else:
            with open("startup.ini", "a") as f:
                f.write("[preference]\n")
                f.write("do_not_crypt_log = true\n")
            print("解码log添加")
        f.close()

if __name__ == "__main__":
    #获取输入值
    if is_admin() == False:
        print("1:打开studio\n2:关闭studio\n3:清除缓存\n4:强制关闭studio\n5:更改缩略图进程名\n6:云测环境开关\n7:去紫边开关\n8:打印fps\n9:解码log开关")
        choice = int(input())
        if choice == 1:
            openstudio(0)
        elif choice == 2:
            expecttimes = int(input("期望次数:"))
            closestudio(expecttimes)
        elif choice == 3:
            cleancache()
        elif choice == 4:
            forceclosestudio()
        elif choice == 5:
            if find_platform() == 1:
                thumbchoice = int(input("1:更改 2:还原\n"))
                changethumbnailname(thumbchoice)
            elif find_platform() == 2:
                runas_admin()
        elif choice == 6:
            if find_platform() == 1:
                cloud_service_test(r"/Users/insta360/Library/Application Support/Insta360/Insta360 Studio")
            elif find_platform() == 2:
                cloud_service_test(r"C:\Users\insta360\AppData\Local\Insta360\Insta360 Studio")
        elif choice == 7:
            if find_platform() == 1:
                defringechange(r"/Users/insta360/Library/Application Support/Insta360/Insta360 Studio")
            elif find_platform() == 2:
                defringechange(r"C:\Users\insta360\AppData\Local\Insta360\Insta360 Studio")
        elif choice == 8:
            if find_platform() == 1:
                printfps(r"/Users/insta360/Library/Application Support/Insta360/Insta360 Studio")
            elif find_platform() == 2:
                printfps(r"C:\Users\insta360\AppData\Local\Insta360\Insta360 Studio")
        elif choice == 9:
            if find_platform() == 1:
                decodelog(r"/Users/insta360/Library/Application Support/Insta360/Insta360 Studio")
            elif find_platform() == 2:
                decodelog(r"C:\Users\insta360\AppData\Local\Insta360\Insta360 Studio")
    else:
        ch = int(input("1:更改 2:还原\n"))
        changethumbnailname(ch)
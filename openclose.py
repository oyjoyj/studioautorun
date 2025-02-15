import os
import subprocess
import time

from pyautogui import click

import monitorfile
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

def closestudio(expecttimes):
    flag = monitorfile.monitorfile(r"C:\Users\insta360\AppData\Local\Insta360\Insta360 Studio\log", expecttimes)
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

def changethumbnailname(choice):
    path = r"C:\Program Files\Insta360 Studio"
    source = path + r"\insta360-thumbnail-service.exe"
    dest = path + r"\111.exe"
    if choice == 1:
        os.rename(source, dest)
        
    elif choice == 2:
        os.rename(dest, source)
        
def cloud_service_test(inipath):
    os.chdir(inipath)
    ifopen = int(input("1:open 2:close\n"))
    with open("startup.ini", "r") as f:
        content = f.read()
        if 'test_environment' in content:
            if ifopen == 1:
                if 'test_environment=true' in content:
                    f.close()
                    print("test environment is already open")
                else:
                    content = content.replace('test_environment=false', 'test_environment=true')
                    with open("startup.ini", "w") as f:
                        f.write(content)
                    f.close()
                    print("test environment is open")
            elif ifopen == 2:
                if 'test_environment=false' in content:
                    f.close()
                    print("test environment is already close")
                else:
                    content = content.replace('test_environment=true', 'test_environment=false')
                    with open("startup.ini", "w") as f:
                        f.write(content)
                    f.close()
                    print("test environment is close")
        else:
            with open("startup.ini", "a") as f:
                f.write("[cloud_service]\n")
                if ifopen == 1:
                    f.write("test_environment=true\n")
                elif ifopen == 2:
                    f.write("test_environment=false\n")
            print("test environment is added")
            f.close()

def defringechange(inipath):
    os.chdir(inipath)
    ifopen = int(input("1:open 2:close\n"))
    ifcheck = int(input("1:yes 2:no\n"))
    with open("startup.ini", "r") as f:
        content = f.read()
        if 'defringe' in content:
            if ifopen == 1:
                if 'defringe=true' in content:
                    print("defringe is already open")
                else:
                    content = content.replace('defringe=false', 'defringe=true')
                    with open("startup.ini", "w") as f:
                        f.write(content)
                    print("defringe is open")
            elif ifopen == 2:
                if 'defringe=false' in content:
                    print("defringe is already close")
                else:
                    content = content.replace('defringe=true', 'defringe=false')
                    with open("startup.ini", "w") as f:
                        f.write(content)
                    print("defringe is close")
        else:
            with open("startup.ini", "a") as f:
                f.write("[filter]\n")
                if ifopen == 1:
                    f.write("defringe=true\n")
                elif ifopen == 2:
                    f.write("defringe=false\n")
            print("defringe is added")
        if 'defringe_detect' in content:
            if ifcheck == 1:
                if 'defringe_detect=true' in content:
                    print("defringe_detect is already open")
                else:
                    content = content.replace('defringe_detect=false', 'defringe_detect=true')
                    with open("startup.ini", "w") as f:
                        f.write(content)
                    print("defringe_detect is open")
            elif ifcheck == 2:
                if 'defringe_detect=false' in content:
                    print("defringe_detect is already close")
                else:
                    content = content.replace('defringe_detect=true', 'defringe_detect=false')
                    with open("startup.ini", "w") as f:
                        f.write(content)
                    print("defringe_detect is close")
        else:
            with open("startup.ini", "a") as f:
                if ifcheck == 1:
                    f.write("defringe_detect=true\n")
                elif ifcheck == 2:
                    f.write("defringe_detect=false\n")
            print("defringe_detect is added")
        f.close()

def printfps(inipath):
    os.chdir(inipath)
    with open("startup.ini", "r") as f:
        content = f.read()
        if 'print_fps' in content:
            print("fps is already added")
        else:
            with open("startup.ini", "a") as f:
                f.write("[ui]\n")
                f.write("print_fps=true\n")
            print("fps is added")
        f.close()

if __name__ == "__main__":
    #获取输入值
    if is_admin() == False:
        print("1:open 2:close 3:cleancache 4:forceclose 5:change thumbnail name 6:cloud service test environment change 7:defringe change 8:print fps")
        choice = int(input())
        if choice == 1:
            openstudio(0)
        elif choice == 2:
            closestudio()
        elif choice == 3:
            cleancache()
        elif choice == 4:
            forceclosestudio()
        elif choice == 5:
            runas_admin()
        elif choice == 6:
            cloud_service_test(r"C:\Users\insta360\AppData\Local\Insta360\Insta360 Studio")
        elif choice == 7:
            defringechange(r"C:\Users\insta360\AppData\Local\Insta360\Insta360 Studio")
        elif choice == 8:
            printfps(r"C:\Users\insta360\AppData\Local\Insta360\Insta360 Studio")
    else:
        ch = int(input("1:change 2:recover\n"))
        changethumbnailname(ch)
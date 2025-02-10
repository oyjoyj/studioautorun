import os
import re
import time

from PIL.Image import Image
from pyautogui import *
from pynput import mouse, keyboard

import checkconfig
import change360

def openbackdoorexport(inipath,ifsingle=True):
    #进入inipath路径
    os.chdir(inipath)
    #打开startup.ini文件，读
    with open("startup.ini", "r") as f:
        #如果找到export_backdoor字段
        con = re.findall('export_backdoor',f.read())
        if con:
            f.close()
        else:
            f = open("startup.ini", "a")
            f.write("[export_backdoor]\n")
            f.write("enable=true\n")
            if ifsingle:
                f.write("json_path=C:/Users/insta360/AppData/Local/Insta360/Insta360 Studio/export_backdoor.json\n")
            else:
                f.write("json_path=C:/Users/insta360/AppData/Local/Insta360/Insta360 Studio/export.json\n")
            f.close()

def changesignal(path):
    #将\转换为/
    path = path.replace("\\", "/")
    return path


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
        click(242,240)#导入到时间线
        time.sleep(2)

#路径不能带中文 ex:path = r"C:\Users\Administrator\Desktop\0109sucai\photo"
def export_file(importPath="",exportPath="",ifsingle=True,type=0,resolution=0,fps=24,Mbps=25,ifspherical=False,denoise=0,encodefmt=0):
    os.chdir("C:\\Users\\insta360\\AppData\\Local\\Insta360\\Insta360 Studio")
    importPath = changesignal(importPath)
    exportPath = changesignal(exportPath)
    #关闭缩略图进程
    os.system("taskkill /im insta360-thumbnail-service.exe")
    #创建一个json文件并写入
    if ifsingle:#单段-测试中
        with open("export.json", "w") as f:
            f.write("{\n")
            f.write("\"export_destination_path\": \"" + exportPath + "\",\n")
            f.write("\"export_source_file_path\": \"" + importPath + "\",\n")
            f.write("\"projects\": [\n{\n")
            f.write("\"project_name\": \"output.mp4\",\n")
            f.write("\"clip_params\": [\n{\n")
            f.write("\"file_name\": \"output.mp4\",\n")
            f.write("\"enable_color_plus\": true,\n")#色彩增强
            f.write("\"color_plus_strength\": 100,\n")
            f.write("\"enable_denoise\": " + str(denoise) + ",\n") # 降噪
            f.write("\"enable_stabilizer\": true,\n")#防抖
            f.write("\"trim_start\": 0,\n")#从头丢弃的片段长度
            f.write("\"trim_end\": 0\n")#从尾丢弃的片段长度
            f.write("}\n],\n")
            if resolution == 1:
                f.write("\"resolution\": {\n\"width\": 1920,\n\"height\": 1080\n},\n")
            elif resolution == 2:
                f.write("\"resolution\": {\n\"width\": 2560,\n\"height\": 1440\n},\n")
            elif resolution == 3:
                f.write("\"resolution\": {\n\"width\": 3840,\n\"height\": 2160\n},\n")
            f.write("\"frame_rate\": " + str(fps) + ",\n")
            f.write("\"bit_in_mbps\": " + str(Mbps) + ",\n")
            f.write("\"is_spherical\": " + str(ifspherical) + ",\n")#全景
            f.write("\"export_type\": " + str(type) + "\n")
            f.write("}\n]\n")
            f.write("}")
            f.close()

    else: #多段-可用
        with open("export.json", "w") as f:
            f.write("{\n")
            f.write("\"saveDir\": \"" + exportPath + "\",\n")
            f.write("\"saveName\": \"output\",\n")
            f.write("\"bitrate\": " + str(Mbps) + ",\n")
            if resolution == 1:
                f.write("\"width\": 1920,\n\"height\": 1080,\n")
            elif resolution == 2:
                f.write("\"width\": 2560,\n\"height\": 1440,\n")
            elif resolution == 3:
                f.write("\"width\": 3840,\n\"height\": 2160,\n")
            f.write("\"fps\": " + str(fps) + ",\n")
            f.write("\"encodeFormat\": " + str(encodefmt) + ",\n")
            f.write("\"denoise\": " + str(denoise) + ",\n")
            f.write("\"video\": [\n{\n")
            f.write("\"filePath\": \"" + importPath + "\",\n")
            f.write("\"rightTrim\": 0,\n")
            f.write("\"leftTrim\": 0,\n")
            f.write("\"transition\": {\n")
            f.write(("\"uuid\": \"{UUID}\",\n"))
            f.write("\"duration\": 2000\n")
            f.write("}\n")
            f.write("}\n]\n")
            f.write("}")
            f.close()

if __name__ == "__main__":
    time.sleep(3)
    # import_file(r"C:\Users\insta360\Desktop\sucai\5.7K30fps", False)
    inputpath = r"C:\Users\insta360\Desktop\sucai\5.7K60\VID_20250120_121244_00_032.insv"
    openbackdoorexport(r"C:\Users\insta360\AppData\Local\Insta360\Insta360 Studio", 0)
    # export_file(inputpath,r"C:\Users\insta360\Desktop\daochu",1, 1, 1, 30, 25, 0, 0, 0)
    # time.sleep(1)
    # hotkey('ctrl', 'alt', 'e')
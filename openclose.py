import subprocess
import time

from pyautogui import click

def openstudio(ifsingle = True):
    exe_path = r"C:\Program Files\Insta360 Studio\Insta360 Studio.exe"
    subprocess.Popen(exe_path)
    time.sleep(15)
    if ifsingle:
        click(1314,281)
    else:
        click(1007,23)
    time.sleep(2)

def closestudio():
    click(1900, 10)
    time.sleep(8)
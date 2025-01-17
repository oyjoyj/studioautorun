import subprocess
import time

from pyautogui import click

def openstudio():
    exe_path = r"C:\Program Files\Insta360 Studio\Insta360 Studio.exe"
    subprocess.Popen(exe_path)

def closestudio():
    click(1900, 10)
    time.sleep(8)
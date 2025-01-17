import time

from pyautogui import click


def change360():
    click(995, 270)

def changesquare():
    click(877, 270)

if __name__ == "__main__":
    time.sleep(5)
    change360()
    changesquare()
    pass
import time

from pyautogui import click


def change360():
    click(995, 270)

def changesquare():
    click(877, 270)

#1.16:9 2.2.35:1 3.1:1 4.9:16 5.2:1
def changeproportion(pro=1):
    click(963,542)
    if(pro==1):
        click(963, 591)
    elif(pro==2):
        click(963, 623)
    elif(pro==3):
        click(963, 660)
    elif(pro==4):
        click(963, 695)
    elif(pro==5):
        click(963, 733)

if __name__ == "__main__":
    time.sleep(5)
    change360()
    changesquare()
    pass
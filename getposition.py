import pyautogui
import time
import pygetwindow as gw

def getappwindowpos():
    windows = gw.getWindows()

# 遍历所有窗口，找到标题为 "Insta360 Studio" 的窗口
    insta360_windows = [window for window in windows if window.title == "Insta360 Studio"]

# 打印出找到的窗口的左上角和右下角坐标
    for window in insta360_windows:
        print("Window title:", window.title)
        print("Left corner coordinates (x, y):", window.left, window.top)
        print("Right corner coordinates (x, y):", window.left + window.width, window.top + window.height)



    
if __name__ == "__main__":
    print(getappwindowpos())
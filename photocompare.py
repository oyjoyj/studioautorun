import time

import cv2
import imagehash
import numpy
from PIL import Image, ImageGrab
from networkx.algorithms.operators.binary import difference
from pyautogui import hotkey


#截取指定区域的屏幕截图
def getscreenshot(ifsingle=True):
    if ifsingle:
        hotkey('ctrl','shift','f')
        time.sleep(3)
        img = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
        img = numpy.array(img.getdata(), numpy.uint8).reshape(img.size[1], img.size[0], 3)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        cv2.imwrite("2.jpg", img)
        hotkey('esc')
    else:
        img = ImageGrab.grab(bbox=(501, 48, 1601, 700))
        img = numpy.array(img.getdata(), numpy.uint8).reshape(img.size[1], img.size[0], 3)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        cv2.imwrite("2.jpg", img)


def compare_image(image_path1, image_path2):
    img1 = Image.open(image_path1)
    img2 = Image.open(image_path2)
    img1 = img1.convert('L')
    img2 = img2.convert('L')
    img1_array = numpy.array(img1)
    img2_array = numpy.array(img2)
    if img1_array.shape != img2_array.shape:
        return False
    difference = numpy.sum(img1_array != img2_array)
    return difference == 0

if __name__ == '__main__':
    time.sleep(2)
    #getscreenshot(True)
    image_path1 = r"11.jpg"
    image_path2 = r"2.jpg"
    difference = compare_image(image_path1, image_path2)
    print(difference)

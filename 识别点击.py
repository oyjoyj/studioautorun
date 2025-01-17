import keyboard
from pyautogui import *
from PIL import Image
import numpy as np
from paddleocr import PaddleOCR, draw_ocr

from pynput import mouse

def get_curtime(time_format="%Y-%m-%d %H:%M:%S"):
    curTime = time.localtime()
    curTime = time.strftime(time_format, curTime)
    return curTime


def ocr_get_txt_pos(path="", text=""):
    '''
    获取文字与位置对应map
    :param path:图片路径，图片路径为空则默认获取当前屏幕截图
    :param text: 筛选需要查找的内容，匹配所有位置
    :return:list
    '''

    result, img_path = ocr_img_text(path, saveimg=False)

    #print("图片识别结果保存：", img_path)

    poslist = [detection[0][0] for line in result for detection in line]
    txtlist = [detection[1][0] for line in result for detection in line]

    # 用list存文字与位置信息
    find_txt_pos = []

    items = 0

    if text == "":
        find_txt_pos = result
    else:
        for i in range(len(poslist)):
            if txtlist[i] == text:
                find_txt_pos.append(poslist[i])
                items += 1

    print(find_txt_pos)
    return find_txt_pos


def ocr_img_text(path="", saveimg=False, printResult=False):
    '''
    图像文字识别
    :param path:图片路径
    :param saveimg:是否把结果保存成图片
    :param printResult:是否打印出识别结果
    :return:result,img_name
    '''
    image = path

    # 图片路径为空就默认获取屏幕截图
    if image == "":
        image = screenshot()
        image = np.array(image)
    else:
        # 不为空就打开
        image = Image.open(image).convert('RGB')

    ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory

    result = ocr.ocr(image, cls=True)
    if printResult is True:
        for line in result:
            for word in line:
                print(word)

    # 识别出来的文字保存为图片
    img_name = "ImgTextOCR-img-" + get_curtime("%Y%m%d%H%M%S") + ".jpg"
    if saveimg is True:
        boxes = [detection[0] for line in result for detection in line]  # Nested loop added
        txts = [detection[1][0] for line in result for detection in line]  # Nested loop added
        scores = [detection[1][1] for line in result for detection in line]  # Nested loop added
        im_show = draw_ocr(image, boxes, txts, scores)
        im_show = Image.fromarray(im_show)
        im_show.save(img_name)

    return result, img_name


if __name__ == '__main__':

    while True:
        # pos_list = ocr_get_txt_pos(text="菜单")
        # if len(pos_list) > 0:
        #     while True:
        #         print("开始识别")
        #         pos_list = ocr_get_txt_pos(text="汇报")
        #         if len(pos_list) > 0:
        #             click(pos_list[0][0], pos_list[0][1])
        #         else:
        #             print("未找到文字")

        pos_list = ocr_get_txt_pos(text="Insta360 Studio")
        if len(pos_list) > 0:
            #双击文字
            click(pos_list[0][0], pos_list[0][1], clicks=2)
            break




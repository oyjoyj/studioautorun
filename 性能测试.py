#适用于1080p屏幕
import time

import openclose
import importandexport
import checklog
import checkconfig

#路径不能带中文
import_path = r"C:\Users\Administrator\Desktop\0109sucai\video"
export_path = r"C:\Users\Administrator\Desktop\daochu"

if __name__ == "__main__":
    openclose.openstudio()
    checkconfig(1,1)
    importandexport.import_file(import_path, True)
    #播放预览
    importandexport.export_file(export_path, True, False)
    time.sleep(60)
    openclose.closestudio()
    checklog.check(r"C:\Users\Administrator\AppData\Local\Insta360\Insta360 Studio\log")




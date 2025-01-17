#适用于1080p屏幕
import time

import openclose
import importandexport
import checklog
import checkconfig
import play

#路径不能带中文
import_path = r"C:\Users\insta360\Desktop\sucai\5.7K30fps"
export_path = r"C:\Users\insta360\Desktop\daochu"
log_path = r"C:\Users\insta360\AppData\Local\Insta360\Insta360 Studio\log"
expectexporttime = 250

if __name__ == "__main__":
    openclose.openstudio(1)
    checkconfig.check(1,1)
    importandexport.import_file(import_path, True)
    #play.play()
    time.sleep(3)
    importandexport.export_file(export_path, True, False, 1,1)
    # time.sleep(expectexporttime)
    # openclose.closestudio()
    # checklog.check(log_path)




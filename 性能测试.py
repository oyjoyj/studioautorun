#适用于1080p屏幕
import time

import openclose
import importandexport
import checklog
import checkconfig
import play

#路径不能带中文
import_path1 = r"C:\Users\insta360\Desktop\sucai\ilog"
import_path2 = r"C:\Users\insta360\Desktop\sucai\8K30fps"
export_path = r"C:\Users\insta360\Desktop\daochu"
log_path = r"C:\Users\insta360\AppData\Local\Insta360\Insta360 Studio\log"
expectexporttime = 700


if __name__ == "__main__":
    # times = 1
    # while True:
    #     openclose.openstudio(1)
    #     checkconfig.check(1,1)
    #     importandexport.import_file(import_path1, True)
    #     #play.play()
    #     time.sleep(3)
    #     importandexport.export_file(export_path, True, False, 1,times)
    #     time.sleep(expectexporttime)
    #     openclose.closestudio(True)
    #     checklog.check(log_path)
    #     times += 1
    #     if(times>4):
    #         break
    #
    # times = 1
    # while True:
    #     openclose.openstudio(1)
    #     checkconfig.check(1,1)
    #     importandexport.import_file(import_path1, False)
    #     #play.play()
    #     time.sleep(3)
    #     importandexport.export_file(export_path, False, False, 2,times)
    #     time.sleep(expectexporttime)
    #     openclose.closestudio(False)
    #     checklog.check(log_path)
    #     times += 1
    #     if(times>4):
    #         break
    #
    # times = 1
    # while True:
    #     openclose.openstudio(1)
    #     checkconfig.check(1,1)
    #     importandexport.import_file(import_path2, True)
    #     #play.play()
    #     time.sleep(3)
    #     importandexport.export_file(export_path, True, False, 3,times)
    #     time.sleep(expectexporttime)
    #     openclose.closestudio(True)
    #     checklog.check(log_path)
    #     times += 1
    #     if(times>4):
    #         break
    #
    # times = 1
    # while True:
    #     openclose.openstudio(1)
    #     checkconfig.check(1,1)
    #     importandexport.import_file(import_path2, False)
    #     #play.play()
    #     time.sleep(3)
    #     importandexport.export_file(export_path, False, False, 4,times)
    #     time.sleep(expectexporttime)
    #     openclose.closestudio(False)
    #     checklog.check(log_path)
    #     times += 1
    #     if(times>4):
    #         break
    openclose.openstudio(1)
    checkconfig.check(1,1)
    importandexport.import_file(import_path1, True)
    #play.play()
    time.sleep(3)
    checkconfig.checkcpandilog(1,0)
    importandexport.export_file(export_path, True, False, 1)





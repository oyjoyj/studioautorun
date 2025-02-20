#适用于1080p屏幕
import time

import openclose
import importandexport
import checklog
import checkconfig
import play

#路径不能带中文
import_path1 = r"C:\Users\insta360\Desktop\sucai"
import_path2 = r"C:\Users\insta360\Desktop\sucai\VID_20240426_113757_00_112.mp4"
export_path = r"C:\Users\insta360\Desktop\daochu"
log_path = r"C:\Users\insta360\AppData\Local\Insta360\Insta360 Studio\log"
expectexporttime = 700


if __name__ == "__main__":
    importandexport.openbackdoorexport(r"C:\Users\insta360\AppData\Local\Insta360\Insta360 Studio", 0)

    openclose.openstudio(0)
    checkconfig.check(1,1)
    importandexport.import_file(import_path1, False)
    play.playthevideo()
    #checkconfig.checkcpandilog(1,0)
    importandexport.export_file(import_path2, export_path, 0, 1, 1, 30, 25, 0, 0, 0)
    openclose.closestudio()
    checklog.check(log_path)

    openclose.openstudio(0)
    checkconfig.check(1, 1)
    importandexport.import_file(import_path2, False)
    play.playthevideo()
    # checkconfig.checkcpandilog(1,0)
    importandexport.export_file(import_path2, export_path, 0, 1, 1, 30, 25, 0, 0, 0)
    openclose.closestudio()
    checklog.check(log_path)





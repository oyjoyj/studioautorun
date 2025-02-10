import os
import time


def monitorfile(path):
    dir_list = os.listdir(path)
    dir_time = [os.path.getmtime(os.path.join(path, dir)) for dir in dir_list]
    newest_dir = dir_list[dir_time.index(max(dir_time))]
    os.chdir(os.path.join(path, newest_dir))
    file_list = os.listdir(os.path.join(path, newest_dir))
    # 找到文件名中含有export的文件
    for file in file_list:
        if 'export' in file:
            export_file = file
    times = 0
    #持续监控文件内容变化，直到找到Export task completed字段
    while True:
        with open(export_file, 'r', encoding='utf-8', errors='ignore') as file:
            log_content = file.read()
            if 'Export task final' in log_content:
                print("Export task completed 1")
                break
            time.sleep(10)
            times += 1
            if times >= 360:
                print("Export task failed 1")
                return False
    file.close()
    os.chdir("..")
    del dir_list
    del dir_time
    del file_list
    return True

if __name__ == "__main__":
    path = r"C:\Users\insta360\AppData\Local\Insta360\Insta360 Studio\log"
    monitorfile(path)
import os
import re
from monitorfile import deleteotherdir
from findplatform import find_platform

def get_fps_graph(path):
    while(True):
        if deleteotherdir(path):
            break
    dir_list = os.listdir(path)
    dir_time = [os.path.getmtime(os.path.join(path, dir)) for dir in dir_list]
    newest_dir = dir_list[dir_time.index(max(dir_time))]
    os.chdir(os.path.join(path, newest_dir))
    file_list = os.listdir(os.path.join(path, newest_dir))
    file_len = [len(file) for file in file_list]
    shortest_file = file_list[file_len.index(min(file_len))]
    with open(shortest_file, 'r', encoding='utf-8', errors='ignore') as file:
        log_content = file.read()
    frame_fps_list = re.findall(r'previewer fps:(\d+\.\d+)', log_content)
    print(frame_fps_list)
    #创建一个新的文件，将帧率数据写入
    f = open('fps.txt', 'w')
    for fps in frame_fps_list:
        f.write(fps + '\n')
    file.close()
    f.close()

if __name__ == '__main__':
    if find_platform() == 1:
        path = r"/Users/insta360/Library/Application Support/Insta360/Insta360 Studio/log"
    elif find_platform() == 2:
        path = r"C:\Users\insta360\AppData\Local\Insta360\Insta360 Studio\log"
    get_fps_graph(path)
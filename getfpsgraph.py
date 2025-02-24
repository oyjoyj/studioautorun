import os
import re
import csv

def get_fps_graph(path):
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
    # print(frame_fps_list)
    #创建一个新的文件，将帧率数据写入
    with open('fps.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(frame_fps_list)


if __name__ == '__main__':
    path = r"C:\Users\insta360\Desktop\daochu"
    get_fps_graph(path)
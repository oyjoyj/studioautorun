#打开特定路径下修改时间最新的文件夹，进入这个文件夹，并打开文件名最短的文件
import os
import re
import time


def check(path):
    dir_list = os.listdir(path)
    dir_time = [os.path.getmtime(os.path.join(path, dir)) for dir in dir_list]
    newest_dir = dir_list[dir_time.index(max(dir_time))]
    os.chdir(os.path.join(path, newest_dir))
    file_list = os.listdir(os.path.join(path, newest_dir))
    file_len = [len(file) for file in file_list]
    shortest_file = file_list[file_len.index(min(file_len))]
    #找到文件名中含有export的文件
    for file in file_list:
        if 'export' in file:
            export_file = file
    print(shortest_file)
    print(export_file)

    with open(shortest_file, 'r', encoding='utf-8', errors='ignore') as file:
        log_content = file.read()
    #找到import cost字段，读取这一行这个字段后的数字
    import_cost = re.findall(r'import cost: (\d+)', log_content)
    if not import_cost:
        import_cost = re.findall(r'from single clip panel, cost: (\d+)', log_content)
        if not import_cost:
            import_cost = re.findall(r'Import footage, cost: (\d+)', log_content)
    #找到frame fps字段，读取这一行这个字段后的数字
    frame_fps_list = re.findall(r'HRenderNewFrame fps:(\d+\.\d+)', log_content)
    framefps = sum(map(float, frame_fps_list)) / len(frame_fps_list) if frame_fps_list else 0

    #找到export cost字段，读取这一行这个字段后的数字
    with open(export_file, 'r', encoding='utf-8', errors='ignore') as file:
        export_content = file.read()
    export_cost = re.findall(r'exporter time cost (\d+)', export_content)
    if not export_cost:
        export_cost = re.findall(r'exporter time cost: (\d+)', export_content)
    print("import cost:", import_cost)
    print("frame fps:", framefps)
    print("export cost:", export_cost)
    file.close()
    os.chdir("..")
    del dir_list
    del dir_time
    del file_list
    del file_len
    return export_cost

def checkothers(path):
    choice = input("Please input 1 or 2:\n1:check main log\n2:check export log\n")
    content = input("Please input the content you want to check:\n")
    dir_list = os.listdir(path)
    dir_time = [os.path.getmtime(os.path.join(path, dir)) for dir in dir_list]
    newest_dir = dir_list[dir_time.index(max(dir_time))]
    os.chdir(os.path.join(path, newest_dir))
    file_list = os.listdir(os.path.join(path, newest_dir))
    file_len = [len(file) for file in file_list]
    judge = 0
    if choice == '1':
        shortest_file = file_list[file_len.index(min(file_len))]
        with open(shortest_file, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                if content in line:
                    print(line)
                    judge = 1
        if judge == 0:
            print("No content found")
        file.close()
    elif choice == '2':
        for file in file_list:
            if 'export' in file:
                export_file = file
        with open(export_file, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                if content in line:
                    print(line)
                    judge = 1
        if judge == 0:
            print("No content found")
        file.close()


if __name__ == "__main__":

    path = r"C:\Users\insta360\AppData\Local\Insta360\Insta360 Studio\log"
    choice = input("1:check log\n2:check others\n")
    if choice == '1':
        check(path)
    elif choice == '2':
        checkothers(path)
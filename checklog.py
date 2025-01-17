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
    importcost = sum(map(float, import_cost)) / len(import_cost)
    if importcost == 0:
        import_cost = re.findall(r'from single clip panel, cost: (\d+)', log_content)
        importcost = sum(map(float, import_cost)) / len(import_cost)
        if importcost == 0:
            import_cost = re.findall(r'Import footage, cost: (\d+)', log_content)
            importcost = sum(map(float, import_cost)) / len(import_cost) if import_cost else 0
    frame_fps_list = re.findall(r'HRenderNewFrame fps:(\d+\.\d+)', log_content)
    framefps = sum(map(float, frame_fps_list)) / len(frame_fps_list) if frame_fps_list else 0
    with open(export_file, 'r', encoding='utf-8', errors='ignore') as file:
        export_content = file.read()
    export_cost = re.findall(r'exporter time cost (\d+)', export_content)
    exportcost = sum(map(float, export_cost)) / len(export_cost) if export_cost else 0
    print("import cost:", importcost)
    print("frame fps:", framefps)
    print("export cost:", exportcost)


if __name__ == "__main__":
    path = r"C:\Users\insta360\AppData\Local\Insta360\Insta360 Studio\log"
    check(path)
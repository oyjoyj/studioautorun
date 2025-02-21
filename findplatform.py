import platform

def find_platform():
    os = platform.platform()
    if 'mac' in os:
        return 1
    else:
        return 2
    

if __name__ == '__main__':
    print(find_platform())
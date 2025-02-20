import platform

def find_platform():
    os = platform.platform()
    if 'mac' in os:
        return 1
    elif 'win' in os:
        return 2
    

if __name__ == '__main__':
    print(find_platform())
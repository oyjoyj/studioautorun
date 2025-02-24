#鼠标按下后记录当前坐标
from pynput.mouse import Listener, Button


def on_click(x, y, button, pressed):
    if button == Button.left and pressed:
        print(int(x), int(y))
    elif button == Button.right and pressed:
        print(int(x), int(y))

if __name__ == '__main__':
    with Listener(on_click=on_click) as listener:
        listener.join()
import time
import pyautogui
import keyboard
import win32api
import win32con

# import win32ui

pixel_color_list = [
    # black upgrade
    (32, 0, 0),
    (0, 0, 0),
    # red upgrade
    (128, 0, 0),
    (64, 0, 0),
    # green upgrade
    (94, 255, 62),
    (41, 255, 0),
    # orange upgrade
    (255, 156, 62),
    (255, 123, 0)
]

coordinate_list = []


def build_coordinate_list(x, y, offset):
    for i in range(5):
        coordinate_list.append((x, y + offset * i))


'''
def rgb_int_to_rgb_tuple(rgb_int):
    red = rgb_int & 255
    green = (rgb_int >> 8) & 255
    blue = (rgb_int >> 16) & 255
    return red, green, blue


def get_color(x, y):
    return rgb_int_to_rgb_tuple(win32ui.FindWindow(None, "Time Clickers").GetWindowDC().GetPixel(x, y))
'''


def check_if_is_clickable(x, y):
    try:
        pixel_color_list.index(pyautogui.pixel(x, y))
        return True
    except:
        return False


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def main():
    print('Running...')
    build_coordinate_list(2615, 560, 50)
    rainbow_ball_coordinate = (2800, 650)
    while True:
        if keyboard.is_pressed("-"):
            break
        for coordinate in coordinate_list:
            if check_if_is_clickable(coordinate[0], coordinate[1]):
                click(coordinate[0], coordinate[1])
                time.sleep(0.05)
            else:
                click(rainbow_ball_coordinate[0], rainbow_ball_coordinate[1])
                time.sleep(0.05)


main()

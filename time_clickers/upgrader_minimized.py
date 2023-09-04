from pyautogui import *
import pyautogui
import pywinauto
import time
import keyboard
import numpy as np
import random
import win32api
import win32con
import win32gui
import win32ui


pixel_color_list = [
    # black upgrade
    [0, 0, 0], [32, 0, 0],
    # red upgrade
    [64, 0, 0], [128, 0, 0],
    # green upgrade
    [94, 255, 62], [41, 255, 0],
    # orange upgrade
    [255, 156, 62], [255, 123, 0]
]

coordinate_list = [
    (140, 340),
    (140, 480),
    (140, 615),
    (140, 740),
    (140, 880)
]


def rgb_int_to_rgb_tuple(rgb_int):
    red = rgb_int & 255
    green = (rgb_int >> 8) & 255
    blue = (rgb_int >> 16) & 255
    return red, green, blue


def check_if_is_clickable(window_handle, x, y):
    color = win32gui.GetPixel(win32gui.GetDC(window_handle), x, y)
    rgb = rgb_int_to_rgb_tuple(color)
    for pixel_color in pixel_color_list:
        if (
                (rgb[0] == pixel_color[0])
                & (rgb[1] == pixel_color[1])
                & (rgb[2] == pixel_color[2])
        ):
            return True


def main():
    window_name = 'Time Clickers'
    window_handle = win32gui.FindWindow(None, window_name)

    pywinauto.Application(backend="uia")
    app = pywinauto.Application()
    app.connect(handle=window_handle)

    win = win32ui.CreateWindowFromHandle(window_handle)

    for coordinate in coordinate_list:
        print('check', coordinate)
        if check_if_is_clickable(window_handle, coordinate[0], coordinate[1]):
            print('click')
            lParam = win32api.MAKELONG(coordinate[0], coordinate[1])
            win.SendMessage(win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
            win.SendMessage(win32con.WM_LBUTTONUP, None, lParam)


main()


print('end')

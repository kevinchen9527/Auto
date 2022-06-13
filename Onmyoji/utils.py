# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址): 
@File:static_demo.py
@Time:2022/6/1 20:30

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
from pynput.mouse import Button, Controller as mouse_Controller
import win32api, win32gui, win32con, time
import os
import aircv as ac
import cv2
from PIL import ImageGrab

WINDOW_TITLE = "阴阳师 - MuMu模拟器"
WINDOW_CLASS = "Qt5QWindowIcon"

class utils():

    @staticmethod
    def mouse_click(circle_center_pos):
        """
        模拟鼠标操作
        :param circle_center_pos:
        :return:
        """
        win32api.SetCursorPos((int(circle_center_pos[0]) - 5, int(circle_center_pos[1]) + 5))  # 设置鼠标位置(x, y)

        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
                             win32con.MOUSEEVENTF_LEFTUP, int(circle_center_pos[0]) - 5, int(circle_center_pos[1]) + 5,
                             0, 0)  # 点击鼠标左键
    
    @staticmethod
    def check_img(up_img, last_img):
        """
        通过aircv库查找图片位置
        :return:
        """
        imsrc = ac.imread(os.path.abspath(os.path.dirname(__file__)) + '/' + up_img)
        imobj = ac.imread(os.path.abspath(os.path.dirname(__file__)) + '/' + last_img)
        # find the match position
        pos = ac.find_template(imsrc, imobj)
        if pos:
            circle_center_pos = pos['result']
            print('图片所在位置', circle_center_pos)
            return circle_center_pos
        else:
            print('没有找到图片')
            return None
    
    @staticmethod
    def save_screen_image(img_name):
        """
        保存窗体图片
        :return:
        """
        scim = ImageGrab.grab()
        scim.save(os.path.abspath(os.path.dirname(__file__)) + img_name)
    
    @staticmethod
    def find_game_windows():
        """
        获取游戏窗口
        :return:
        """
        window = win32gui.FindWindow(WINDOW_CLASS, WINDOW_TITLE)
        while not window:
            time.sleep(10)
            window = win32gui.FindWindow(None, WINDOW_TITLE)
        win32gui.SetForegroundWindow(window)
        pos = win32gui.GetWindowRect(window)
        return (pos[0], pos[1]), window
    
    @staticmethod
    def click_hell_ghost_king():
        """
        点击鬼王
        """


    def clicked_mitama():
        """
        御魂
        :return:
        """
        print('用户点击了探索')
        # ii. 获取屏幕截图 找到游戏里面的御魂按钮并调动鼠标去点击
        circle_center_pos = utils.check_img('screen.png','tan_suo.png')
        if circle_center_pos:
            utils.mouse_click(circle_center_pos)  # 模拟鼠标点击御魂主按钮
            time.sleep(2)
            utils.save_screen_image('/second_pic.png') # 保存探索进来的页面 继续进行操作
            pos = utils.check_img('second_pic.png', 'hell_ghost_king.png')
            if pos:
                utils.mouse_click(pos)

            

    @staticmethod
    def clicked_boss():
        """
        逢魔Boss
        :return:
        """
        print('用户点击了逢魔Boss')
        circle_center_pos = utils.check_img('screen.png', 'boss.png')
        if circle_center_pos:
            utils.mouse_click(circle_center_pos)  # 模拟鼠标点击御魂主按钮
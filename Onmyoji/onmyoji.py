# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址): 
@File:onmyoji.py
@Time:2022/5/17 17:04

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import time
import tkinter as tk
from utils import *

class onmyoji:
    def __init__(self, window):
        self.root = None
        self.window = window

    def create_windows(self):
        """
        创建功能窗口
        :return:
        """
        self.root = tk.Tk()
        self.root.title('阴阳师辅助')
        self.root.geometry('400x200')
        btn_1 = tk.Button(self.root, text="探索", width=8, height=2, command=utils.clicked_mitama)
        btn_1.grid(column=0, row=0)

        btn_2 = tk.Button(self.root, text="逢魔Boss", width=8, height=2, command= utils.clicked_boss)
        btn_2.grid(column=1, row=0)

if __name__ == '__main__':
    # 创建脚本窗口
    pos, window = utils.find_game_windows()
    onmyoji_example = onmyoji(window)
    if pos:
        time.sleep(3)
        utils.save_screen_image('/screen.png')
        onmyoji_example.create_windows()
        onmyoji_example.root.mainloop()
    else:
        print('没有找到游戏窗口')

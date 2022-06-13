# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址): 
@File:*.py
@Time:2022/6/10 19:08

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import os
import sys
import time
import threading
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


'''让电脑主板上的蜂鸣器哼歌'''
class ComputerSinger(QWidget):
    tool_name = '让电脑主板上的蜂鸣器哼歌'
    def __init__(self, parent=None, title='电脑主板上的蜂鸣器哼歌', **kwargs):
        super(ComputerSinger, self).__init__(parent)
        import ctypes
        rootdir = os.path.split(os.path.abspath(__file__))[0]
        self.rootdir = rootdir
        self.setFixedSize(500, 100)
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(os.path.join(rootdir, 'resources/icon.ico')))
        self.grid = QGridLayout()
        # 定义必要的组件
        # --label
        self.musicfilepath_label = QLabel('音乐简谱路径:')
        # --输入框
        self.musicfilepath_edit = QLineEdit(os.path.join(rootdir, 'resources/musicfiles/小幸运'))
        # --按钮
        self.choose_button = QPushButton('选择')
        self.play_button = QPushButton('播放')
        # 布局
        self.grid.addWidget(self.musicfilepath_label, 0, 0, 1, 1)
        self.grid.addWidget(self.musicfilepath_edit, 0, 1, 1, 4)
        self.grid.addWidget(self.choose_button, 1, 3, 1, 1)
        self.grid.addWidget(self.play_button, 1, 4, 1, 1)
        self.setLayout(self.grid)
        # 事件绑定
        self.choose_button.clicked.connect(self.openfile)
        self.play_button.clicked.connect(lambda _: threading.Thread(target=self.play).start())
        # 一些常量
        self.pitchs_dict = {'l': 0.5, 'm': 1., 'h': 2.}
        self.tone2freq_dict = {'C': 523, 'D': 587, 'E': 659, 'F': 698, 'G': 784, 'A': 880, 'B': 988}
        self.tone_scale = 1.06
        self.beats = 1000 * 60 / 65
        self.beep_player = ctypes.windll.kernel32
    '''打开文件'''
    def openfile(self):
        filepath = QFileDialog.getOpenFileName(self, '请选取音乐简谱', self.rootdir)
        self.musicfilepath_edit.setText(filepath[0])
    '''解析音乐简谱'''
    def parse(self, filepath):
        song_info = open(filepath, 'r').read().replace('\n', '').split(',')
        tone = song_info[0]
        song_info = song_info[1:]
        return tone, song_info
    '''播放'''
    def play(self):
        filepath = self.musicfilepath_edit.text()
        if not os.path.isfile(filepath):
            return
        tone, song_info = self.parse(filepath)
        do = self.tone2freq_dict[tone]
        re = int(do * self.tone_scale * self.tone_scale)
        mi = int(re * self.tone_scale * self.tone_scale)
        fa = int(mi * self.tone_scale * self.tone_scale)
        sol = int(fa * self.tone_scale * self.tone_scale)
        la = int(sol * self.tone_scale * self.tone_scale)
        si = int(la * self.tone_scale * self.tone_scale)
        notes = [0, do, re, mi, fa, sol, la, si]
        for item in song_info:
            if notes[int(item[0])] == 0:
                time.sleep(self.beats / 1000)
            else:
                self.beep_player.Beep(int(notes[int(item[0])]*self.pitchs_dict[item[1]]), int(self.beats * float(item[2:])))
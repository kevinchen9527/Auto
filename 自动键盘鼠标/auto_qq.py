# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址): 
@File:auto_qq.py
@Time:2022/5/28 13:53

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
from pynput.mouse import Button, Controller as mouse_Controller
from pynput.keyboard import Key, Controller as key_Controller
import time

mouse = mouse_Controller()  # 控制鼠标欢迎大家！
keyboard = key_Controller()  # 实例化了一个虚拟的键盘
mouse.press(Button.left)  # 按住鼠标左键
mouse.release(Button.left)  # 松开鼠标左键
for _ in range(100):  # 总共发多少次祝聚盛学老师全部中奖!!!/n祝聚盛学老师全部中奖!!!/n祝聚盛学老师全部中奖!!!/n祝聚盛学老师全部中奖!!!/n祝聚盛学老师全部中奖!!!
    time.sleep(0.2)  # 消息发送间隔时间
    keyboard.type('祝聚盛学老师全部中奖!!!') # 发送的消息内容
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)












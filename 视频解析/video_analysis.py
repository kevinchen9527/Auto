# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址): 
@File:video_analysis.py
@Time:2022/5/28 15:08

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import tkinter as tk
import requests
import webbrowser  # 使应用程序直接接入网页内容
from bs4 import BeautifulSoup


# 定义获取接口url地址的函数
def get_interface_url():
    url = 'http://ent.bigla.net//'  # 全民解析网址
    resp = requests.get(url)
    # print(resp.content.decode('utf-8'))  # 正确解码，显示包括汉字的二进制的网页源代码(前提是源代码是utf-8的
    resp.encoding = resp.apparent_encoding  # 从网页中获得源代码的编码，并设置解码
    response = resp.text  #
    bs = BeautifulSoup(response, 'html.parser')
    info_list = bs.findAll('option')
    # print(info_list)
    rootweb = list()
    for i in info_list:
        # print(i['value'])
        rootweb.append(i['value'])
    return (rootweb)  # 返回接口url列表


# 定义播放GUI
root = tk.Tk()
root.title('VIP视频播放器')
root.geometry('600x300+100+100')
l1 = tk.Label(root, text='播放接口:\n(打不开的换个接口)', font=('仿宋', 12), fg='red')
l1.grid(row=0, column=0)


# 定义播放函数
def play():
    webbrowser.open(var.get() + t1.get())


# 定义清除函数
def del_text():
    t1.delete(0, 'end')  # 清除文本输入框中的内容


# def savechrome():
#     new_addr = t2.get()
#     with open('addr.txt', 'w') as f:
#         f.write(new_addr)


one, two, three = get_interface_url()  # 获取接口地址并重新赋值给变量
six = 'https://www.1717yun.com/jx/ty.php?url='
seven = 'https://z1.m1907.cn/?jx='
# 定义变量，开始单选钮界面
var = tk.StringVar()
var.set(one)  # 设定初始单选钮值为one
r1 = tk.Radiobutton(root, text='vip专用解析', variable=var, value=one, justify='center', padx=100)
r1.grid(row=0, column=1)
r2 = tk.Radiobutton(root, text='优酷腾讯通道', variable=var, value=two,  justify='center', padx=150)
r2.grid(row=1, column=1)
r3 = tk.Radiobutton(root, text='电视剧解析', variable=var, value=three, justify='center')
r3.grid(row=2, column=1)
# r4 = tk.Radiobutton(root, text='B站解析(接口)', variable=var, value=four, justify='center')
# r4.grid(row=3, column=1)
r5 = tk.Radiobutton(root, text='默认VIP解析', variable=var, value=six, justify='center')
r5.grid(row=4, column=1)
r6 = tk.Radiobutton(root, text='其它引擎(接口)', variable=var, value=seven, justify='center')
r6.grid(row=5, column=1)

l2 = tk.Label(root, text='播放链接:', font=('仿宋', 12))
l2.grid(row=6, column=0)
t1 = tk.Entry(root, text='', width=50)
t1.grid(row=6, column=1)
# 定义播放按钮
b1 = tk.Button(root, text='播放', width=8, font=('仿宋', 12), command=play)
b1.grid(row=7, column=1)
b2 = tk.Button(root, text='清除', width=8, font=('仿宋', 12), command=del_text)
b2.grid(row=8, column=1)
# l3 = tk.Label(root, text='chrome地址:', font=('仿宋', 12))
# l3.grid(row=9, column=0)
# my_add = tk.StringVar()
# with open('addr.txt', 'r') as f:
#     addr_content = f.readline()
# my_add.set(addr_content)
# t2 = tk.Entry(root, width=50, textvariable=my_add)
# t2.grid(row=9, column=1)
# b3 = tk.Button(root, text='保存chrome地址', font=('仿宋', 12), command=savechrome)
# b3.grid(row=10, column=1)
root.mainloop()

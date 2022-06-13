# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址): 
@File:confession.py
@Time:2022/5/24 13:31

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""

from tkinter import *
from tkinter import messagebox


def closeallwindow():
    window.destroy()


def closeWindow():
    messagebox.showinfo(title="警告", message="关不掉吧,哈哈哈")
    return


def love():
    """
    按的喜欢
    :return: 
    """
    love = Toplevel(window)
    love.geometry("300x150+610+260")
    love.title("就知道你也是喜欢我的")
    label = Label(love, text="如家酒店9527等你", font=("华文行楷", 20), fg='red')
    label.pack()
    label = Label(love, text="电话给我,哈哈哈", font=("华文行楷", 25))
    label.pack()
    entry = Entry(love, font=("楷体", 15))
    entry.pack()
    btn = Button(love, text="嗯嗯", width=10, height=2, command=closeallwindow)
    btn.pack()
    love.protocol("WM_DELETE_WINDOW", closelove)


def closelove():
    messagebox.showinfo(title="好怂啊你", message="今天必须把事给办了!!!")
    return


def noLove():
    """
    按的不愿意
    :return:
    """
    no_love = Toplevel(window)

    no_love.geometry("320x120+610+260")

    no_love.title("我好喜欢你")

    label = Label(no_love, text="再给你一次机会考虑考虑呗", font=("华文行楷", 20), fg="red")

    label.pack()

    btn = Button(no_love, text="好吧", width=10, height=2, command=no_love.destroy)
    btn.pack()

    no_love.protocol("WM_DELETE_WINDOW", closeNoLove)


def closeNoLove():
    messagebox.showinfo(title="警告", message="不喜欢我，你就关不掉")
    noLove()


window = None


def createWindow():
    global window
    window = Tk()
    window.title("喜欢我么,来自一个帅哥的告白？")
    window.geometry("450x500+590+230")
    window.protocol("WM_DELETE_WINDOW", closeWindow)
    label1 = Label(window, text="小姐姐关注你很久了！", font=("华文行楷", 16), fg="red")
    label1.grid()
    label2 = Label(window, text="做我女朋友么?", font=("华文行楷", 26))
    label2.grid(row=1, column=1, sticky=E)
    photo = PhotoImage(file="cc.gif")
    imageLable = Label(window, image=photo)
    imageLable.grid(row=2, columnspan=2)
    btn1 = Button(window, text="愿意", width=15, height=2, command=love)
    btn1.grid(row=3, column=0, sticky=W)

    btn2 = Button(window, text="不愿意", width=15, height=2, command=noLove)

    btn2.grid(row=3, column=1, sticky=E)

    window.mainloop()


if __name__ == '__main__':
    createWindow()

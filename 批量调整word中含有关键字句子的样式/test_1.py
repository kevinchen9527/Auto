# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址): 
@File:test_1.py
@Time:2022/5/14 16:11

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import subprocess
import tkinter

from docx import Document
from docx.shared import RGBColor, Pt, Cm
from pptx import Presentation
import os
import glob
from tkinter import Tk, Frame, Button, Label, mainloop, filedialog, messagebox


class auto_work:
    def __init__(self) -> None:
        self.filepath = None

        # 创建窗体
        self.root = Tk()
        self.root.title("关键字")
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) // 3
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) // 3
        self.root.geometry(f"{x}x{y}")
        self.frame = Frame(self.root).grid(row=0, column=0)
        self.width = 10
        Button(self.frame, text="打开文件", width=self.width, height=1, command=self.open_file).grid(
            row=0, column=0)  #
        Label(self.frame, text="", height=1, width=self.width).grid(
            row=0, column=1)
        Button(self.frame, text="输入关键字", width=self.width, height=1, command=self.input_keyword).grid(
            row=0, column=2)  #
        Label(self.frame, text="", height=1, width=self.width).grid(
            row=0, column=3)
        Button(self.frame, text="导出ppt到word", width=self.width, height=1, command=self.export).grid(
            row=0, column=4)  #

    def export(self):
        """
        导出ppt内容到word
        :return:
        """
        pptx = Presentation(self.filepath)
        for slide in pptx.slides:
            pass



    def open_file(self):
        """
        选择文件
        :return:
        """
        self.screenwidth = self.root.winfo_screenwidth()
        self.screenheight = self.root.winfo_screenheight()
        self.root.geometry(
            f"{self.screenwidth}x{self.screenheight}+0+0")
        self.filepath = filedialog.askopenfilename(title='选择文件', filetypes=[
            ('文件', ['*.docx', '*.word', '*.ppt', '*.xlsx'])])
        print('打印文件地址', self.filepath)
        if self.filepath is None or self.filepath == "":
            messagebox.showwarning('警告', "请选择文件!")
        else:
            messagebox.showinfo('温馨提示', "选择文件成功!")

    def input_keyword(self):
        """
        弹出输入框
        :return:
        """
        if self.filepath is None or self.filepath == '':
            messagebox.showerror('错误', '请先选择要修改的文件')
            return
        self.windows = tkinter.Tk(className='输入关键字')  # 弹出框框名
        self.windows.geometry('270x60')  # 设置弹出框的大小 w x h
        self.entry_keyword = tkinter.Entry(self.windows, textvariable=tkinter.StringVar()).pack()
        tkinter.Button(self.windows, text="确认", command=self.recoder_keyword).pack()

    def recoder_keyword(self):
        """
        记录关键字
        :return:
        """
        print("===调起输入框了===", )
        user_keyword = self.entry_keyword.get()
        self.windows.destroy()
        new_file_path = r'd:\users\administrator\desktop\改变后的'
        if user_keyword == "":
            messagebox.showinfo("输入内容不能为空")
        else:
            for file in glob.glob(self.filepath):
                docx = Document(file)
                for paragraphs in docx.paragraphs:
                    for run in paragraphs.runs:
                        if user_keyword in run.text:
                            run.font.bold = True
                            run.font.color.rgb = RGBColor(255, 0, 0)
                docx.save(new_file_path + '/' + os.path.basename(file))
                messagebox.showinfo('温馨提示', '操作成功')


if __name__ == '__main__':
    main = auto_work()
    img = None
    new_img = None
    mainloop()

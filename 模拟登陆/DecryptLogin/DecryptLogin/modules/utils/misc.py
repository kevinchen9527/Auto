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
import imghdr
import shutil
from PIL import Image


'''显示图像'''
def showImage(imagepath):
    img = Image.open(imagepath)
    img.show()
    img.close()


'''移除图像'''
def removeImage(imagepath):
    os.remove(imagepath)


'''保存图像'''
def saveImage(image, imagepath):
    fp = open(imagepath, 'wb')
    fp.write(image)
    fp.close()
    filetype = imghdr.what(imagepath)
    assert filetype in ['jpg', 'jpeg', 'png', 'bmp', 'gif']
    imagepath_correct = f"{'.'.join(imagepath.split('.')[:-1])}.{filetype}"
    shutil.move(imagepath, imagepath_correct)
    return imagepath_correct
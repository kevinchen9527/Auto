# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址): 
@File:picture_compression.py
@Time:2022/5/27 19:08

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
from cv2 import cv2

imgs = cv2.imread('lingnai.jpg')
# 图片缩放至原图的1/4
resize_img = cv2.resize(imgs, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)
# 重写图片并保存
cv2.imwrite('lingnai_copy.jpg', resize_img)

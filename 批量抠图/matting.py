# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址): 
@File:matting.py
@Time:2022/5/26 17:00

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import paddlehub as hub
import os

huseg = hub.Module(name='deeplabv3p_xception65_humanseg')
path = './imgs/'  # 文件目录
files = [path + i for i in os.listdir(path)]  # 获取文件列表
results = huseg.segmentation(data={'image': files})  # 抠图

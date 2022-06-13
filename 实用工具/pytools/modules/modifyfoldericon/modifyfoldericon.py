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
import stat


'''文件夹图标批量修改'''
class ModifyFolderICON():
    def __init__(self, icon_path, **kwargs):
        assert os.path.exists(icon_path)
        self.icon_path = icon_path
    '''run'''
    def run(self):
        cur_dir = os.getcwd()
        for root, dirs, files in os.walk(os.getcwd(), topdown=False):
            os.chmod(root, stat.S_IREAD)
            for d in dirs:
                os.chdir(f'{os.path.join(root, d)}')
                if os.path.exists('desktop.ini'):
                    os.system('attrib -h -s desktop.ini')
                fp = open('desktop.ini', 'w')
                fp.write('[.ShellClassInfo]' + '\n' + f'IconResource={self.icon_path},0')
                fp.close()
                os.system('attrib +h desktop.ini')
                os.chdir(f'{cur_dir}')
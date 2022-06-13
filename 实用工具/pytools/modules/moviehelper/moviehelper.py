# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址): 
@File:*.py
@Time:2022/6/10 19:08

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import sys
from .apis import *


'''电影小助手'''
class MovieHelper():
    tool_name = '电影小助手'
    def __init__(self, **kwargs):
        self.__version = 'V 1.1.0'
        self.__author = '安然'
        self.__source = '微信公众号: ***'
        self.__helper_info = '输入<Q>退出, 输入<R>返回主界面.'
        self.__logo = r"""
__  __            _
|  \/  |          (_)
| \  / | _____   ___  ___
| |\/| |/ _ \ \ / / |/ _ \\
| |  | | (_) \ V /| |  __/
|_|  |_|\___/ \_/ |_|\___|
"""
    '''外部调用'''
    def run(self):
        while True:
            self.___printInfo()
            user_input = self.__input('请选择您需要的功能(输入对应的序号即可):\n[1].豆瓣电影查询\n[2].泡饭网电影资源搜索\n请输入:')
            if user_input == 'restart':
                continue
            if user_input == '1':
                flag = self.___doubanInquiry()
                if not flag:
                    continue
            elif user_input == '2':
                flag = self.__paofanSearch()
                if not flag:
                    continue
            else:
                print('[Warning]: 您的输入有误, 请重新输入.')
    '''豆瓣电影查询'''
    def ___doubanInquiry(self):
        douban_inquiry = Douban()
        flag = douban_inquiry.run()
        return flag
    '''泡饭影视电影资源搜索'''
    def __paofanSearch(self):
        paofan_search = Paofan()
        flag = paofan_search.run()
        return flag
    '''打印必要的信息'''
    def ___printInfo(self):
        print('-' * 60)
        print(self.__logo)
        print('[作者]: %s' % self.__author)
        print('[版本号]: %s' % self.__version)
        print('[微信公众号]: %s' % self.__source)
        print('[操作提示]: %s' % self.__helper_info)
        print('-' * 60)
    '''处理用户输入'''
    def __input(self, info):
        user_input = input(info)
        if user_input == 'q' or user_input == 'Q':
            sys.exit(0)
        elif user_input == 'r' or user_input == 'R':
            return 'restart'
        else:
            return user_input
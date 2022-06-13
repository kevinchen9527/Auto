# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址): 
@File:*.py
@Time:2022/6/10 19:08

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
from .baseclient import BaseClient


'''网易云音乐客户端'''
class Music163Client(BaseClient):
    def __init__(self, reload_history=True, **kwargs):
        super(Music163Client, self).__init__(website_name='music163', reload_history=reload_history, **kwargs)
    '''检查会话是否已经过期, 过期返回True'''
    def checksessionstatus(self, session, infos_return):
        url = 'https://music.163.com/#'
        response = session.get(url)
        if infos_return['response']['profile']['nickname'] in response.text:
            return False
        return True
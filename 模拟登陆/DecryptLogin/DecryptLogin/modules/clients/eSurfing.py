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


'''天翼客户端'''
class eSurfingClient(BaseClient):
    def __init__(self, reload_history=True, **kwargs):
        super(eSurfingClient, self).__init__(website_name='eSurfing', reload_history=reload_history, **kwargs)
    '''检查会话是否已经过期, 过期返回True'''
    def checksessionstatus(self, session, infos_return):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
            'referer': 'https://e.189.cn/user/index.do'
        }
        url = 'https://e.189.cn/user/safe/level.do'
        response = session.get(url, headers=headers)
        if infos_return['username'] in response.text:
            return False
        return True
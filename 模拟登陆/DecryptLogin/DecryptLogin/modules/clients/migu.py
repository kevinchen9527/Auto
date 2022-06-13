# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址): 
@File:*.py
@Time:2022/6/10 19:08

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import requests
from .baseclient import BaseClient


'''咪咕客户端'''
class MiguClient(BaseClient):
    def __init__(self, reload_history=True, **kwargs):
        super(MiguClient, self).__init__(website_name='migu', reload_history=reload_history, **kwargs)
    '''检查会话是否已经过期, 过期返回True'''
    def checksessionstatus(self, session, infos_return):
        cookies = requests.utils.dict_from_cookiejar(session.cookies)
        cookies_str = []
        for key in cookies.keys():
            cookies_str.append(f'{key}={cookies[key]}')
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
            'referer': 'https://music.migu.cn/v3/my',
            'cookie': '; '.join(cookies_str),
        }
        url = 'https://music.migu.cn/v3/api/my/listen/listend?page=1'
        response = session.get(url, headers=headers)
        if '成功' in response.text:
            return False
        return True
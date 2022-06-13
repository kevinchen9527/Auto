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


'''喜马拉雅客户端'''
class XimalayaClient(BaseClient):
    def __init__(self, reload_history=True, **kwargs):
        super(XimalayaClient, self).__init__(website_name='ximalaya', reload_history=reload_history, **kwargs)
    '''检查会话是否已经过期, 过期返回True'''
    def checksessionstatus(self, session, infos_return):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
        url = 'https://www.ximalaya.com/revision/main/getCurrentUser'
        response = session.get(url, headers=headers)
        if response.json()['ret'] == 200:
            return False
        return True
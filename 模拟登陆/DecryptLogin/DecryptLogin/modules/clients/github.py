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


'''Github客户端'''
class GithubClient(BaseClient):
    def __init__(self, reload_history=True, **kwargs):
        super(GithubClient, self).__init__(website_name='github', reload_history=reload_history, **kwargs)
    '''检查会话是否已经过期, 过期返回True'''
    def checksessionstatus(self, session, infos_return):
        url = 'https://github.com/'
        response = session.get(url)
        if 'octolytics-actor-login' in response.text:
            return False
        return True
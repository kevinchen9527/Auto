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


'''去哪儿旅行客户端'''
class QunarClient(BaseClient):
    def __init__(self, reload_history=True, **kwargs):
        super(QunarClient, self).__init__(website_name='qunar', reload_history=reload_history, **kwargs)
    '''检查会话是否已经过期, 过期返回True'''
    def checksessionstatus(self, session, infos_return):
        url = 'https://user.qunar.com/webApi/getPwdType.jsp'
        response = session.post(url)
        if 'success' in response.text:
            return False
        return True
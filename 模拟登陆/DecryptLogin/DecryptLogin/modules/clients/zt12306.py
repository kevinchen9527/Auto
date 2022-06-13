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


'''中国铁路12306客户端'''
class Zt12306Client(BaseClient):
    def __init__(self, reload_history=True, **kwargs):
        super(Zt12306Client, self).__init__(website_name='zt12306', reload_history=reload_history, **kwargs)
    '''检查会话是否已经过期, 过期返回True'''
    def checksessionstatus(self, session, infos_return):
        url = 'https://kyfw.12306.cn/otn/index/initMy12306Api'
        response = session.post(url)
        if response.json()['status'] and response.json()['httpstatus'] == 200:
            return False
        return True
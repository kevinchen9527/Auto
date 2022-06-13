# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址): 
@File:*.py
@Time:2022/6/10 19:08

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import time
from .baseclient import BaseClient


'''坚果云客户端'''
class JianguoyunClient(BaseClient):
    def __init__(self, reload_history=True, **kwargs):
        super(JianguoyunClient, self).__init__(website_name='jianguoyun', reload_history=reload_history, **kwargs)
    '''检查会话是否已经过期, 过期返回True'''
    def checksessionstatus(self, session, infos_return):
        url = f'https://www.jianguoyun.com/d/ajax/userop/getUserInfo?start=1&_={int(time.time() * 1000)}'
        response = session.get(url)
        if response.json()['accountState'] == 1:
            return False
        return True
# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址): 
@File:*.py
@Time:2022/6/10 19:08

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import re
from .baseclient import BaseClient


'''鱼C论坛客户端'''
class FishCClient(BaseClient):
    def __init__(self, reload_history=True, **kwargs):
        super(FishCClient, self).__init__(website_name='fishc', reload_history=reload_history, **kwargs)
    '''检查会话是否已经过期, 过期返回True'''
    def checksessionstatus(self, session, infos_return):
        url = 'https://fishc.com.cn/'
        response = session.get(url)
        nickname = re.findall(r'title="访问我的空间">(.*?)</a>', response.text)[0]
        if infos_return['nickname'] == nickname:
            return False
        return True
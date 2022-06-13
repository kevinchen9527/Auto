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


'''大众点评客户端'''
class DazhongdianpingClient(BaseClient):
    def __init__(self, reload_history=True, **kwargs):
        super(DazhongdianpingClient, self).__init__(website_name='dazhongdianping', reload_history=reload_history, **kwargs)
    '''检查会话是否已经过期, 过期返回True'''
    def checksessionstatus(self, session, infos_return):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        }
        url = 'http://www.dianping.com/'
        response = session.get(url, headers=headers)
        username = re.findall(r"'userName':.*?'(.*?)',", response.text)
        username = username[0] if username else 'fail to extract username'
        if username == infos_return['username']:
            return False
        return True
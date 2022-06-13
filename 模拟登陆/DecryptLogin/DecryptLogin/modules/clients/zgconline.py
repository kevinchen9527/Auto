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


'''中关村在线客户端'''
class ZgconlineClient(BaseClient):
    def __init__(self, reload_history=True, **kwargs):
        super(ZgconlineClient, self).__init__(website_name='zgconline', reload_history=reload_history, **kwargs)
    '''检查会话是否已经过期, 过期返回True'''
    def checksessionstatus(self, session, infos_return):
        url = f'https://my.zol.com.cn/index.php'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
        }
        params = {
            'c': 'Ajax_CalendarCheckV4',
            'a': 'InitSign',
            'callback': 'jQuery171013486989978367947_1646973223254',
            '_': str(int(time.time() * 1000)),
        }
        response = session.get(url, headers=headers, params=params)
        if 'signKeep' in response.text:
            return False
        return True
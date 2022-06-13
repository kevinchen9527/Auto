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
import requests
from .baseclient import BaseClient


'''腾讯视频客户端'''
class TencentVideoClient(BaseClient):
    def __init__(self, reload_history=True, **kwargs):
        super(TencentVideoClient, self).__init__(website_name='tencentvideo', reload_history=reload_history, **kwargs)
    '''检查会话是否已经过期, 过期返回True'''
    def checksessionstatus(self, session, infos_return):
        vqq_vuserid = session.cookies.get('vqq_vuserid')
        url = f'https://v.qq.com/s/videoplus/{vqq_vuserid}'
        response = session.get(url)
        response.encoding = 'utf-8'
        if infos_return['nickname'] in response.text:
            return False
        return True
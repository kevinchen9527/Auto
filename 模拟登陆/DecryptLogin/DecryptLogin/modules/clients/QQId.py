# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址): 
@File:*.py
@Time:2022/6/10 19:08

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import random
from .baseclient import BaseClient


'''QQId客户端'''
class QQIdClient(BaseClient):
    def __init__(self, reload_history=True, **kwargs):
        super(QQIdClient, self).__init__(website_name='QQId', reload_history=reload_history, **kwargs)
    '''检查会话是否已经过期, 过期返回True'''
    def checksessionstatus(self, session, infos_return):
        url = 'https://id.qq.com/cgi-bin/summary?'
        headers = {
            'referer': 'https://id.qq.com/myself/myself.html?ver=10049&',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
        }
        skey = infos_return['cookies']['skey']
        bkn = self.skey2bkn(skey)
        params = {
            'r': str(random.random()),
            'ldw': str(bkn)
        }
        response = session.get(url, headers=headers, params=params)
        if response.json().get('account_flag', None) == 0:
            return False
        return True
    '''根据skey参数得到bkn参数'''
    def skey2bkn(self, skey):
        bkn = 5381
        for c in skey:
            bkn += (bkn << 5) + ord(c)
        return 2147483647 & bkn
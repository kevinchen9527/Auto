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


'''爱课程客户端'''
class Icourse163Client(BaseClient):
    def __init__(self, reload_history=True, **kwargs):
        super(Icourse163Client, self).__init__(website_name='icourse163', reload_history=reload_history, **kwargs)
    '''检查会话是否已经过期, 过期返回True'''
    def checksessionstatus(self, session, infos_return):
        url = 'https://www.icourse163.org/course/SJTU-1003381021'
        response = session.get(url)
        term_id = re.findall(r'termId : "(\d+)"', response.text)[0]
        data = {
            'tid': term_id,
            'mob-token': infos_return['results']['mob-token'],
        }
        response = session.post('https://www.icourse163.org/mob/course/courseLearn/v1', data=data)
        if response.json()['status']['code'] == 0:
            return False
        return True
# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址): 
@File:*.py
@Time:2022/6/10 19:08

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import os
import json
import pickle
import requests


'''
Function:
    保存requests.Session()的cookies
Input:
    --session: 需要保存cookies的requests.Session()对象
    --cookiespath: cookies的保存路径
    --encoding: 编码方式
Return:
    --infos_return: 是否保存成功的flag, 以及错误原因
'''
def saveSessionCookies(session, cookiespath, encoding='utf-8'):
    infos_return = {'is_success': False, 'error_info': ''}
    # session格式不对
    if not isinstance(session, requests.Session):
        infos_return.update({'error_info': 'Expect requests.Session for session, but get %s' % type(session)})
        return infos_return
    # 以json格式保存
    if cookiespath.endswith('.json'):
        f = open(cookiespath, 'w', encoding=encoding)
        json.dump(session.cookies.get_dict(), f)
        f.close()
        infos_return.update({'is_success': True})
    # 以pikcle格式保存
    elif cookiespath.endswith('.pkl'):
        f = open(cookiespath, 'wb')
        pickle.dump(session.cookies, f)
        f.close()
        infos_return.update({'is_success': True})
    # 格式错误
    else:
        infos_return.update({'error_info': 'The format of cookiespath is wrong, expect json or pkl'})
    return infos_return


'''
Function:
    导入cookies到requests.Session()
Input:
    --session: 待导入cookies的requests.Session()对象
    --cookiespath: cookies的保存路径
    --encoding: 编码方式
Return:
    --infos_return: 是否导入成功的flag, 以及错误原因
    --session: 导入cookies之后requests.Session()对象
'''
def loadSessionCookies(session, cookiespath=None, encoding='utf-8'):
    infos_return = {'is_success': False, 'error_info': ''}
    # cookiespath不存在
    if not os.path.isfile(cookiespath):
        infos_return.update({'error_info': 'The cookiespath %s does not exist' % cookiespath})
        return infos_return, session
    # session格式不对
    if not isinstance(session, requests.Session):
        infos_return.update({'error_info': 'Expect requests.Session for session, but get %s' % type(session)})
        return infos_return, session
    # 导入json格式的cookies
    if cookiespath.endswith('.json'):
        f = open(cookiespath, 'r', encoding=encoding)
        session.cookies.update(json.load(f))
        f.close()
        infos_return.update({'is_success': True})
    # 导入pikcle格式的cookies
    elif cookiespath.endswith('.pkl'):
        f = open(cookiespath, 'rb')
        session.cookies = pickle.load(f)
        f.close()
        infos_return.update({'is_success': True})
    # 格式错误
    else:
        infos_return.update({'error_info': 'The format of cookiespath is wrong, expect json or pkl'})
    return infos_return, session
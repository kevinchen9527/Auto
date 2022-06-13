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
import requests
from ..utils import removeImage, showImage, saveImage


'''PC端登录凤凰网'''
class ifengPC():
    is_callable = True
    def __init__(self, **kwargs):
        for key, value in kwargs.items(): setattr(self, key, value)
        self.info = 'login in ifeng in pc mode'
        self.cur_path = os.getcwd()
        self.session = requests.Session()
        self.__initialize()
    '''登录函数'''
    def login(self, username, password, crack_captcha_func=None, **kwargs):
        # 设置代理
        self.session.proxies.update(kwargs.get('proxies', {}))
        # 获取验证码
        response = self.session.get(self.authcode_url)
        captcha_path = saveImage(response.content, os.path.join(self.cur_path, 'captcha.jpg'))
        if crack_captcha_func is None:
            showImage(captcha_path)
            captcha = input('Input the captcha: ')
        else:
            captcha = crack_captcha_func(captcha_path)
        removeImage(captcha_path)
        # 请求登录接口api_login_url进行模拟登录
        self.session.headers.update({
            'Upgrade-Insecure-Requests': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': 'http://id.ifeng.com/allsite/login'
        })
        data = {
            'u': username,
            'k': password,
            'auth': captcha,
            'type': '3',
            'confrom': ''
        }
        response = self.session.post(self.api_login_url, data=data)
        response_json = response.json()
        # 登录成功
        if response_json.get('code') == 1 and response_json.get('msgcode') == '0':
            print('[INFO]: Account -> %s, login successfully' % username)
            infos_return = {'username': username}
            infos_return.update(response_json)
            return infos_return, self.session
        # 验证码错误
        elif response_json.get('code') == 0 and response_json.get('msgcode') == '4009':
            raise RuntimeError('Account -> %s, fail to login, crack captcha error' % username)
        # 用户名或密码错误
        elif response_json.get('code') == 0 and response_json.get('msgcode') == '8003':
            raise RuntimeError('Account -> %s, fail to login, username or password error' % username)
        # 其他错误
        else:
            raise RuntimeError(response_json.get('message'))
    '''初始化'''
    def __initialize(self):
        self.headers = {
            'Host': 'id.ifeng.com',
            'Origin': 'https://id.ifeng.com',
            'Referer': 'https://id.ifeng.com/user/login',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
        }
        self.api_login_url = 'https://id.ifeng.com/api/login'
        self.authcode_url = 'https://id.ifeng.com/public/authcode'
        self.session.headers.update(self.headers)


'''移动端登录凤凰网'''
class ifengMobile():
    is_callable = False
    def __init__(self, **kwargs):
        for key, value in kwargs.items(): setattr(self, key, value)
        self.info = 'login in ifeng in mobile mode'


'''扫码登录凤凰网'''
class ifengScanqr():
    is_callable = False
    def __init__(self, **kwargs):
        for key, value in kwargs.items(): setattr(self, key, value)
        self.info = 'login in ifeng in scanqr mode'


'''
Function:
    凤凰网模拟登录
Detail:
    -login:
        Input:
            --username: 用户名
            --password: 密码
            --mode: mobile/pc/scanqr
            --crack_captcha_func: 若提供验证码接口, 则利用该接口来实现验证码的自动识别
            --proxies: 为requests.Session()设置代理
        Return:
            --infos_return: 用户名等信息
            --session: 登录后的requests.Session()
'''
class ifeng():
    def __init__(self, **kwargs):
        self.info = 'login in ifeng'
        self.supported_modes = {
            'pc': ifengPC(**kwargs),
            'mobile': ifengMobile(**kwargs),
            'scanqr': ifengScanqr(**kwargs),
        }
    '''登录函数'''
    def login(self, username, password, mode='pc', crack_captcha_func=None, **kwargs):
        assert mode in self.supported_modes, 'unsupport mode %s in ifeng.login' % mode
        selected_api = self.supported_modes[mode]
        if not selected_api.is_callable: raise NotImplementedError('not be implemented for mode %s in ifeng.login' % mode)
        args = {
            'username': username,
            'password': password,
            'crack_captcha_func': crack_captcha_func,
        }
        args.update(kwargs)
        return selected_api.login(**args)
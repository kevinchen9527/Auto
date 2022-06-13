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
import time
import execjs
import requests
from hashlib import md5


'''PC端登录搜狐'''
class sohuPC():
    is_callable = True
    def __init__(self, **kwargs):
        for key, value in kwargs.items(): setattr(self, key, value)
        self.info = 'login in sohu in pc mode'
        self.session = requests.Session()
        self.__initialize()
    '''登录函数'''
    def login(self, username, password, crack_captcha_func=None, **kwargs):
        # 设置代理
        self.session.proxies.update(kwargs.get('proxies', {}))
        # 初始化session
        headers = {'cookie': 'itssohu=true; reqtype=pc; SUV=210320172555UVPR; a=123'}
        response = self.session.get('https://v4.passport.sohu.com/i/cookie/common?callback=passport403_cb1623241226789', headers=headers)
        response = self.session.get('https://v4.passport.sohu.com/i/jf/code?type=0')
        response_text = response.text
        response_text = execjs.compile('''function convert(inputs) {
            document = {};
            return eval(inputs)
        }''').call('convert', response_text.replace('"', ''))
        jv = re.search('jv=(.*?);', response_text).group(1)
        self.session.cookies.set('jv', jv)
        # 请求login_url
        data = {
            'userid': username,
            'password': md5(password.encode(encoding='utf-8')).hexdigest(),
            'persistentCookie': '1',
            'appid': '116005',
        }
        response = self.session.post(self.login_url, data=data)
        response_json = response.json()
        # 登录成功
        if response_json.get('status') == 200 and response_json.get('message') == 'Success':
            print('[INFO]: Account -> %s, login successfully' % username)
            infos_return = {'username': username}
            infos_return.update(response_json)
            return infos_return, self.session
        # 账号或密码有误
        elif response_json.get('status') in [404, 459]:
            raise RuntimeError('Account -> %s, fail to login, username or password error' % username)
        # 其他原因
        else:
            raise RuntimeError(response_json.get('message'))
    '''初始化'''
    def __initialize(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
            'referer': 'https://www.sohu.com/',
            'origin': 'https://www.sohu.com',
        }
        self.login_url = 'https://v4.passport.sohu.com/i/login/116005'
        self.session.headers.update(self.headers)


'''移动端登录搜狐'''
class sohuMobile():
    is_callable = True
    def __init__(self, **kwargs):
        for key, value in kwargs.items(): setattr(self, key, value)
        self.info = 'login in sohu in mobile mode'
        self.session = requests.Session()
        self.__initialize()
    '''登录函数'''
    def login(self, username, password, crack_captcha_func=None, **kwargs):
        # 设置代理
        self.session.proxies.update(kwargs.get('proxies', {}))
        # 访问app_login_url
        params = {
            'appid': '116001',
            'r': 'https://m.sohu.com/ucenter?_from=passport'
        }
        self.session.get(self.app_login_url, params=params)
        # 请求security_login_url
        data = {
            'userid': username,
            'password': md5(password.encode(encoding='utf-8')).hexdigest(),
            'appid': '116001'
        }
        self.session.headers.update({
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://m.passport.sohu.com',
            'Referer': 'https://m.passport.sohu.com/app/login?appid=116001&r=https%3A%2F%2Fm.sohu.com%2Fucenter%3F_from%3Dpassport'
        })
        response = self.session.post(self.security_login_url.format(int(time.time()*1000)), data=data)
        response_json = response.json()
        # 登录成功
        if response_json.get('status') == 200 and response_json.get('message') == 'Success':
            print('[INFO]: Account -> %s, login successfully' % username)
            infos_return = {'username': username}
            infos_return.update(response_json)
            return infos_return, self.session
        # 账号或密码有误
        elif response_json.get('status') in [404, 459]:
            raise RuntimeError('Account -> %s, fail to login, username or password error' % username)
        # 其他原因
        else:
            raise RuntimeError(response_json.get('message'))
    '''初始化'''
    def __initialize(self):
        self.headers = {
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
        }
        self.app_login_url = 'https://m.passport.sohu.com/app/login'
        self.security_login_url = 'https://m.passport.sohu.com/security/login?t={}'
        self.session.headers.update(self.headers)


'''扫码登录搜狐'''
class sohuScanqr():
    is_callable = False
    def __init__(self, **kwargs):
        for key, value in kwargs.items(): setattr(self, key, value)
        self.info = 'login in sohu in scanqr mode'


'''
Function:
    搜狐模拟登录
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
class sohu():
    def __init__(self, **kwargs):
        self.info = 'login in sohu'
        self.supported_modes = {
            'pc': sohuPC(**kwargs),
            'mobile': sohuMobile(**kwargs),
            'scanqr': sohuScanqr(**kwargs),
        }
    '''登录函数'''
    def login(self, username, password, mode='mobile', crack_captcha_func=None, **kwargs):
        assert mode in self.supported_modes, 'unsupport mode %s in sohu.login' % mode
        selected_api = self.supported_modes[mode]
        if not selected_api.is_callable: raise NotImplementedError('not be implemented for mode %s in sohu.login' % mode)
        args = {
            'username': username,
            'password': password,
            'crack_captcha_func': crack_captcha_func,
        }
        args.update(kwargs)
        return selected_api.login(**args)
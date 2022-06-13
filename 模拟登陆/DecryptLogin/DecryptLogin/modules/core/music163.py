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
import time
import codecs
import qrcode
import base64
import hashlib
import requests
from Crypto.Cipher import AES
from ..utils import removeImage, saveImage, showImage


'''用于算post的两个参数, 具体原理详见知乎: https://www.zhihu.com/question/36081767'''
class Cracker():
    def __init__(self):
        self.modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
        self.nonce = '0CoJUm6Qyw8W8jud'
        self.pubKey = '010001'
    '''get'''
    def get(self, text):
        text = json.dumps(text)
        secKey = self.__createSecretKey(16)
        encText = self.__aesEncrypt(self.__aesEncrypt(text, self.nonce), secKey)
        encSecKey = self.__rsaEncrypt(secKey, self.pubKey, self.modulus)
        post_data = {
            'params': encText,
            'encSecKey': encSecKey
        }
        return post_data
    '''aesEncrypt'''
    def __aesEncrypt(self, text, secKey):
        pad = 16 - len(text) % 16
        if isinstance(text, bytes):
            text = text.decode('utf-8')
        text = text + str(pad * chr(pad))
        secKey = secKey.encode('utf-8')
        encryptor = AES.new(secKey, 2, b'0102030405060708')
        text = text.encode('utf-8')
        ciphertext = encryptor.encrypt(text)
        ciphertext = base64.b64encode(ciphertext)
        return ciphertext
    '''rsaEncrypt'''
    def __rsaEncrypt(self, text, pubKey, modulus):
        text = text[::-1]
        rs = int(codecs.encode(text.encode('utf-8'), 'hex_codec'), 16) ** int(pubKey, 16) % int(modulus, 16)
        return format(rs, 'x').zfill(256)
    '''createSecretKey'''
    def __createSecretKey(self, size):
        return (''.join(map(lambda xx: (hex(ord(xx))[2:]), str(os.urandom(size)))))[0:16]


'''PC端登录网易云音乐'''
class music163PC():
    is_callable = True
    def __init__(self, **kwargs):
        for key, value in kwargs.items(): setattr(self, key, value)
        self.info = 'login in music163 in pc mode'
        self.session = requests.Session()
        self.__initialize()
    '''登录函数'''
    def login(self, username, password, crack_captcha_func=None, **kwargs):
        # 设置代理
        self.session.proxies.update(kwargs.get('proxies', {}))
        # 获得账号类型
        account_type = self.__getAccountType(username)
        # 模拟登录
        password = hashlib.md5(password.encode('utf-8')).hexdigest()
        data = {
            'password': password,
            'rememberLogin': 'True'
        }
        if account_type == 'phone':
            data['phone'] = username
            data = self.cracker.get(data)
            response = self.session.post(self.login_url_phone, headers=self.login_headers, data=data)
        else:
            data['username'] = username
            data = self.cracker.get(data)
            response = self.session.post(self.login_url_email, headers=self.login_headers, data=data)
        response_json = response.json()
        # 登录成功
        if response_json['code'] == 200:
            print('[INFO]: Account -> %s, login successfully' % username)
            infos_return = {'username': username, 'response': response_json}
            return infos_return, self.session
        # 账户名/密码错误
        elif (response_json['code'] == 400) or (response_json['code'] == 502):
            raise RuntimeError('Account -> %s, fail to login, username or password error' % username)
        # 其他错误
        else:
            raise RuntimeError(response_json.get('msg')) if 'msg' in response_json else RuntimeError(response_json.get('message'))
    '''获取账号类型(手机号/邮箱)'''
    def __getAccountType(self, username):
        if '@' not in username: account_type = 'phone'
        else: account_type = 'email'
        return account_type
    '''初始化'''
    def __initialize(self):
        self.login_headers = {
            'Accept':'*/*',
            'Accept-Language':'zh-CN,zh;q=0.8,gl;q=0.6,zh-TW;q=0.4',
            'Connection':'keep-alive',
            'Content-Type':'application/x-www-form-urlencoded',
            'Referer':'http://music.163.com',
            'Host':'music.163.com',
            'Cookie': 'os=pc; osver=Microsoft-Windows-10-Professional-build-10586-64bit; appver=2.0.3.131777; channel=netease; __remember_me=true;',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
        }
        self.login_url_email = 'http://music.163.com/weapi/login?csrf_token='
        self.login_url_phone = 'http://music.163.com/weapi/login/cellphone?csrf_token='
        self.cracker = Cracker()


'''移动端登录网易云音乐'''
class music163Mobile():
    is_callable = False
    def __init__(self, **kwargs):
        for key, value in kwargs.items(): setattr(self, key, value)
        self.info = 'login in music163 in mobile mode'


'''扫码登录网易云音乐'''
class music163Scanqr():
    is_callable = True
    def __init__(self, **kwargs):
        for key, value in kwargs.items(): setattr(self, key, value)
        self.info = 'login in music163 in scanqr mode'
        self.cur_path = os.getcwd()
        self.session = requests.Session()
        self.__initialize()
    '''登录函数'''
    def login(self, username='', password='', crack_captcha_func=None, **kwargs):
        # 获得unikey
        data = {
            'type': '1',
            'csrf_token': ''
        }
        data = self.cracker.get(data)
        response = self.session.post(self.unikey_url, data=data)
        # 制作二维码
        scan_url = self.codekey_url.format(response.json()['unikey'])
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=2)
        qr.add_data(scan_url)
        qr.make(fit=True)
        img = qr.make_image(fill_color='black', back_color='white')
        img.save(os.path.join(self.cur_path, 'qrcode.jpg'))
        showImage(os.path.join(self.cur_path, 'qrcode.jpg'))
        # 检测二维码状态
        data = {
            'csrf_token': '',
            'key': response.json()['unikey'],
            'type': '1',
        }
        data = self.cracker.get(data)
        while True:
            response = self.session.post(self.checklogin_url, data=data)
            if response.json()['code'] in [803]:
                break
            elif response.json()['code'] in [801, 802]:
                continue
            else:
                raise RuntimeError(response.json())
            time.sleep(0.5)
        # 登录成功
        removeImage(os.path.join(self.cur_path, 'qrcode.jpg'))
        csrf = self.session.cookies.get('__csrf')
        data = self.cracker.get({'csrf_token': csrf})
        response = self.session.post(self.account_url.format(csrf), data=data)
        response_json = response.json()
        infos_return = {
            'nickname': response_json['profile']['nickname'], 
            'csrf': csrf,
            'response': response_json,
        }
        print('[INFO]: Account -> %s, login successfully' % infos_return['nickname'])
        return infos_return, self.session
    '''初始化'''
    def __initialize(self):
        self.headers = {
            'Content-Type':'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62',
        }
        self.session.headers.update(self.headers)
        self.unikey_url = 'https://music.163.com/weapi/login/qrcode/unikey?csrf_token='
        self.codekey_url = 'http://music.163.com/login?codekey={}'
        self.checklogin_url = 'https://music.163.com/weapi/login/qrcode/client/login?csrf_token='
        self.account_url = 'https://music.163.com/weapi/w/nuser/account/get?csrf_token={}'
        self.cracker = Cracker()


'''
Function:
    网易云音乐模拟登录
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
class music163():
    def __init__(self, **kwargs):
        self.info = 'login in music163'
        self.supported_modes = {
            'pc': music163PC(**kwargs),
            'mobile': music163Mobile(**kwargs),
            'scanqr': music163Scanqr(**kwargs),
        }
    '''登录函数'''
    def login(self, username, password, mode='pc', crack_captcha_func=None, **kwargs):
        assert mode in self.supported_modes, 'unsupport mode %s in music163.login' % mode
        selected_api = self.supported_modes[mode]
        if not selected_api.is_callable: raise NotImplementedError('not be implemented for mode %s in music163.login' % mode)
        args = {
            'username': username,
            'password': password,
            'crack_captcha_func': crack_captcha_func,
        }
        args.update(kwargs)
        return selected_api.login(**args)
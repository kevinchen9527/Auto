# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址): 
@File:*.py
@Time:2022/6/10 19:08

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import warnings
if __name__ == '__main__':
    from modules import *
    from __init__ import __version__
else:
    from .modules import *
    from .__init__ import __version__
warnings.filterwarnings('ignore')


'''微信小助手'''
class pikachuwechat():
    def __init__(self, **kwargs):
        print(self)
        for key, value in kwargs.items(): setattr(self, key, value)
        self.supported_funcs = self.initializeallfuncs()
    '''开发者调用对应的功能'''
    def execute(self, func_type=None, config={}):
        assert func_type in self.supported_funcs, 'unsupport func_type %s...' % func_type
        client = self.supported_funcs[func_type](**config)
        client.run()
    '''初始化所有功能'''
    def initializeallfuncs(self):
        supported_funcs = {
            'AutoReply': AutoReply,
            'AntiWithdrawal': AntiWithdrawal,
            'AnalysisFriends': AnalysisFriends,
        }
        return supported_funcs
    '''获得所有支持的功能信息'''
    def getallsupported(self):
        all_supports = {}
        for key, value in self.supported_funcs.items():
            all_supports[value.func_name] = key
        return all_supports


'''run'''
if __name__ == '__main__':
    import random
    wechat_helper = pikachuwechat()
    all_supports = wechat_helper.getallsupported()
    wechat_helper.execute('AnalysisFriends')
    # wechat_helper.execute(random.choice(list(all_supports.values())))
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
try: from .crawlers import *
except: from crawlers import *
warnings.filterwarnings('ignore')


'''模拟登录系列爬虫调用客户端'''
class Client():
    def __init__(self, disable_print_auth=True, **kwargs):
        if not disable_print_auth: print(self)
        self.supported_crawlers = {
            'bilibililottery': BiliBiliLottery, 'weiboemoji': WeiboEmoji, 'weiboblacklist': WeiboBlackList, 'weibowater': WeiboWater,
            'weibosender': WeiboSender, 'weibomonitor': WeiboMonitor, 'userweibospider': UserWeiboSpider, 'delallweibos': DelAllWeibos,
            'cloud189signin': Cloud189Signin, 'clearqzone': ClearQzone, 'moocdl': MOOCDL, 'bilibiliupmonitor': BilibiliUPMonitor,
            'bilibiliuservideos': BilibiliUserVideos, 'modifymihealthsteps': ModifyMiHealthSteps, 'neteaseeveryday': NeteaseEveryday,
            'neteaseclickplaylist': NeteaseClickPlaylist, 'neteaselistenleaderboard': NeteaseListenLeaderboard, 'neteasesignin': NeteaseSignin,
            'neteasesonglistdownloader': NeteaseSongListDownloader, 'tbgoods': TBGoods, 'jdgoods': JDGoods, 'jingdongsnap': JingDongSnap,
            'taobaosnap': TaobaoSnap, 'qqreports': QQReports, 'weibolottery': WeiboLottery,
        }
        for key, value in self.supported_crawlers.items():
            setattr(self, key, value)
    '''执行对应的爬虫'''
    def executor(self, crawler_type=None, config={}):
        crawler = self.supported_crawlers[crawler_type](**config)
        return crawler.run()
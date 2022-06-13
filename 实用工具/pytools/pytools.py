# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址): 
@File:pytools.py
@Time:2022/6/10 19:08

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import sys
import warnings
from PyQt5.QtWidgets import QApplication
import tkinter as tk

if __name__ == '__main__':
    from modules import *
    from __init__ import __version__
else:
    from .modules import *
    from .__init__ import __version__
warnings.filterwarnings('ignore')

'''Python实用工具集'''


class pytools():
    def __init__(self, **kwargs):
        for key, value in kwargs.items(): setattr(self, key, value)
        self.supported_tools = self.initialize()
        print(self)

    '''执行对应的小程序'''

    def execute(self, tool_type=None, config={}):
        assert tool_type in self.supported_tools, 'unsupport tool_type %s...' % tool_type
        qt_tools = [
            'newyearcardgenerator', 'luxunsentencesquery', 'artsigngenerator', 'genderpredictor', 'musicplayer',
            'qrcodegenerator', 'videoplayer',
            'trumptweetsgenerator', 'coupletgenerator', 'idcardquery', 'idiomsolitaire', 'inquiryexpress',
            'succulentquery', 'translator',
            'desktoppet', 'computersinger', 'hubbleseeonbirthday', 'ukrainemap', 'sovietgenerator', 'goodgoodgenerator',
            'tianyancha'
        ]
        if tool_type in qt_tools:
            app = QApplication(sys.argv)
            client = self.supported_tools[tool_type](**config)
            client.show()
            sys.exit(app.exec_())
        else:
            client = self.supported_tools[tool_type](**config)
            client.run()

    '''初始化'''

    def initialize(self):
        supported_tools = {
            'timer': Timer, 'clock': Clock, 'runcat': RunCat, 'ukrainemap': UkraineMap,
            'desktoppet': DesktopPet, 'translator': Translator, 'calculator': Calculator, 'arxivhelper': ArxivHelper,
            'moviehelper': MovieHelper, 'videoplayer': VideoPlayer, 'musicplayer': MusicPlayer,
            'idcardquery': IDCardQuery,
            'portscanner': PortScanner, 'playfireworks': PlayFireworks, 'emailsecurity': EmailSecurity,
            'earthwallpaper': EarthWallpaper,
            'computersinger': ComputerSinger, 'inquiryexpress': InquiryExpress, 'idiomsolitaire': IdiomSolitaire,
            'succulentquery': SucculentQuery,
            'iplocationquery': IPLocationQuery, 'genderpredictor': GenderPredictor, 'qrcodegenerator': QRCodeGenerator,
            'coupletgenerator': CoupletGenerator,
            'artsigngenerator': ArtSignGenerator, 'controlpcbyemail': ControlPCbyEmail,
            'naughtyconfession': NaughtyConfession, 'luxunsentencesquery': LuxunSentencesQuery,
            'hubbleseeonbirthday': HubbleSeeOnBirthday, 'newyearcardgenerator': NewYearCardGenerator,
            'trumptweetsgenerator': TrumpTweetsGenerator, 'sovietgenerator': SovietGenerator,
            'goodgoodgenerator': GoodGoodGenerator, 'tianyancha': Tianyancha, 'decryptbrowser': DecryptBrowser,
            'githubacceleration': GithubAcceleration,
            'modifyfoldericon': ModifyFolderICON,
        }
        return supported_tools

    '''获得所有支持的tools信息'''

    def getallsupported(self):
        all_supports = {}
        for key, value in self.supported_tools.items():
            all_supports[value] = key
        return all_supports

def init_tool_name():
    supported_tool_name = {
        'timer': '简易定时器', 'clock': '简易时钟', 'runcat': '奔跑的猫', 'ukrainemap': '乌克兰地图查询系统',
            'desktoppet': '桌面宠物', 'translator': '翻译软件', 'calculator': '简易计算器', 'arxivhelper': 'arxiv获取论文',
            'moviehelper': '电影小助手', 'videoplayer': '视频播放器', 'musicplayer': '音乐播放器',
            'idcardquery': '身份证信息查询',
            'portscanner': '端口扫描器', 'playfireworks': '放烟花效果', 'emailsecurity': '邮箱安全性验证工具',
            'earthwallpaper': '动态更新地球壁纸',
            'computersinger': '电脑主板上的蜂鸣器哼歌', 'inquiryexpress': '快递查询系统', 'idiomsolitaire': '成语接龙',
            'succulentquery': '多肉数据查询系统',
            'iplocationquery': 'IP地址查询地理信息', 'genderpredictor': '中文名性别猜测', 'qrcodegenerator': '二维码生成器',
            'coupletgenerator': '对联生成器',
            'artsigngenerator': '艺术签名生成器', 'controlpcbyemail': '邮件控制电脑',
            'naughtyconfession': '仿抖音表白神器', 'luxunsentencesquery': '鲁迅名言查询系统',
            'hubbleseeonbirthday': '生日那天的宇宙', 'newyearcardgenerator': '新年贺卡生成器',
            'trumptweetsgenerator': '特朗普推特生成器', 'sovietgenerator': '苏联笑话生成器',
            'goodgoodgenerator': '稳中向好生成器', 'tianyancha': '天眼查', 'decryptbrowser': '盗取浏览器里的账号密码',
            'githubacceleration': '国内访问Github一键加速脚本',
            'modifyfoldericon': '文件夹图标批量修改',
    }
    return supported_tool_name

def printf_button(f):
    print('用户点击了', f)
    print('is here hava root?', root)
    root.destroy()
    tool_client.execute(f)
    

def createButton(supported_tool_name):
    global root
    root = tk.Tk()
    root.title('游戏选择窗口')
    root.geometry('700x300+100+100')
    ButtonList = []
    for _ in range(len(supported_tool_name)):
        ButtonList.append(0)  # 创建储存按钮对象的列表
    sx = 20
    ssx = 20
    sssx = 20
    ssssx = 20
    i = 0
    for k, v in supported_tool_name.items():
        i += 1
        if sx <= 540:
            ButtonList[i - 1] = tk.Button(root, text=v, bg="white", width=10, height=2, justify='center', fg='black',
                                          command=lambda f=k: printf_button(f))
            ButtonList[i - 1].place(x=sx, y=20)
        else:
            if ssx <= 540:
                ButtonList[i - 1] = tk.Button(root, text=v, bg="white", width=10, height=2, justify='center', fg='black',
                                              command=lambda f=k: printf_button(f))
                ButtonList[i - 1].place(x=ssx, y=80)
            else:
                if sssx <= 540:
                    ButtonList[i - 1] = tk.Button(root, text=v, bg="white", width=10, height=2, justify='center',
                                                  fg='black', command=lambda f=k: printf_button(f))
                    ButtonList[i - 1].place(x=sssx, y=140)
                else:
                    ButtonList[i - 1] = tk.Button(root, text=v, bg="white", width=10, height=2, justify='center',
                                                  fg='black', command=lambda f=k: printf_button(f))
                    ButtonList[i - 1].place(x=ssssx, y=200)
                    ssssx += 60
                sssx += 60
            ssx += 60
        sx += 60
    root.mainloop()



'''run'''
if __name__ == '__main__':
    supported_tool_name = init_tool_name()
    tool_client = pytools()
    # all_supports = tool_client.getallsupported()
    createButton(supported_tool_name)
    # tool_client.execute(random.choice(list(all_supports.values())))

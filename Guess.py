# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址):
@File:guess.py
@Time:2022/5/14 13:31
@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
# 做一个商城抽奖系统 抽奖范围是1-20 只有一个中奖号码 每个人有三次机会 要给出每次猜的结果的提示 三次内答错继续 3次完结束 或者答对结束
import random
winning_num = random.randint(1, 20)  # 中奖号码
counts = 3  # 每个人有三次机会
while True:
    if counts > 0:
        you_num = int(input('请告诉我你的号码:'))
        if you_num == winning_num:
            print('恭喜你中奖了')
        elif you_num > winning_num:
            print('你的中奖号码大了哦')
        elif you_num < winning_num:
            print('你的中奖号码小了哦')
    else:
        print('你没次数了哦')
        break
    counts -= 1










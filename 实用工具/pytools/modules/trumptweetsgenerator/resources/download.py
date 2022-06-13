# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址): 
@File:*.py
@Time:2022/6/10 19:08

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import json
import requests


'''下载'''
def download():
    tweets = []
    for year in range(2009, 2021):
        url = f'http://www.trumptwitterarchive.com/data/realdonaldtrump/{year}.json'
        response = requests.get(url)
        response_json = response.json()
        for item in response_json:
            tweets.append(item)
    with open('trump_tweets.json', 'w', encoding='utf-8') as fp:
        json.dump(tweets, fp)


'''run'''
if __name__ == '__main__':
    download()
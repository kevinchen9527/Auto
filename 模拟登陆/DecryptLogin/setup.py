# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址): 
@File:*.py
@Time:2022/6/10 19:08

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import DecryptLogin
from setuptools import setup, find_packages


'''readme'''
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()


'''setup'''
setup(
    name=DecryptLogin.__title__,
    version=DecryptLogin.__version__,
    description=DecryptLogin.__description__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent'
    ],
    author=DecryptLogin.__author__,
    url=DecryptLogin.__url__,
    author_email=DecryptLogin.__email__,
    license=DecryptLogin.__license__,
    include_package_data=True,
    install_requires=list(open('requirements.txt', 'r').readlines()),
    zip_safe=True,
    packages=find_packages()
)
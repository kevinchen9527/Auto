# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址): 
@File:read_excel.py
@Time:2022/5/14 13:59

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import pandas as pd
import numpy as np
"""
函数传值介绍 
    io,   文件地址
    sheet_name: str | int | list[IntStrT] | None = 0, sheet_name 可以传名字 也可以传Int从0开始
    header: int | Sequence[int] | None = 0,
    names=None,
    index_col: int | Sequence[int] | None = None,  从0开始 把第几列作为索引
    usecols=None,  # 取第几列 [A, 'C:D'] 取A 和 C D  A为第一列
    squeeze: bool | None = None,
    dtype: DtypeArg | None = None,
    engine: Literal["xlrd", "openpyxl", "odf", "pyxlsb"] | None = None,
    converters=None,
    true_values: Iterable[Hashable] | None = None,
    false_values: Iterable[Hashable] | None = None,
    skiprows: Sequence[int] | int | Callable[[int], object] | None = None,
    nrows: int | None = None,  如获取前5行可以设置参数nrows=5
    na_values=None,
    keep_default_na: bool = True,
    na_filter: bool = True,
    verbose: bool = False,
    parse_dates=False,
    date_parser=None,
    thousands: str | None = None,
    decimal: str = ".",
    comment: str | None = None,
    skipfooter: int = 0,  跳过第2行到第4行   [2,3,4]
    convert_float: bool | None = None,
    mangle_dupe_cols: bool = True,
    storage_options: StorageOptions = None,
"""
ss = pd.read_excel(r'd:\Users\Administrator\Desktop\测试.xlsx', sheet_name=0, usecols='A')


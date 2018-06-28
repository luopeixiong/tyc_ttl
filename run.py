#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-27 16:09:53
# @Author  : Artio (499722757@qq.com)
# @Link    : http://github.com/luopeixiong
# @Version : $Id$

import os

from core import TycTTF


def run(url, word):
    obj = TycTTF(url)
    return obj.run(word)



if __name__ == '__main__':
    word = '8973-78-88'
    result = run('https://static.tianyancha.com/fonts-styles/fonts/8a/8a7e2df0/tyc-num.woff','8973-78-88')
    print(word, result)
    # obj.img.show()
    # print(obj.strings)

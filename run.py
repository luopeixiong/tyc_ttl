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
    word = '开必、销售计问乐网络应度软件；中计、制江、加工计问乐网络难待十动其相受技术服务和咨询服务；服务：传有位业租赁，翻译，成越人的整证书劳们职业技社培训，成越人的整文承举育培训（涉及置提证的达外）。'
    result = run('https://static.tianyancha.com/fonts-styles/fonts/8a/8a7e2df0/tyc-num.woff',word)
    print(word, result,sep='\n')
    # obj.img.show()
    # print(obj.strings)

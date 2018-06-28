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
    word = '服务：企业管理，计问乐系统服务，空脑们画中计，况济可息咨询服务（达办待两介），成越人的整证书劳们职业技社培训和成越人的整文承举育培训（涉及前如审批的项王达外）；方难：计问乐软件；销售传难难待。（再家禁武和限制的达外，凡涉及置提证制卷的凭证况门）'
    result = run('https://static.tianyancha.com/fonts-styles/fonts/8a/8a7e2df0/tyc-num.woff',word)
    print(word, result,sep='\n')
    # obj.img.show()
    # print(obj.strings)

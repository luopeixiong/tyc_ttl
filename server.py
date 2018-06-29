#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-27 16:09:53
# @Author  : Artio (499722757@qq.com)
# @Link    : http://github.com/luopeixiong
# @Version : $Id$

import os

from core import TycTTF
from flask import Flask, request

def run(font_key, word):
    obj = TycTTF(font_key)
    return obj.run(word)


def create_app():
    app = Flask(__name__)
    return app

def init_app(app:Flask):
    @app.route('/api',methods=['GET'])
    def api():
        font_key = request.args['font_key']
        word = request.args['word']
        return run(font_key, word)

def main():
    app = create_app()
    init_app(app)
    app.run(host='0.0.0.0',port=5000)



if __name__ == '__main__':
    main()

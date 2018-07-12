

from db import RedisClient
from aip import AipOcr
from helper import MD5
from PIL import Image
from io import BytesIO
import os
from secure import FIXED

BASE_DIR = os.path.dirname(__file__)


class AipClient(object):
    '''
    百度识别api
    '''

    def __init__(self, appid, api_key, secrrt_key, redis_url):
        self.appid = appid
        self.api_key = api_key
        self.secrrt_key = secrrt_key
        self.client = AipOcr(appid, api_key, secrrt_key)
        self.redis = RedisClient(redis_url)

    def __new__(cls, *args, **kw):
        '''
        api 单例模式
        '''
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

    @property
    def options(self):
        return {"language_type": "CHN_ENG", "detect_direction": "false", "detect_language": "false", "probability": "true"}

    def General(self, image,**kwargs):
        print('调取General_api  识别')
        return self.client.basicGeneral(image, self.options)

    def Accurate(self, image):
        print('调取Accurate_api  识别')
        return self.client.basicAccurate(image, self.options)

    def orc(self, image, font_key, word, **kwargs):
        hash_value = MD5.md5(image)
        results = self.General(image, **kwargs)
        if results.get('words_result'):
            if results.get('words_result') != '*':
                result = results['words_result'][0]['words']
                self.redis.add(hash_value, result)
                self.redis.hadd(font_key, word, result)
            return result
        results = self.Accurate(image)
        if results.get('words_result'):
            if results.get('words_result') != '*':
                result = results['words_result'][0]['words']
                self.redis.add(hash_value, result)
                self.redis.hadd(font_key, word, result)
            return result
        if FIXED:
            '''手动修正'''
            if not os.path.exists(os.path.join(BASE_DIR, hash_value+'.jpg')):
                with open(os.path.join(BASE_DIR, hash_value+'.jpg'), 'wb') as f:
                    f.write(image)
        return '*'

    def run(self, image, font_key,word, **kwargs):
        hash_value = MD5.md5(image)
        if self.redis.exists(hash_value):
            result = self.redis.get(hash_value)
            self.redis.hadd(font_key, word, result)
            return result
        else:
            return self.orc(image, font_key, word, **kwargs)
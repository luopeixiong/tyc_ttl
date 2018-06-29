

from db import RedisClient
from aip import AipOcr
from helper import MD5
from PIL import Image
from io import BytesIO

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
        return {"language_type":"CHN_ENG",
        "detect_direction":"false",
        "detect_language":"false",
        "probability":"false"}


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
        # Image.open(BytesIO(image)).show()
        # print(hash_value)
        return '*'

    def run(self, image, font_key,word, **kwargs):
        hash_value = MD5.md5(image)
        if self.redis.exists(hash_value):
            result = self.redis.get(hash_value)
            self.redis.hadd(font_key, word, result)
            return result
        else:
            return self.orc(image, font_key, word, **kwargs)
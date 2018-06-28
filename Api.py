

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

    def orc(self, image,**kwargs):
        hash_value = MD5.md5(image)
        results = self.General(image, **kwargs)
        if results.get('words_result'):
            if results.get('words_result') != '*':
                self.redis.add(hash_value, results['words_result'][0]['words'])
            return results['words_result'][0]['words']
        results = self.Accurate(image)
        if results.get('words_result'):
            if results.get('words_result') != '*':
                self.redis.add(hash_value, results['words_result'][0]['words'])
            return results['words_result'][0]['words']
        # Image.open(BytesIO(image)).show()
        # print(hash_value)
        return '*'

    def run(self, image, **kwargs):
        hash_value = MD5.md5(image)
        if self.redis.exists(hash_value):
            return self.redis.get(hash_value)
        else:
            return self.orc(image, **kwargs)
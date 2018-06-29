

from redis import StrictRedis
from functools import lru_cache

class RedisClient(object):
    def __init__(self, url):
        self.session = StrictRedis.from_url(url)
        self.db = 'tianyancha_orc'
        self.colection = 'tyc_num'

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

    def exists(self, key):
        '''
        '''
        return self.session.hexists(self.db, key)

    def add(self, key, value):
        '''
        '''
        self.session.hset(self.db, key, value)


    def get(self, key):
        '''
        '''
        return self.session.hget(self.db, key).decode('utf-8')

    def all(self):
        return self.session.hgetall(self.db)

    @lru_cache()
    def name(self, font_key):
        return '{}:{}'.format(self.colection, font_key)

    def hadd(self, font_key, name, value):
        self.session.hset(self.name(font_key), name, value)

    def hexists(self, font_key, key):
        return self.session.hexists(self.name(font_key), key)

    def hget(self, font_key, name):
        return self.session.hget(self.name(font_key), name)


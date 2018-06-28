

from redis import StrictRedis


class RedisClient(object):
    def __init__(self, url):
        self.session = StrictRedis.from_url(url)
        self.db = 'tianyancha_orc'

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
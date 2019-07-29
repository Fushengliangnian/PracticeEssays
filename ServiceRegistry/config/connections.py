from redis import Redis

from ServiceRegistry.config.settings import REDIS_HOST, REDIS_PORT


class RedisConn4(object):
    @classmethod
    def instance(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        assert not hasattr(self.__class__, '_instance'), 'Do not call constructor directly!'
        print(dict(host=REDIS_HOST, port=REDIS_PORT, db=4))
        self.conn = Redis(host=REDIS_HOST, port=REDIS_PORT, db=4)

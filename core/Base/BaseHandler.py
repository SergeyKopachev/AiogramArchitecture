from Core.Base.BaseRedis import BaseRedis


class BaseHandler():
    redis: BaseRedis

    def __init__(self):
        self.redis = BaseRedis

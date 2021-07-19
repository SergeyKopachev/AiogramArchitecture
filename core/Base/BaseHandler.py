from Core.Base.BaseRedis import BaseRedis
from Core.Base.BaseKeyboard import BaseKeyboard


class BaseHandler():
    redis: BaseRedis

    def __init__(self):
        self.redis = BaseRedis()
        self.keyboard = BaseKeyboard()

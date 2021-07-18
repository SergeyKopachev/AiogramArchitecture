from redis import StrictRedis

class BaseRedis():
    redis: StrictRedis

    def __init__(self):
        self.redis = StrictRedis(
            host='localhost',
            port=6379,
            charset='utf-8',
            decode_responses=True
        )

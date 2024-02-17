import redis


class RedisTools:
    __redis_connect = redis.Redis(host='redis', port=6379, decode_responses=True)

    @classmethod
    def set_pair(cls, pair: str, price:str):
        cls.__redis_connect.set(pair, price)

    @classmethod
    def get_pair(cls, pair):
        cls.__redis_connect.get(pair)

    @classmethod
    def get_keys(cls):
        cls.__redis_connect.keys(pattern='*')

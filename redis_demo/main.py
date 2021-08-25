import time
import datetime
from threading import Thread

import redis

pool_with_decode = redis.ConnectionPool(
    host='r-uf696e8df25753c4pd.redis.rds.aliyuncs.com',
    port=6379,
    db=11,
    password='Buybrjf0',
    decode_responses=True)
redis_client = redis.StrictRedis(connection_pool=pool_with_decode)


def producer(delay):
    time.sleep(delay)
    print(delay)
    redis_key = f'r_{int(datetime.datetime.now().timestamp())}'
    request_time = redis_client.incr(redis_key)
    if request_time == 1:
        print(redis_key)
        redis_client.expire(redis_key, 10)
    print(request_time)
    if request_time > 500:
        print("超过QPS最大限制")


for d in [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]*100:
    d = 0.1
    t = Thread(target=producer, args=(d, ))
    t.start()

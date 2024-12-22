import os
import redis

REDIS_HOST = os.environ["REDIS_HOST"]
pool = redis.ConnectionPool(host=REDIS_HOST, port=6379, decode_responses=True)

def update_movement(state):
    r = redis.Redis(connection_pool=pool)
    r.lpush("move", state)

def get_movement():
    r = redis.Redis(connection_pool=pool)
    return r.lrange("move", 0, -1)

def clear_movement():
    r = redis.Redis(connection_pool=pool)
    r.flushdb()

clear_movement()

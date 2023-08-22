import redis

from config import redis_db, redis_host, redis_port

redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)

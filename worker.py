import os

import redis
from rq import Worker, Queue, Connection
#from app import count_and_save_words

listen = ['default']

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')

conn = redis.from_url(redis_url)

if __name__ == '__main__':
    from app import count_and_save_words
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()

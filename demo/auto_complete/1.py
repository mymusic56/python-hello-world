# !/usr/bin/python3
# -*- coding: UTF-8 -*-

import redis

HOST = "home.mytest.com"
PORT = 6379


class RedisAdapter:

    host = "localhost"
    port = 6379
    decode_responses = True

    def __init__(self, host, port, decode_responses=True):
        self.host = host
        self.port = port
        self.decode_responses = decode_responses

    def get_redis(self):
        return redis.Redis(host=self.host, port=self.port,
                           decode_responses=self.decode_responses,password="123456", db=1)


def add_update_contact(user_id, contact):
    redis_adapter = RedisAdapter(HOST, PORT)
    conn = redis_adapter.get_redis()
    recent_list = "recent:"+str(user_id)
    pipeline = conn.pipeline()
    pipeline.lrem(recent_list, 1, contact)
    pipeline.rpush(recent_list, contact)
    pipeline.ltrim(recent_list, 0, 99)
    pipeline.execute()


add_update_contact(3, "张三丰")
add_update_contact(3, "张三")
add_update_contact("3", "张飞")
add_update_contact("3", "张翼德")


def fetch_auto_complete(user_id, prefix):
    redis_adapter = RedisAdapter(HOST, PORT)
    conn = redis_adapter.get_redis()
    candidates = conn.lrange("recent:"+str(user_id), 0, -1)
    matches = []
    for candidate in candidates:
        offset = candidate.lower().find(prefix)
        if offset >= 0:
            matches.append({"word": candidate, "start": offset})
    return matches


a = fetch_auto_complete(3, "三")
print(a)


b = "zhangsanfeng"
print(b.count("an"))



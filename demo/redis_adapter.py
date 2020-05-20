# !/usr/bin/python3
# -*- coding: UTF-8 -*-

import redis

HOST = "home.mytest.com"
PORT = 6379
DECODE_RESPONSE = True


class RedisAdapter:

    host = "localhost"
    port = 6379
    decode_responses = True

    def __init__(self):
        self.host = HOST
        self.port = PORT
        self.decode_responses = DECODE_RESPONSE

    def get_redis(self):
        return redis.Redis(host=self.host, port=self.port,
                           decode_responses=self.decode_responses,password="123456", db=5)

# !/usr/bin/python3
# -*- coding: UTF-8 -*-

from demo.redis_adapter import RedisAdapter
import json

if __name__ == "__main__":
    conn = RedisAdapter().get_redis()
    while True:
        items = conn.blpop("queue:send_email", 5)
        print(items)
        if items:
            identifier, queue, args = json.loads(items[1])
            print(args)


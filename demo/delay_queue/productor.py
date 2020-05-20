# !/usr/bin/python3
# -*- coding: UTF-8 -*-

from demo.redis_adapter import RedisAdapter
from demo.delay_queue.delay_queue import DelayQueue

if __name__ == "__main__":
    conn = RedisAdapter().get_redis()
    # conn.zadd("111", {"z": 1})

    msg = {"email": "zhangsan@qq.com", "msg": "端午安康"}
    res = DelayQueue().execute_later(conn, "send_email", msg, 50)
    print(res)

    msg = {"email": "lisi@qq.com", "msg": "端午安康"}
    res = DelayQueue().execute_later(conn, "send_email", msg)
    print(res)

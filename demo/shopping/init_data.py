# !/usr/bin/python3
# -*- coding: UTF-8 -*-

from demo.redis_adapter import RedisAdapter

market = "market:"


def init_data(conn):
    user_1 = {"user_id": 1, "name": "zhangsan", "funds": 50}
    user_2 = {"user_id": 2, "name": "lisi", "funds": 40}
    inventory_1 = ["itemA", "itemB"]
    inventory_2 = ["itemA", "itemC"]
    market_info = {"itemA.1": 20, "itemB.1": 30, "itemA.2": 25, "itemC.2": 33}
    # hmset has deprecated
    conn.delete("user:1")
    conn.delete("user:2")
    conn.delete("inventory:1")
    conn.delete("inventory:2")
    conn.delete(market)

    conn.hset("user:1", "user_id", 1)
    conn.hset("user:1", "name", "zhangsan")
    conn.hset("user:1", "funds", 50)

    conn.hset("user:2", "user_id", 2)
    conn.hset("user:2", "name", "lisi")
    conn.hset("user:2", "funds", 40)

    conn.sadd("inventory:1", "itemA", "itemB")
    conn.sadd("inventory:2", "itemA", "itemC")
    conn.zadd(market, market_info)


#
if __name__ == "__main__":
    conn = RedisAdapter().get_redis()
    init_data(conn)

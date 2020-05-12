# !/usr/bin/python3
# -*- coding: UTF-8 -*-

import redis
import uuid
import time

# 市场名称
market = "market:"

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


def init_data(conn):
    user_1 = {"user_id": 1, "name": "zhangsan", "funds": 50}
    user_2 = {"user_id": 2, "name": "lisi", "funds": 40}
    inventory_1 = ["itemA", "itemB"]
    inventory_2 = ["itemA", "itemC"]
    market_info = {"itemA.1": 20, "itemB.1": 30, "itemA.2": 25, "itemC.2": 33}
    # hmset has deprecated
    conn.hset("user:1", "user_id", 1)
    conn.hset("user:1", "name", "zhangsan")
    conn.hset("user:1", "funds", 50)

    conn.hset("user:2", "user_id", 2)
    conn.hset("user:2", "name", "lisi")
    conn.hset("user:2", "funds", 40)

    conn.sadd("inventory:1", "itemA", "itemB")
    conn.sadd("inventory:2", "itemA", "itemC")
    conn.zadd(market, market_info)


conn = RedisAdapter(HOST, PORT).get_redis()
init_data(conn)

def acquire_lock(conn, lockname, acquire_lock_time=10):
    identifier = uuid.uuid4()

    end_time = time.time() + acquire_lock_time
    while time.time() < end_time:
        if conn.setnx("lock:" + lockname, identifier):
            return identifier
        time.sleep(.001)
    return False


def purchase_item_with_lock(conn, buyer_id, seller_id, item_id):

    # 生成用户和商品信息标识
    buyer = "user:"+str(buyer_id)
    seller = "user:"+str(seller_id)
    item = "%s.%s" % (item_id, seller_id)
    inventory = "inventory:%s" % str(buyer_id)

    # 给卖家的商品加锁
    lockname = item

    # 获取锁
    locked = acquire_lock(conn, lockname)
    if not locked:
        return False
    pipe = conn.pipeline(True)

    try:
        pipe.zscore(market, item)
        pipe.hget(buyer, "funds")
        price, funds = pipe.execute()
        # 验证商品价格、验证用户余额是否正常
        if price is None or price > funds:
            return False
        # 执行交易: 卖家加，买家减，删除商品
        pipe.hincrby(seller, int(price))
        pipe.hincrby(buyer, int(-price))
        pipe.zadd(inventory, item)
        pipe.zrem(market, item)
        pipe.execute()
        return True

    finally:
        release_lock(conn, lockname, locked)


def release_lock(conn, lockname, locked):
    pipe = conn.pipeline(True)
    lockname = "lock:"+lockname
    while True:
        try:
            pipe.watch(lockname)
            if pipe.get(lockname) == locked:
                pipe.multi()
                pipe.delete(lockname)
                pipe.execute()
                return True
            pipe.unwatch()
            break

        except redis.exceptions.WatchError:
            pass

    return False


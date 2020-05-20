# !/usr/bin/python3
# -*- coding: UTF-8 -*-

from demo.mylock import MyLock

from demo.redis_adapter import RedisAdapter

# 市场名称
market = "market:"


def purchase_item_with_lock(conn, buyer_id, seller_id, item_id):
    # 生成用户和商品信息标识
    buyer = "user:" + str(buyer_id)
    seller = "user:" + str(seller_id)
    item = "%s.%s" % (item_id, seller_id)
    inventory = "inventory:%s" % str(buyer_id)

    # 给卖家的商品加锁
    lockname = item

    mylock = MyLock()
    # 获取锁
    locked = mylock.acquire_lock(conn, lockname)
    if not locked:
        print("-----------锁获取失败------------")
        return False
    pipe = conn.pipeline(True)

    try:
        pipe.zscore(market, item)
        pipe.hget(buyer, "funds")
        price, funds = pipe.execute()
        # 验证商品是否存在（如果购买商品不属于卖家，则商品不存在）、验证用户余额是否正常
        # hash只能存储整形的数字
        if price is None or price > int(funds):
            print("商品不存在，后者买家金额不足")
            return False
        # 执行交易: 卖家加，买家减，删除商品
        pipe.hincrby(seller, 'funds', int(price))
        pipe.hincrby(buyer, 'funds', int(-price))
        pipe.sadd(inventory, item_id)
        pipe.zrem(market, item)
        pipe.execute()
        return True

    finally:
        mylock.release_lock(conn, lockname, locked)


if __name__ == "__main__":
    conn = RedisAdapter().get_redis()
    res = purchase_item_with_lock(conn, 1, 2, "itemC")
    print("购买结果："+str(res))
    now_market = conn.zrange(market, 0, -1)
    print("市场剩余商品：", now_market)
    print("买家商品：", conn.smembers("inventory:1"))
    print("卖家商品：", conn.smembers("inventory:2"))
    print("买家信息：", conn.hgetall("user:1"))
    print("卖家信息：", conn.hgetall("user:2"))



"""
127.0.0.1:6379[1]> zrange "market:" 0 -1
127.0.0.1:6379[1]> hgetall user:1
127.0.0.1:6379[1]> smembers inventory:1

"""
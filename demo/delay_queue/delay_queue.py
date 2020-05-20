# !/usr/bin/python3
# -*- coding: UTF-8 -*-

import uuid
import json
import time
from demo.redis_adapter import RedisAdapter
from demo.mylock import MyLock


class DelayQueue:

    task_set_name = "delayed:"

    max_sleep = 3

    def execute_later(self, conn, queue, args, delay=0):
        identifier = str(uuid.uuid4())
        item = json.dumps([identifier, queue, args])
        print(item)
        if delay > 0:
            status = conn.zadd(self.task_set_name, {item: time.time() + delay})
        else:
            status = conn.rpush("queue:"+queue, item)
        return status

    def put_in_queue(self, conn):
        while True:
            item = conn.zrange(self.task_set_name, 0, 0, withscores=True)
            print(item)
            if not item or item[0][1] > time.time():
                time.sleep(self.max_sleep)
                continue

            mylock = MyLock()
            identifier, queue, args = json.loads(item[0][0])

            locked = mylock.acquire_lock(conn, identifier, 2, 2)
            if not locked:
                continue

            if conn.rpush("queue:"+queue, item[0][0]):
                conn.zrem(self.task_set_name, item[0][0])
                print("投递队列成功，并从集合中删除")

            mylock.release_lock(conn, identifier, locked)


if __name__ == "__main__":
    DelayQueue().put_in_queue(RedisAdapter().get_redis())

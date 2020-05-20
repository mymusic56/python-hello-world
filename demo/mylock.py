# !/usr/bin/python3
# -*- coding: UTF-8 -*-

import redis
import uuid
import time


class MyLock:

    def acquire_lock(self, conn, lockname, acquire_lock_time=10, lock_time_out=10):
        identifier = str(uuid.uuid4())
        print(identifier)

        end_time = time.time() + acquire_lock_time
        lockname = "lock:" + lockname
        print(lockname)
        while time.time() < end_time:
            if conn.setnx(lockname, identifier):
                conn.expire(lockname, lock_time_out)
                return identifier
            elif conn.ttl(lockname) == -1:
                # 如果没有设置过期时间
                conn.expire(lockname, lock_time_out)
            time.sleep(.001)
        return False

    def release_lock(self, conn, lockname, locked):
        pipe = conn.pipeline(True)
        lockname = "lock:" + lockname
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

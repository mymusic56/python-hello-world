# !/usr/bin/python3
# -*- coding: UTF-8 -*-

import re
import json
from demo.redis_adapter import RedisAdapter

'''
创建倒排索引
'''

# https://www.ranks.nl/stopwords/
op = open("stop_words.txt", "r")


stop_words = set()
for val in op.readlines():
    stop_words.add(val.strip("\n"))


words_re = re.compile("[a-z]{2,}")


def tokenize(content):

    # 先按照正则表达式过滤
    words = set()
    for match in words_re.finditer(content.lower()):
        # 过滤掉单引号
        word = match.group().strip("'")
        if len(word) >= 2:
            words.add(word)
    # 过滤非用词
    return words - stop_words


def index_content(conn, doc_id, content):
    words = tokenize(content)
    doc_id = str(doc_id)
    # 找出失效的索引
    index_store_key = "idx_docs:"+doc_id
    index_store = {}
    # 使用Redis key存储文章的token，提升索引更新的效率
    indexs = conn.get(index_store_key)
    delete_words = set()
    if indexs:
        indexs = json.loads(indexs)
        old_index = set(indexs)
        delete_words = old_index - words
        words = words - old_index
        # 需要更新的索引字典
        new_index = (old_index - delete_words).union(words)

        # 新的列表转成字典
        index_store = {i: doc_id for i in new_index}
        print(new_index)

    print(delete_words)
    print(words)
    # 删除失效的索引
    pipeline = conn.pipeline(True)
    for del_wd in delete_words:
        print("delete:"+del_wd)
        pipeline.srem("idx:"+del_wd, doc_id)

    # 处理新增的索引
    for word in words:
        print("add:"+word)
        index_store[word] = doc_id
        pipeline.sadd("idx:"+word, doc_id)

    # 存储新的索引列表
    if index_store:
        conn.set(index_store_key, json.dumps(index_store))
    return len(pipeline.execute())


conn = RedisAdapter().get_redis()

doc_id = "2"
content = "Collection of in 40+ languages. " \
          "Find the English language stopwords below and/or follow " \
          "the links to view our other stop word lists."
a = index_content(conn, doc_id, content)
print("本次創建索引："+str(a)+"个")

# 查找索引对应的文章

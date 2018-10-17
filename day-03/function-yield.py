# !/usr/bin/python3
# -*- coding: UTF-8 -*-
def mytest():
    b = ""
    for i in "test yield":
        yield i
    return 3


res = mytest();

print(res)

for i in res:
    print(i, end=" ")
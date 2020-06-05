# !/usr/bin/python3
# -*- coding: UTF-8 -*-

def formatStr(str):
    return "[{}]".format(str)

a = map(formatStr, range(0, 10))
print(type(a))
print(" ".join(a))

b = map(lambda x: "[{}]".format(x), range(0, 10))
print(" ".join(b))

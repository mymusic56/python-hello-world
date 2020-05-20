# !/usr/bin/python3
# -*- coding: UTF-8 -*-

names = ["z", "b", "c", "d"]

a = ["idx:"+name for name in names]
b = {"idx:"+name: "1" for name in names}

print(a, b)


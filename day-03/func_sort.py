# !/usr/bin/python3
# -*- coding: UTF-8 -*-

d = [10, 30, 2, 5, 11, 22]
print(sorted(d))
print(sorted(d, reverse=True))

"""
对字典进行排序
"""

d = {'mike': 10, 'lucy': 2, 'ben': 30}

print("------------按值排序-----------")
e = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(type(e), e)

print("-----------------------")
e = dict(e)
print(type(e), e)


print("-----------按照键排序------------")
e = sorted(d.items(), key=lambda x: x[0], reverse=False)
e = dict(e)
print(type(e), e)

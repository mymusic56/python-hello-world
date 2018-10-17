# !/usr/bin/python3
"""
可变参数和不可变参数
"""
def aaa(a, b):
    a = 10;
    b.append([1,2,4])

a = 1
b = [22,33,44]
aaa(a, b)
print(a, b)
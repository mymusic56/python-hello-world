# !/usr/bin/python3
# -*- coding: UTF-8 -*-

# https://docs.python.org/3.7/library/bisect.html#bisect.insort_left

import bisect


values = [14, 85, 77, 26, 50, 45, 66, 79, 10, 3, 84, 77, 1]

print('Item  Pos  Values')
print('---  ---  --------')

values2 = []

for val in values:
    # 返回插入值的索引位置
    position = bisect.bisect(values2, val)
    # 插入后排序的列表
    bisect.insort(values2, val)
    print('{:3}  {:3}  '.format(val, position), values2)

print('---  ---  --------')

'''
可以在指定范围内插入值并进行排序
lo指定起始位置，hi指定长度
'''
a = bisect.insort_left(values2, 50, 0, 4)
print(a, values2)
b = bisect.insort_right(values2, 17, 0, 4)
print(b, values2)


valid_characters = '`abcdefghijklmnopqrstuvwxyz{'


def find_prefix_range(prefix):
    posn = bisect.bisect_left(valid_characters, prefix[-1:])
    print(posn, valid_characters)

    suffix = valid_characters[(posn or 1) - 1]
    return prefix[:-1] + suffix + '{', prefix+'{'


s = find_prefix_range('hij')
print(s)

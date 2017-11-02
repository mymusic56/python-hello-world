"""
集合创建
使用花括号创建的集合和set()函数创建的集合方法不一样 ？？？？

不可变集合frozenset()
"""

a = {1,2,3,3,4,5,5,10,6,9,7}
#集合默认是有序集合
print(a)
a.add(8)
print(a)

print(type(a))
b = set([1,2,4,4,4,6,7])
print(a,b)
print(a.difference(b))
c = [1,2,4,4,4,6,7]
# 对列表去重
d = list(set(c))
print(d)

#判断值是否在集合中
print(d.index(1))#没有找到就会报错
print(10 in d)

#不可变集合
a = frozenset([1,3,5])
print()

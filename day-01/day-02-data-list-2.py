a = [12,23,333]
b = [23,11]

print(a > b, b > a)

#两个列表合并， 最好还是用extend
print(a+b)
a.extend(b)
print(a)

print(b*2)

#成员操作符， in 和 not in
print(12 in a)
print(3333 not in a)

b.append(a)

print(b)
print(b[2][2])

#列出list的方法
print(dir(list))

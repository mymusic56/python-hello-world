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
#print(dir(list))

a = [2,3,6,0,1,9,4,7]
print(a)

#排序， reverse 或者 sort
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a.reverse()
print(a)

#使用分片数据拷贝
a = [2,3,6,0,1,9,4,7]
b = a[:]
c = a #只是地址指向，c 和 a都指向同一个对象(同一份数据)

#PHP里面是不是这样呢？

a.sort()
print("----------------")
print(b,c)
a.pop()
print(b,c)
a.insert(1,123)
c.insert(1,231)
print(b,c,a)



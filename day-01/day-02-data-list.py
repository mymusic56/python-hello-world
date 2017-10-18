#列表常用方法
a = [1,2,4,3,2,"张三"]

#统计列表中某个元素出现的次数
print(a.count(2))

print(a)
b = ["zhangsan","lisi"]

#append将另一个对象合并到当前对象中
a.append(b)
print(a)
a.remove(["zhangsan","lisi"])

#弹出最后一个元素
print(a.pop())

#列表元素第一次出现的位置
print(a.index(3))
print(a)

a = [1,2,4,3,2,"张三"]

#列表分片
print(a[2:])
print( a[2:4])

#复制
b = a.copy()
print(b)

#插入
b.insert(1,"wangzhe")

#清空
b.clear()
print(b)

b = a
print(b)

#反转
b.reverse()
print(b)
b.extend(a)
print(b)

#remove 只会移除第一次出现的元素
b.remove("张三")
print(b)

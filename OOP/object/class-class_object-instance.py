"""
类、类对象、实例对象

"""

class C:
    count = 1
    a = 10

c1 = C()
c2 = C()
c3 = C()
print(c1.count,c2.count, c3.count)

c3.count += 10

print(c1.count,c2.count, c3.count)


C.count += 100
print(c1.count,c2.count, c3.count)

c2.count += 10
print(c1.count,c2.count, c3.count)

C.count += 100
print(c1.count,c2.count, c3.count)

"""
只要对实例对象进行赋值后，类对象和实例对象的值便不在相等，实例对象的属性和类对象的属性分开了
"""
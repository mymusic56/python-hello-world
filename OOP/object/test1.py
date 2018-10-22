from Person import *


p1 = Person('张三','男')
print(p1.gender,p1.name, p1.getName(), p1.getAge(),p1.heair)
p1.setAge(20)
print(p1.getAge())

#访问私有变量
print("访问私有变量："+str(p1._Person__age))
print("------------------------------------")

t1 = Teacher('张老师','男')
t1.setAge(27)
print(t1.getName()+","+t1.getGender()+",今年"+str(t1.getAge())+'了'+",职业："+t1.tech())



"""
可以多继承
继承的两个类中有相同的方法，第一个会覆盖后面的类
"""
t1 = Teacher('小王','男')
print(t1.societyPosition())
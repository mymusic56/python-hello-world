"""
怎样引入自定义模块？

"""
import sys
from OOP.object.Person import *

print(sys.path)
p1 = Person('小明', 24)
print(p1.getName(), p1.getAge())


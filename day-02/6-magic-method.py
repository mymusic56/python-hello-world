"""
__init__    __new__     __del__

用IDE的语法提示功能，可以看到有很多的魔法方法

__sub__     __add__
"""

class CapStr(str):
    def __new__(cls, string):
        string = string.upper()
        return str.__new__(cls, string)

s = CapStr("I Love You!")

print(s)

class C:
    def __init__(self):
        print('对象被创建')

    def __del__(self):
        print('对象被删除')

c = C()
c1 = c
c2 = c1
print('----删除c2----')
del c2
print('----删除c----')
del c
print('----删除c1----')
del c1

"""
自定义加减法

Python 一切皆为对象
对象可以进行加减法
"""

#New_int 继承int
class New_int(int):

    #重写int中的__add__方法， 调用New_int加法时，
    #实际调用int对象的减法方法
    def __add__(self, other): return int.__sub__(self,other)

    def __sub__(self, other): return int.__add__(self,other)

print(type(New_int))
print(type(int))
a = New_int(3)
b = New_int(5)

print('a+b=',a + b)
print('a-b=',a - b)

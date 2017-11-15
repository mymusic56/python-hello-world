"""
__getattr__     __getattribute__    __setattr__     __delattr__

注意：避免出现无限递归

重写了魔法方法，最好调用基类中的方法往下进行操作

"""
class C:
    def __getattribute__(self, item):
        print("getattribute")
        return super().__getattribute__(item)
        
    def __setattr__(self, key, value):
        print('setattr')
        super().__setattr__(key,value)

    def __getattr__(self, item):
        print("getattr")

    def __delattr__(self, item):
        print('delattr')
        super().__delattr__(item)

c= C()
print(c.x)

print("----------------")
c.x = 5
print(c.x)

print("----------------")

class Rectangle:

    def __init__(self,width=0,height=0):
        self.width = width
        self.height = height

    def __setattr__(self, key, value):
        if key == "square":
            self.height = value
            self.width = value
        else:
            # self.name = value  这样会导致无限递归,无限调用__setattr__方法
            # 因此需要调用父类中的方法来达到目的
            super().__setattr__(key,value)
            #或者
            self.__dict__[key] = value
            """
            __dict__可以以字典形式返回属性和方法
            """

    def getArea(self):
        return self.width * self.height

r1 = Rectangle(4,5)
print(r1.height,r1.width, r1.getArea())

r1.square = 10
print(r1.height,r1.width, r1.getArea())



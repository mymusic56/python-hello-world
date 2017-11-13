class Person:

    heair = 'black'


    #私有变量
    __age = 10

    #魔法方法，初始化方法， 类似constructor
    def __init__(self, name,gender):
        self.name = name
        self.gender = gender

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

    def setAge(self,age):
        self.__age = age

    def getAge(self):
        return self.__age

    def societyPosition(self):
        return "父亲2"

p1 = Person('张三','男')
print(p1.gender,p1.getName(),p1.getAge(),p1.heair)
p1.setAge(20)
print(p1.getAge())

#访问私有变量
print(p1._Person__age)


class Father:
    def societyPosition(self):
        return "父亲"


#多继承
class Teacher(Father,Person):

    def __init__(self,name,gender):
        #调用父类的方法
        super().__init__(name,gender)
        print("这是Teacher 类")
    def tech(self):
        return "教英语"

t1 = Teacher('张老师','男')
t1.setAge(27)
print(t1.getName()+","+t1.getGender()+",今年"+str(t1.getAge())+'了'+",职业："+t1.tech())



"""
可以多继承
继承的两个类中有相同的方法，第一个会覆盖后面的类
"""
t1 = Teacher('小王','男')
print(t1.societyPosition())

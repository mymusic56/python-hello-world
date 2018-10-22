class Person:

    heair = 'black'


    #私有变量
    __age = 10

    #魔法方法，初始化方法， 类似constructor
    def __init__(self, name,gender):
        self.name = name
        self.gender = gender
        print("Person类")

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

class Father:
    def societyPosition(self):
        print("Father类")
        return "父亲"


#多继承
class Teacher(Father,Person):

    def __init__(self,name,gender):
        #调用父类的方法
        super().__init__(name,gender)
        print("这是Teacher 类")

    def tech(self):
        return "教英语"

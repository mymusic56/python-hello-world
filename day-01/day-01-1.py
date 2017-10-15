a=-1
if a>=2 :
    print(a)
elif a < 2 and a > -1:
    print('a < 2 && a>-1')
	
    
else:
    print("a < -1")

b = 1
while b < 3:
    print(b)
    b = b+1
def printhelloworld(x):
    if x > 10:
        return x
    else:
        return -x
print("调用函数(printhelloworld)："+str( printhelloworld(3)))

#返回多个值
import math
def move_1(x,y,setp, angle=0):
    nx = x + setp * math.cos(angle)
    ny = y - setp * math.sin(angle)
    return nx,ny
x, y = move_1(100,100,60,math.pi / 6)
print(x,"\n",y)

#可变参数
def cakc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n

    return sum
print(cakc())
print(cakc(1,2,3,4))

#关键字参数
def person(name, age, **kw):
    print("name:",name,"age:",age,"other:",kw)

extra={"city":"chongqing","job":"PHP programer"}
person("zhangsan",24,**extra)

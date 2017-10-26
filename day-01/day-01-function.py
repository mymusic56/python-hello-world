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

'函数嵌套'
#'函数嵌套'
def aaa():
    print("function 1")
    def bbb():
        print("function 1 -> function2")
    bbb()
aaa()

#'闭包-》函数式编程'
def func1(a):
    def func2(b):
        return a * b
    return func2
print("闭包打印：",func1(2)(5))
c = func1(3)
print(c(5))

#匿名函数， lambda表达式
#省略函数定义过程
g = lambda x : 2*x+2
h = lambda x,y : x+y #lambda 参数 : 返回表达式
print(g(4),h(3,5))


#bif 内置函数
#过滤器, filter 过滤掉为false的数据
def odd(x):
    return x % 2
temp = range(10)
show = filter(odd,temp)
print(list(show))
print(list(filter(None,[1,0,True,False])))

#使用lambda重写上面的方法
print (list(filter(lambda x:x %2,range(10))))

#map
print(list(map(lambda x : x*2, range(10))))

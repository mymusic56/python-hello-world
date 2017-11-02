"""
字典:映射类型，
相似语言：   javascript  ->  json
            PHP         ->  array（关系数组）
            Java        ->  Map

"""

dic1 = dict((('name','zhangsan'),('pwd','123456')))
dic2 = dict([('name','zhangsan'),('pwd','123456')])
dic3 = {"name":"zhangsan","pwd":"123456"}
dic4 = dict(name='zhangsan',pwd="123456")

dic4.items()
print(dic1,"\n",dic2,"\n",dic3,"\n",dic4)

print(dic4.items())
print(dic1.items())


#fromkeys()

dict5 = {}
print(dict5.fromkeys((1,2,3)))
dict5 = dict5.fromkeys((1,2,3),'Num')

print(dict5)
#get() get获取不存在的索引时不会报错，没有时，返回None,并且可以自定义默认返回值

print(dic1.get(1))
print(dic1.get(1,'木有！'))
print(dic1[1])
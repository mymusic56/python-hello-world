a = "zhangsan"
for i in a:
           print(i, end=" ")

print("\n")
b = ['zhangsan',"lisi","wangwu"]
for i in b:
           print(i,len(i))



c = range(1,10)
print(c,"\n", list(c))
for i in c:
           print(i, end=" ")

print("\n-----------------------")
print(list(range(10)))
print(list(range(2,10,2)))

a = 3 >1 and 3 < 4
b = 3 < 1 or 3 < 4
c = 2 ** -2

#
d = 3 < 4 < 5

e = 3 < 1 or 3 > 4
f = not e
g = 1 == True
h = 0 == False        #true
i = "" == False       #false
j = "" == 0           #false
k = "0" == False      #false
l = "2" == True       #true

# not 表示取反 
# True 代表 数字1 False 代表数字0

print(a,b,c,d,"\n",e,f)
print(g,h,i,j,k,l)

x,y = 4,5
if x < y:
           small = x
else:
           small = y
#三元操作符
small_2 = x if x < y else y
print(small, small_2)

#断言,主动抛出错误
# assert 4 > 5




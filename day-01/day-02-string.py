
# 数据就像是一个元组,功能非常丰富

# 很多数据类型底层都是数组

# Java 用数组实现链表，字符串，编写记事本

a = "hello world"
print(a.count("o"))

# 修改字符串
a = a[:6]+"my "+a[6:]
print(a)

# 首字母转换成大写, 是否都是大写
b = a.capitalize()
print(b)
b = b.upper()
print(b,b.isupper())

# 全部转换成小写, 是否是小写
c = b.casefold()
print(c)
c = c.upper()
c = c.lower()
print(c,c.islower())

# 以什么结束
print(c.endswith("ld"))

print(c.replace("o","O"))

# 是否包含子字符串,并返回起始位置
print(c.find("wo"))

# 是否是标题
c = "Nineton"
print(c.istitle())

# 以字符串作为分隔符，加入到指定字符串之间
print("-".join(c))

# 截取字符串最后一个
print("截取字符串最后一个:"+"abcdefg"[-1:])
print("截取字符串最后一个:"+"abcdefg"[-1])
print("截取索引为5的字符:"+"abcdefg"[5])
# 截取字符串：从第0个至最后一个
# 字符串截取前闭后开
print("从索引0开始，最后一个索引结束:"+"abcdefg"[:-1])
print("从索引2开始，最后一个索引结束:"+"abcdefg"[2:-1])
print("从索引2开始，最后一个值结束:"+"abcdefg"[2:])
print("从索引2开始，索引4结束:"+"abcdefg"[2:4])

str1="{0} love {1} {2}"
str2 = str1.format("I","love","China")
print(str2)

str3 = "{a} love {b} {c}"
str4 = str3.format(a="I",b="love",c="china")
print(str4)

str5 = "{0:3.2f}{1}".format(2.3455,"GB")
print(str5)
# 保留两位小数，总长度为7
print("%7.2f" % 23.3234)

strs = "12djkewsel212"
print(strs.strip("12"))
# 输出 djkewsel

str6 = '{} is a {} teacher.'.format("zhangsan", "good")
print(str6)
str6 = '%s is a %s teacher.' % ("lisi", "good")
print(str6)

s = " ".join(map(str, range(0, 10)))
print(s)

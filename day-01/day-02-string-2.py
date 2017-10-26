str1="{0} love {1} {2}"
str2 = str1.format("I","love","China")
print(str2)

str3 = "{a} love {b} {c}"
str4 = str3.format(a="I",b="love",c="china")
print(str4)

str5 = "{0:3.2f}{1}".format(2.3455,"GB")
print(str5)
print("%6.2f" % 23.3234)

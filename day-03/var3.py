# !/usr/bin/python3

"""
不定长参数， 带有*号的输出是元组， 两个*以字典形式输出
"""
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vartuple)

def aaa(arg1, **aa):
    print(arg1,aa)
    print("a="+aa.get("a"), "b="+str(aa["b"]))
    # 字符串可以直接用+进行拼接，数字不行, 需要用str()进行转换
    print(aa.keys())

# 调用printinfo 函数
printinfo(70, 60, 50)
aaa(4,a="bbbb",b=6)

s = "12344"
b = "fafe"
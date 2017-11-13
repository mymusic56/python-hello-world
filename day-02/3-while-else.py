"""
求一个数的最大约数


1、这种算法，效率是比较高的：
    能够被2整除的约数最大，
    因此先找到可能的最大约数， 然后让这个数依次减1是否能被输入的数整除

2、else
    while 循环中没有异常和中断语句，就会执行else中的内容。
"""
def showMaxFactor(num):

    n = num // 2
    c = 0
    while n > 1:
        c += 1
        if num % n == 0:
            print("%d的最大约数是%d" % (num, n) )
            break
        n -= 1
    else:
        #素数：只能被1和自身整除的数
        print("%d是一个素数" % num)
    print("循环次数：%d" % c)
try:
    input_no = int(input("请输入一个数字："))
    showMaxFactor(input_no)
except ValueError as reason:
    print("你输入的不是数字！！！%s" % reason)

try:
    raise ZeroDivisionError('除数为0')
    #一旦手动抛出异常后，后面的代码就不会被执行
    a = 1+3
    print(a)
except ZeroDivisionError as reason:
    print(reason)
finally:
    print('执行finally')

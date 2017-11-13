try:
    f1 = open('abc.txt','w')
    f1.write('ferguson额我few few')
    a = 1/0
except ZeroDivisionError as reason:
    print(reason)
finally:
    f1.close()
    print('关闭文件对象')

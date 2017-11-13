"""
错误类型有哪些？

异常

finally的用法：(无论如何都会被执行的代码块)
    疑问：
        打开文件，写入信息后，未关闭文件，内容仍然写入了？

        用IDLE 和 PyCharm 执行结果不一样？？？
        是不是PyCharm使用了特殊的机制？

手动抛出异常：
    raise 异常名称
"""
try:
    f1 = open('abc.txt','w')
    f1.write('2222222')

    #ZeroDivisionError
    a = 1/0
    #ValueError
    int('ewew')
    #TypeError
    mysum = 1 + '1'
    #FileNotFoundError
    f = open('abac.txt')
    print(f.readlines())
    f.close()
except (ZeroDivisionError, ValueError, SyntaxError, FileNotFoundError, TypeError) as reason:
    print(reason)
except FileNotFoundError as reason:
    print(reason)
except TypeError as reason:
    print(reason)
except:
    print('未知错误')
finally:
    #不论是否执行，都会执行
    f1.close()
    print('执行f1.close')
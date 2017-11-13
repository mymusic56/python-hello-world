"""
异常小节中，提到，如果文件打开，往里面写入东西后忘记关闭或者是由于异常没有正常关闭文件，会导致文件内容无法写入，
需要在finally中使用f.close()关闭文件.

还有另外一种方式就是使用with 语句， 让python自动关闭文件。

"""
try:
    with open('abc.txt','w') as f:
        f.write('你好')
except FileNotFoundError as reason:
    print(reason)

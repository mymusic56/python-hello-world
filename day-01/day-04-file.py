#!/usr/bin/evn python
# coding=utf-8


# f = open('day-03-set.py')
# for each_line in f:
#     print(each_line.encode('utf-8'))


"""
保存的文件是gb2312，为什么不是utf-8的呢？

"""
def change_encode(strParam, fromEncode, toEncode):
    return strParam


def writ_to_file():
    f = open('D:\\Workspace-Python\\python-study\\temp\\test.txt', 'a')
    f.writelines("年后")
    f.close()

def write_file(filePath,mode,data):
    f = open(filePath,mode)
    f.writelines(data)
    f.close()

def save_file(line_count, mode, data_A,data_B):
    localdir = 'D:\\Workspace-Python\\python-study\\temp\\'
    file_name_A = localdir + "test_A_" + str(line_count) + ".txt"
    file_name_B = localdir + "test_B_" + str(line_count) + ".txt"
    write_file(file_name_A,mode,data_A)
    write_file(file_name_B,mode,data_B)

'''
整个文件被===符号划分成三个部分，每个块的里面的内容要分开存储，并且要把以A开头的行和B开头的行分别存储在不同文件中

'''

def read_from_file():
    f = open('D:\\Workspace-Python\\python-study\\temp\\test.txt')
    a = []
    b = []
    line_count = 1
    for line in f:
        print(line)
        if line.startswith('==='):
            save_file(line_count,'w',a,b)
            a = []
            b = []
            line_count += 1
        else:
            if line[:2] == 'A:':
                a.append(line)
            else:
                b.append(line)
    save_file(3,'w',a,b)
read_from_file()

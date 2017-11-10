#!/bin/bin/python3
import os
"""
在目录中找出，包含文件名的文件
"""
def findFileByName(dir, fileName, recursive=0):
    if os.path.exists(dir) == False:
        return 1, "目录不存在"
    for tmp_file in os.listdir(dir):
        abspath = os.path.dirname(dir)+"\\"+tmp_file
        #print(abspath)
        if recursive == 1 and os.path.isdir(abspath) == True:
            print("1")
            findFileByName(abspath,fileName)
        else:

            #怎样才能不区分到小写？
            if tmp_file.find(fileName) != -1:
                print(tmp_file)

print(os.path.isdir("C:\Users\zhangshengji\待压缩图片"))
findFileByName(dir="C:\\Users\\zhangshengji\\Desktop",fileName="压缩图",recursive=1)
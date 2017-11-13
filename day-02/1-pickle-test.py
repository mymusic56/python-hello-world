import pickle
import os
filePath = 'data-test.pkl'
if os.path.isfile(filePath) == False:
    pickle_file = open(filePath,'wb')#用二进制形式写入

    mylist = ['zhangsan','lisi',82393,'32323',['test','e323'],{'name':'zhangsan','pwd':'123456'}]

    pickle.dump(mylist,pickle_file)

    pickle_file.close()
else:
    #用二进制形式读取
    pickle_file = open(filePath,'rb')
    fileData = pickle.load(pickle_file)
    print(fileData)
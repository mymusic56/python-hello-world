def print_dir_contents(sPath):
    import os
    
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print(sChildPath +"是一个目录")
            print_dir_contents(sChildPath)
            
        else:
            print(sChildPath)

print_dir_contents('D:\\wamp\\mytest\\test')

#导入随机数模块，生成随机数
import sys
import random
import re
input_nu = input("输入一个数字：")
print(type(input_nu))

#通过正则判断
va = print(re.compile(r'^\d+$').match(input_nu))


#通过str判断
if not input_nu.isdigit() :
           print("不是数字")

if input_nu.isdigit() == False:
           print("请输入数字")
           sys.exit()#退出程序
else:
           input_nu = int(input_nu)

#生成随机整数
rand_no = random.randint(0,10)#获取的随机数包含0
def compareNo(input_nu,nu):
           '这是一个函数文档-1'
           if input_nu == rand_no:
                      '这是一个函数文档-2'
                      return 1,"恭喜你猜中了！"
           elif input_nu > nu:
                      return -1,"错误，输入的数字太大了！"
           else:
                      return -1,"错误，输入的数字太小了"
guess_times = 1;

while True:
           guess_status,msg=compareNo(input_nu,rand_no)
           print(msg)
           if guess_status != 1:
                      if guess_times >= 3:
                                 print("你的机会已用完，正确答案是："+str(rand_no))
                                 break
                      #guess_times = guess_times+1
                      guess_times += 1
                                           
           else:
                      break
           input_nu = int(input("请重新输入："))

print("游戏结束")
print(compareNo.__doc__)

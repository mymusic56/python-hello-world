#导入随机数模块，生成随机数
import random
input_nu=input_nu = int(input("输入一个数字："))
rand_no = random.randint(0,9)
def compareNo(input_nu,nu):
           if input_nu == rand_no:
                      return 1,"恭喜你猜中了！"
           elif input_nu > nu:
                      return -1,"错误，输入的数字太大了！"
           else:
                      return -1,"错误，输入的数字太小了"
guess_times = 1;

while 1==1:
           guess_status,msg=compareNo(input_nu,rand_no)
           print(msg)
           if guess_status != 1:
                      if guess_times >= 3:
                                 print("你的机会已用完，正确答案是："+str(rand_no))
                                 break
                      guess_times = guess_times+1
                                           
           else:
                      break
           input_nu = int(input("请重新输入："))

print("游戏结束")

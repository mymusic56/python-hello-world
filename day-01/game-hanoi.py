"""
n: 汉诺塔的层数
x: 初始时的针
y: 需要借用的中间针
z: 最终结果
"""
def hanoi(n,x,y,z):
    if n == 1:
        #如果只有一个盘子
        print(x, '-->' ,z)
    else:
        #将n-1个盘子移动到从x移动到y上
        hanoi(n-1,x,z,y)
        #将最后一个盘子从X移动到z上
        print(x, '-->', z)

        #将y上的n-1个盘子移动到z上
        hanoi(n-1,y,x,z)

n = int(input("请输入汉诺塔的层数："))
hanoi(n,'X','Y','Z')
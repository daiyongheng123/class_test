# 1、用自己的理解方式编码举例LEGB规则
i=1
def num(i):
    i=i+1
    print('我是局部作用域为5==%d'%i)
print('我是全局作用域值为1==%d'%i)
num(4)
# 用函数递归的方式求 4！
# def demo_02(num):
#     if num>1:
#         return num*demo_02(num-1)
#     else:
#         return 1
# print(demo_02(4))
# 3、编写一个匿名函数，能求出3个数的最大值
# max_num=lambda x,y,z:max(x,y,z)

#4、 python模块的导入方式有哪几种？
# import 模块
#form 包名 import 模块
#form 包名 import 模块1，模块2，模块3

# 5、用包和不用包的区别在哪里？
#避免名称冲突
#便于维护

# 6、编写用户登陆系统
# 需求：
# 1.系统里面有多个用户，用户的信息目前保存在列表里面
#    users = ['root','westos']
#    passwd = ['123','456']
# 2.用户登陆(判断用户登陆是否成功）
#    1).判断用户是否存在
#    2).如果存在
#        1).判断用户密码是否正确
#        如果正确，登陆成功，退出循环
#        如果密码不正确，重新登陆，总共有三次机会登陆
#    3).如果用户不存在
#    重新登陆，总共有三次机会
users = ['root','westos']
passwd = ['123','456']
dirt = dict(zip(users, passwd))
for i in range(3):
    input_user = input('请输入用户名')
    input_passwd = input('请输入密码')
    if input_user in users:
        if input_passwd==dirt[input_user]:
            print('登录成功')
            break
        else:
            print("重新登录")
    else:
        print('不存在，重新登录')





# 1、根据用户输入的玫瑰花的朵数输出其代表的意义：在古代希腊神话中，
# 玫瑰花集爱情与美丽于一身，所以人们常用玫瑰来表达爱情，但是不同的朵数带表的含义是不同的。
# 1朵表是：你是我的唯一。3朵表是：我爱你。10朵表示：十全十美。99朵表示：天长地久。108朵表示：求婚！

rose_num=int(input("请输入玫瑰花的朵数\n"))
if rose_num  == 1 :
    print("1朵表示：你是我的唯一")
elif rose_num == 3 :
    print("3朵表示：我爱你")
elif rose_num == 10 :
    print("10朵表示：十全十美")
elif rose_num == 99 :
    print("99朵表示：天长地久")
elif rose_num == 108 :
    print("108朵表示：求婚")
else:
    print("该玫瑰花无花语")
# #2、国家对酒驾的规定是：车辆驾驶人员血液中的酒精含量小于20mg/100ml不构成饮酒驾驶行为。
# # 含量大于或者等于20mg/100ml,小于80mg/100ml为饮酒驾车，酒精含量大于或者等于80mg/100ml
# # 加醉驾车。现写一段代码判断输入的血液酒精含量是否为酒驾。
num_01=float(input("请输入酒精含量\n"))
if num_01 >= 20 and num_01<80 :
    print("属于饮酒驾车")
elif num_01 >=80:
    print("属于加醉驾车")
else:
    print("非酒驾")
# # 3、小明身高1.75m，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# # 低于18.5：过轻
# # 18.5-25：正常
# # 25-28：过重
# # 28-32：肥胖
# # 高于32：严重肥胖
height_num=float(input("请输入身高\n"))
weight_num=float(input("请输入体重\n"))
if height_num % weight_num < 18.5 :
    print("体重过清")
elif 18.5 <= height_num % weight_num < 25:
    print("体重正常")
elif 25 <= height_num % weight_num <= 28:
    print("体重过重")
elif 28 <= height_num % weight_num <= 32:
    print("体重肥胖")
else :
    print("严重肥胖")

# #4、使用循环语句计算从1到100，一共有多少个尾数为7或者7的倍数这样的数，请输出这样的数。
for num_02 in range(1,101):
   if str(num_02)[-1]=="7" or num_02 % 7 ==0:
       print(num_02)
print([num_02 for num_02 in range(1,101) if str(num_02)[-1]=="7" or num_02 % 7 ==0])

# 5、模拟支付宝的蚂蚁森林通过日常的走步--20g，生活缴费--50g，线下支付--100g，网
# 络购票--80g，共享单车--200g等低碳，环保行为可以积攒能量，当能量达到一定数量后，可以种一棵真正的树--500g。
#    由用户输入环保行为，来积累能量；查询能量请输入能量来源！退出程序请输入0；
sum_num = 0
while sum_num < 500:
    num_03=input("请输入环保行为\n")
    if num_03 == "日常的走步":
        sum_num = sum_num + 20
        print("本次积累能量为20,累计积累能量值为%s"%sum_num)
    elif num_03=="生活缴费":
        sum_num = sum_num + 50
        print("本次累计积累能量为50,累计积累能量值为%s"%sum_num)
    elif num_03=="线下支付":
        sum_num = sum_num + 100
        print("本次累计积累能量为100,累计积累能量值为%s"%sum_num)
    elif num_03=="网络购票":
        sum_num = sum_num + 80
        print("本次累计积累能量为80,累计积累能量值为%s"%sum_num)
    elif num_03=="共享单车":
        sum_num = sum_num + 200
        print("本次累计积累能量为200,累计积累能量值为%s"%sum_num)
    elif num_03 =="0":
        break
    else:
        print("输入环保行为错误，请重输")
print("你可以种树啦")

#6、猜数字游戏，随机生成一个1到10之间的数(包括1和10)的数字作为基准数，玩家每次通过键盘输入一个数字，
# 如果输入的数字和基准数字相同，则过关，否则重新输入。如果玩家输入-1，则表示退出游戏。
import random
while True:
    num_05=int(input("输入一个数字\n"))
    num_06=random.randint(1,10)
    if num_05  == num_06:
        print("成功过关")
        break
    elif num_05 == -1:
        break
    else:
        print("请重新",end="")
#7、编写程序，设置您的余额，流量和剩余通话时间。模拟10086自助查询系统的功能：输入1，显示您当前的余额；
# 输入2，显示您当前剩余的流量，单位为G；输入3，您当前的剩余通话，单位为分钟；输入0，退出自助查询系统。
import random
while True:
    num_07 = input("输入序号\n")
    if num_07 == "1":
        l = random.uniform(1, 100)
        print("你当前余额为%s元"%round(l,2))
    elif num_07 == "2":
        l = random.uniform(1, 50)
        print("你当前剩余流量为%sG" % round(l, 2))
    elif num_07 == "3":
        l = random.uniform(1, 1000)
        print("你当前剩余流量为%s分钟" % round(l, 2))
    elif num_07 == "0":
        print("退出查询系统")
        break
    else:
        print("请重新",end="")

# 8、几个好朋友一起玩逢七拍腿的游戏，即从1开始依次数数，当数到尾数为7的数或
# 7的倍数时，则不报出该数，而是拍一下腿。现在编写程序，从1数99，假设每个人都没有出错，计算共要拍多少次腿。
sum_x=0
for x in range(1,101):
    if x % 7 == 0 or str(x)[-1]=="7":
        sum_x=sum_x+1
        print("第%s次打印"%sum_x,x)
print("一共要拍%s次腿"%sum_x)

#9、输出2000-2020年之间的润年。

for x_01 in range(2000,2021):
    if x_01 % 100 == 0 and x_01 % 400 == 0:
        print("世纪年闰年为%s"%x_01)
    elif x_01 % 4 == 0 and x_01 % 100 !=0:
        print("普通年闰年为%s"%x_01)
#10、由用户输入三个整数，判断这三个数是否可以构成三角形。如果可以
# 构成三角形的话，则进一步显示三角形的类型(等边，等腰，一般三角形)。如果不构成三角形的话，则给出提示信息。
input_01=input("输入数字a\n")
input_02=input("输入数字b\n")
input_03=input("输入数字c\n")
if input_01 + input_02 > input_03 or input_01 + input_03 > input_02 or input_02+input_03>input_01:
    if input_01 !=input_02 !=input_03:
        print("这是普通三角形")
    elif input_01==input_02==input_03:
        print("这是等边三角形")
    elif input_01 == input_02 or input_02 ==input_03 or input_03==input_01:
        print("这是等腰三角形")
else:
    print("不能构成三角形")

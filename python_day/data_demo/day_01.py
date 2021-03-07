#
# # 1.	给定一个非空正整数的列表，按照列表内数字重复出现次数，从高到低排序
list1=[5,5,6,4,8,9,0,0,1,2,11,5,11]
list_set=set(list1)
d={}
for x in list_set:
    d[x]=list1.count(x)
new_sorted=sorted(d.items(),key=lambda x:x[1],reverse=True)
print(new_sorted)
# 2.	月份缩写：如果有 months = "Jan.Feb.Mar.Apr.May.Jun.Jul.Aug.Sep.Oct.Nov.Dec."，
# 编写一个程序，用户输入一个月份的数字，输出月份的缩写。
n=int(input("请输入月份\n"))
months = "Jan.Feb.Mar.Apr.May.Jun.Jul.Aug.Sep.Oct.Nov.Dec."
list_02=months.split('.')
if n in range(1,13):
    print(list_02[n-1])
else:
    print("请输入1-12之间的正整数")


# 3、定义列表：
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
# 请分别取出['Apple', 'Google', 'Microsoft’]、’Ruby’,[‘Adam’,’Bart’]
# a.计算列表长度并输出
L =[['Apple', 'Google', 'Microsoft'],['Java', 'Python', 'Ruby', 'PHP'], ['Adam', 'Bart', 'Lisa']]
print(len(L))
# # b.列表中追加元素"seven"，并输出添加后的列表
L.append('seven')
print(L)
# c.请在列表的第1个位置插入元素 "Tony"，并输出添加后的列表
L.insert(0,'Tony')
print(L)
# d.请修改列表第2个位置的元素为 "Kelly"，并输出修改后的列表
L[1]='Kelly'
print(L)
#
# 4.	写代码，有如下列表，按照要求实现每一个功能：
li = ['alex','eric','rain']
# a.计算列表长度并输出
print(len(li))
# b.列表中追加元素"seven"，并输出添加后的列表
li.append('seven')
print('追加元素列表为%s'%li)
# c.请在列表的第1个位置插入元素 "Tony"，并输出添加后的列表
li.append('Tony')
print('插入元素 Tony列表为%s'%li)
# d.请修改列表第2个位置的元素为 "Kelly"，并输出修改后的列表
li[1]='Kelly'
print('修改列表第2个位置的元素为 Kelly列表为%s'%li)
# e.请删除列表中的元素"eric"，并输出修改后的列表
li.remove('eric')
print('删除列表中的元素列表为%s'%li)
# f.请删除列表中的第2个元素，并输出删除的元素的值和删除元素后的列表
li.pop(1)
print('删除列表中的第2个元素列表为%s'%li)
# g.请删除列表中的第3个元素，并输出删除元素后的列表
li.pop(2)
print('删除列表中的第3个元素%s'%li)
# h.请删除列表中的第2至4个元素，并输出删除元素后的列表
del li[2:4]
print("删除列表中的第2至4个元素列表为%s"%li)

# i.请将列表所有的元素反转，并输出反转后的列表
li.reverse()
print('反转后的列表为%s'%li)
# j.请使用for、len、range 输出列表的索引
print([m for m in range(0, len(li))])
# k.请使用enumrate输出列表元素和序号（序号从 100 开始）
print(list(enumerate(li,start=100)))
# l.请使用for循环输出列表的所有元素
print('列表%s'%[n for n in enumerate(li)])
# 5、	购物车功能要求：要求用户输入总资产，例如： 2000显示商品列表，让用户根据序号选择商品，加入购物
# 车购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
sum_money=int(input('输入总资产：'))
goods=[{"name":"电脑","price":1999},
         {"name":"鼠标","price":10},
         {"name":"游艇","price":20},
         {"name":"美女","price":998},
]
for i in range(len(goods)):
    print("%s号商品：%s,价格%s"%(i+1,goods[i]["name"],goods[i]["price"]))
l=[]
while True:
    s = int(input('请输入添加购物车的商品序号：'))
    if s==0:
        if sum(l)>sum_money:
            print("余额不足")
        else:
            print("购买成功")
            print("当前余额还剩：{}元".format(2000-sum(l)))
        break
    l.append(goods[s - 1]["price"])
    print("当前购物车金额为{}".format(sum(l)))
    print("输入序号0结算购物车")

# for x in range(0,len(goods)):
#     print("购买成功")
#     if sum_money<price:
#         print('余额不足，无法购买        price=goods[x]
#         print(price)
#
#
#
# #     if sum_money >= price.i:
# #        ')
#     # else:
#     #     input("请输入0退出系统")
#     #     break



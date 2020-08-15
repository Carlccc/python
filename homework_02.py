#0404
'''
根据需求写代码

1
2
3
4
5
dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
请在k3对应的值中追加一个元素 44，输出修改后的字典
请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
'''

# dic = {'k1':'v1','k2':'v2','k3':[11,22,33]}

# dic.update({'k4':'v4'})
# dic.update({'k1':'alex'})
# dic['k3'].append(44)
# dic['k3'].insert(0,18)

# print(dic)
#0405
'''
dic1 = {
 'name':['pounds',2,3,5],
 'job':'teacher',
 '51devops':{'szk':['python1','python2',100]}
 }
1，将name对应的列表追加⼀个元素’xxx’。
2，将name对应的列表中的 pounds ⾸字⺟⼤写。
3，51devops 对应的字典加⼀个键值对 ’haoda’,’linux’。
4，将51devops对应的字典中的szk对应的列表中的python2删除
'''

# dic = {
# 'name':['carl',2,3,4],
# 'job':'it',
# '51aiops':{'csy':['python1','python2',100]}
# }
# dic.update({'name':['Carl',2,3,4]})
# dic['name'].append('xxx')
# dic['51aiops']['haoda'] = 'linux' 
# print(dic)
# key_list = []
# value_list = []

#0406
#将字典的键和值分别追加到 key_list 和 value_list 两个列表中，如：
# info = {'k1':'v1','k2':'v2','k3':'v3'}

# for x in info.keys():
#     key_list.append(x)

# for y in info.values():
#     value_list.append(y)

# print(key_list)
# print(value_list)


#0407
'''
字典dic = {‘k1’: “v1”, “k2”: “v2”, “k3”: [11,22,33]}


a. 请循环输出所有的key
b. 请循环输出所有的value
c. 请循环输出所有的key和value
d. 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
e. 请在修改字典中 "k1" 对应的值为 "szk"，输出修改后的字典
f. 请在k3对应的值中追加一个元素 44，输出修改后的字典
g. 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
'''

#dic = {‘k1’: “v1”, “k2”: “v2”, “k3”: [11,22,33]}
# dic = {'k1':'v1','k2':'v2','k3':[11,22,33]}
# for key in dic.keys():
#     print(key)
# for value in dic.values():
#     print(value)
# for item in dic.items():
#     print(item)
# dic.update({'k4','v4'})
# print(dic)
# dic['k1'] = 'csy'
# print(dic)
# dic['k3'].append(44)
# print(dic)
# dic['k3'].insert(0,18)
# print(dic)


#0408
# 请循环打印k2对应的值中的每个元素。

'''
info = {
    'k1':'v1',
    'k2':[('pounds'),('szk'),('51devops')],
}
'''
# info = {
#     'k1':'v1',
#     'k2':[('pounds'),('szk'),('51devops')],
# }

# for key in info['k2']:
#     print(key)


#0409
'''
输出商品列表，用户输入序号，显示用户选中的商品


"""
商品列表：
  goods = [
		{"name": "电脑", "price": 1999},
		{"name": "鼠标", "price": 10},
		{"name": "游艇", "price": 20},
		{"name": "美女", "price": 998}
	]
要求:
1：页面显示 序号 + 商品名称 + 商品价格，如：
      1 电脑 1999 
      2 鼠标 10
	  ...
2：用户输入选择的商品序号，然后打印商品名称及商品价格
3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
4：用户输入Q或者q，退出程序。
'''

# goods = [
#     {'name':'显卡','price':'3500'},
#     {'name':'CPU','price':'2500'},
#     {'name':'内存','price':'1500'},
#     {'name':'主板','price':'1800'}
# ]
# print(
#     ' 1.' + goods[0]['name'] + ' ' + goods[0]['price'] + '\n',
#     '2.' + goods[1]['name'] + ' ' + goods[1]['price'] + '\n',
#     '3.' + goods[2]['name'] + ' ' + goods[2]['price'] + '\n',
#     '4.' + goods[3]['name'] + ' ' + goods[3]['price']
# )

# while True:

#     user_number = input('请输入你的编号:')

#     if user_number == '1':
#         print('1.' + goods[0]['name'] + ' ' + goods[0]['price'],end='\n')
#     elif user_number == '2':
#         print('2.' + goods[1]['name'] + ' ' + goods[1]['price'],end='\n')
#     elif user_number == '3':
#         print('3.' + goods[2]['name'] + ' ' + goods[2]['price'],end='\n')
#     elif user_number == '4':
#         print('4.' + goods[3]['name'] + ' ' + goods[3]['price'],end='\n')
#     elif user_number.lower() == 'q':
#         break

#     else:
#         print('输入有误，请重新输入')


#0401.写代码，有如下列表，按照要求实现每一个功能。

'''
li = ["pounds", "szk", "haoda", "barry", "devops"]
计算列表的长度并输出
请通过步长获取索引为偶数的所有值，并打印出获取后的列表
列表中追加元素”seven”,并输出添加后的列表
请在列表的第1个位置插入元素”Tony”,并输出添加后的列表
请修改列表第2个位置的元素为”Kelly”,并输出修改后的列表
请删除列表中的元素”haoda”,并输出添加后的列表
请删除列表中的第2个元素，并输出删除元素后的列表
请删除列表中的第2至第4个元素，并输出删除元素后的列表
'''
# li = ["pounds", "szk", "haoda", "barry", "devops"]
#计算列表的长度并输出
# result = len(li)
# print(result)

# 请通过步长获取索引为偶数的所有值，并打印出获取后的列表
# result = li[0::2]
# print(result)

# 列表中追加元素”seven”,并输出添加后的列表
# li.append('seven')
# print(li)

# 请在列表的第1个位置插入元素”Tony”,并输出添加后的列表
# li.insert(0,'Tony')
# print(li)

# 请修改列表第2个位置的元素为”Kelly”,并输出修改后的列表
# li[1] = 'Kelly'
# print(li)

# 请删除列表中的元素”haoda”,并输出添加后的列表
# li.remove('haoda')
# print(li)

# 请删除列表中的第2个元素，并输出删除元素后的列表
# del li[1]
# print(li)

# 请删除列表中的第2至第4个元素，并输出删除元素后的列表
# del li[1:5]
# print(li)

# 0402.写代码，有如下列表，利用切片实现每一个功能

'''
li = [1, 3, 2, "a", 4, "b", 5,"c"]
通过对li列表的切片形成新的列表 [1,3,2]
通过对li列表的切片形成新的列表 [“a”,4,”b”]
通过对li列表的切片形成新的列表 [1,2,4,5]
通过对li列表的切片形成新的列表 [3,”a”,”b”]
通过对li列表的切片形成新的列表 [3,”a”,”b”,”c”]
通过对li列表的切片形成新的列表 [“c”]
通过对li列表的切片形成新的列表 [“b”,”a”,3]
'''
# li = [1, 3, 2, "a", 4, "b", 5,"c"]
# # 通过对li列表的切片形成新的列表 [1,3,2]
# # li_new = li[0:3]
# # print(li_new)

# # 通过对li列表的切片形成新的列表 [“a”,4,”b”]
# # li_new = li[3:6]
# # print(li_new)

# # 通过对li列表的切片形成新的列表 [1,2,4,5]
# li_new = li[0::2]
# print(li_new)

# # 通过对li列表的切片形成新的列表 [3,”a”,”b”]
# li_new = li[1:6:2]
# print(li_new)

# #通过对li列表的切片形成新的列表 [3,”a”,”b”,”c”]
# li_new = li[1::2]
# print(li_new)

# # 通过对li列表的切片形成新的列表 [“c”]
# li_new = [li[-1]]
# print(li_new)

# # 通过对li列表的切片形成新的列表 [“b”,”a”,3]
# li_new = li[-3:0:-2]
# print(li_new)

# 0403 
'''
写代码，有如下列表，按照要求实现每一个功能。


lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
将列表lis中的”k”变成大写，并打印列表。
将列表中的数字3变成字符串”100”
将列表中的字符串”tt”变成数字 101
在 “qwe”前面插入字符串：”火车头”
'''
# lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# # 将列表lis中的”k”变成大写，并打印列表。
# lis[2] = "K"
# print(lis)

# # 将列表中的数字3变成字符串”100”
# lis[1] = 100
# lis[3][2][1][1] = 100
# print(lis)

# # 将列表中的字符串”tt”变成数字 101
# lis[3][2][1][0] = 101
# print(lis)

# # 在 “qwe”前面插入字符串：”火车头”
# lis[3].insert(0,'火车头')
# print(lis)

# 0404.请用代码实现循环输出元素和值：users = [“szk”,”pounds”,”波姐”] ，如：

'''
0 szk
1 pounds
2 波姐
'''
# users = ['szk','pounds','波姐']

# for i in range(0,len(users)):
#     print(i,users[i])

# 0405
'''
写代码实现以下功能

如有变量 googs = [‘汽车’,’飞机’,’火箭’] 提示用户可供选择的商品：

0,汽车
1,飞机
2,火箭
用户输入索引后，将指定商品的内容拼接打印，如：用户输入0，则打印 您选择的商品是汽车。
'''
# googs = ['汽车','飞机','火箭']
# for i in range(0,len(googs)):
#     print(i,googs[i])

# resp = int(input('请输入你的序号：'))
# if resp == 0:
# 	print('你选择的商品是汽车')
# elif resp == 1:
#     print('你选择的商品是飞机')
# elif resp == 2:
#     print('你选择的商品是火箭')

# 0407.请用代码实现

# li = "szk"
# 利用下划线将列表的每一个元素拼接成字符串”s_z_k”
# li = "szk"
# result = '_'.join(li)
# print(result)

# 0408
# 利用for循环和range找出 0 ~ 100 以内所有的偶数，并追加到一个列表。
# even = []
# for i in range(1,101):
#     if i % 2 == 0:
#         even.append(i)
# print(even)
# 0409.
# 利用for循环和range 找出 0 ~ 50 以内能被3整除的数，并追加到一个列表。

# number = []
# for i in range(1,50):
#     if i % 3 == 0:
#         number.append(i)
# print(number)

# 利用for循环和range从100~1，倒序打印
# number = []
# for i in range(0,101):
#     number.append(i)
# print(number[-1:0:-1])

# 利用for循环和range循环1-30的数字，将能被3整除的添加到一个列表中，将能被4整除的添加到另外一个列表中。

# number1 = []
# number2 = []
# for i in range(1,30):
#     if i % 3 == 0:
#         number1.append(i)
#     if i % 4 == 0:
#         number2.append(i)
# print(number1,number2)


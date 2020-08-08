#第二章

#0201.列举你了解的编码及他们之间的区别

#1.gbk 是指中国的中文字符，其它它包含了简体中文与繁体中文字符，另外还有一种字符“gb2312”，这种字符仅能存储简体中文字符。
#2.utf-8 它是一种全国家通过的一种编码，如果你的网站涉及到多个国家的语言，那么建议你选择UTF-8编码。
#3.ASCII ASCII编码方案一共规定了128个字符对应的二进制表示，只占用了一个字节的后面7bit，最高位为0

#0202.列举你了解的Python2和Python3的区别？
# 1.print
#     1.1 python2 print是打印语句，将print后面的对象直接打印出来
#     1.2 python3 print是一个函数，可以接收多个参数

# 2.编码
#     2.1 python2 默认ASCII编码方式，未指定编码格式就会报错
#     2.2 python3 默认采用了UTF-8编码

# 3.True&False
#     3.1 python2 把True&False视为全局变量，可以随意赋值
#     3.2 python3 True&False为固定值，不能再被赋值

# 4.long和int类型
#     4.1 python2 区分长短数据类型
#     4.2 python3 统一为int类型

# 5.输入
#     5.1 python2 raw_input
#     5.2 python3 input

# 0203.你了解的python都有那些数据类型？

# 1.bool #布尔值 true&false
# 2.int #整数据类型 1 2 3
# 3.string #字符串类型 'hello world' 
# 4.float #浮点型 1.74 2.56 3.86
# 5.list #列表 [1,2,3] ['python','php']
# 6.tuple #元组 (1,2,3,'hello')
# 7.dictionary #字典 {'name':'carl','age':18}

# 0204.补充代码，实现以下功能
'''
value =  _____ 
print(value)  # 要求输出  51devops"niubi
'''
# value = '51devops"niu bi '
# print(value)


#第三章
# 0301.猜数字，设定一个理想数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了；
# 如果比66小，则显示猜测的结果小了;只有等于66，显示猜测结果正确，然后退出循环。

# while True:
#     number = int(input('请输入你的数字: '))
#     if number == 66:
#         print('恭喜你答对了！')
#         break
#     elif number < 66:
#         print('猜测的结果小了！')
#     else:
#         print('猜测的结果大了！')

#0302.在上一题的基础，设置：给用户三次猜测机会，如果三次之内猜测对了，则显示猜测正确，退出循环，
# 如果三次之内没有猜测正确，则自动退出循环，并显示‘大笨蛋’。

# chance = 1
# while chance <= 3:
#     number = int(input('请输入你的数字: '))
#     if number == 66:
#         print('恭喜你答对了！')
#         break
#     elif number < 66:
#         chance += 1
#         print('猜测的结果小了！')
#     else:
#         chance += 1
#         print('猜测的结果大了！')

#     while chance > 3:
#         print('大笨蛋')
#         break

# 0303.使用两种方法实现输出 1 2 3 4 5 6 8 9 10 。
# number = 1,2,3,4,5,6,7,8,9,10
# print(number)

# number = [i for i in range(1,11)]
# print(number)

# 0304.求1-100的所有数的和
# sum = 0
# for i in range(1,101):
#     sum += i 
# print(sum)

# 0305.输出 1-100 内的所有奇数
# result = []
# for i in range(1,101):
#     if i % 2 != 0:
#         result.append(i)
# print(result)

# 0306.输出 1-100 内的所有偶数
# for i in range(1,101):
#     if i % 2 != 0:
#         continue
#     print(i,end=' ')

# 0307.求1-2+3-4+5 … 99的所有数的和
# sum = 0
# for i in range(1,100):
#     if i % 2 == 0:
#         sum -= i
#     else:
#         sum += i

# print(sum)

# 0308.⽤户登陆（三次输错机会）且每次输错误时显示剩余错误次数（提示：使⽤字符串格式化）

# chance = 1
# residue_chance = 3
# while chance <= 3:
#     user_name = input('请输入你的用户名：')
#     pass_word = int(input('请输入你的密码：'))
#     if user_name == 'root' and pass_word == 666666:      
#         print('登陆成功！')

#     else:
#         residue_chance -= 1
#         print('用户名或者密码错误！你还有 %s 次机会！' % residue_chance)
#         chance += 1
#         while chance == 3:
#             break

# 0309.猜年龄游戏
# 要求：允许用户最多尝试3次，3次都没猜对的话，就直接退出，如果猜对了，打印恭喜信息并退出。 
#        
# chance = 3
# while chance > 0 :        
#     age = int(input('请输入你猜的年龄：'))
#     if age == 26:
#         print('恭喜你答对了！')
#         break
#     else:
#         chance -= 1
#         print('对不起你答错了！')
        
#         while chance == 0:
#             break

# 0310.猜年龄游戏升级版
# 要求：允许用户最多尝试3次，每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y，就继续让其猜3次，以此往复，如果回答N，就退出程序，如何猜对了，就直接退出。
# chance = 3
# while chance > 0 :        
#     age = int(input('请输入你猜的年龄：'))
#     if age == 26:
#         print('恭喜你答对了！')
#         break
#     else:
#         chance -= 1
#         print('对不起你答错了！')
        
#         while chance == 0:
#             result = input('输入Y可获得新的三次机会，输入N退出游戏！')
#             if result == 'Y':
#                 chance = 3
#             elif result == 'N':
#                 break
#             else:
#                 print('输入有误请重新输入！')


# 第四章
# 0401.有变量name = “szk zeNb “ 完成如下操作：

# 移除 name 变量对应的值两边的空格,并输出处理结果
# name = ' szk zeNb '
# print(name.strip())

# 判断 name 变量是否以 “sz” 开头,并输出结果（用切片）
# name = 'szk zeNb'
# section = (name[0:2])
# print(section == 'sz')
# print(name.startswith('sz'))

# 判断name变量是否以”Nb”结尾,并输出结果（用切片）
# name = 'szk zeNb'
# section = (name[6:8])
# print(section == 'Nb')
# print(name.endswith('Nb'))

# # 将 name 变量对应的值中的 所有的”z” 替换为 “p”,并输出结果
# name = 'szk zeNb'
# print(name.replace('z','p'))

# # 将name变量对应的值中的第一个”z”替换成”p”,并输出结果
# name = 'szk zeNb'
# print(name.replace('z','p',1))

# # 将 name 变量对应的值根据 所有的”z” 分割,并输出结果
# name = 'szk zeNb'
# print(name.split('z'))

# # 将name变量对应的值根据第一个”z”分割,并输出结果
# name = 'szk zeNb'
# print(name.split('z',1))

# # 将 name 变量对应的值变大写,并输出结果
# name = 'szk zeNb'
# print(name.upper())

# # 将 name 变量对应的值变小写,并输出结果
# name = 'szk zeNb'
# print(name.lower())
# print(name.title())

# # 请输出 name 变量对应的值的第 2 个字符?
# name = 'szk zeNb'
# print(name[2])

# # 请输出 name 变量对应的值的前 3 个字符?
# name = 'szk zeNb'
# print(name[0:3])

# # 请输出 name 变量对应的值的后 2 个字符?
# name = 'szk zeNb'
# print(name[6:8])


# #0402.有字符串s = “123a4b5c”
# s = '123a4b5c'
# # 通过对s切片形成新的字符串 “123”
# print(s[0:3])
# # 通过对s切片形成新的字符串 “a4b”
# print(s[3:6])
# # 通过对s切片形成字符串s5,s5 = “c”
# s5 = (s[-1:8])
# print(s5)
# # 通过对s切片形成字符串s6,s6 = “ba2”
# s6 = (s[5]) + (s[3]) + (s[1])
# print(s6)

# 0403使用while和for循环字符串 s=”asdfer” 中每个元素。
#for
# s = 'asdfer'
# for i in s:
#     print(i)

#while 
# s = 'asdfer'
# index = 0
# length = len(s)
# while index < length:
#     a = s[index]
#     print(a)
#     index += 1
#     while index == length:
#         break

#0404.使用while和for循环分别对字符串 message = “伤情最是晚凉天，憔悴厮人不堪言。” 进行打印。
# message = '伤情最是晚凉天，憔悴厮人不堪言。'
# # #for
# result = []
# for x in (message):
#     result.append(x)
# res = ''.join(result)
# print(res)

# # #while 
# result = []
# index = 0
# length = len(message)
# while index < length:
#     a = message[index]
#     index += 1
#     # print(a)
#     result.append(a)
#     while index == length:
#         break
# res = ''.join(result)
# print(res)


# #0405.获取用户输入的内容，并计算前四位”l”出现几次,并输出结果。
# acount =  input('请输入你的内容:')
# result = acount.count('l',4)
# print(result)

# #0406.获取用户两次输入的内容，并将所有的数据获取并进行相加
# first_acount =  input('请输入你的内容:')
# second_acount =  input('请再次输入你的内容:')
# result1 = list(filter(str.isdigit,first_acount))
# result2 = list(filter(str.isdigit,second_acount))
# num1 = int(''.join(result1))
# num2 = int(''.join(result2))
# sum = num1 + num2
# print(sum)



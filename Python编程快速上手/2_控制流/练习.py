# 1．布尔数据类型的两个值是什么？如何拼写？
True 
False 

# 2．个布尔操作符是什么？
True and False
True or False
not True 

# 3. 练习
a = (5 > 4) and (3 == 5) # False 
a = not (5 > 4) # False  
a = (5 > 4) or (3 == 5) # True 
a = not ((5 > 4) or (3 == 5)) # False 
a = (True and True) and (True == False) # False 
a = (not False) or (not True) # True 
# print(a)

# 6 个比较操作符是什么？
'''
== 
!= 
>
< 
>=
<= 
'''

# 等于操作符和赋值操作符的区别是什么？
'''
== 和 =
== 是比较两个值的是否相等
= 是为变量赋值
'''

# 编写代码，如果变量 spam 中存放 1，就打印 Hello，如果变量中存放 2，就打印 Howdy，如果变量中存放其他值，就打印 Greetings!
# num = 4
# if num == 1:
#     print('Hello')
# elif num == 2:
#     print('Howdy')
# else:
#     print('Greetings')

'''
break 和 continue 之间的区别是什么？
    break 结束当前循环
    continue 跳出当此循环，继续执行下一次
'''

'''
在 for 循环中，range(10)、range(0, 10)和 range(0, 10, 1)之间的区别是什么？
    
'''

# 如果在名为 spam 的模块中，有一个名为 bacon()的函数，那么在导入 spam模块后，如何调用它？
# import spam
# spam.bacon()


# 附加题：在因特网上查找 round()和 abs()函数，弄清楚它们的作用。在交互式环境中尝试使用它们。
# abs(整负数)：请一个数的绝对值
# round(数值,精度)：保留指定位数的小数(四舍五入)，小数位为0的话自动舍去
print(round(-10))
print(round(12.77,1))
# 单行注释
'''
多行注释
多行注释
多行注释
'''

# 整数 
# print(1)
# print(10_000_000_000 == 10000000000)


# 浮点数(小数)


# 字符串 
# 不同数据类型运算需要转换成相同类型
# int() str()
# print(10 + int(1))
'''
输入框返回的是字符串，如果需要不同类型的数据需要对输入的数据进行类型转换
'''
# age = int(input('请输入年龄'))
# if age >= 16:
#   print('您已成年')
# else:
#   print('未成年')  


# 布尔值 and or not
# age = int(input('请输入年龄'))
# if age > 18:
#   print('成年了')
# else:
#   print('未成年')
a = 3
b = 2
c = 1
print(a>b and a>c)
print(not b>a)

# 变量的赋值
a = 10
b = a 
a = 30
print(a) # 30
print(b) # 10
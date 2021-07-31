# for in 循环
names = ['张三','李四']
for name in names:
    print(name)


# range(数组长度)函数
num = 0
for x in range(20):
    num = num + x
print(num)


# while 只要满足条件就不停止
num1 = 0
maxNum = 10
# while num1 < 10:
#     num1 = num1 + 1


# break 跳出循环
# while num1 < 10:
#     if num1 > 2:
#         break 
#     print(num1)
#     num1 = num1 + 1

# continue 跳过
for x in range(10):
    if x % 2 == 0:
        continue 
    print(x)



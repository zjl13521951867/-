# 练习1 100以内的奇数和
i = 0
count = 0
num = 0 
# while i < 99:
#     i = i + 1
#     if i % 2 != 0:
#         count = count + i 
# print('100内的奇数和 = ',count)

# 练习2 100内7的倍数的和以及个数
# while i < 99:
#     i = i + 1
#     if i % 7 == 0:
#         print('i = ',i)
#         count = count + i
#         num = num + 1
# print('100内7的倍数和',count)
# print('100内7的倍数的个数',num)

# 练习3 
# i = 100 
# while i < 1000:
#     i = i + 1
#     bai = i // 100 
#     shi = (i // 10) % 10 
#     ge = i % 10 
#     if (bai ** 3 + shi ** 3 + ge ** 3) == i:
#         print('水仙花',i)


# 练习4 ，输入任意数字判断是否是质数
i = 0
num = int(input('请输入任意大于1的整数:')) 
count = 0
while i < num:
    i = i + 1
    if num % i == 0:
        print('我被整除',i)
        count = count + 1
if count > 2:
    print('我不是质数')
else:
    print('我是质数')

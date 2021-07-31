# if语句执行特点：当遇到符合添加的的判断后，执行完对应代码就不再向下执行
age = 4
if age >= 18:
    print('成年了')
elif age >= 16:
    print('成熟了')
elif age >= 8:
    print('小孩')
else:
    print('吃奶去')


# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
bmi = 80.7 / (1.75*1.75)
print(bmi)
if bmi < 18.5:
    print('过轻')
elif bmi > 18.5 and bmi < 25:
    print('正常')
elif bmi > 25 and bmi < 28:
    print('过重')
elif bmi > 28 and bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')



# sorted(list, key=fun, reverse=True)
# 参数1：列表(必填)
# 参数2：执行函数(选填)
# 参数3：是否反转排序(选填)
# return 的返回值就是排序的依据
# 规则1：数字按照重大到小
# 规则2：字符串按照ASCII的大小比较的
# 注意点：大小写字母的问题 Z > a, 一般情况下要不区分大小写





# 练习 按照名字排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
L2 = sorted(L, key=by_name)
print(L2)

# 练习 按照分数排序
def by_score(t):
    return t[1]
L3 = sorted(L, key=by_score)
print(L3)

# 练习 不区分大小写
names = ['Bob','jack','Z','atom']
names2 = sorted(names)
names3 = sorted(names,key=str.lower)
print('names2',names2)
print('names3',names3)
# 迭代：循环遍历一个列表
# list = ['第一','第二','第三']
# for idx, val in enumerate(list):
#     print(idx,val)

# 字典(dict)的迭代
# d = {'name':'张三','age':20,'address':'芜湖'}
# 取key
# for key in d:
#     print('单独key',key)
# # 取value
# for value in d.values():
#     print('单独value',value)
# # 同时取key value 
# for key,value in d.items():
#     print('一起key',key)
#     print('一起value',value)


# 判断当前对象是否可以迭代
from collections.abc import Iterable
# print('是否可以迭代',isinstance('123',Iterable)) # True
# print('是否可以迭代',isinstance([1,2,3],Iterable)) # True
# print('是否可以迭代',isinstance(d,Iterable)) # True
# print('是否可以迭代',isinstance(111,Iterable)) # False

# 取出数组的最大值和最小值
def findMax(list=[]):
    empList = []
    # 无数
    if not list:
        empList = [None,None]
    # 列表长度1    
    elif len(list) == 1:
        empList = [list[0],list[0]]
    # 列表长度大于1    
    else:
        maxItem = list[0]
        minItem = list[0]
        for item in list:
            if item > maxItem:
                print('最大',item)
                maxItem = item 
            if item < minItem:
                print('最小',item)
                minItem = item 
        # maxItem = max(list)
        # minItem = min(list)
        # # empList.append(minItem)
        # # empList.append(maxItem)
        empList.insert(0,maxItem)
        empList.insert(0,minItem)
    return tuple(empList)

if findMax([]) != (None, None):
    print('测试失败!')
elif findMax([7]) != (7, 7):
    print('测试失败!')
elif findMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
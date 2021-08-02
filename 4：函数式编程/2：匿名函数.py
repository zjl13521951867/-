# 匿名函数 lambda 参数:函数体
# 冒号前面是参数，冒号后面是执行方法(省略return)

from functools import reduce
list1 = [1,2,3,4,5,6,7,8,9]
list2 = filter(lambda x:x > 5,list1)
list3 = reduce(lambda x,y:x+y,list1)
print(list(list2))
print(list3)
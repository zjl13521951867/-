# 可以循环的数据类型 
# list(数组) [1,2,3]
# tuple(元数组) (1,2,3)
# set(key的集合) (key1,key2,key3)
# dict(字典 对象) {'name':'Jack'}
# str(字符串) '字符串'
# generator 

# Iterable(可迭代对象)：这些可以直接作用于for循环的对象
# 通过 isinstance(数据,Iterable)来判断是否可以for循环遍历
from collections.abc import Iterable
from typing import Generator
# print(isinstance([1,2,3],Iterable))
# print(isinstance((1,2,3),Iterable))
# print(isinstance(set([1,2,3]),Iterable))
# print(isinstance({'name':'Jack'},Iterable))
# print(isinstance('字符串',Iterable))
# print(isinstance(100,Iterable))
# print(isinstance((x for x in range(1,11)),Iterable))

print('----------------') 

# Iterator(迭代器)：可以被next()函数调用并不断返回下一个值的对象
# 通过 isinstance(数据,Iterator)来判断是否可以next()调用
from collections.abc import Iterator
# print(isinstance([1,2,3],Iterator))
# print(isinstance((1,2,3),Iterator))
# print(isinstance(set([1,2,3]),Iterator))
# print(isinstance({'name':'Jack'},Iterator))
# print(isinstance('字符串',Iterator))
# print(isinstance(100,Iterator))
# print(isinstance((x for x in range(1,11)),Iterator))


# iter()函数：可以将可循环的Iterable对象，转换成Iterator对象(generator)
# Iterator(包括generator)的优点：generator表示的是一个数据流，且是一个堕性的数据流，只有通过next()调用才能获取下一个数据
list = [1,2,3,4]
print(list)
print(iter(list))

d = {'name':'张三','age':20}
# print(d)
# print(iter(d))
for key,val in d.items():
    print(key,val)
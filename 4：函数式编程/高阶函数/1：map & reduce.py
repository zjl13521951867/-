'''
map(fun(x),Iterable) 列表中的每一项执行一下fun()
参数1：函数 
参数2：可迭代的列表
返回值：Iterator 可执行next()的
'''
a = [1,2,3,4,5]
def add(item):
    return item + 10 
b = map(add,a)
# print(next(b))
# print(next(b))
for x in b:
    pass
    # print(x)


'''
使用前需要先引入，Python中reduce函数在 functools内
reduce(fun(x,y),Iterable)
参数1：函数，接受两个参数(当前结果 + 下一个元素)
参数2：可迭代的列表
返回值：累计后的结果
'''
from functools import reduce
def add2(x,y):
    # print('x',x)
    # print('y',y)
    return x + y 
c = reduce(add2,[1,2,3])
# print(c) # 结果为6 1+2+3

# 练习 map转换大小写
def normalize(name):
    return name.capitalize()
print(list(map(normalize,['adam', 'LISA', 'barT'])))

# 练习 reduce求乘积
def add3(x,y):
    return x * y 
def prod(list):
    result = reduce(add3,list)
    return result 
print(prod([3,5,7,9]))

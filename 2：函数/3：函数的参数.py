# 参数默认值 fun(x=1)
# 注意：必选参数必须在后面
'''
* 数组
** 对象
'''

from typing import Deque


def power(x,n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x 
    return s

def person(name,age=6,address='北京'):
    print(f'{name}今年{age}岁了,住在{address}')
person('张加乐')

def addList(list=[]):
    if len(list) == 0:
        list = []
    list.append('结尾')
    print('列表',list)


# 默认传入list / tuple
# 参数为列表时间，如果实参无值将会报错，需要做好兼容
# 形参和实参前面加上*，表示动态参数，不确定个数，可能没有
# *nums 相当于将多个参数解构出来
def add(*nums):
    num = 0
    for x in nums:
        num = num + x * x
    return num 
# print(add([1,2,3]))
# print(add((1,2)))
# print(add(1))
print(add(*[1,2,3,4,5,6]))
print(add())

# 
def add2(nums=[]):
    num = 0
    if not nums:
        pass 
    else:
        for n in nums:
            num = num + n * n 
    return num 

print('add2',add2())
print('add2',add2([1,2,3]))


# 关键字参数，将多个参数组成一个对象传入 fun(**object)
# 扩展字段有没有都可以
# kw是personData的一份拷贝，改动不会影响到函数外部的personData数据
personData = {'address':'成都'}
def person2(name,age,**kw):
   
    print('姓名',name)
    print('年龄',age)
    print('扩展信息',kw['address'])
person2('张三',20,**personData)


def mul(*list):
    num = 1
    if len(list):
        for x in list:
            num = num * x 
    else:
        num = 0 
    return num 
print(mul(1,2,3))
print(mul(*[1,2,3,4,5]))
print(mul())



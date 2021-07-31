# Python内置函数 http://docs.python.org/3/library/functions.html
# 常用 https://www.cnblogs.com/wujiaqing/p/10709207.html

# abs() 绝对值
print(abs(-1))

# all(arr) 所有元素都为真返回true，任意一个不为真都返回false
# 值为False的情况
# 1：None  2：False  3：数值0(0.0 0j) 4：空列表(数组 [] ())  5：空字典({})
print(all([1,2,'']))
print(all((1,2,3)))

# any(arr) 任意一项为真返回True 都不为真返回False
print('any -- ',any([1,'']))

# ascii(object)  将对象(字典)转换成字符串
a = ascii({'bob':20})
print('ascii -- ',ascii({'bob':20}))
# print('ascii -- ',a['bob']) 此时a为字符串

# bin() 将一个整数转变为一个前缀为“0b”的二进制字符串，必须为整数
print('bin -- ',bin(10))

# bool() false：空串 空数组 空对象 0 None
print('bool -- ',bool(0))
print('bool -- ',bool(1))
print('bool -- ',bool(None))

# breakpoint() 待学习

# bytearray()
b = bytearray('张加乐',encoding='utf-8')
print('bytearray -- ',b)
b[0] = 12
print('bytearray -- ',b)

# isinstance
# 判断一个对象是否是已知类型

# map
# python3中，map返回的是map对象，需要用list()函数转化成 
# 对象(字典)取值的时候需要做校验，判断当前key在此对象内是否存在
def mapListHandle(item):
    if 'score' in item:
        print('score',item['score'])
    else:
        item['score'] = 0
    
    return item 
mapList = [{'score':20},{'tom':40}]
newList = list(map(mapListHandle,mapList))
print('newList',newList)


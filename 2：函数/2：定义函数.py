# def 声明函数
def abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('类型错误')
    if x > 0:
        return x
    else:
        return -x 
# print('10 -- ',abs(10))
# print('-1 -- ',abs(-1))

# 空函数 空判断
# pass 占位符，不执行任何代码(其他代码可正常运行)
def nop():
    pass 
if nop:
    pass 


import math
def quadratic(a,b,c):
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)) or not isinstance(c,(int,float)):
        return '参数异常'
    x = (-b + math.sqrt(math.exp(b) - 4*a*c)) / 2*a 
    y = (-b - math.sqrt(math.exp(b) - 4*a*c)) / 2*a 
    return (x,y)

print(quadratic(2, 3, 1))
print(quadratic(1, 3, 2))

# 对象
# 
def mapListHandle(item):
    if 'score' in item:
        print('score',item['score'])
    else:
        item['score'] = 0
    
    return item 
mapList = [{'score':20},{'tom':40}]
newList = list(map(mapListHandle,mapList))
print('newList',newList)



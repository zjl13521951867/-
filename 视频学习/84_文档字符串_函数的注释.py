'''
help()函数
    获取函数的使用说明
    自定义的函数也可以使用，但是需要开发人员手动加注释
'''
desc = help(print)

def sum(a=0,b=0,c=0):
    '''
    函数作用：计算任意三个值的累加，并返回结果(返回值为int)
    参数a：类型 int 默认值0
    参数b：类型 int 默认值0
    参数c：类型 int 默认值0
    '''
    return a + b + c 
print(help(sum))
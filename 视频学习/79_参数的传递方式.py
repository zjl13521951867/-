'''
    位置参数：
        按照参数传递的位置赋值

    关键字参数：
        key值相同的赋值

    不定长参数(*args)：
        不定长参数*args是一个元组
        不定长参数需要写在位置参数后面，位置参数取完的参数会同统一存到不定长参数内，组成元组
        假如不定长参数没有在最后一位，
            那么'实参'需要以关键字参数传入，
            因为不定长参数会将所有剩余的参数存入一个元组内，如果不适用关键字参数，则后面位置的参数拿不到对应的值，会报错

    字典参数(**args):
        如果所有的实参都是关键字参数，则可以用**args来接受所有参数，组装成一个字典

    参数结包：
        位置参数
            *list 解包列表
            **dict 解包字典
'''


# def person(name,age,gender='男'):
#     print(f'我叫{name} 今年{age}岁了，我是{gender}性')
# person(age=20,name='王麻子',gender='男')
# person('张三',30,'女')
# person('赵四',30)


# 不定长参数
# def sum(a,b,*args):
#     result = 0
#     for x in args:
#         result += x 
#     print('result =',result)
# sum(1,2,3,4,5) 
# sum(6,7) 


# **字典参数
# {'a': 1, 'b': 2, 'c': 3}
# def sum(**args):
#     print(args['a'])
#     print(args['b'])
#     print(args['c'])
# sum(a=1,b=2,c=3)


# 参数解包
list = [1,2,3]
d = {'a':20,'b':30,'c':40}
def sum(a,b,c):
    print(a)
    print(b)
    print(c)
sum(*list)
sum(**d)
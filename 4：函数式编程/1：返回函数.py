# 函数当作返回值
# 内部函数引用外部函数的变量

# global 变量 => 函数内部使用全局变量需要先声明
# nonlocal 变量 => 内部函数引用外部函数的变量需要声明下


def fun(x,y):
    def add():
        return x + y 
    return add 
add = fun(1,3)
print(add())


# 练习 每次执行返回函数自增1
def createCounter():
    a = 0
    def counter():
        nonlocal a 
        a = a + 1
        return a 
    return counter

counterA = createCounter()
print('counterA',counterA())
print('counterA',counterA())
print('counterA',counterA())
print('counterA',counterA())

counterB = createCounter()
print('counterB',counterB())
print('counterB',counterB())
print('counterB',counterB())
print('counterB',counterB())



# 生成器
# []表示list
# ()表示一个generator
# 为什么要使用generator：生成器的值真正使用的时候才会创建(计算出来),不用创建一个完整的list，在数据量大的时候性能会更好
# 函数中使用yield就是generator函数，返回一个generator
# 1 - Python的Iterator对象表示的是一个数据流，
# 2 - Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。
# 3 - 可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，
# 4 - 所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
L = [x for x in range(1,11)]
def LHandle(list):
    for x in list:
        if x % 2 == 0:
            yield x 

print('哈哈',LHandle(L))
for x in LHandle(L):
    print('%2',x)


# next(g)获取下一个值，但是正常使用时都是以for循环的方式调用
g = (x for x in range(1,11))
for n in g:
    pass

# 练习 
# a, b = b, a + b 等同于 (a = b) (b = a + b)，但是此时是同时计算a + b中a的值还是没有赋值为b前的值
def fib(max):
    n = 0
    a = 0
    b = 1
    prev = 0 
    while n < max:
        # print('当前',b)
        a = b 
        b = prev + b 
        prev = a 
        n = n + 1
fib(6)


# 函数中包含yield就不同一个普通函数，是一个generator
# yeild 后边跟的就是返回值
def fib2(max):
    n = 0
    a = 0
    b = 1
    prev = 0 
    while n < max:
        yield b
        a = b 
        b = prev + b 
        prev = a 
        n = n + 1
for n in fib2(6):
    pass
    # print('结果',n)

# 列表直接将一千万条数据直接生成，
# largeL = [x for x in range(10000000)]
# print(largeL)

# generator只是生成了,但是数据直会在运算和使用中产生，并且是逐个产生(当前项的返回值就是下一项的值)
largeG = (x for x in range(10000000))
print(len(list(largeG)))
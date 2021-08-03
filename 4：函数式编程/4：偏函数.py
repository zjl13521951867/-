from functools import partial
# 参数1：函数
# 参数2：*args
# 参数3：**kw
# 优点1：partial执行时的(args和kw)，在写代码时，可能需要用到相同的函数，但是会有部分参数不同，这样操作起来就会方便很多
# 有点2：原函数的参数过多时，修改和操作原函数相对困难，这时候创建新函调用会相对简单点
int2 = partial(int,base=2)
print(int2('1000000'))

def add(*args):
    return sum(args)
add_101 = partial(add,100)
print(add_101(1))

add_201 = partial(add,200)
print(add_201(1))
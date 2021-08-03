# 1：定义一个函数
# 2：函数内还有一个内部函数，内部函数的返回值是一个函数
# 3：将这个内部函数return
# @metric 相当与执行le metric(fast)，修饰符的作用相当于把一个函数作为参数传入decorator这个函数内
# 优点：在不改变原有方法的基础上，新增一些功能

import time, functools
def metric(fn):
    # 这里是新增的代码
    print('%s executed in %s ms' % (fn.__name__, 10.24))
    
    # 这里执行的是原函数的代码
    def fun(*args,**kv):
        print('参数',*args)
        return fn(*args,**kv)
    return fun

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

f = fast(11, 22)
print('f=',f)
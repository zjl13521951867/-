'''
    locals()：获取当前作用域的命名空间
        locals()返回值就是一个字典，作用域内的变量和函数以key-value的形式保存

    globals()：可以在任意作用域获取全局的命名空间 
'''

a = 10 
b = 20 
def fn():
    # c = 40 
    # d = 50 
    scope = locals()
    print(scope)
    return scope

scope = locals()
# print(scope)
# print(type(scope)) # <class 'dict'>

fn_scope = fn()
print(fn_scope)

fn_scope['c'] = 90
fn_scope['d'] = 400
# fn()
fn()
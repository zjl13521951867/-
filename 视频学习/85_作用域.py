'''
    global关键字：
        在函数内部以global关键字声明变量，修改这个变量就是全局的变量
'''

num = 10 
def fn():
    global num 
    num = 20  
    print('内部',num) # 20

fn()
print('外部',num) # 如果不加global = 10   加global = 20 
# 函数
def fun(options):
  # 对象取值前必须判断key是否存在
  if 'name' in options:
    pass
    print(options)
    
options = {'name':'Jack','address':'北京'}
fun(options)


# 模块 每一个.py的文件都是一个模块
# 引入方式1：from module1 import foo => foo()
# 引入方式2：import module1 as m1 => m1.foo()
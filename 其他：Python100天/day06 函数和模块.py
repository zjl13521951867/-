# https://zhuanlan.zhihu.com/p/64893308
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

# 同级引入
# 1：直接引入函数
from module1 import conso
conso('同级引入1')
# 2：引入此模块
import module1
module1.conso('同级引2')
# 3：引入模块赋值给一个变量
import module1 as module_1 
module_1.conso('同级引入3')

print('----------')

# 导入下级模块
# 1：引入模块
from next import next1 
next1.nextConso('下级模块1')
# 
import next.next1



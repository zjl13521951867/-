# 元类扩展：https://www.liaoxuefeng.com/wiki/1016959663602400/1017592449371072#0

# class创建
class Hello(object):
    def hello(self,name):
        print(f'Hello{name}')
Hello().hello('张三')

# 运行时创建
# 参数1：类的名称
# 参数2：父类的集合(注意元组的用法，继承单一类也需要加逗号) (object,)
# 参数3：函数
def hello(self,name):
    print(f'{name}')
def hello2(self,name):
    print(f'第二个{name}')
def __init__(self,name):
    self._name = name 
Hello2 = type('Hello',(object,),dict(hello=hello,hello2=hello2))
Hello2().hello('王麻子')
Hello2().hello2('王麻子')

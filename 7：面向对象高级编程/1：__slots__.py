class Person(object):
    # 限定指定Person类只能绑定name和age属性，绑定其他属性会报错
    # __slots__ 对子类无法限制
    __slots__ = ('name','age')
    def __init__(self,name,age):
        self._name = name 
        self._age = age
    
    # 读取
    @property
    def name(self):
        return self._name 
    
    # 更新(修改)
    @name.setter
    def name(self,name):
        self._name = name 



p1 = Person('张三',20)
p2 = Person('王麻子',20)
p1.name = '三孙子'
print(p1.name)
print(p2.name)

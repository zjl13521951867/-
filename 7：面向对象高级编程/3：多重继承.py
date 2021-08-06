# 多重继承原则：https://blog.csdn.net/qq_31362767/article/details/99192735

# 多重继承：一个子类有多个父类
# 例：狗是动物 在动物内又属于哺乳动物
class Animal(object):
  def __init__(self,name):
    self._name = name 
  
  @property
  def name(self):
    return self._name 

class Mammal(Animal):
  pass 

class Dog(Mammal,Animal):
  pass 

class Cat(Mammal):
  pass 

print(Dog('狗狗').name) 
print(Dog('猫咪').name) 

print(Dog('狗狗').__repr__)
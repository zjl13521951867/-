# 继承：当新增一个类的时候，将别的类作为object传入，新建的类就是这个类的子类，也将继承这个类的所有属性和方法
class Animal(object):
    def run(self):
        print('Animal is running')
ani = Animal()
ani.run()

# 子类
# 当子类和父类存在相同的方法时，子类的方法会覆盖父类的
class Dog(Animal):
    def run(self):
        print('dom is running') 
dog = Dog()
dog.run()


# https://blog.csdn.net/weixin_34365635/article/details/94569022
# 多态性是指具有不同功能的函数可以使用相同的函数名，这样就可以用一个函数名调用不同内容的函数。
from abc import ABCMeta,abstractmethod
class Pet(object,metaclass=ABCMeta):
  def __init__(self,pet_name):
    self._pet_name = pet_name
  
  # @abstractmethod 表示子类必须有这个方法
  @abstractmethod
  def talk(self):
    raise AttributeError('子类必须实现这个方法')

class Dog(Pet):
  def talk(self):
    print(f'{self._pet_name} 汪汪汪')
Dog('狗狗').talk()

class Cat(Pet):
  def talk(self):
    print(f'{self._pet_name} 喵喵喵')
Cat('猫咪').talk()

class Fish(Pet):
  def talk(self):
    print(f'{self._pet_name} 咕噜咕噜咕噜')
Fish('鱼').talk()


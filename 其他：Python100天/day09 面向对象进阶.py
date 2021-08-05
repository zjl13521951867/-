# 不建议直接将属性设置为私有属性，所以在内部绑定属性时，重新命名属性值，然后通过函数返回属性来获取这些属性
# _name相当于私有属性，虽然通过p1._name还是可以获取，但是在对外暴露的时候指挥暴露name的getter()和setter()方法

# _slots__魔法：限定当前类只能新增哪些属性(不在指定的属性内添加会报错)，这个限定对子类不生效

# 静态方法：@staticmethod 装饰的函数就是静态方法
# 类似于前置的校验，并不是对象方法
# 实例和类都可以调用静态方法
# 例：计算三角形的周长(a,b,c)，但是需要知道a,b,c能否组成三角形，所以需要一个方法来判断，通过了才走计算周长的方法

class Person(object):
  __slots__ = ('_name','_age')
  def __init__(self,name,age):
    self._name = name 
    self._age = age 
  
  # getter 通过函数返回私有的属性，但是调用时直接 p1.name直接调用就可以拿到属性值，不用加函数调用()
  @property
  def name(self):
    return self._name 

  # setter
  @name.setter
  def name(self,name):
    self._name = name 

  @property
  def age(self):
    return self._age 

  @age.setter
  def age(self,age):
    self._age = age 

  @staticmethod
  def get_score(score):
    if score > 85:
      print('优秀')
    else:
      print('不好')
# p1.nage 读取   
# p1.name = '' 更新
p1 = Person('张三',30)
Person.get_score(99)

class Child(Person):
  def __init__(self,name,age,gender):
    self._name = name 
    self._age = age 
    self._gender = gender 
c1 = Child('儿子',12,'男')
print(c1.name)
Child.get_score(20)


print('下面为练习1-----------')
# 练习1 
class Triangle(object):
  def __init__(self,a,b,c):
    self._a = a 
    self._b = b 
    self._c = c 
  
  # 静态方法 - 检查是否能构成三角形
  @staticmethod
  def is_valid(a, b, c):
    return a + b > c and b + c > a and a + c > b

  # 对象方法 - 计算三角形的周长
  def count_long(self):
    return self._a + self._b + self._c 

# a,b,c = 3,4,5
a,b,c = 1,2,3
if Triangle.is_valid(a,b,c):
  t1 = Triangle(a,b,c)
  print('周长',t1.count_long())
else:
  print('无法构成三角形')
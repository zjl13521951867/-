# Python坑：https://blog.csdn.net/jackfrued/article/details/79521404

# 定义类
class Student(object):
  # 每次调用Student生成实例就会触发 __init__
  def __init__(self,name,age):
    pass

# 创建对象
s1 = Student('张三',18)


# 练习1：时钟
from time import sleep
class Clock(object):
  def __init__(self,h=0,m=0,s=0):
    self.h = h 
    self.m = m 
    self.s = s
  
  def run(self):
    self.s = self.s + 1
    if self.s == 60:
      self.s = 0
      self.m = self.m + 1
    if self.m == 60:
      self.m = 0
      self.h = self.h + 1
    if self.h == 24:
      self.h = 0
    
    # h = self.h if self.h >= 10 else '0' + str(self.h)
    # m = self.m if self.m >= 10 else '0' + str(self.m) 
    # s = self.s if self.s >= 10 else '0' + str(self.s)
    # return f'{h}:{m}:{s}'
    return ('%02d:%02d:%02d' %(self.h, self.m, self.s))

  
c1 = Clock(0,0,0)
# while True:
#   sleep(1)
#   print(c1.run())


# 练习2  定义一个类描述平面上的点 并提供计算
class Point(object):
  def __init__(self,x=0,y=0):
    self.x = x 
    self.y = y 
  
  # 移动
  def move(self,x,y):
    self.x = x 
    self.y = y 

  # 计算距离
  def distance(self,x,y):
    dis_x = abs(self.x - x)
    dis_y = abs(self.y - y)
    return (dis_x,dis_y)

p1 = Point(0,0)
print('起始',p1.x,p1.y)

p1.move(10,10)
print('移动到',p1.x,p1.y)

dis1 = p1.distance(30,20)
print('移动距离',dis1)

# 1：可以限制只读，不添加setter方法

class Person(object):
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



class Screen(object):
    @property
    def width(self,width):
        return width

    @width.setter 
    def width(self,width):
        self.wdith = width 


    @property
    def height(self,height):
        return height 
    
    @height.setter
    def height(self,height):
        self.wdith = height

    @property
    def resolution(self,resolution=786432):
        return resolution

s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)

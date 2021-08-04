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



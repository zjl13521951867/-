# 实例属性：通过实例的变量或者self添加
# 类属性：在当前类上添加，类属性实例也可以访问，存在同名属性 实例属性 > 类属性
# class内 __init__在类被调用后才会执行

class Student(object):
    count = 0
    def __init__(self,name):
        self.name = name 
        Student.count = Student.count + 1 
print(Student.count)
s1 = Student()
print(Student.count)
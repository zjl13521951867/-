# type()函数返回的是什么类型呢？它返回对应的Class类型
print(type(123) == int) # True 
print(type('哈哈') == str) # True 

# 判断一个对象是否是函数
# types 模块
import types
def fn():
    pass 
print(type(fn) == types.FunctionType)


# 判断对象属于哪个类 isinstance(数据,类)
# 继承的子类都属于父类型
print('整数',isinstance(123,int))
print('小数',isinstance(1.23,float))
class Father(object):
    pass 
class Mather(Father):
    pass 
f1 = Father()
m1 = Mather()
print('自定义类',isinstance(f1,Father))
print('自定义类',isinstance(m1,Father))

# dir(数据) 获取当前数据类的的所有属性和方法，这些方法都是底层方法，我们使用的一下方法都是基于这些底层方法封装的
# print(dir(123))


# 对象属性的操作
# getattr(obj,key,status)：获取对象属性，不存在的属性会爆粗和，参数3选填，指定不存在的数据查询时的返回状态
# hasattr(obj,key)：检查该对象是否有指定属性
# setATTR(obj,key,value)：设置对象属性值
class Student(object):
    # 默认写法，将一些基础数据绑定上
    def __init__(self,name,score):
        self.name = name 
        self.score = score 
    
    # 自定义方法
    def print_score(self):
        print(f'{self.name}期末考试的成绩是{self.score}分')
s1 = Student('王麻子',20)
setattr(s1,'name','二狗子')
print('s1',hasattr(s1,'name'))
print('s1',hasattr(s1,'address'))
print('s1',s1.name)
print(getattr(s1,'address',404))
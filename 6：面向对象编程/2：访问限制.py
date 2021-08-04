# 内部属性不被外部访问和修改
# 私有属性的前面加上 __(两个下划线)，就是能在Class内部访问了
# 假如外部需要读取私有属性怎么办？添加对应的方法 "获取" 例：def get_name(self):return name 即可
# 加入外部需要修改私有属性怎么办？添加对应的方法 "设置" 例：def set_name(self,name):self.__name = name 

class Student(object):
    # 默认写法，将一些基础数据绑定上
    def __init__(self,name,score):
        self.__name = name 
        self.score = score 
    
    # 自定义方法
    def print_score(self):
        print(f'{self.__name}期末考试的成绩是 {self.score}分')

    # 获取私有属性
    def get_name(self):
        return self.__name 

    # 更新私有属性
    def set_name(self,name):
        self.__name = name 

s1 = Student('张三',60)
s1.address = '朝阳区'
print(s1.score)
s1.print_score()

s2 = Student('李四',80)
s2.print_score()
print('私有属性name',s2.get_name())
s2.set_name('王麻子')
print('私有属性name - 更新后',s2.get_name())


# 练习 gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：

class Student2(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    
    def get_gender(self):
        return self.__gender

    def set_gender(self,gender):
        self.__gender = gender




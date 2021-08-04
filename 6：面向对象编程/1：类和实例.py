class Student(object):
    # 默认写法，将一些基础数据绑定上
    def __init__(self,name,score):
        self.name = name 
        self.score = score 
    
    # 自定义方法
    def print_score(self):
        print(f'{self.name}期末考试的成绩是{self.score}分 家住{self.address}')

s1 = Student('张三',60)
s1.address = '朝阳区'
print(s1.name,s1.score)
s1.print_score()
from abc import ABCMeta, abstractmethod

"""
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""
class Employee(object,metaclass=ABCMeta):
  def __init__(self,name):
    self._name = name
  
  # 姓名
  @property
  def name(self):
    return self._name 

  # 工资计算 => 当前方法需要所有子类都有
  @abstractmethod
  def get_salary(self):
    pass 


# 经理工资
class Manager(Employee):
  def get_salary(self):
    return 15000

# 程序员工资
class Programmer(Employee):
  def __init__(self,name,work_hours=0):
    super().__init__(name)
    self._work_hours = work_hours

  @property
  def work_hours(self):
    return self._work_hours
  
  @work_hours.setter
  def work_hours(self,work_hours):
    self._work_hours = work_hours

  def get_salary(self):
    return self._work_hours * 150 

# 销售人员工资
class Salesman(Employee):
  def __init__(self,name,sales=0):
    super().__init__(name)
    self._sales = sales

  @property
  def sales(self):
    return self._sales 

  @sales.setter
  def sales(self,sales):
    self._sales = sales

  def get_salary(self):
    return 1200 + self._sales * 0.05


m1 = Manager('王经理')
print(f'{m1.name}本月工资为{m1.get_salary()}')

p1 = Programmer('王二')
p1.work_hours = 264
print(f'{p1.name}本月工资为{p1.get_salary()}')

s1 = Salesman('王二')
s1.sales = 150000
print(f'{s1.name}本月工资为{s1.get_salary()}')

# p_list = ['张三','李四','王五','赵六']
# for p in p_list:
#   p2 = Programmer(p)
#   p2.work_hours = int(input(f'请输入{p}本月的工作时长：'))
#   print(f'{p}本月的工资为 {p2.get_salary()}')

s_list = ['成妍','王鹏']
for s in s_list:
  s2 = Salesman(s)
  s2.sales = int(input(f'请输入{s}本月的销售额：'))
  print(f'{s}本月的工资为 {s2.get_salary()}')

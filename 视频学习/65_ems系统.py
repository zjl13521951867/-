# 查询
# 添加
# 删除
# 退出

from typing import ForwardRef


class Ems(object):
    def __init__(self,list):
        self._list = list 

    @property
    def list(self):
        return self._list
    
    @list.setter
    def list(self,list):
        self._list = list 

    def look(self):
        print('序号\t','姓名\t','年龄\t','性别\t','住址\t')
        for idx,emp in enumerate(self._list):
            print(f'{idx+1} \t {emp["name"]}\t {emp["age"]} \t {emp["gender"]} \t {emp["address"]}')

    def add_emp(self,emp):
        self._list.append(emp)
ems1 = Ems([{'name':'孙悟空','age':'9000','gender':'男','address':'花果山'}])
ems1.look()

while True:
    print('请选择操作：')
    print('1、查询员工：')
    print('2、添加员工：')
    print('3、删除员工：')
    print('4、退出系统：')
    choose = input('请选择1-4')

    # 查询
    if choose == '1':
        ems1.look()
        pass 
    elif choose == '2':
        dict_emp = {}
        dict_emp['name'] = input('请输入员工姓名：')
        dict_emp['age'] = input('请输入员工年龄：')
        dict_emp['gender'] = input('请输入员工性别：')
        dict_emp['address'] = input('请输入员工住址：')
        ems1.add_emp(dict_emp)
        pass 
    elif choose == '3':
        pass 
    elif choose == '4':
        print('退出系统')
        break
        pass 
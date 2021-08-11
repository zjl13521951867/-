from genericpath import isdir,isfile
import os 

# 系统名称 
# nt：windows系统
# print(os.name)

# 环境变量
# print(os.environ)

# 获取某个环境变量的值
# print(os.environ.get('APPDATA'))

# 获取绝对路径
# print(os.path.abspath('./1：Python基础/1：第一个Python.py'))
# f = open(os.path.abspath('./1：Python基础/1：第一个Python.py'), mode='r', encoding='utf-8')
# print(f.read())


def get_file(dir):
    dir_list = os.listdir(now_dif)
    for d in dir_list:
        if d == '.git':
            continue
        if isfile(rf'{dir}\{d}'):
            pass 
            print('文件',d)
        else:
            get_file(f'{dir}\{d}')

# 获取当前目录  c:\Users\13521\Desktop\Python\-
now_dif = os.getcwd()
# 根据当前目录查找目录下的所有文件/文件夹
get_file(now_dif)

# 文件操作使用open()函数
# open(src,mode,encoding) 路径 读/写... 编码
# with open(src,mode,encoding) as f  等价于  f = open(src,mode,encoding)

# 文件异常
# FileNotFoundError 文件找不到
# LookupError 指定了未知的编码会引发
# UnicodeDecodeError 而如果读取文件时无法按指定方式解码

# file1 = open(r'C:\Users\13521\Desktop\Python\-\pythonModule\file1.txt',mode='r',encoding='utf-8')
# print(file1)
# print(file1.read())
# file1.close()

# 文件循环
# txt文件循环，循环中可逐行读取文本内容
# file.readlines() 返回一个将每行内容读取到一个列表的容器

# 文件读取 mode='r'
# 将可能产生错误打代码放入try，抛出异常
# import time 
# file1 = ''
# try:
#     file1 = open(r'C:\Users\13521\Desktop\Python\-\pythonModule\file1.txt',mode='r',encoding='utf-8')
#     for f in file1:
#         print(f)
#         time.sleep(0.5)
    
#     lines = file1.readlines()
#     for l in lines:
#         print(l)
#         time.sleep(0.5)
# except FileNotFoundError:
#     print('查找不到指定文件 / 文件无法打开')
# except LookupError:
#     print('编码问题')
# finally:
#     file1 and file1.close()


# 文件写入 
# mode='w' 写入文件，但是之前的内容会被删除 (相当于覆盖)
# mode='x' 写入文件, 文件如果存在的话会报错 (相当于新建一个文件)
# mode='a' 写入文件，像文件内追加内容(不会覆盖原有内容)
# try:
#     # file1 = open(r'C:\Users\13521\Desktop\Python\-\pythonModule\file2.txt',mode='w',encoding='utf-8')
#     # file1 = open(r'C:\Users\13521\Desktop\Python\-\pythonModule\file2.txt',mode='x',encoding='utf-8')
#     # file1 = open(r'C:\Users\13521\Desktop\Python\-\pythonModule\file2.txt',mode='a',encoding='utf-8')
#     with open(r'C:\Users\13521\Desktop\Python\-\pythonModule\file1.txt',mode='w',encoding='utf-8') as file1:
#         file1.write('作者：李绅\n锄禾日当午，\n汗滴禾下土，\n谁之盘中餐，\n粒粒皆辛苦。')
#         file1 = open(r'C:\Users\13521\Desktop\Python\-\pythonModule\file1.txt',mode='r',encoding='utf-8')
#         print(file1.read())
# except FileNotFoundError:
#     print('查找不到指定文件 / 文件无法打开')
# except LookupError:
#     print('编码问题')
# finally:
#     file1 and file1.close()


# 练习，将99乘法表写入一个新文件内
# def multiplication_table():
#     try:
#         with open(r'C:\Users\13521\Desktop\Python\-\pythonModule\file2.txt',mode='a',encoding='utf-8') as file2:
#             i = 0
#             while i < 9:
#                 i = i + 1
#                 j = 0 
#                 a = ''
#                 while j < i:
#                     space = '\t'
#                     j = j + 1
#                     a = f'{j}*{i}={i*j}'
#                     if j == i:
#                         space = '\n'
#                     file2.write(a + space)
#     except IOError:
#         print('文件写入时发生错误，请稍后重试')
#     finally:
#         file2 and file2.close()
# multiplication_table()


# 二进制文件的读写  而进入模式为b
# 读取：mode='rb'
# 写入：mode='wb'
# def image_handle(path=''):
#     image_file = open(path,'rb')
#     image = image_file.read()

#     image_file = open(r'C:\Users\13521\Desktop\new_image.jpg','wb')
#     image_file.write(image)
# image_handle(r'C:\Users\13521\Desktop\U想家测试临时用图_0509\综合活动 + 分享\750X630.jpg')


# 读写JSON，JSON是纯文本内容 C:\Users\13521\Desktop\Python\-\pythonModule\file3.json
# json.loads() 将json字符串转换为Python对象(数组)
# json.dump(参数1(保存的数据), 参数2(文件), 参数3(ensure_ascii=False 不进行编码)) 将Python对象保存到json文件中
# json.dumps() 将Python对象转换成JSON字符串

# 序列化 ：将对象转换成方便传输的JSON字符串
# 反序列化：将字符串转换成对象

# import json
# mydict = {
#     'name': '骆昊',
#     'age': 38,
#     'qq': 957658,
#     'friends': ['王大锤', '白元芳'],
#     'cars': [
#         {'brand': 'BYD', 'max_speed': 180},
#         {'brand': 'Audi', 'max_speed': 280},
#         {'brand': 'Benz', 'max_speed': 320}
#     ]
# }
# print('哈哈',json.dumps(mydict))

# def json_handle():
#     # 读取
#     file3 = open(r'C:\Users\13521\Desktop\Python\-\pythonModule\file3.json',mode='r',encoding='utf-8')
#     file3_data = file3.read()

#     # 写入
#     file4 = open(r'C:\Users\13521\Desktop\Python\-\pythonModule\file4.json',mode='w',encoding='utf-8')
#     # file4.write(file3_data)
#     json.dump(mydict,file4,ensure_ascii=False)
#     file4 = open(r'C:\Users\13521\Desktop\Python\-\pythonModule\file4.json',mode='r',encoding='utf-8')
#     print(file4.read())


#     # 将json数据转换为Python对象
#     # for x in json.loads(file3_data)['data']['list']:
#     #     print(x['ProjectName'])
#     file3 and file3.close()
#     file4 and file4.close()
# json_handle()


# os模块
import os 
# 当前目录 (根目录路径)
now_path = os.getcwd()
print('当前路径',now_path)

# 当前路径下的所有文件
# os.listdir(文件夹路径)
list = os.listdir(os.getcwd())
print('当前路径下的所有文件',list)
for x in list:
    pass 
    # print(f'{now_path}\\{x}')

# 绝对路径  .表示当前    ../表示上一级     ./视频学习 表示下级目录
print('绝对',os.path.abspath('./视频学习'))

# 查看路径的 "文件夹和文件名部分" 元组类型
# 例：c:\Users\13521\Desktop\Python\- (这里是文件夹)    7：面向对象高级编程 (这里是文件名)
# 返回一个元组，第一位是文件夹名称   第二位是文件名称
print('文件夹和文件名',os.path.split(r'c:\Users\13521\Desktop\Python\-\7：面向对象高级编程'))
print('文件夹和文件名',os.path.split(r'c:\Users\13521\Desktop\Python\-\.git'))

# 获取路径的 "文件夹部分"
print('路径的文件夹部分',os.path.dirname(r'c:\Users\13521\Desktop\Python\-\7：面向对象高级编程'))

# 获取路径的 "文件名"
print('路径的文件名称',os.path.basename(r'c:\Users\13521\Desktop\Python\-\7：面向对象高级编程'))


# 文件时间
# 最后修改时间
print(os.path.getmtime(r'C:\Users\13521\Desktop\Python\-\pythonModule\file4.json'))
# 最后的访问时间
print(os.path.getatime(r'c:\Users\13521\Desktop\Python\-\7：面向对象高级编程'))
# 创建时间
print(os.path.getctime(r'c:\Users\13521\Desktop\Python\-\7：面向对象高级编程'))


# 查看文件大小，文件夹会返回0
# 单位：byte(字节)
print('文件大小',os.path.getsize(r'C:\Users\13521\Desktop\Python\-\pythonModule\file3.json'))


# 练习 查找目录下的最新文件
# sorted 从小到大，所以要反序
list = os.listdir(os.getcwd() + '\其他：Python100天')
# print(list)
list = sorted(list, key=lambda x: os.path.getmtime(f'{os.getcwd()}\其他：Python100天\{x}'), reverse=True)
print('列表',list)
for x in list:
    path = f'{os.getcwd()}\其他：Python100天\{x}'
    # print(path)
    # print(os.getcwd() + '\\' + x)
    print(os.path.getmtime(path))

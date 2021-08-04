import random
import time
import os
import sys

# s1 = 'hello, world!'
# s2 = "hello, world!"
# # 以三个双引号或单引号开头的字符串可以折行
# s3 = """
# 第一行
# 第二行
# 第三行
# """
# print(s1, s2, s3, end='')

# s4 = "\\hello"
# s5 = r"\\hello"
# print(s4,s5)

# s1 = r'\'hello, world!\''
# s2 = r'\n\\hello, world!\\\n'
# print(s1, s2, end='')


# str1 = "hello world"
# 字符串的长度
# print('字符串的长度',len(str1))
# # 首字母大写拷贝
# print('首字母大写',str.capitalize(str1))
# # 每个单词的大写拷贝
# print('每个单词的大写拷贝',str.title(str1))

# str1.find('x') ：查询指定字符在str1内的索引，查询不到返回-1
# str1.index('x')：查询指定字符在str1内的索引，查询不到会报错(不建议)

# str1.startswith('x') : 查询当前字符串是否以指定字符 "开头" => 返回True / False
# str1.endswith('x') : 查询当前字符串是否以指定字符 "结尾" => 返回True / False

# 格式化字符串 %d：整数 %f：小数 %s：字符串
# print('%s %s'%('哈哈','呵呵'))
# # 格式化字符串  参数不需要关注数据类型
# print('{0} {1} {2[name]}'.format(1,2,{'name':'哈哈'}))
# # f字符串格式化
# name,age = ('张三',20)
# print(f'{name}今年{age}岁')
# name,age = '李四',18
# print(f'{name}今年{age}岁')


print('列表------------')
list1 = [3, 5, 1, 7, 2]
# 列表乘法计算，n个相同的列表拼装在一起
list2 = list1 * 3

# 列表加法计算，列表元素加到一起，按照加号的前后顺序添加到同一个列表内
list3 = list1 + list1

# 下表索引，不存在的索引会报错
# 下表0标识从头开始的第一位，下标-1表示从尾部开始的第一位(-2尾部第二位，依此类推)
list1[2]
list1[-1]
list4 = sorted(list1, key=lambda x: x)
list5 = sorted(list1)

# 列表清空 clear() 原始数据直接被清除
list5.clear()


print('生成式 / 生成器--------------')

# getsizeof 占用内存 sys.getsizeof()
# 生成式 -> 直接生成列表容器，列表元素也准备好了，比较耗费内存
f1 = [x for x in range(0, 10)]
f2 = [x + y for x in 'ABCDE' for y in '1234567']

# 生成器 -> 生成的是一个生成器对象，占用空间极小，数据在运算时得到(相对耗时)
f3 = [x for x in range(10000000)]
f4 = (x for x in range(10000000))

# generator函数 返回一个 generator


def f5(list):
    for x in list:
        if x > 1:
            yield x


f6 = f5(list1)
for x in f6:
    pass

print('元组---------')

# 元组(tuple)
# 使用 tuple()函数可以转换成元组
# 优点1：相对于列表占用空间更小
# 优点2：元组不可更改，相对更安全
# 优点3：函数有多个返回值可以使用元组
y1 = (1, 2, 3, 4, 5)


def getName(fullName):
    firstName = fullName[0:1]
    lastName = fullName[1:]
    return (firstName, lastName)


firstName, lastName = getName('张加乐')


print('使用集合-------------')

# 集合是key的集合，集合内相同的key会被去重
set1 = {1, 2, 3, 3, 3, 2}
# add 添加
set1.add(10)
# remove 移除
set1.remove(3)
# update 更新，类似于add，但是添加的值是一个可遍历的 Iterable
set1.update([11, 12])
set1.update((13, 14))
# discard和remove类似，但是remove一个不存在的key会报错，discard不会报错
set1.discard(20)
set1.remove(11)
# 交集  两个集合内都有的数据集合
# 并集  两个集合内所有数据的集合(相同的数据去重)
# 差集  前一个 减 后一个  前一个集合内有但是后一个集合内没有的
set2 = {1, 2, 3, 4}
set3 = {5, 6, 7, 8, 1, 2}
set4 = set2 & set3
set5 = set2 | set3
set6 = set2 - set3
# print('交集',set4)
# print('并集',set5)
# print('差集',set6)


print('字典-----------------')

# 字典创建1：字面量
item1 = {'name': '张三', 'age': 20}
# 字典创建2：构造器语法
item2 = dict(name='李四', age=30)
# 字典创建3：dict([元组,元组]) 每个元组内只能有两个元素，不然会报错 (dictionary update sequence element #0 has length 4; 2 is required)
item3 = dict([('name', '张三'), ('age', 20)])

# zip()：将多个可迭代的对象作为参数，将对象内的元素打包成元组 => 返回多个元组组成的列表
item7 = zip([1, 2, 3], [4, 5, 6])
item8 = zip([1, 2, 3], (4, 5, 6))
item9 = zip([1, 2, 3], '456')

# 练习1 跑马灯
# os.system('cls') 清除屏幕


def main1(str):
    index1 = 0
    content = ''
    # 遍历歌词
    for x in str:
        os.system('cls')
        content = content + str[index1]
        print(content)
        index1 = index1 + 1


# 随机数 https://www.runoob.com/python/func-number-random.html
# 练习2 生成指定长度的密码，由于大小写和数字构成
# randint(起始,结束) 随机整数 前后都是闭区间(包含前后的起始 结束位)
# choice(字符串) 在指定的字符串内随机返回
# sample(字符串,数量) 指定字符串内生成多个随机值
def generate_code(length=6):
    allStr = '0123456789'
    code = ''
    for _ in range(6):
        index = random.randint(0, len(allStr)-1)
        # code = code + allStr[index]
        code = code + random.choice(allStr)
    return code


print('验证码1', generate_code())
print('验证码2', generate_code())
print('验证码3', generate_code())
print('验证码4', generate_code())
print('验证码5', generate_code())


# 练习3：设计一个函数返回给定文件名的后缀名。
# str.rfind(字符) 返回字符串中最后一次出现的索引
def get_suffix(fileName):
    index = fileName.rfind('.')
    file = '格式错误'
    if index > 0:
        file = fileName[index:]
    return file


print(get_suffix('a.jpg'))
print(get_suffix('aaa'))

# 练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。
# 方法1：列表从大到小排序，查询列表的长度，大于1的就取后两位 等于1的就取第一位 小于1的默认0
# 方法2：列表从大到小排序，截取列表最后两位，reduce累加
def max2(list):
    listLength = len(list)
    max1 = 0
    max2 = 0
    if listLength > 0:
        list = sorted(list)
        print('列表',list)
        if listLength > 1:
            max1 = list[-1]
            max2 = list[-2]
        else:
            max1 = list[0]
            max2 = 0
    return (max1,max2) 
print('最大值',max2([1,4,6,9,33]))

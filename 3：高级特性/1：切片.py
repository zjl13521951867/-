# https://www.jianshu.com/p/15715d6f4dad => 切片常规操作
# 切片：取一个list或tuple的部分元素
# [0:2] 表示从0开始截取，截取到2为止(但不包括2)
# [-1:] 倒数第一个元素 -2表示倒数后两位，依次类推
# [0:10:5] 5代表间隔多少位截取一个
# [:] 没有截取的前后位置等于复制一个list/tuple => 浅拷贝
# [::] 从左向右 => 从头切到尾巴
# [::-1] 从右向左 => 从尾巴切到头

'''
1：切单个 [1] [-1]
2：窃完整对象 [::]  [::-1]
3：
'''




# list和tuple一样都可以进行切片操作，但是tuple截取后还是tuple
# nameList = ['张三','李四','王麻子','二狗子']
# print(nameList[0:2])
# print(nameList[-3:])

# 0-99一共100个
# list = range(100)
# print(list[0:10])
# print(list[-10:])

# 间隔取值
def listHandle(list):
    for x in list:
        print(x)
# listHandle(list[0:10:2])
# listHandle(list[:])

# 字符串截取
def trim(s):
    if not isinstance(s,(str)):
        print('请输入字符串')
    else:
        first = s[0:1]
        if first == ' ':
            s = s[1:]
        last = s[-1:]
        if last == ' ':
            s = s[0:len(s) -1]
        return s

# 测试:
if trim('hello ') != 'hello':
    print('测试失败1!')
elif trim(' hello') != 'hello':
    print('测试失败2!')
elif trim(' hello ') != 'hello':
    print('测试失败3!')
elif trim(' hello  world ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('  ') != '':
    print('测试失败6!')
else:
    print('测试成功!')


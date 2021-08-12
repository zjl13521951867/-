# 转换大小写，调用不会修改本身，会返回一个新字符串
str = 'abcd'
str = str.upper()
str = str.lower()
# print(str)

# 只要字符串中含有字母 且 字符串中的字母都是大写或者小写，返回True
# isupper()  islower()
str = '123abc' # True 
str = '123abC' # False 
# print(str.islower())

# str.isalpha()返回 True，如果字符串只包含字母，并且非空；
str = 'abc1' # False
str = 'abc' # True

# str.isalnum()返回 True，如果字符串只包含字母和数字，并且非空；
# 只有数字或者字母
str = 'abc' # True
str = 'abc2' # True 
str = '222' # True 
str = '222!' # False 

# str.isdecimal()返回 True，如果字符串只包含数字字符，并且非空；
# 纯数字
str = '123'
str = '123a'
# print(str.isdecimal())

# 字符串方法 startswith(str)和 endswith(str)
# 是否以指定的字符串开头或者结尾，是返回True
str = 'abc 123'
# print(str.startswith('a'))
# print(str.endswith('123'))

# join() 连接字符串列表
# 列表间以默认字符串连接
str = '*'
list = ['哈哈','呵呵','嘻嘻']
str = str.join(list) # 哈哈*呵呵*嘻嘻

# split() 将字符串按照指定字符分割成字符串列表
str = '哈哈*呵呵*嘻嘻'
list = str.split('*')
print(list)
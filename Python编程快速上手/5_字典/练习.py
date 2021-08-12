# 1．空字典的代码是怎样的？
a = {}

# 2．一个字典包含键'fow'和值 42，看起来是怎样的？
b = {'fow':42}

# 3．字典和列表的主要区别是什么？
# 列表：有序、索引取值
# 字典：无序、通过key取值

# 4．如果 spam 是{'bar': 100}，你试图访问 spam['foo']，会发生什么
spam = {'bar': 100}
# print(spam['foo']) # KeyError

# 5．如果一个字典保存在 spam 中，表达式'cat' in spam 和'cat' in spam.keys()之间的区别是什么？
# 没区别，都是检查当前key是否在spam字典中

#6．如果一个字典保存在变量中，表达式'cat' in spam 和'cat' in spam.values()之间的区别是什么？
# 前者检查spam中是否又'cat'这个key， 后者检查spam中是否有 'cat'这个value

# 7．下面代码的简洁写法是什么？
if 'color' not in spam:
    spam['color'] = 'black'
spam.setdefault('color','black')

# 


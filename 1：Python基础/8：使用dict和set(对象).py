# dict字典 key-value
# 读取 d['key']
# 添加 d['key'] = value

d = {'bob':20,'tom':50}
d['张三'] = 200
# print(d['bob'])
# print(d['张三'])

# key值不存在会报错
# 避免方法1：in方法判断key是否存在，不存在返回False
# 避免方法2：get('key',指定的返回值)函数判断，默认返回值为None

# print('lisi' in d)
# print('bob' in d)
# print(d.get('tom'))
# print(d.get('lisi',False))


# 删除指定的key pop('key')
# print(d)
# d.pop('tom')
# print(d)


# set()
# key的集合，但是不存储value
# add(key)：添加新的key，重复添加的key不会生效 (操作不存在的key会报错)
# remove(key)：删除指定key
# s1 = set([1,2,3,4,1])
# s1.add(6)
# s1.remove(3)
# print(s1)

# set 计算集合的交集并集
s3 = set([1,2,3,4])
s4 = set([3,4,5,6])

# 交集 两个集合中都存在的
print(s3 & s4)
# 并集 两个集合合并，相同的去重
print(s3 | s4)
# 差集
print(s4 - s3)



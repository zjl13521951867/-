person = {'name':'张三','age':20,'gender':'男'}

# 字典中所有key的遍历
for k in person.keys():
    pass 
# 字典中所有value的遍历
for v in person.values():
    pass 
# 字典中所有键值对的遍历key-value
for item in person.items():
    pass 


# 检查字段中是否存在key或value in   not in
# 直接写是检查key是否存在于字典中
# print('name' in person)
# print('address' in person)
# 返回值是一个不可修改的列表，可以通过list()转换成列表格式
value_list = person.values()
key_list = person.keys()
items = person.items()
# print(20 in value_list)
# print(key_list)
# print(items)


# 获取某个key的值，可以设置默认值，不存在的key就会返回默认值
# get(key,defaultValue)
# print(person.get('name'))
# print(person.get('address','北京市'))

# 给一个不存在的键设置默认值
# setdefault()
person.setdefault('name','2000')
person.setdefault('address','上海')
# print(person)

# 字典格式化打印
import pprint
pprint.pformat(person)


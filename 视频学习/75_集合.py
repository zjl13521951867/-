# 列表去重，可以将列表转换成set直接就去重了，然后再转换成list

# 添加方法
# add()
# update() 参数可以是列表，可以是元组、可以是dict(字典 字典会将key添加到集合中，value不会添加)

# 删除方法
# pop() 随即删除一个，删除的作为返回值
# clear() 清空集合
# remove(项) 删除集合内的指定项


s1 = {1,2,3,4,5,'六','七'}
# print(s1,type(s1))

l1 = [1,2,3,1,2,4,5]
# print(l1,type(l1))

s2 = set(l1)
print(s2,type(s2))

l1 = list(s2)
print(l1,type(l1))
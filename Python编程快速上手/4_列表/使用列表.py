# sort排序 默认从小到大，reverse=True表示反转数组
spam = [2, 5, 3.14, 1, -7]
spam.sort(reverse=True)
# print(spam)


'''
数据传递：
    可变数据
        数据的修改'不会'改变对象再内存中的指向
        数据重新赋值'会'改变对象再内存中的指向
    不可变数据
'''

# 数据改变对象的指向不会变，数据重新赋值后对象的指向被改变了
# list = [1,2,3]
# print(id(list)) 

# list[1] = 10 
# print(id(list))

# list = [5,6,7]
# print(id(list))


# copy()：浅拷贝  
# deepcopy()：深拷贝
from copy import copy,deepcopy
list = [1,2,3,[4,5]]
list1 = copy(list)

# 浅拷贝指挥复制数据的第一层，
# 例如列表，如果列表内的某个数据也是列表或者字典，那么就直接继承原数据的，修改这些数据原数据也会被修改数据
list1[0] = 100 
list[3][1] = 500
print(list)
print(list1)

# 深拷贝是完整的复制当前数据，不管多少层的数据都会完全复制下来
 

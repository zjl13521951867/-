# list
# len(list)获取数组长度
# list[index]获取数组某项
# 超出最大索引取值会报错(IndexError)
# 获取列表的最后一项 list[-1] -1倒数第一个  -2倒数第二个 以此类推，但是也不可以超出索引限制
list = [1,2,3]
print('数组长度',len(list))
print('数组第一项',list[0])
print('数组的最后一项',list[-1])
print('数组的最后一项',list[len(list)-1])

# 数组末尾添加 append(添加项)
list.append(4)
print('数组末尾添加',list)

# 数组指定位置添加 insert(索引,添加项)
list.insert(0,'哈哈')
print('数组指定位置添加',list)

# 数组末尾删除 pop()
list.pop()
print('末尾删除',list)

# 删除指定位置数组项
list.pop(0)
print('指定位置删除',list)

list[0] = '我被替换了'
print('替换',list)


# tuple有序数组
# 取值放视 tupleList[0] tupleList[1] tupleList[2]
# 值不可被修改
# 注意：如果只有1个元素的tuple(1,)必须要加逗号',' 当只有一个元素时，()当成数学公式的小括号使用，所以加逗号来区分
tupleList = ('第一','第二','第三')
print('tuple有序数组',tupleList)

# tuple也并非完全不可变
# 定义的tuple数组内有 list，修改list的数组项
tupleList2 = (1,2,3,[4,5])
print('tupleList2',tupleList2)
tupleList2[3][0] = '第一'
tupleList2[3][1] = '第二'
print('tupleList2',tupleList2)

a = [1,2,3]
print('a=',a)
a = tuple(a)
print(a)

b = (1,3)
print('b=',list(b))



stus = ['孙悟空','猪八戒','沙和尚','唐僧','蜘蛛精','白骨精']

# 切片[开始:结束:不常]
# 正常切片
stu1 = stus[0:3]
# 全复制
stu1 = stus[:]
# 反转 reverse()方法也可以实现反转
stu1 = stus[::-1]


# 列表的通用操作
list1 = [1,2,3]
list2 = [4,5,6]
# 列表相加 => 两个列表组合成一个和列表
list3 = list1 + list2 
# 列表乘法运算 => n个列表组合成一个列表
list3 = list1 * 3 
# in not in => 检查指定元素是否在列表内 返回True/False
1 in list3 # True
8 in list3 # False
# len() => 查询列表内元素的个数
len(list3) # 9 
# max() min() => 返回数组中的最大值/最小值
max(list3) # 3 
min(list3) # 1
# 方法1：list.index(item,start,end) => 查找列表中的指定元素首次出现的位置，返回对应的索引，参数2和3表示在指定索引区间内查找(2 3选填参数)
list3.index(1,0,3)
# 方法2：list.count(item) => 查询指定项在列表内的出现次数
list3.count(1)



print(list3)
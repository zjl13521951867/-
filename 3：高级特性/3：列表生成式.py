# 列表生成器
# (x*x)生成的元素  (for x in range(1,11)) 循环产生数组  (if x % 2 == 0) 条件判断，符合条件的才会进入list内
# for后面的if条件是筛选条件，不可以加else，
# 类似三元运算  True执行这里 if a > b else False执行这里
# for前面if的控制x的结果，for后面的if控制整个列表的结果
list = [x * x for x in range(1,11) if x % 2 == 0]
print(list)

# 双层列表
list2 = [m + n for m in 'ABC' for n in 'EFG']
print(list2)

# 获取当前文件夹内的所有目录
import os 
list3 = [d for d in os.listdir('.')]
print(list3)

list4 = ['A','B','C']
list5 = [s.lower() for s in list4]
print('大小写',list5)

# True执行if前的 False执行else后的
list6 = [x if x > 5 else -x for x in range(1,11)]
print(list6)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x,(str))]
print(11111,L2)
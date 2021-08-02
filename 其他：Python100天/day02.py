# 语言元素
# 变量和类型
# 1：整数
# 2：浮点(小数)
# 3：布尔
# 4: 字符串

# 数据类型检查 type()
a = 100
b = 10.1
c = True
d = '哈哈'
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

# 数据类型转化
# int() 将一个数值或字符串转换成整数，可以指定进制，若需要添加进制参数，则第一个参数需要是字符串
a1 = int('20',10)
print('a1',a1 // 3)

# float()：将一个字符串转换成浮点数
b1 = float(2)
print('b1',b1)

# str(): 将指定的对象转换成字符串形式，可以指定编码
c1 = str(12)
print('c1',c1)

# 与和或 -- and和or
print(True & True)
print(True | False)

# is is not(比较内存地址) 和 == !=(表述数据值) 
# 如变量指向不可变类型，两者相同
# 如果变量指向可变类型(list dict)
print('is',2 is 2)

# in not in (检查当前元素是否在列表内)
list = [1,2,3]
print('在不在',1 in list) 
print('在不在',10 in list) 

# 练习1 华氏温度转换为摄氏温度 (华氏温度到摄氏温度的转换公式为：$C=(F - 32) \div 1.8$。)
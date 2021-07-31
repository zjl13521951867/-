# ord()函数，对 "单个" 字符进行编码
# print(ord('好'))
# # char()函数，将编码转换成字符
# print(chr(22909))


# encode()编码
# 纯英文可以使用ascii编码成byte，但是带有中文的只可以使用utf-8编码成byte
# 网络传输和硬盘存储只能使用字节存储
# 问：中文为什么不可以用ascii编码？中文超过了ascii编码的最大长度
# 解码是遇到可能会碰到无法解码的字符，少量字符可以忽略 decode(解码方式,errors='ignore')
# print('ABC'.encode('ascii'))
# print(b'ABC'.decode('ascii'))
# print('ABC'.encode('utf-8'))
# print(b'ABC'.decode('utf-8'))
# print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))


# %d 整数 (小数的话也是自动取整) 
# %f 小数 (默认保留6位,即时是整数也会保留)
# %s 字符串 (自动转换未字符串)
# print('我有%f万，我是个%s人' %(100,23))


# 字符长度
# 英文的一个字符为1字节，中文一个字符3字节
# 字节和字符的相互转换 常用的就是utf-8编码
# a = '魑魅魍魉'
# b = 'b'
# print('字符长度',len(b))
# print('字节大小',len(b.encode('utf-8')))

# 格式化
# name = '张加乐'
# age = 20 
# print('%s今年%d岁' %(name,age))
# print(name+'今年'+str(age)+'岁')

# format 
# print('hello,{0}成绩提升了{1:.3f}%'.format('小红',12.52323))

# f-string
# name = '小王'
# score = 12.3556
# print(f'{name}成绩提升了{score:.2f}%')

# name = '小明'
# score1 = 72
# score2 = 85
# score = ((score2 / score1) - 1) * 100 
# print(f'{name}成绩提高了{score:.1f}%')
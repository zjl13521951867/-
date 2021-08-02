# 循环结构
# 1: for in 循环

# 练习1 九九乘法表
for i in range(1,10):
  for j in range(1,i+1):
    pass 
    #print('%d*%d=%d' % (i, j, i * j), end='\t')
  # print()


# 输出*组成的不同图形
def star1(row):
  for r in range(row):
    print((r+1) * '*')
star1(5)

def star2(row):
  for r in range(row):
    print((row -(r+1)) * ' '+(r+1)*'*')
star2(5)

def star3(row):
  s = -1
  for r in range(row):
    s = s + 2 
    print((row-r)* ' ' + s * '*')
star3(5)
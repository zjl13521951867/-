# 练习1 寻找水仙花
def getFlower(flowerList):
  for flower in flowerList:
    bai = flower // 100 
    shi = (flower // 10)%10
    ge = flower % 10 
    if (bai ** 3 + shi ** 3 + ge ** 3) == flower:
      pass 
      # print('水仙花',flower)
getFlower(range(100,1000))

# 练习2 百钱百鸡
for x in range(0,20):
  for y in range(0,33):
    z = 100 - x - y 
    if (5*x + 3*y + z/3) == 100:
      pass 
      # print('公鸡%d 母鸡%d 小鸡%d'%(x,y,z))
      # print(f'公鸡{x} 母鸡{y} 小鸡{z}')


# 斐波那契数列 -  两个数都是1，从第三个数开始，每个数都是它前面两个数的和
list = []
for x in range(0,20):
  # 第三位开始累加
  if x > 1:
    now = list[x -1] + list[x-2]
    list.append(now)
  else:
    now = 1
    list.append(now)
print('数组',list)



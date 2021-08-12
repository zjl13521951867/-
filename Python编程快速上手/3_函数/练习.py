# 如果参数是偶数，那么 collatz()就打印出 number // 2，并返回该值。如果 number 是奇数，collatz()就打印并返回 3 * number + 1。
def collatz(number):
    '''
        number:int  
    '''
    if number % 2 == 0:
        number = number // 2
    else:
        number = number * 3 + 1
    print(number)
    return number 

# number = 420 
# while True:
#     number = collatz(number)
#     if number == 1:
#         break


# 
try:
    number = input('请输入一个整数')
except ValueError:
    print('输入有误')

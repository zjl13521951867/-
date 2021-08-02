# filter(fun(x),Iterable) 过滤
# 重点1：返回值为可用 next()的 Iterator
# 重点2：原始数据不会被修改
a = [1,2,3,4]
def delete(x):
    return x > 3
b = filter(delete,a)
print(a)
print(b)
print(list(filter(delete,a))) # []
for x in b:
    print('哈哈',x)

# 练习 filter删选回数
def is_palindrome(x):
    if str(x) == str(x)[::-1]:
        return x 
c = filter(is_palindrome,range(1,200))
print(list(c))

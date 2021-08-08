# 非布尔值的逻辑运算符比较，返回的是原值
# and：与运算找False，任意一个不符合就是返回False，第一个值为False直接返回第一个值，第一个值为True则直接返回第二个
# or：与或找True，任意一个为True就返回True，第一个值为True直接返回第一个值，第一个值为False则直接返回第二个

a = 1 and 0 
a = 1 and 2 
if a:
    print('成立')
else:
    print('不成立')

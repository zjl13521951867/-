# 条件判断语句（if语句）
# 语法：if 条件表达式 : 
#           代码块
# 执行的流程：if语句在执行时，会先对条件表达式进行求值判断，
#   如果为True，则执行if后的语句
#   如果为False，则不执行
# 默认情况下，if语句只会控制紧随其后的那条语句，如果希望if可以控制多条语句，
#   则可以在if后跟着一个代码块
# 代码块
#   代码块中保存着一组代码，同一个代码块中的代码，要么都执行要么都不执行
#   代码块就是一种为代码分组的机制
#   如果要编写代码块，语句就不能紧随在:后边，而是要写在下一行
#   代码块以缩进开始，直到代码恢复到之前的缩进级别时结束
#   鲁迅说过：
#       世上本来没有路，走的人多了自然就有了！
#       xxxx
#   yyyy....
# 缩进有两种方式，一种是使用tab键，一种是使用空格（四个）
#   Python的官方文档中推荐我们使用空格来缩进
#   Python代码中使用的缩进方式必须统一
#   "translate_tabs_to_spaces": true,     

# if False : print('你猜我出来么？')

num = 10
# if num > 10 : print('num比10大！')
# print('谁也管不了我')

if False :
    print(123)
    print(456)
    print(789)
    print(101112)
# print('hello')

num = 28

# 可以使用逻辑运算符来连接多个条件，
#   如果希望所有条件同时满足，则需要使用and
#   如果希望只要有一个条件满足即可，则需要使用or
# if num > 10 and num < 20 :
#     print('num比10大,num比20小！')

# if 10 < num < 20 :
#     print('num比10大,num比20小！')

# 在命令行让用户输入一个用户名，获取用户输入，并进行判断
# 如果用户输入的用户名是admin，则显示欢迎管理员光临
# 如果用户输入的是其他的用户名，则什么也不做
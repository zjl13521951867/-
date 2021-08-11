'''
    文件操作方式：
        r：读取
        w：写入，覆盖原文件
        x：新建文件写入，如果文件名存在则报错
        a：追加写入，会添加在当前文件的原内容后面

    模式：需要配合操作方式使用
        t：文本模式(默认模式可以不写)
            rt 文本模式读取
            wt 文本模式写入
            ...
        b：二进制模式(读取图片 音频 视频...)
            rb 读取二进制文件
            wb 写入二进制文件
        
        +：用于读取和写入
            r+ 读取和写入，但是打开文件时"不会清空"当前文件
            w+ 读取和写入，打开文件后当前文件的内容会被"清空"
'''


import os 
# f1 = ''
# try:  
#     f1 = open(rf'{os.getcwd()}\pythonModule\file2.txt',mode='r+',encoding='utf-8')
#     f1_text = f1.read()
#     print(f1_text)

# finally:
#     f1 and f1.close()

with open(rf'{os.getcwd()}\pythonModule\file2.txt',mode='w+',encoding='utf-8') as f1:
    pass 
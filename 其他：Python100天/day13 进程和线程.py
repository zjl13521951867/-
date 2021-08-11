'''
多线程的优势：
    1：多个线程同时进行，减少了功能(代码)的运行时间
    2：锁的用处是多个人操作同一个状态 例：多个人取钱，但是银行的总额是固定的，所以需要加锁逐个处理
'''





from random import randint
from time import time, sleep

# 默认模式，每次下载完才能下载另一个
# def donload_task(file_name):
#     print(f'开始下载 {file_name}...')
#     sleep_time = randint(5,10)
#     sleep(sleep_time)
#     print(f'下载 {file_name} 花费了 {sleep_time}秒')

# def main():
#     star = time()
#     donload_task('功夫.mkv')
#     donload_task('蜡笔小新.gif')
#     end = time()
#     print('一共花费了 %d 秒'%(end-star))
# main()



'''
1：多进程的优点就是，多个任务同时进行，减少程序的等待时间
2：多进程的代码需要执行在  if __name__ == 'main'内
3：Process(target=fn, args=(参数元组))，返回一个进程对象
    进程对象.star()开始执行此进程
    进程对象.join()，join后的代码会等到当前进程 '执行完成' 再执行
'''
# from multiprocessing import Process
# from os import getpid, startfile
# from random import randint
# from time import time, sleep

# def download_task(file_name):
#     print(f'正在下载 {file_name}...')
#     print(f'当前进程号 [{getpid()}]')
#     donload_time = randint(5,10)
#     sleep(donload_time)
#     print(f'下载 {file_name} 用了 {donload_time}秒')
# def main():
#     start = time()
#     p1 = Process(target=download_task, args=('Python从入门到住院.pdf', ))
#     p1.start()
#     p2 = Process(target=download_task, args=('Peking Hot.avi', ))
#     p2.start()
#     p1.join()
#     p2.join()
#     end = time()
#     print('总共耗费了%d秒.' % (end - start))
# if __name__ == '__main__':
#     main()



'''
1：线程
2：Thread(target=fn, args=(元组参数,)) 返回线程对象
    线程对象.start() 开始执行此进程
    线程对象.join() 等线程的代码执行完成才执行join()方法下的代码
3: 线程的run()方法，线程在生成后会自动执行run()函数，所以写子类的时候会有个run()函数

4：锁
    当我们多个线程操作同一个数据时，这个数据就有可能会发生混乱
    在操作数据前需要加上锁，在操作完成后解锁，下一次操作会在上一次操作解锁后再进行
'''
# from random import randint
# from threading import Thread
# from time import time, sleep

# def download_task(file_name):
#     print(f'正在下载 {file_name}...')
#     donload_time = randint(5,10)
#     sleep(donload_time)
#     print(f'下载 {file_name} 用了 {donload_time}秒')
# def main():
#     start = time()
#     p1 = Thread(target=download_task, args=('Python从入门到住院.pdf', ))
#     p1.start()
#     p2 = Thread(target=download_task, args=('Peking Hot.avi', ))
#     p2.start()
#     p1.join()
#     p2.join()
#     end = time()
#     print('总共耗费了%d秒.' % (end - start))
# if __name__ == '__main__':
#     main()


'''
原版100个账号向银行内存钱：
    线程的代码时同时进行的，所有线程拿到的初始化余额都是0，每个账户都时往0上 +1，最终得到的就只能是1
'''
# from time import sleep
# from threading import Thread,Lock 

# class Account(object):
#     # 初始化余额为0
#     def __init__(self):
#         self._blance = 0
#         self._lock = Lock()

#     # 计算金额
#     def deposit(self,money):
#         # 先获取锁才能执行后续的代码
#         #self._lock.acquire()
#         # try:
#         # 当前金额
#         new_blance = self._blance + money 
#         # 模拟银行的存款时间
#         sleep(0.0001)
#         # 存款过后重置余额
#         self._blance = new_blance

#         print('当前',self._blance)
#         #self._lock.release()
#         # finally:
#         #     # 释放锁
#         #     self._lock.release()
#     # 获取存款余额
#     @property
#     def blance(self):
#         return self._blance

# class AddMoney(Thread):
#     def __init__(self,account,money):
#         super().__init__()
#         self._account = account
#         self._money = money
    
#     def run(self):
#         self._account.deposit(self._money)

# def main():
#     account = Account()
#     threads = []

#     for _ in range(100):
#         t = AddMoney(account,1)
#         threads.append(t)
#         t.start()
        
#     for t in threads:
#         t.join()
#     print('账户余额',account.blance,'元')



'''
两个人同时从银行取钱，银行一共又1000元，大事难事两人分别取800

'''
from time import sleep
from threading import Thread,Lock 
count_money = 1000
def get_money(name,money):
    global count_money
    lock = Lock()
    lock.acquire()
    print(f'{name} 正在取钱')
    sleep(1)
    if count_money > money:
        count_money = count_money - money 
    else:
        print('余额不足')
    lock.release()
   

def main():
    t1 = Thread(target=get_money, args=('张三',800)) 
    t1.start()
    t2 = Thread(target=get_money, args=('王麻子',800,)) 
    t2.start()
    
    t1.join()
    t2.join()
    print('余额还有',count_money)




import time
import tkinter
import tkinter.messagebox

def download():
    # 模拟下载任务需要花费10秒钟时间
    time.sleep(10)
    tkinter.messagebox.showinfo('提示', '下载完成!')

def show_about():
    tkinter.messagebox.showinfo('关于', '作者: 骆昊(v1.0)')

def main():
    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()






if __name__ == '__main__':
    main()


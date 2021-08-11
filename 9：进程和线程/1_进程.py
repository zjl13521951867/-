from multiprocessing import Process,Pool 
import os 
from time import sleep,time 
'''
创建子进程时，只需要传入一个执行函数和函数的参数
    - 创建一个Process实例，用start()方法启动
    - join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。

批量生成进程：
    - Pool(n) 生成n个进程
    - 不需要通过star()来开启进程
    - 调用join()之前必须先调用close()
'''


def run_pro(name):
    print(f'name = {name}', os.getpid())
    sleep(2)

# 逐个生成
def main():
    start_time = time()
    p1 = Process(target=run_pro,args=(1,))
    p1.start()
    p2 = Process(target=run_pro,args=(2,))
    p2.start()
    p1.join()
    p2.join()
    end_time = time()
    print('执行完成','一共花费了 %d 秒'%(end_time - start_time))

# 批量生成
def main():
    p = Pool(5)
    for x in range(5):
        p.apply_async(run_pro,args=(x,))
    p.close()
    p.join()

if __name__ == '__main__':
    main()
    
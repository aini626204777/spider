from multiprocessing import Process
import os

def write_data(num):
    pass
if __name__ == '__main__':
    print('主进程开启',os.getpid())
    # 创建子进程
    """
    target=None,:设置进程要执行的函数
    name = NOne,:设置进程的名字
    args=():给进程执行的函数传参数（tuple类型）
    kwargs={}:给进程执行的函数传递参数
    """
    process1 = Process(target=write_data,args=(10,))

    # 使用start()启动进程
    process1.start()

    process1.join()

import threading, time
from threading import Thread

# def download_image(url,num):
#     time.sleep(5)
#     print(url,num)
#
#
# if __name__ == '__main__':
#     print('主线程开启',threading.currentThread().name)
#     thred = Thread(target=download_image,name='王小B',args=('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1545642426739&di=99dae605ea1fdf98aa6fdc589b5004d2&imgtype=0&src=http%3A%2F%2Fpic11.nipic.com%2F20101130%2F5653289_070500644000_2.jpg',))
#     # 启动线程
#     thred.start()
#
#     # 是否开启守护进程
#     # daemon:False,在主线程结束的时候，会检测子线程任务是否结束，
#     # 如果子线程中任务没有结束，则会让子线程正常结束任务
#     # daemon:True 在主线程结束的时候，会检测子线程任务是否结束，
#     # 如果子线程中任务没有结束，则会让子线程跟随主线程一起结束

# # 多线程执行
# # coding=utf-8
# import threading
# import time
#
#
# def saySorry():
#     # for i in range(5):
#     print("亲爱的，我错了，我能吃饭了吗？")
#     print('123')
#     time.sleep(1)
#
#
# def do():
#     for i in range(5):
#         print("亲爱的，我错了，我给你按摩")
#         time.sleep(1)
#
#
# if __name__ == "__main__":
#     for i in range(5):
#         td1 = threading.Thread(target=saySorry)
#         td1.start()  # 启动线程，即让线程开始执行
#         td2 = threading.Thread(target=saySorry)
#         td2.start()  # 启动线程，即让线程开始执行

# 主线程与子线程的执行顺序
# coding=utf-8
import threading
from time import sleep,ctime

def sing():
    for i in range(3):
        print("正在唱歌...%d"%i)
        sleep(1)

def dance():
    for i in range(3):
        print("正在跳舞...%d"%i)
        sleep(1)

if __name__ == '__main__':
    print('---开始---:%s'%ctime())

    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    # sleep(5) # 屏蔽此行代码，试试看，程序是否会立马结束？
    print('---结束---:%s'%ctime())
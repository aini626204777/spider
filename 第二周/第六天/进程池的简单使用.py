from concurrent.futures import ProcessPoolExecutor
import os, time

#
# def download_page_data(page):
#     print(page, os.getpid())
#     time.sleep(1)
#     return '请求成功'+ str(page),page
#
#
# # 进程执行的回调函数
# def download_done(futures):
#     result = futures.result()
#     print(result)
#
#     next_page = int(result[1])+1
#     handler = pool.submit(download_page_data,next_page)
#     handler.add_done_callback(download_done)
#
#
# if __name__ == '__main__':
#
#     # 创建进程池
#     # max_workers:设置进程池中的进程数量
#     pool = ProcessPoolExecutor(4)
#
#     for i in range(0, 201):
#
#         # fn：执行函数
#         # *args：给进程执行的函数传参数（tuple类型）
#         handler = pool.submit(download_page_data,i)
#         handler.add_done_callback(download_done)
#     # pool.shutdown()


# 方式二
from multiprocessing import Pool


def download_page_data(page):
    print(page, os.getpid())
    time.sleep(1)
    return '请求成功' + str(page), page

#
# def done(futures):
#     print(futures)


if __name__ == '__main__':

    # 创建进程池
    pool = Pool(4)
    for page in range(0, 200):
        # pool.apply_async():异步非阻塞添加任务
        # pool.apply()：同步的方式添加任务
        # func：要执行的函数
        # args=()：给函数传递的参数
        pool.apply_async(download_page_data, args=(page,))

    pool.close()
    pool.join()

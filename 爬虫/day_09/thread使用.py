import threading
import time
import requests


def download(url, url2):
    print(url, url2)
    # time.sleep(2)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0)'
    }
    response = requests.get('http://blog.jobbole.com/all-posts/', headers=headers)
    print(response.status_code)
    print(threading.current_thread().name)


def main():
    starttime = time.time()
    task_list = ['url1', 'url2', 'url3', 'url4', 'url5']
    # for url in task_list:
    #     download(url=url)

    # list存放你当前创建的线程对象
    thread_list = []
    for url in task_list:
        # 创建一个线程
        # target参数表示当前线程要执行的任务，name参数表示当前线程的名称，
        thread = threading.Thread(target=download, name='线程' + url, args=(url, url))
        # setDaemon如果设置为True,表示后台线程
        thread.setDaemon(True)
        # 默认是False，前台线程
        # thread.setDaemon(False)
        # 启动线程
        thread.start()
        task_list.append(thread)
    # thread子线程调用join()，表示告诉主线程，必须等我执行完毕，你才能结束
    for thread in thread_list:
        thread.join()

    print(threading.current_thread().name)
    endtime = time.time()

    print('耗时' + str(endtime - starttime))


if __name__ == '__main__':
    main()

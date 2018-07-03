#使用python3.2之后为我们封装的线程池
from concurrent.futures import ThreadPoolExecutor
import time
import threading
import requests
def get_data(url):
    print('开始下载'+url)
    print(threading.current_thread().name)
    # time.sleep(2)
    header = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0'
    }
    response = requests.get(url,headers=header) 
    # print(response.status_code)
    if response.status_code == 200:
        # return response.text,url
        return response.status_code,url

def done(future):
    #线程池执行设定任务结束后的结果参数
    print('下载完了'+ str(time.time()))
    response = future.result()
    print(response)


def main():
    #如何定义一个线程池(池子里面有三个创建好的线程，可以同时使用)
    #max_workers：这个参数是说，同时能够执行的最大的线程数
    srarttime = time.time()
    navalpool = ThreadPoolExecutor(20)
    chapterpool = ThreadPoolExecutor(20)
    #如何提交任务给线程池呢？
    for i in range(1,200):
        #submit: 表示将我们需要执行的任务给这个线程池，
        a = navalpool.submit(get_data,'http://www.baidu.com')
        #给线程池设置任务之后，可以设置一个回调函数，
        #作用是：当我们某个任务执行完毕之后，就会回调你设置的回调函数
        a.add_done_callback(done)

    navalpool.shutdown()

    endtime = time.time()
    #如何设置才能让主线程等待子线程任务结束再结束
    print(threading.current_thread().name)
    print(endtime-srarttime)

if __name__ == '__main__':
    main()




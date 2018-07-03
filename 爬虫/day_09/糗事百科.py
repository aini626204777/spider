# 多线程
import threading
# 请求模块
import requests
# 数据存储
import json
# 数据解析
from lxml import etree
# 队列
import queue


# https://www.qiushibaike.com/
# https://www.qiushibaike.com/8hr/page/2/


class ThreadCrawl(threading.Thread):
    def __init__(self, threadName, pageQueue, dataQueue):
        # 重写父类方法,
        # 多继承要这样写
        # super(ThreadCrawl, self).__init__()
        # 单继承这样写
        super().__init__()
        # 线程名称
        self.threadName = threadName
        # 下载任务队列
        self.pageQueue = pageQueue
        # 存放结果的队列，一开始为空
        self.dataQueue = dataQueue
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        }
        # print(self.threadName)

    # 重写父类的方法，目的是为了发起请求，拿到响应结果
    def run(self):
        # self
        while self.pageQueue.empty() != True:
            print('开启' + self.threadName)
            # 从任务队列里面拿页码
            page = self.pageQueue.get()
            # 拼接完整的url
            fullurl = 'https://www.qiushibaike.com/8hr/page/' + str(page) + '/'
            # 发起请求，获得响应结果
            response = requests.get(url=fullurl, headers=self.headers)
            print(response.status_code)
            if response.status_code == 200:
                self.dataQueue.put(response.text)
            # print(self.dataQueue,type(self.dataQueue))
            print('run起来')


class ThreadParse(threading.Thread):
    def __init__(self, threadName, dataQueue,lock):
        super(ThreadParse, self).__init__()
        # threadName线程名称
        self.threadName = threadName
        # 解析任务队列
        self.dataQueue = dataQueue
        self.lock = lock
    def run(self):
        print('解析' + threading.current_thread().name)
        # 解析获取的数据
        # 判断如果队列里面有值，则继续执行，从队列中获取页码源码进行解析
        while self.dataQueue.empty() != True:
            html = self.dataQueue.get()
            print('获取到数据了')
            self.parse(html)

    def parse(self, html):
        # 解析数据
        parse_data = etree.HTML(html)
        # 获取段子列表
        contentList = parse_data.xpath('//div[@id="content-left"]/div')
        for sub_div in contentList:
            # 取段子的发布者名字
            title = sub_div.xpath('.//h2/text()')[0]
            # 去段子的内容
            content = sub_div.xpath('.//div[@class="content"]/span/text()')[0]
            dict = {
                'title': title,
                'content': content,
            }
            print(dict)
            # 加锁（为了保证同一个资源，某一时刻只被一个线程执行）
            self.lock.acquire()
            # 使用json.dumps将python对象转换为一个json字符串
            with open('duanzi.json','a') as f:
                # ensure_ascii默认为True，是ascii编码，这里我们需要设置为False
                f.write(json.dumps(dict,ensure_ascii=False)+'\n')
            # 解锁（解锁后其他线程才能够使用
            self.lock.release()


# 主线程
def main():
    # 首先创建一个任务队列
    pageQueue = queue.Queue(30)
    # 创建一个数据队列，将获取到的请求结果，放在这个队列中
    dataQueue = queue.Queue()
    for i in range(1, 20):
        # 往任务队列中存需要请求的页码
        pageQueue.put(i)

    # 创建线程来获取网页的内容
    # 首先创建爬取任务线程的名称
    crawlThreadNames = ['crawl美女1号', 'crawl美女2号', 'crawl美女3号']
    threadcreaws = []

    for threadName in crawlThreadNames:
        thread = ThreadCrawl(threadName, pageQueue, dataQueue)
        thread.start()
        threadcreaws.append(thread)
        # print(threadcreaws)
    for thread in threadcreaws:
        thread.join()


    # 创建一个锁，为了同一个资源，某一时刻只被一个线程执行
    lock = threading.Lock()
    # 创建解析的线程名称
    parseThreadName = ['巨无霸1号', '巨无霸2号', '巨无霸3号']
    # 创建一个list，来存放所有解析线程
    threadParses = []
    for threadName in parseThreadName:
        parsethread = ThreadParse(threadName, dataQueue,lock)
        parsethread.start()
        threadParses.append(parsethread)

    for thread in threadParses:
        thread.join()


if __name__ == '__main__':
    main()

# 爬取雪球网的内容使用多线程
import requests
import re
import threading
import queue
import json

next_id = -1


class Thread_spider(threading.Thread):
    def __init__(self, threadName, pageQueue, dataQueue, id):
        super(Thread_spider, self).__init__()
        self.threadName = threadName
        self.pageQueue = pageQueue
        self.dataQueue = dataQueue
        self.id = id
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
            'Cookie': 'aliyungf_tc=AQAAADztpUb8+QMABlBbXd0IkVkwxM0E; xq_a_token=019174f18bf425d22c8e965e48243d9fcfbd2cc0; xq_a_token.sig=_pB0kKy3fV9fvtvkOzxduQTrp7E; xq_r_token=2d465aa5d312fbe8d88b4e7de81e1e915de7989a; xq_r_token.sig=lOCElS5ycgbih9P-Ny3cohQ-FSA; _ga=GA1.2.769241157.1528717598; _gid=GA1.2.219577195.1528717598; Hm_lvt_1db88642e346389874251b5a1eded6e3=1528717599; u=761528717601597; device_id=c6d7af88af8e6cdbc1482119cd6f468b; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1528719335'
        }

    def run(self):
        print('爬取' + threading.current_thread().name)
        page = self.pageQueue.qsize()
        for i in (0, page):
            fullurl = 'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=' + str(
                next_id) + '&count=10&category=' + str(self.id)
            response = requests.get(fullurl, headers=self.headers)
            if response.status_code == 200:
                self.dataQueue.put(response.text)
                print(json.loads(response.text)['next_max_id'])


class Thread_parse(threading.Thread):
    def __init__(self, threadName, dataQueue, lock):
        super(Thread_parse, self).__init__()
        self.threadName = threadName
        self.dataQueue = dataQueue
        self.lock = lock

    def run(self):
        print('解析' + threading.current_thread().name)
        while not self.dataQueue.empty():
            html = self.dataQueue.get()
            # print('获取到数据了')
            self.parse(html)

    def parse(self, html):
        parse_data = json.loads(html)
        # print(parse_data)
        data_list = parse_data['list']
        for data in data_list:
            string = data['data']
            str = json.loads(string)
            text = str['text']
            target = str['text']
            self.lock.acquire()
            with open('xueqiu.text', 'a') as f:
                f.write(text + ':' + target + '\n')
            self.lock.release()


def Spider_page(id):
    # 创建一个任务队列
    pageQueue = queue.Queue(40)
    dataQueue = queue.Queue()
    page = int(input('请输入爬取多少页内容'))
    for i in (0, page):
        pageQueue.put(i)
    # 创建一个爬虫线程列表
    spider_threadNames = ['爬虫1号', '爬虫2号', '爬虫3号']
    spider_threads = []
    for threadName in spider_threadNames:
        thread = Thread_spider(threadName, pageQueue, dataQueue, id)
        thread.start()
        spider_threads.append(thread)
    for thread in spider_threads:
        thread.join()
    lock = threading.Lock()
    # 创建一个解析线程列表
    parse_threadNames = ['解析1号', '解析2号', '解析3号']
    parse_threads = []
    for threadName in parse_threadNames:
        thread = Thread_parse(threadName, dataQueue, lock)
        thread.start()
        parse_threads.append(thread)

    for thread in parse_threads:
        thread.join()

    print(threading.current_thread().name)


# 主函数
def main():
    url = 'https://xueqiu.com/today/#/'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
    }
    response = requests.get(url, headers=header)
    html = response.text
    pattern = re.compile('<router-link.*?class="tab__item".*?data-category="(.*?)".*?>(.*?)</router-link>')
    result = re.findall(pattern, html)
    for type in result:
        print(type[1])
    type_input = input('请您输入你要爬取的内容')
    for i in result:
        if type_input == i[1]:
            Spider_page(i[0])


# 调用主函数
if __name__ == '__main__':
    main()

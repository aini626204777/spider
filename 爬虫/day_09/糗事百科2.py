# -*- coding:utf-8 -8-
# https://www.qiushibaike.com/8hr/page/1/
# https://www.qiushibaike.com/8hr/page/2/

# 多线程
import threading
import requests
from lxml import etree
import queue
import json


class ThreadCrawl(threading.Thread):
    def __init__(self, threadName, pageQueue, dataQueue):
        super(ThreadCrawl, self).__init__()
        self.threadName = threadName
        self.pageQueue = pageQueue
        self.dataQueue = dataQueue
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0)'
        }
        # print(self.threadName)

    def run(self):
        print('爬取' + threading.current_thread().name)
        while not self.pageQueue.empty():
            page = self.pageQueue.get()
            fullurl = 'https://www.qiushibaike.com/8hr/page/' + str(page) + '/'
            response = requests.get(url=fullurl, headers=self.headers)
            # print(response.status_code)
            if response.status_code == 200:
                self.dataQueue.put(response.text)
            # print(self.dataQueue)


class ThreadParse(threading.Thread):
    def __init__(self, threadname, dataQueue):
        super(ThreadParse, self).__init__()
        self.dataQueue = dataQueue
        self.threadname = threadname

    def run(self):
        print('解析'+threading.current_thread().name)

        while not self.dataQueue.empty():
            html = self.dataQueue.get()
            # print(html)
            self.parse(html)
    def parse(self,html):
        parse_data = etree.HTML(html)
        contentList = parse_data.xpath('//div[@id="content-left"]/div')
        for sub_div in contentList:
            title = sub_div.xpath('.//h2/text()')[0]
            content = sub_div.xpath('.//div[@class="content"]/span/text()')[0]
            dict = {
                'title':title,
                'content':content,
            }
            print(dict)
            with open('qiushi.json','a') as f:
                f.write(json.dumps(dict,ensure_ascii=False)+'\n')


def main():
    pageQueue = queue.Queue(30)
    dataQueue = queue.Queue()
    for i in range(1, 20):
        pageQueue.put(i)

    crawlThreadName = ['crawl美女1号', 'crawl美女2号', 'crawl美女3号']
    threadcreaws = []
    for threadName in crawlThreadName:
        thread = ThreadCrawl(threadName, pageQueue, dataQueue)
        thread.start()
        threadcreaws.append(thread)
    for thread in threadcreaws:
        thread.join()

    threadParses = []
    parseThreadName = ['嘿嘿1号', '嘿嘿2号', '嘿嘿3号']
    for threadname in parseThreadName:
        parsethread = ThreadParse(threadname, dataQueue)
        parsethread.start()
        threadParses.append(parsethread)
    for thread in threadParses:
        thread.join()


if __name__ == '__main__':
    main()

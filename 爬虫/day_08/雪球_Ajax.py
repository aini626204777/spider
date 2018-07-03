import threading
import requests
import json
from lxml import etree
import queue
lb = []
zidian = {}
class ThreadCrawl(threading.Thread):
    def __init__(self,threadName,pageQueue,dataQueue):
        super(ThreadCrawl,self).__init__()
        self.threadName = threadName
        self.pageQueue = pageQueue
        self.dataQueue = dataQueue
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
            'Cookie': 'aliyungf_tc=AQAAAFuOTB0E7AYADUF5ahoG/e8JSARM; xq_a_token=019174f18bf425d22c8e965e48243d9fcfbd2cc0; xq_a_token.sig=_pB0kKy3fV9fvtvkOzxduQTrp7E; xq_r_token=2d465aa5d312fbe8d88b4e7de81e1e915de7989a; xq_r_token.sig=lOCElS5ycgbih9P-Ny3cohQ-FSA; Hm_lvt_1db88642e346389874251b5a1eded6e3=1528716823; u=521528716822937; device_id=dfa2a3a1b381ea40ecb96f71dd70d167; _ga=GA1.2.1321525895.1528716824; _gid=GA1.2.430573630.1528716824; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1528717023'
        }


    def run(self):
        # print(threading.current_thread().name+'正在爬取')
        # print('*' * 30)
        while not self.pageQueue.empty():
            print(self.threadName + '开启')

            print('*'*30)
            page = self.pageQueue.get()
            fullurl = 'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=-1&count=10&category='+str(page)
            response = requests.get(fullurl,headers=self.headers)
            if response.status_code == 200:
                self.dataQueue.put(response.text)
                print(self.threadName + '结束')

class ThreadParse(threading.Thread):
    def __init__(self,threadName,dataQueue):
        super(ThreadParse,self).__init__()
        self.threadName = threadName
        self.dataQueue = dataQueue


    def run(self):
        # print(threading.current_thread().name+'正在解析')
        # print('*'*30)
        while not self.dataQueue.empty():
            print(self.threadName + '开启')
            print(self.threadName + '正在解析')
            html = self.dataQueue.get()
            self.parse(html)

    def parse(self,html):
        parse_data =  json.loads(html)
        pinlss = parse_data["list"]
        for i in pinlss:
            try:
                data = json.loads(i['data'])
                print('文章的id:' + str(data['id']))
                print('标题:' + str(data['title']))
                print('描述:' + str(data['description']))
                print('用户名:' + str(data['user']['screen_name']))
                print('地区:' + str(i['column']))
                print('用户头像:' + str(data['user']['profile_image_url']))
                print('详情的链接详情的链接:' + str(data['target']))
                print('*' * 100)
            except:
                data = json.loads(i['data'])
                print('描述:' + str(data['text']))
                print('地区:' + str(i['column']))
                print('详情的链接详情的链接:' + str(data['target']))
                print('*' * 100)


def main():
    pageQueue = queue.Queue(10)
    dataQueue = queue.Queue()
    for i in lb:
        pageQueue.put(i[0])

    crawlThreadNames = ['狼狼1号', '狼狼2号', '狼狼3号']
    threadcreaws = []
    for threadName in crawlThreadNames:
        thread = ThreadCrawl(threadName=threadName,pageQueue=pageQueue,dataQueue=dataQueue)
        thread.start()
        threadcreaws.append(thread)

    for thread in threadcreaws:
        thread.join()



    parseThreadNames = ['大狼狼1号','大狼狼2号','大狼狼3号']
    threadParses = []
    for threadName in parseThreadNames:
        parsethread = ThreadParse(threadName,dataQueue)
        parsethread.start()
        threadParses.append(parsethread)

    for thread in threadParses:
        thread.join()

        # 打印主线程

    print(threading.current_thread().name)
    print('所有线程结束')

def yiqu_soyan():
    with open('雪球信息.txt', 'r', encoding='utf-8') as f:
        q = f.read()
        html = etree.HTML(q)
        tiquyiji = html.xpath('//div[@ class="home__timeline__tabs tabs"]/router-link[@ class="tab__item"]')
        for i in tiquyiji:
            tioatiao = i.xpath('text()')
            to = i.xpath('@to')
            data = i.xpath('@data-category')
            # print(tioatiao)
            # print(to)
            # print(data)
            # print('*'*30)
            zidian[str(tioatiao)] = data
            lb.append(data)




if __name__ == '__main__':
    yiqu_soyan()
    main()
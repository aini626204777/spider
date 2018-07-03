# -*- coding:utf-8 -*-
import requests
from lxml import etree
from fake_useragent import UserAgent
from concurrent.futures import ThreadPoolExecutor
import os
from bs4 import BeautifulSoup

ua = UserAgent()
headers = {
    'User-Agent': ua.chrome
}


def request_sheying(url, params, headers):
    response = requests.get(url=url, params=params, headers=headers)
    # response.encoding = 'gbk'
    html = response.text
    # print(response.status_code)
    # with open('简书.html','w') as f:
    #     f.write(html)
    mkdir_directory(html)


def mkdir_directory(html):
    html = etree.HTML(html)
    # print(html)
    li_list = html.xpath('//ul[@class="note-list"]/li')
    # print(len(li_list))
    li_title = []
    for directory in li_list:
        title = directory.xpath('.//a[@class="title"]/text()')[0]
        url = directory.xpath('.//a[@class="title"]/@href')[0]
        # print(url)
        # print(title)
        # print('*'*10)
        a = os.getcwd()
        file_path = a + '/' + title
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        li_title.append(title)
        request_particulars(url=url)


def request_particulars(url):
    url = 'https://www.jianshu.com/' + url
    response = requests.get(url=url, headers=headers)
    # response.encoding = 'gbk'
    # print(response.status_code)
    html = response.text
    get_content(html)


def get_content(html):
    html = etree.HTML(html)
    # 获取标题和名字列表
    div_name = html.xpath('//div[@class="article"]')
    for name in div_name:
        # 获取标题
        global title
        title = name.xpath('.//h1[@class="title"]/text()')[0]
        # print(title)
        # 获取名字
        global name1
        name1 = name.xpath('.//span[@class="name"]/a/text()')[0]
        # print(name1)
    # 获取时间
    shijian = html.xpath('//div[@class="author"]')
    for i in shijian:
        global time
        time = i.xpath('.//span[@class="publish-time"]/text()')[0]
        # print(time)
    # 获取文本内容
    content_list = html.xpath('.//div[@class="show-content"]')
    for item in content_list:
        global content
        content = item.xpath('//p/text()')
        # print(content)
    global a
    a = os.getcwd()
    # print(a)
    txt_path = a + '/' + title + '/' + title + '.txt'
    # print(txt_path)
    title1 = '标题：' + title + '\n'
    # print(title1)
    name2 = '作者：' + name1 + '\n'
    # print(name2)
    time1 = '时间：' + time + '\n'
    content_join = '\n'.join(content)
    content1 = '内容：' + content_join + '\n'
    # print(content1)
    b = title1 + name2 + time1 + content1
    # print(b)
    img_list = html.xpath("//div[@class='show-content-free']/div[@class='image-package']//div[@class='image-view']")
    for i in img_list:
        img_path = i.xpath('//@src')
        # print(i)
        print(img_path)
    # with open(txt_path, 'w') as f:
    #     f.write(b)
    #     f.close()

#         url = 'http:'+img_path
#         loadimg(url)
#
# def loadimg(imgpath):
#     response = requests.get(imgpath,headers=headers)
#     print(imgpath)
#     print(response.status_code)
#     path = a + '/' + title+'/'+title+'.png'
#     with open(path, 'a+') as f:
#         f.write(response.text)
#         f.close()

def main():
    book_name = ThreadPoolExecutor(1)
    url = 'https://www.jianshu.com/c/7b2be866f564?'
    params = {
        'utm_source': 'desktop',
        'utm_medium': 'index-collections',
    }
    a = book_name.submit(request_sheying, url, params, headers)
    book_name.shutdown()


if __name__ == '__main__':
    main()
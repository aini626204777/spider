import re
import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
from fake_useragent import UserAgent
import os

ua = UserAgent()
chrome = ua.chrome
headers = {
    'User-Agent': chrome,
}


def request_html(url):
    response = requests.get(url=url, headers=headers)
    response.encoding = 'gbk'
    html = response.text
    # with open('全书网.html','w') as f:
    #     f.write(html)
    book_mkdir(html)


# 获取书名创建文件夹
def book_mkdir(html):
    html = etree.HTML(html)
    li_list = html.xpath('//ul[@class="seeWell cf"]/li')
    # print(len(li_list))
    # b = []
    for book in li_list:
        catalog_name = book.xpath('.//a[@class="clearfix stitle"]/@title')[0]
        # print(book_name)
        url = book.xpath('.//a[@class="readTo"]/@href')[0]
        # os.mkdir(book_name)
        # print(url)
        # http: // www.quanshuwang.com / book_134338.html
        a = re.compile(r'.*?/book_(\d+).html')
        number = re.findall(a, url)[0]
        # os.mkdir(catalog_name)
        # b.append(number)
        # print(len(b))
        # print(number)
        requests_book_catalog(number=number, catalog_name=catalog_name)


def requests_book_catalog(number, catalog_name):
    num = number[:3]
    #url = 'http://www.quanshuwang.com/book/' + str(num) + '/' + str(number)
    response = requests.get(url='http://www.quanshuwang.com/book/162/162782', headers=headers)
    response.encoding = 'gbk'
    html = etree.HTML(response.text)
    li_list = html.xpath('//div[@class="clearfix dirconone"]/li')
    for catalog in li_list:
        a = catalog.xpath('.//a/@href')[0]
        num2 = re.compile('.*?/book/(\d+)/(\d+)/(\d+).html')
        number2, number3, number4 = re.findall(num2, a)[0]
        url2 = 'http://www.quanshuwang.com/book/' + str(number2) + '/' + str(number3) + '/' + str(number4) + '.html'
        request_book_content(url2=url2, catalog_name=catalog_name)


def request_book_content(url2, catalog_name):
    response = requests.get(url=url2, headers=headers)
    response.encoding = 'gbk'
    html = etree.HTML(response.text)
    title = html.xpath('//div[@class="bookInfo"]')
    # content = re.compile(r'<div.*?class="mainContenr".*?id="content">.*?</script>(.*?)<script type="text/javascript">'
    #                      r'style6.*?</script></div>.*?', re.S)
    # book_content = re.findall(content, html)
    # print(book_content)
    for name in title:
        book_name = name.xpath('.//h1/em[@class="l"]/text()')[0]
        # if not os.mkdir(book_name):
        #     os.mkdir(book_name)
        book_catalog = name.xpath('.//h1/strong[@class="l jieqi_title"]/text()')[0]
        book_content = name.xpath('.//div[@class="mainContenr"]/text()')
        book_content1 = ''.join(book_content).replace('\r', '').replace('\xa0', '')
        print(book_name,book_catalog)
        file_name = book_name + '/' + book_catalog + '.txt'
        with open(file_name, 'w') as f:
            f.write(book_content1)
        # print(book_name,book_catalog,book_content1)


def main():
    book_name = ThreadPoolExecutor(3)
    for i in range(1, 2):
        url = 'http://www.quanshuwang.com/list/1_' + str(i) + '.html'
        a = book_name.submit(request_html, url)
    book_name.shutdown()


if __name__ == '__main__':
    main()

import requests
from concurrent.futures import ThreadPoolExecutor
from lxml.html import etree
import re
import pymysql


def download_fenlei_data(url, page):
    html = request_url(url)
    html = etree.HTML(html.text)
    inner_dl = html.xpath('//div[@class="con flq_body"]/div[8]/div/div/div[1]/dl/dd/a/@href')
    for i in inner_dl:
        pattern = re.compile('.*?html')
        result = re.findall(pattern, i)
        if result:
            parse_fenlei_data(result[0],page)


def parse_fenlei_data(url,page):

    full_url = re.sub('com/.*?cp', 'com/pg' + str(page) + '-cp', url)
    # page += 1
    # print('这是第' + str(page) + '页')
    response = request_url(full_url)
    download_detail_url(response.text)



def download_detail_url(html):
    # html = futures.result()
    html = etree.HTML(html)
    data = html.xpath('//div[@class="con shoplist"]/div/ul/li/a/@href')

    # 分类详情的url
    for url in data:
        response = request_url(url)
        parse_detail_data(response.text)


def parse_detail_data(html):
    # html = futures.result()
    html = etree.HTML(html)
    data = {}
    # 书名
    data['book_name'] = html.xpath('//div[@class="name_info"]/h1/@title')[0]
    # 简介
    data['introduction'] = html.xpath('//div[@class="name_info"]/h2/span[1]/text()')[0].strip()
    # 作者
    data['author'] = html.xpath('//div[@class="messbox_info"]/span/a/text()')[0]
    # 出判社
    data['press'] = html.xpath('//div[@class="messbox_info"]/span[2]/a/text()')[0]
    # 发布时间
    data['pubdate'] = html.xpath('//div[@class="messbox_info"]/span[3]/text()')[0].strip()
    # 评论数
    data['comment'] = html.xpath('//div[@class="messbox_info"]/div/span[2]/a/text()')[0]
    # 现价钱
    data['price'] = html.xpath('//p[@id="dd-price"]/text()')[1].strip()
    # 收藏人气
    data['Popularity'] = html.xpath('//a[@class="btn_scsp"]/text()')[0].strip()
    # 封面
    data['cover'] = html.xpath('//div[@id="largePicDiv"]/a/img/@src')[0]
    print(data)


def request_url(url):
    """
    请求url函数
    :param url: 需要请求的url
    :return:
    """
    req_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    response = requests.get(url, headers=req_headers)
    if response.status_code == 200:
        return response


def save_data_to_db(self, table, data):
    """
    保存数据到数据库
    :param self:
    :param table: 数据库表名
    :param data: 需要存储的数据
    :return:
    """
    connect = pymysql.Connect('localhost', "root", "abcd1234", "1712B", 3306, charset="utf8")
    keys = ','.join(data.keys())
    sql = """INSERT INTO {table}({columns}) values ({values})""".format(table=table, columns=keys,
                                                                        values=(','.join(["%s"] * len(data))))
    cr = connect.cursor()
    cr.execute(sql, list(data.values()))
    connect.commit()
    cr.close()
    connect.close()


if __name__ == '__main__':
    url = 'http://book.dangdang.com/'
    page = 1
    download_fenlei_data(url, page)

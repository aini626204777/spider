import requests
from lxml.html import etree
import re
from concurrent.futures import ThreadPoolExecutor
import pymysql


def down_page_data(url, page):
    """
    解析分页数据和下一页
    :param url: 起始url
    :param page:
    :return:
    """
    response = req_requests(url)
    data_dict = {}
    data_dict['page'] = page
    if response.status_code == 200:
        html = etree.HTML(response.text)
        li_list = html.xpath('//ul[@class="all-img-list cf"]/li')
        for i in li_list:
            book_type = i.xpath('./div[@class="book-mid-info"]/p[1]/a[2]/text()')[0]
            bookName = i.xpath('./div[@class="book-mid-info"]/h4/a/text()')[0]
            data_dict['sum'] = html.xpath('//*[@id="page-container"]/div/ul/li/a/text()')[-2]
            full_url = i.xpath('./div[@class="book-mid-info"]/h4/a/@href')[0]
            fl_url = re.sub('//book.qidian.com/', 'https://book.qidian.com/', full_url)
            result_url = fl_url + '#Catalog'
            print('当前第' + str(page) + '页:', book_type, bookName, '共' + str(data_dict['sum'] + '页.'))
            data_dict['url'] = result_url
            download_detail_page(data_dict)

        # 　获取下一页
        if page < int(data_dict['sum']):
            page += 1
            full_url = re.sub('page=\d+', 'page=' + str(page), url)
            print(full_url)
            down_page_data(full_url, page)
        else:
            print('爬取完毕！！！')


def download_detail_page(data_dict):
    """
    解析详情url链接
    :param data_dict:
    :return:
    """
    url = data_dict['url']
    response = req_requests(url)
    # 小说信息字典
    Novel_data_dict = {}
    data_dict = {'page': page}

    if response.status_code == 200:
        html = etree.HTML(response.text)
        li_list = html.xpath('//div[@class="volume-wrap"]/div[1]/ul/li/a/@href')
        Novel_data_dict['title'] = html.xpath('//div[@class="book-info "]/h1/em/text()')[0]
        Novel_data_dict['type'] = html.xpath('//div[@class="book-info "]/p[1]/a[1]/text()')[0]
        for i in li_list:
            full_url = re.sub('//read.qidian.com/', 'https://read.qidian.com/', i)
            data_dict['url'] = full_url
            # parse_detail_data(data_dict,Novel_data_dict)


def parse_detail_data(data_dict, Novel_data_dict):
    """
    解析数据详情
    :param data_dict:
    :param Novel_data_dict: # 小说信息字典
    :return:
    """
    response = req_requests(data_dict['url'])
    if response.status_code == 200:
        # 章节信息字典
        chapter_data_dict = {}
        html = etree.HTML(response.text)

        # 书名
        chapter_data_dict['title'] = Novel_data_dict['title']
        # 类型
        chapter_data_dict['type'] = Novel_data_dict['type']
        # # 作者
        chapter_data_dict['author'] = html.xpath('//div[@class="info fl"]/a[2]/text()')[0]
        # # 时间
        chapter_data_dict['date'] = html.xpath('//div[@class="info fl"]/i[2]/span/text()')[0]
        # # 字数
        chapter_data_dict['number'] = html.xpath('//div[@class="info fl"]/i[1]/span/text()')[0]
        # # 章节
        chapter_data_dict['chapter'] = html.xpath('//h3[@class="j_chapterName"]/text()')[0]
        # # 内容
        chapter_data_dict['content'] = ','.join(
            html.xpath('//div[@class="read-content j_readContent"]/p/text()')).replace("\u3000",
                                                                                       "").rstrip()
        print('当前获取' + chapter_data_dict['type'] + '类,' + '第' + str(data_dict['page']) + '页：' + chapter_data_dict[
            'title'] + ':' + chapter_data_dict['chapter'], chapter_data_dict)

        save_data_to_DB('xiaoshuo',data_dict)
def req_requests(url):
    """
    向浏览器发送请求的函数
    :param url: 目标ｕｒｌ地址
    :return:
    """
    req_headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
    }
    response = requests.get(url, headers=req_headers)
    if response.status_code == 200:
        # with open('起点中文网.html','w') as f:
        #     f.write(response.text)
        return response


def save_data_to_DB(table, data):
    """
    将数据保存到数据库
    :param data: 需要保存的数据
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
    url = 'https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=1'
    page = 1
    # pool = ThreadPoolExecutor(max_workers=5)
    # for i in range(5):
    #     pool.submit(down_page_data, url, page)

    down_page_data(url, page)

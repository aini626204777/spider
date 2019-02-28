# http://date.jiayuan.com/eventslist_new.php?page=0&city_id=31&shop_id=15
# http://date.jiayuan.com/eventslist.php
# /eventsdetail.php?id=11860
# http://date.jiayuan.com/eventsdetail.php?id=11860
# http://date.jiayuan.com/activityreviewdetail.php?id=11826

import requests
import pymysql
from lxml.html import etree


def jySpider(url):

    headers = {
        'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
        'Cookie': 'PHPSESSID=21f1f689651b348652554bd9a03f7aef; DATE_SHOW_LOC=11; DATE_SHOW_SHOP=61; accessID=20181223194501430510; user_access=1; plat=date_pc; uv_flag=114.242.248.43',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        jydata(response.text)


def jydata(html):

    html_data = etree.HTML(html)
    data = html_data.xpath('//div[@class="act_hot"]/div')
    city = html_data.xpath('//div[@class="act_review"]/ul/li')
    print(city, 'changshi')
    for item in data:
        url = item.xpath('./div[@class="hot_right fn-left"]/h2/a/@href')[0]
        url_data = 'http://date.jiayuan.com' + url
        Detali(url_data)
    for i in city:
        urls = i.xpath('./a/@href')[0]
        urls_data = 'http://date.jiayuan.com' + urls
        Detali(urls_data)




def jyJson(url, parmars):

    headers = {
        'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
    }

    response = requests.get(url, headers=headers, params=parmars)
    print('第' + str(parmars['page']) + '页')
    if response.status_code == 200:
        json_list = response.json()
        if len(json_list) > 2:
            jyJsonData(json_list)
            parmars['page'] = parmars['page'] + 1
            jyJson(url, parmars)
        else:
            print('ok')


def jyJsonData(json_list):

    for i in json_list:
        url = 'http://date.jiayuan.com/activityreviewdetail.php?id=' + str(i['id'])
        Detali(url)


#获取详情
def Detali(url):

    headers = {
        'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',

    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        details_data(response.text)
    else:
        print('请求失败')


def details_data(html):
    # print(html)
    introduce = {}
    html_data = etree.HTML(html)
    # 标题
    introduce['title_data'] = html_data.xpath('//h1[@class="detail_title"]/text()')[0]
    # 图片链接
    introduce['img_data'] = html_data.xpath('//div[contains(@class,"detail_left")]/img/@data-original')[0]
    # 活动时间
    introduce['time_data'] = ' '.join(html_data.xpath('//ul[@class="detail_info"]/li[1]//text()'))
    # 活动地点
    introduce['place_data'] = ' '.join(html_data.xpath('//ul[@class="detail_info"]/li[2]//text()'))
    # 参与人数
    introduce['number_data'] = ' '.join(html_data.xpath('//ul[@class="detail_info"]/li[3]//text()'))
    # 活动介绍
    introduce['introduce_data'] = html_data.xpath('//div[@id="date_float"]/div[2]//p/span/text()')[0]
    # 温馨提示
    introduce['tips_data'] = html_data.xpath('//div[@id="date_float"]/div[3]//p/text()')[0]
    # 体验店介绍
    introduce['jiesao_data'] = html_data.xpath('//div[@id="date_float"]/div[4]//p/text()')[0]
    save_date_db(introduce)


#数据库

def save_date_db(introduce):
    sql = 'INSERT INTO jiayuan values (0,%s)' % (','.join(['"%s"'] * len(introduce)))
    try:
        cur.execute(sql, list(introduce.values()))
        conn.commit()
    except Exception as err:
        print(err)
        conn.rollback()


if __name__ == '__main__':
    conn = pymysql.connect(host='localhost', port=3306, db='sun', user='root', passwd='sun123', charset='utf8')
    cur = conn.cursor()
    url = 'http://date.jiayuan.com/eventslist.php'
    json_url = 'http://date.jiayuan.com/eventslist_new.php?'
    parmars = {
        'page': 2,
        'city_id': 31,
        'shop_id': 15
    }
    jySpider(url)
    jyJsonData(json_url, parmars)

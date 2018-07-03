# 作业1，爬取咨讯内容
import requests
from lxml import etree
import pymysql


def Spider(url, start, stop):
    for i in range(start, stop + 1):
        fillurl = url + str(i)
        loadPage(fillurl, i)


def loadPage(fillurl, i):
    print('正在爬取第%s页内容' % i)
    response = requests.get(fillurl, verify=False)
    html = response.text
    disposePage(html, i)


def disposePage(html, i):
    print('正在处理第%s页信息' % i)
    text = etree.HTML(html)
    result = text.xpath('//li[@class="media"]/div/h3/a/text()')
    result1 = text.xpath('//li[@class="media"]/div/p/span[1]/text()')
    result5 = text.xpath('//li[@class="media"]/div/h3/a/@href')
    result2 = text.xpath('//li[@class="media"]/div/p')
    list_type = []
    list_acc = []
    for item in result2:
        result3 = item.xpath('./span[@class="p-tags"]/a/text()')
        if len(result3) == 0:
            result3 = ['未知']
        list_type.append(result3[0])
        result4 = item.xpath('./span/a/text()')
        if len(result4) == 2:
            result4.remove(result4[0])
        elif len(result4) == 0 or result4 == result3:
            result4 = ['未知']
        list_acc.append(result4[0])
    for i in range(1, len(result1)):
        write_DB(result1[i], result[i], list_type[i], list_acc[i], result5[i])


# 写入数据库
def write_DB(a, b, c, d, e):
    con = pymysql.Connect(host='localhost', user='root', password='bc123', database='bole', port=3306,
                          charset='utf8')
    cur = con.cursor()
    print('写入数据')
    sql = 'INSERT INTO bole2 VALUES(0,"%s","%s","%s","%s","%s")' % (a, b, c, d, e)
    cur.execute(sql)
    result = cur.fetchall()
    con.commit()
    con.close()


def get_data(a):
    c = (a - 1) * 15
    b = a * 15
    con = pymysql.Connect(host='localhost', user='root', password='bc123', database='bole', port=3306,
                          charset='utf8')
    cur = con.cursor()
    sql = 'select * from bole2 where id <="%d" and id > "%d"' % (b, c)
    cur.execute(sql)
    data = cur.fetchall()
    for mes in data:
        print(mes)
    con.commit()
    con.close()


if __name__ == '__main__':
    ac = int((input('请输入操作内容：1.爬取，2.查看')))
    url = 'http://top.jobbole.com/page/'
    if ac == 1:
        start = int(input('请输入开始页码'))
        stop = int(input('请输入停止页码'))
        Spider(url, start, stop)
    elif ac == 2:
        show = int(input('请输入显示内容'))
        get_data(show)
    else:
        print('bye')

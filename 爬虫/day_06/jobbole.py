import requests
from lxml import etree
import pymysql


def request_jobbole(url,headers):
    response = requests.get(url=url,headers=headers)
    html = response.text
    txt = etree.HTML(html)
    for txt in txt.xpath('//li[@class="media"]'):
        # 标题
        title = txt.xpath('.//div/h3/a/text()')[0]
        # 链接
        link = txt.xpath('.//div/h3/a/@href')[0]
        # 文章发布时间
        publishtime = txt.xpath('.//div/p/span[1]/text()')[0]
        # 类型
        type1 = txt.xpath('.//p/span[@class="p-tags"]/a/text()')
        if len(type1) == 0:
            type1 = '未知类型'
        # 评论
        commentnum = txt.xpath('.//i[@class="fa fa-comments-o"]')
        if len(commentnum) == 0:
            commentnum = '0'
        elif len(commentnum) > 0:
            if type1 == '未知类型':
                commentnum = txt.xpath('.//p[@class="p-meta"]/span[2]/a/text()')[0]
            else:
                commentnum = txt.xpath('.//p[@class="p-meta"]/span[3]/a/text()')
        print(type1)
        write_DB(title1=title,link1=link,type1=type1,publishtime1=publishtime,commentnum1=commentnum)



def write_DB(title1, link1, type1, publishtime1, commentnum1):
    sql = pymysql.Connect(host='localhost', user='root', password='bc123', database='bole', port=3306, charset='utf8')
    cursor = sql.cursor()
    print('正在存储数据')

    write_data = "insert into bole2 values(0,'%s','%s','%s','%s','%s')" % (title1, type1, commentnum1, publishtime1, link1)
    cursor.execute(write_data)
    sql.commit()
    print('存储成功')
    
    cursor.close()
    sql.close()


if __name__ == "__main__":
    url = 'http://top.jobbole.com/'

    # proxy = {

    #     'HTTP': '125.121.120.215:808',
    # }
    headers = {
        'Referer': 'http://www.jobbole.com/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    request_jobbole(url,headers)

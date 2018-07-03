from lxml import etree
import requests
import pymysql
def get(url,start,end):
    for page in range(start,end + 1):
        furl = url + 'page/%s/'%page
        chuli(furl)
        print(furl)
def chuli(furl):
    header = {
        'User - Agent': 'Mozilla / 5.0(Linux;Android6.0;Nexus5Build / MRA58N) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 65.0.3325.146MobileSafari / 537.36'
    }
    response = requests.get(furl, headers=header)
    page_html = etree.HTML(response.text)
    print(page_html)
    a = page_html.xpath('//li[@class="media"]')
    for item in a:
        title = item.xpath('.//h3[@class="p-tit"]/a/text()')[0]
        link = item.xpath('.//h3[@class="p-tit"]/a/@href')[0]
        time = item.xpath('.//p[@class="p-meta"]/span/text()')[0]
        type = item.xpath('.//span[@class="p-tags"]/a/text()')
        if len(type) == 0:
            type = '无'
        comment = item.xpath('.//i[@class="fa fa-comments-o"]')
        if len(comment) == 0:
            comment = '0'
        elif len(comment) > 0:
            if type == '无':
                # 没有标签的情况
                comment = item.xpath('.//p[@class="p-meta"]/span[2]/a/text()')[0]
                #print(comment)
            else:
                comment = item.xpath('.//p[@class="p-meta"]/span[3]/a/text()')[0]

        print(title, link, time,type,comment)
        conn = pymysql.connect(host='127.0.0.1', user='root', password='bc123', database='bole', port=3306,
                               charset='utf8')
        cur = conn.cursor()
        sql = 'INSERT INTO bole(title, link, time,type,comment) VALUES("%s","%s","%s","%s","%s")'
        cur.execute(sql,(title, link, time,type,comment))
        # result = cur.fetchall()
        conn.commit()
        conn.close()
def fenye():
    fenye = int(input('请输入查询的页数：'))
    q = ( fenye - 1)*15
    conn = pymysql.connect(host='127.0.0.1', user='root', password='bc123', database='bole', port=3306,
                           charset='utf8')
    cur = conn.cursor()
    sql = 'select * from bole limit %d,15'%int(q)
    cur.execute(sql)
    result = cur.fetchall()
    print(result)
    conn.commit()
    conn.close()
fenye()
if __name__ == '__main__':
    start = int(input("请输入开始的页数："))
    end = int(input("请输入截止的页数："))
    url = 'http://top.jobbole.com/'
    #http://top.jobbole.com/page/2/
    get(url,start,end)


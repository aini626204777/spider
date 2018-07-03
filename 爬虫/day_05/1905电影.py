from lxml import etree
import requests
import pymysql
def sousuo():
    sousuo = input("请输入你要搜索的电影:")
    conn = pymysql.connect(host='localhost', user='root', password='bc123', database='1905dyw', port=3306,charset='utf8')
    cur = conn.cursor()
    a = '%'+ sousuo +'%'
    sql = "select * from dyw where name like '%s'"%a
    cur.execute(sql)
    result = cur.fetchall()
    print(result)
    conn.commit()
    conn.close()

def get(url,start,end):
    for page in range(start,end + 1):
        furl = url + 'n_1/o1p%s.html'%page
        chuli(furl)
        print(furl)
def chuli(furl):
    header = {
        'User - Agent': 'Mozilla / 5.0(Linux;Android6.0;Nexus5Build / MRA58N) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 65.0.3325.146MobileSafari / 537.36'
    }
    response = requests.get(furl,headers=header)
    page_html = etree.HTML(response.text)
    a = page_html.xpath('.//div[@class="grid-2x grid-3x-md grid-6x-sm"]')
    for item in a:
        name = item.xpath('.//h3/text()')[0]
        link = item.xpath('.//a/@href')[0]
        fenmian = item.xpath('.//img/@src')[0]
        score1 = item.xpath('.//i[@class="score"]/b/text()')[0]
        score2 = item.xpath('.//i[@class="score"]/text()')[0]
        score = score1+score2
        conn = pymysql.connect(host='localhost', user='root', password='bc123', database='1905dyw', port=3306,charset='utf8')
        cur = conn.cursor()
        sql = 'INSERT INTO dyw(name,link,fenmian,score) VALUES("%s","%s","%s","%s")'
        cur.execute(sql,(name,link,fenmian,score))
        # result = cur.fetchall()
        conn.commit()
        conn.close()


if __name__ == '__main__':
    start = int(input("请输入开始的页数："))
    end = int(input("请输入截止的页数："))
    url = 'http://www.1905.com/vod/list/'
    #http://www.1905.com/vod/list/n_1/o1p1.html
    get(url,start,end)
    sousuo()







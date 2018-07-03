import requests
from bs4 import BeautifulSoup
import demjson
import json
import pymysql
import re

pllist = []
db = pymysql.connect('localhost', 'root', 'bc123', 'qichezhijia', use_unicode=True, charset='utf8')
kk = db.cursor()
url = 'https://www.autohome.com.cn/all/1/#liststart'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
response = requests.get(url, headers=headers)
response = response.content.decode("gbk")

soup = BeautifulSoup(response)
pic = soup.select('.article-pic img')
txt = soup.find_all('h3')
data = soup.find_all('span', attrs={'class': 'fn-left'})
renshu = soup.find_all('span', attrs={'class': 'fn-right'})

xiangqing = soup.select('a p')
pl = soup.select('#auto-channel-lazyload-article li a')
ty = ''
for i in pl:
    zzb = re.compile(r'//www.autohome.com.cn/\w+/\d+/(\d+?)[-|.].*?html')
    cy = re.findall(zzb, i.get('href'))
    pllist.append(cy)
    ty = ty + cy[0] + '.'

ty = ty[:-1]
print(ty)
plurl = 'https://reply.autohome.com.cn/api/getData_ReplyCounts.ashx?appid=1&dateType=jsonp&objids=' + str(
    ty) + '&callback=jQuery17209208316883121432_1528446325867&_=1528446327087'
hj = requests.get(plurl)
zh = hj.text
zh = zh[40:]
zh = zh[1:-1]
print(zh.replace('\'', '\"'))
zh = json.loads(zh.replace('\'', '\"'))
print(type(zh))
plsl = zh['commentlist']

for i in pic:
    sy = int(pic.index(i))
    print(txt[int(sy)].get_text())
    print(i.get('src'))
    print(data[int(sy)].get_text())
    print(renshu[int(sy)].select('em')[0].get_text())
    print(xiangqing[int(sy)].get_text())
    print(plsl[int(sy)]['replycount'])
    rr = "select * from 汽车 where title=%s"
    kk.execute(rr, (txt[int(sy)].get_text()))
    oo = kk.fetchone()
    print(oo)
    if oo == None:
        er = "insert into 汽车 values(0,%s,%s,%s,%s,%s,%s)"
        kk.execute(er, (
        txt[int(sy)].get_text(), i.get('src'), data[int(sy)].get_text(), renshu[int(sy)].select('em')[0].get_text(),
        plsl[int(sy)]['replycount'], xiangqing[int(sy)].get_text()))
        db.commit()
    else:
        print('存在了,就不添加')

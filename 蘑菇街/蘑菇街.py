import requests
from lxml.html import etree
import json
import re
import pymongo


## 定义一些需要的参数
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
           #'Cookie': '__mgjuuid=44f00610-70f8-4167-9058-cf34b7473997; _mwp_h5_token_enc=7619b628e3606cc82217b0f5074d2d02; _mwp_h5_token=49604ded913b59a399beda5a2d018272_1545802740450; _ga=GA1.2.2042772456.1545802779; _gid=GA1.2.1847442730.1545908947; _TDeParam=1-QsXNDyVpLjr6/6OFfEEOFg'
           }
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.text
collection = db.students

def gitClassify():
    '''
    获取所有商品分类
    :return: 所有分类的跳转连接
    '''
    url = 'https://list.mogujie.com/sync/menu?callback=jQuery211045232262890995534_1545910269349&action=clothing&fcid=50240&_=1545910269350'
    html = requests.get(url,headers=headers)
    pattern = re.compile(r'\((.*?)\)')  # 查找数字
    result1 = pattern.findall(html.text)
    jsonClassify = json.loads(result1[0])
    classsify = {}
    print(jsonClassify)
    for i in jsonClassify['data']['menus']:
        classsify[i['name']]=[i['action'],'https://list.mogujie.com'+i['link']]
        print()

    return classsify
print(gitClassify())
def allCommodity ():
    '''
    获取所有分类下的所有商品
    :return:
    '''
    gc = gitClassify()
    for i in gc:
        print('正在爬取',i, gc[i][0],gc[i][1])
        html = requests.get( gc[i][1],headers=headers)
        html = etree.HTML(html.text)
        _version = html.xpath('//*[@id="wall_goods_box"]/div[1]/input[3]/@value')[0]
        ratio = html.xpath('//*[@id="wall_goods_box"]/div[1]/input[4]/@value')[0]
        cKey = html.xpath('//*[@id="wall_goods_box"]/div[1]/input[5]/@value')[0]
        sort = html.xpath('//*[@id="wall_goods_box"]/div[1]/input[7]/@value')[0]
        action = gc[i][0]
        for i in range(1,10):
            url = 'https://list.mogujie.com/search?&_version={}&ratio={}&cKey={}&page={}&sort={}&ad=0&fcid=&action={}'.format(_version,ratio,cKey,i,sort,action)
            print('正在获取','第{}页'.format(i),url)
            js = requests.get(url,headers=headers)
            jsonClassify = json.loads(js.text)
            for i in jsonClassify['result']['wall']['docs']:
                print('title',i['title'])
                if 'price' in i:
                    print('price',i['price'])
                else:
                    continue
                print('link',i['link'])
                students = {'title': i['title'], 'price': i['price'], 'link': i['link']}
                print(students)
                # result = collection.insert(students)
                # print(result)
                print('*'*50)


# allCommodity()

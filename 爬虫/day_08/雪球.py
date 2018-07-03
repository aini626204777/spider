import requests
from lxml import etree
import json



lb = []
zidian = {}
def qaqu_syan(url,headers):
    requ = requests.get(url,headers=headers)
    print(requ.status_code)
    with open('雪球信息.txt', 'w', encoding='utf-8') as f:
        f.write(requ.text)


def yiqu_soyan():
    with open('雪球信息.txt', 'r', encoding='utf-8') as f:
        q = f.read()
        html = etree.HTML(q)
        tiquyiji = html.xpath('//div[@ class="home__timeline__tabs tabs"]/router-link[@ class="tab__item"]')
        for i in tiquyiji:
            tioatiao = i.xpath('text()')
            to = i.xpath('@to')
            data = i.xpath('@data-category')
            # print(tioatiao)
            # print(to)
            # print(data)
            # print('*'*30)
            zidian[str(tioatiao)] = data
            lb.append(data)
def huoqujs(headers):
    url = 'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=-1&count=10&category='
    for kv in zidian.items():
        v = kv[1]
        k = kv[0]
        w = url + str(v[0])
        print(k[2:4])
        print('正在请求',w)
        requ = requests.get(w, headers=headers)
        print(requ.status_code)
        print('正在爬取')
        with open('雪球分类信息'+ k[2:4] +'.txt', 'w', encoding='utf-8') as f:
            f.write(requ.text)

def tiquflxx():
    for kv in zidian.items():
        k = kv[0]
        with open('雪球分类信息'+ k[2:4] +'.txt', 'r', encoding='utf-8') as f:
            q = f.read()
            s = q.replace(r"\\",'')
            w = json.loads(q)
            pinlss = w["list"]
            for i in pinlss:
                try:
                    data = json.loads(i['data'])
                    print('文章的id:'+ str(data['id']))
                    print('标题:' + str(data['title']))
                    print('描述:' + str(data['description']))
                    print('用户名:'+ str(data['user']['screen_name']))
                    print('地区:'+ str(i['column']))
                    print('用户头像:'+ str(data['user']['profile_image_url']))
                    print('详情的链接详情的链接:'+ str(data['target']))
                    print('*'*100)
                except:
                    data = json.loads(i['data'])
                    print('描述:' + str(data['text']))
                    print('地区:' + str(i['column']))
                    print('详情的链接详情的链接:' + str(data['target']))
                    print('*' * 30)

def shakanzidian():
    print(zidian)
    print(lb)
    pass
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    'Cookie': 'aliyungf_tc=AQAAAFuOTB0E7AYADUF5ahoG/e8JSARM; xq_a_token=019174f18bf425d22c8e965e48243d9fcfbd2cc0; xq_a_token.sig=_pB0kKy3fV9fvtvkOzxduQTrp7E; xq_r_token=2d465aa5d312fbe8d88b4e7de81e1e915de7989a; xq_r_token.sig=lOCElS5ycgbih9P-Ny3cohQ-FSA; Hm_lvt_1db88642e346389874251b5a1eded6e3=1528716823; u=521528716822937; device_id=dfa2a3a1b381ea40ecb96f71dd70d167; _ga=GA1.2.1321525895.1528716824; _gid=GA1.2.430573630.1528716824; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1528717023'
    }
url = 'https://xueqiu.com/today#/'
if __name__ == '__main__':
    qaqu_syan(url,headers)
    #yiqu_soyan()
    #shakanzidian()
    #huoqujs(headers)
    #tiquflxx()
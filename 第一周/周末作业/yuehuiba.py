import requests
from lxml.html import etree

class yuehuibaSpider(object):
    def __init__(self):
        self.url = 'http://date.jiayuan.com/eventslist.php'
        self.parmars = {
            'page': 1,
            'city_id': 4201,
            'shop_id': 33,
            'Cookie':'accessID=20181222182641836247; user_access=1; _gscu_1380850711=45474402mhw1k021; _gscbrs_1380850711=1; DATE_SHOW_LOC=4201; SESSION_HASH=963b65b7a9f28293ccb96be3e6b369f911e9135e; jy_refer=www.baidu.com; FROM_BD_WD=%25E4%25B8%2596%25E7%25BA%25AA%25E4%25BD%25B3%25E7%25BC%2598; FROM_ST_ID=1764229; FROM_ST=.jiayuan.com; PHPSESSID=03ab20c2e1608530fc98721e67f2ec4a; plat=date_pc; uv_flag=61.158.149.82; DATE_SHOW_SHOP=33'
        }
        self.req_headers = {
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
        }

    def load(self,url,parmars,headers):
        response = requests.get(url=url,headers=headers,params=parmars)
        if response.status_code == 200:
            with open('yuehuiba.html','w') as file:
                file.write(response.text)

if __name__ == '__main__':
    yuehuiba = yuehuibaSpider()
    yuehuiba.load(url=yuehuiba.url,parmars=yuehuiba.parmars,headers=yuehuiba.req_headers)
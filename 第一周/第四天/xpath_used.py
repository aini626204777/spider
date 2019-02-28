import requests
from lxml.html import etree


def load(url):

    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    }

    response = requests.get(url=url,headers=headers)
    if response.status_code == 200:
        parse_data(response.text)



def parse_data(html):
    html = etree.HTML(html)
    autio_list = html.xpath('//div[@class="j-r-c"]/div[@class="j-r-list"]/ul/li')
    print(autio_list)
    for autio in autio_list:
        autio_data = {}
        # 点赞，差评，封面，音频
        autio_data['name'] = autio.xpath('.//a[@class="u-user-name"]/text()')[0]
        autio_data['content'] = autio.xpath('.//div[@class="j-r-list-c-desc"]/text()')[0]
        autio_data['date'] = autio.xpath('.//span[@class="u-time  f-ib f-fr"]/text()')[0]
        autio_data['zanNum'] = autio.xpath('.//li[@class="j-r-list-tool-l-up"]/span/text()')[0]
        autio_data['chacomment'] = autio.xpath('.//li[@class="j-r-list-tool-l-down "]/span/text()')[0]
        autio_data['cover'] = autio.xpath('.//li[@class="j-r-list-tool-l-down f-tar j-down-video j-down-hide ipad-hide"]/@data-pic')[0]
        autio_data['music'] = autio.xpath('.//li[@class="j-r-list-tool-l-down f-tar j-down-video j-down-hide ipad-hide"]/a/@href')[0]
        print(autio_data)






if __name__ == '__main__':
    url = "http://www.budejie.com/audio/1"
    load(url=url)
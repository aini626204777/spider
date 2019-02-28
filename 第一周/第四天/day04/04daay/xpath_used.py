#xpath:可以在xml中查找信息，对xml文档中元素进行遍历和属性的提取

# xml:被设计的目的是为了传输数据,结构和html非常相识,是一种标记语言

"""
xpath常见的语法：
nodename 选取此节点的所有子节点
/        从根节点开始查找
//       匹配节点，不考虑节点的位置
.        选取当前节点
..       选取当前节点的父节点
a/@href        取标签的数据
a/text()       取标签的文本
a[@class="123"] 根据class属性寻找标签
a[@id="123"]    根据id属性寻找标签

a[@id="123"][last()]  取最后一个id为123的a标签
a[@id="123"][postion() < 2]  取id为123的前两个a标签
"""
import requests
from lxml.html import etree
import re

#样例()
#http://www.budejie.com/audio/1
#http://www.budejie.com/audio/2
#http://www.budejie.com/audio/3

def load_page_data(url):
    """
    下载器（根据分页url获取分页的页面源码）
    :param url: 分页url地址
    :return:
    """
    req_header = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    response = requests.get(url,headers=req_header)
    if response.status_code == 200:
        print('请求成功')
        # with open('page.html','w') as file:
        #     file.write(response.text)
        status = parse_page_data(response.text)

        if status:
            #请求下一页数据
            pattern = re.compile('\d+')
            cur_page = re.search(pattern,response.url).group()
            next_page = int(cur_page)+1
            next_page_url = re.sub(pattern,str(next_page),response.url)

            load_page_data(next_page_url)



def parse_page_data(html):
    """
    使用xpath从html页面源码中提取数据
    :param html:
    :return:
    """
    #pip3 install lxml
    #使用etree.HTML()方法将html转为xml(element对象)
    html_element = etree.HTML(html)

    autio_list = html_element.xpath('//div[@class="j-r-c"]/div[@class="j-r-list"]/ul/li')
    print(autio_list)
    print(len(autio_list))

    for autio in autio_list:
        autio_data = {}
        #取出标题
        autio_data['name'] = autio.xpath('.//a[@class="u-user-name"]/text()')[0]
        #取出内容
        autio_data['content'] = autio.xpath('.//div[@class="j-r-list-c-desc"]/text()')[0]
        #发布时间
        autio_data['publishTime'] = autio.xpath('.//span[@class="u-time  f-ib f-fr"]/text()')[0]
        #点赞数
        autio_data['zanNum'] = autio.xpath('.//li[@class="j-r-list-tool-l-up"]/span/text()')[0]
        #差评书
        autio_data['lowNum'] = autio.xpath('.//li[@class="j-r-list-tool-l-down "]/span/text()')[0]
        #封面
        autio_data['coverImage'] = autio.xpath('.//div[@class=" j-audio"]/@data-poster')[0]
        #音频
        autio_data['url'] = autio.xpath('.//div[@class=" j-audio"]/@data-mp3')[0]
        print(autio_data)
        download_audio_by_url(autio_data['url'],autio_data)

    if len(autio_list) > 0:
        return True
    else:
        return False

def download_audio_by_url(url,audioData):
    """
    根据银屏url地址下载银屏数据
    :param url:
    :param audioData:
    :return:
    """
    req_header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    response = requests.get(url,headers=req_header)
    if response.status_code == 200:
        print(response.url,'下载成功')
        filename = response.url[-17:0]
        with open('baisibudejie/'+filename,'wb') as file:
            file.write(response.content)
            audioData['localpath'] = 'baisibudejie/'+filename
        #将数据存储到数据库
        save_data_to_db(audioData)

def save_data_to_db(audio):
    print(audio)


if __name__ == '__main__':

    start_url = 'http://www.budejie.com/audio/1'
    load_page_data(start_url)




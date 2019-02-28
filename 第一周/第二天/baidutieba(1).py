#目标获取百度贴吧中帖子详情里面的图片,并下载到本地
"""
step1：分析贴吧中分页的url地址规律,要根据url构造请求
https://tieba.baidu.com/f?ie=utf-8
&kw=%E7%BE%8E%E5%A5%B3&pn=0

https://tieba.baidu.com/f?kw=%E7%BE%8E%E5%A5%B3
&ie=utf-8&pn=50

https://tieba.baidu.com/f?kw=%E7%BE%8E%E5%A5%B3
&ie=utf-8&pn=100

https://tieba.baidu.com/f?kw=%E7%BE%8E%E5%A5%B3
&ie=utf-8&pn=150

step2:获取分页中帖子详情的url地址,要根据url构造请求

step3:从帖子情页面中总获取图片地址,要根据url构造请求
"""
from urllib import parse,request
import re

def tiebaSpider(name,start_page,end_page):

    for page in range(start_page,end_page+1):
        #https://tieba.baidu.com/f?kw=%E7%BE%8E%E5%A5%B3&ie=utf-8&pn=150
        parmars = {
            'kw':name,
            'ie':'utf-8',
            'pn':(page-1)*50
        }
        #将字典类型的参数,转换为url编码格式的字符串
        result = parse.urlencode(parmars)
        #拼接完整的url地址
        full_url = 'https://tieba.baidu.com/f?'+result
        #根据分页的url地址发起请求,得到响应结果,提取html页面源码
        html = load_data(full_url)
        #从页面源码中匹配出帖子详情的url地址
        parse_page_detail_url(html)

def load_data(url):

    #设置请求头
    req_header = {
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0',
    }
    #构造一个request对象
    req = request.Request(url,headers=req_header)
    #发起请求
    response = request.urlopen(req)

    if response.status == 200:

        return response.read().decode('UTF-8')

def parse_page_detail_url(html):
    """
    使用正则，从每一个分页的html页面源码中,提取帖子详情的url地址
    :param html: 每一个分页页面源码
    :return:
    """
    pattern = re.compile(
        '<div\sclass="threadlist_title pull_left j_th_tit ">'+
        '.*?<a.*?href="(.*?)".*?</div>',re.S
    )
    result = re.findall(pattern,html)
    print(result)


if __name__ == '__main__':
    # 输入贴吧的名称
    name = input('输入贴吧名称:')
    # 起始页
    start_page = int(input('输入起始页:'))
    # 截止页
    end_page = int(input('输入截止页:'))

    tiebaSpider(name,start_page,end_page)




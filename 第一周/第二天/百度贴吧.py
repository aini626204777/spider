from urllib import request, parse
import ssl, re
from fake_useragent import UserAgent

"""
step1:  分析贴吧中分页的url地址规律,要根据url构造请求
step2:  获取分页中帖子详情的url地址
"""


def searchSpider(name, start_page, end_page):
    url = "https://tieba.baidu.com/f?kw=%E7%BE%8E%E5%A5%B3&ie=utf-8&pn=0"
    for page in range(start_page, end_page + 1):
        parmars = {
            "kw": name,
            "ie": "utf-8",
            "pn": (page - 1) * 50,
        }
        result = parse.urlencode(parmars)
        full_url = 'https://tieba.baidu.com/f?' + result
        html = load_page(full_url)
        parse_detail_url(html)


def load_page(url):
    # 设置请求头
    req_header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
    }

    req = request.Request(url, headers=req_header)
    response = request.urlopen(req)
    if response.status == 200:
        return response.read().decode("utf-8","ignore")


def parse_detail_url(html):
    """

    :param html: 网页源代码
    :return:
    """
    pattern = re.compile(
        '<div.*?class="threadlist_title pull_left.*?j_th_tit.*?">.*?<a.*?rel="noreferrer".*?href="(.*?)".*?title=".*?".*?target="_blank".*?class="j_th_tit.*?">.*?</a>.*?</div>',
        re.S)
    detail_url_list = re.findall(pattern, html)
    parse_detail(detail_url_list)

def parse_detail(detail_url_list):

    for url in detail_url_list:
        detail_url = "https://tieba.baidu.com"+url
        html = load_page(detail_url)
        download_image(html)
        print('请求成功了')


# 下载详情image
def download_image(html):


    # with open("百度贴吧详情.html",'w') as f:
    #     f.write(html)
    pattern = re.compile('<img.*?class="BDE_Image".*?src="(.*?)".*?size=".*?".*?changedsize=".*?".*?width=".*?".*?height=".*?">',re.S)
    result = re.findall(pattern, html)
    for i in result:
        with open("百度贴吧图片/",'a') as f:
            f.write(i)


if __name__ == '__main__':
    # 模拟搜索引擎，根据关键字获取页面信息（ＨＴＭＬ页面源码）
    # 输入搜索关键字
    name = input("请输入搜索关键字：")
    # 起始页
    start_page = int(input('输入起始页：'))
    # 截止页
    end_page = int(input('输入截止页：'))
    searchSpider(name, start_page, end_page)

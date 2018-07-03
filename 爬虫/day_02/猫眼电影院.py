from urllib import request, parse
from urllib.request import urlopen
import requests
import ssl
import re
import pymysql


def main():
    # 目标网页
    url = 'http://maoyan.com/cinemas'

    # 获取网页响应头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }
    request_url = request.Request(url=url, headers=headers)
    response = urlopen(request_url)
    html = response.read().decode('utf-8')
    # print(html)
    a = re.compile('<a\sclass="page_19"\shref="(.*?)">下一页</a>', re.S)
    w = re.findall(a, html)
    print(w)
    # with open('猫眼电影院.html', 'w') as f:
    #     f.write(html)

    # content = re.compile('<a.*?href="(.*?)".*?class="cinema-name".*?>(.*?)</a>.*?<p.*?>(.*?)</p>', re.S)
    # w = re.findall(content, html)  # findall返回的是一个list列表
    # print(w)


if __name__ == '__main__':
    main()

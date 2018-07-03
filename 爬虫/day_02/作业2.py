# -*- coding:utf-8 -*-
# import urllib.request,urllib.parse
from urllib.request import Request, urlopen
import re


# 构造请求
# req = urllib.request.Request(url,headers)
# response = urllib.request.urlopen(req)
# req = Request(url,headers)
# response = urlopen(req)

def get_page_data(startpage, endpage, url):
    for i in range(startpage, endpage + 1):
        # 构建完整的目标URL
        fullurl = url + 'list%s.html' % i
        # 调用方法发起请求
        send_request(fullurl)
    print('任务添加成功')


def send_request(fullurl):
    print(fullurl + '正在下载')
    # 构造请求
    req = Request(fullurl)
    # 直接使用urlopen打开网址不是说这个方法不可以使用，而是当我们需要添加headers或
    # 则是其他参数的时候，有些参数这个方法没有，所以我们就需要使用Request构造请求
    response = urlopen(req)
    # response = urlopen(fullurl)
    html = response.read().decode('gbk')
    print()
    print(fullurl + '下载完成')
    # print(response.read().decode('gbk'))
    # <img src="http://www.yggk.net/xiaohua/uploads/allimg/151206/2_1206013353b62.jpg" alt="王馨瑶 广东外语外贸大学" target="_blank" width="184" height="274">
    compile1 = re.compile('<li.*?_Blank.*?<img.*?src="(.*?)".*?target="_blank.*?<p>(.*?)</p>', re.S)
    # result_images = re.findall(compile1,html)
    # print(result_images)
    compile2 = re.compile('<img.*?class="lazy".*?data-original="(.*?)".*?<p>(.*?)</p>', re.S)
    # result2_imges = re.findall(compile2,html)
    # print(result2_imges)
    result_images = re.findall(compile1, html) + re.findall(compile2, html)
    for info in result_images:
        download_image(info[1].replace(' ', '').replace('<b>', '').replace('</b>', ''), info[0])
        infotext = ':'.join(info).replace(' ', '').replace('<b>', '').replace('</b>', '')
        print(infotext)
        with open('xiaohua.txt', 'a') as f:
            f.write(infotext + '\n')


def download_image(filename, image_url):
    response = urlopen(image_url)
    filename = filename + image_url[-4:]
    data = response.read()
    print(type(response))
    print('正在下载图片' + filename)
    with open('校花图片/' + filename, 'wb+') as f:
        f.write(data)


if __name__ == '__main__':
    startpage = input('请输入开始页码（从1开始）：')
    endpage = input('请输入结束页码：')
    print(startpage, endpage)
    url = 'http://www.yggk.net/xiaohua/xiaohua/'
    get_page_data(int(startpage), int(endpage), url)

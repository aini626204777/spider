# -*- coding:utf-8 -*-
import urllib.request
from urllib import parse
import ssl

# 以豆瓣的电影搜索接口为例，构造get请求


def getajax():
    # 目标网站链接
    url = 'https://movie.douban.com/j/search_subjects?'  
    # 变动的参数
    data = {
        'page_limit': '20',
        'page_start': '40',
        'sort': 'recommend',
        'tag': '韩剧',
        'type': 'tv',
    }
    # 转换成url编码格式（字符串，这里不是post请求不用转换成字节，直接拼接在地址上）
    # 将变动的参数转换成url编码格式
    data = parse.urlencode(data)
    url = url+data
    print('urlencode转换后：'+data, '完整的get请求地址为：'+url)

    # 忽略未授权ＳＳＬ证书
    requestContext = ssl._create_unverified_context()
    # Request对象作为urlopen()方法的参数，发送给服务器并接受响应
    response = urllib.request.urlopen(url, context=requestContext)
    # 打印结果可以知道获取的结果为一个json串
    result = response.read()
    print(type(response))
    print(result)
    print(response.url)
    # print(type(dict))
    # print(dict)


if __name__ == '__main__':
    getajax()

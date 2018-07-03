# -*- coding:utf-8 -*-

import urllib.request as request
import http
import ssl
import requests


# 自定义opener
# 之前我们使用的是urlopen()
# request.urlopen()
# https_handler = HTTPSHandler(context=context)
# opener = build_opener(https_handler)

context = ssl._create_unverified_context()
# 构建一个HTTPSHandler 处理器对象，支持处理HTTP请求
https_handler = request.HTTPSHandler(context=context, debuglevel=1)
opener = request.build_opener(https_handler)
# 构建一个HTTPHandler 处理器对象，支持处理HTTPS请求
# http_handler = request.HTTPHandler()
# 调用urllib.request.Request方法，创建支持处理HTTP请求的opener对象
# opener = request.build_opener(http_handler)
req_header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
}
url = 'http://www.baidu.com'
req = request.Request(url, headers=req_header)
response = opener.open(req)
print(response.read().decode('utf-8'))
print(response.code)

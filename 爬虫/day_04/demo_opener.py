# -*- coding:utf-8 -*-
import urllib.request
import ssl

# 构建一个HTTPHandler处理器对象，支持处理HTTP请求
#http_handler = urllib.request.HTTPHandler()

# 调用urlli2.build_opener方法，创建支持处理HTTP请求的opener对象
opener = urllib.request.build_opener(urllib.request.HTTPSHandler(ssl._create_unverified_context()))

url = 'http://www.baidu.com'

request = urllib.request.Request(url)

response = opener.open(request)

print(response.code)
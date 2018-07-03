# 实质：urlopen　内部其实就是使用build_opener来创建了一个opener对象
# 最后将这个对象返回给我们

import urllib.request
import ssl


# urlopen　内部的简单实现原理、流程
# https_handler = HTTPSHandler(context=context)
# 设置这个参数表示我们可以忽略https请求协议
a = ssl._create_unverified_context()

# 构建一个handler,支持发送https请求
https_handler = urllib.request.HTTPSHandler(context=a)

#　创建一个opener
opener = urllib.request.build_opener(https_handler)
url = 'https://www.baidu.com'
# response = opener.open(url)
# print(response.code)
req = urllib.request.Request(url)
response = opener.open(req)
print(response.code)
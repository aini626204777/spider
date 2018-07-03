# coding:utf-8
import urllib.request as request
import ssl
import urllib.parse as parse

# 构造一个请求
# get请求
# 设置这个参数表示我们可以忽略https请求协议

context = ssl._create_unverified_context()

response = request.urlopen(
    'https://docs.python.org/3/library/urllib.html', context=context)

# 打印返回结果
# print(response.read().decode('utf-8'))

# 查看返回的结果类型
# print(type(response))

# # 查看返回的状态码
# print(response.status)

# # 读取返回相应的相应头
# print(response.getheaders())

# # 单独获取响应头里面其中的某一个数
# print(response.getheader('Content-Length'))

# urlopen(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
# *, cafile=None, capath=None, cadefault=False, context=None):

# data:data参数是可选择的，如果没有这个参数，那我们发起的请求默认是get
# 如果有这个参数，默认是post请求，如果要复制，那是字节类型（bytes）
# 创建一个post请求
datadict = {
    "name": "zhangsan",
    "sex": "1"
}

data = bytes(parse.urlencode(datadict), encoding='utf-8')
#data = parse.urlencode(datadict).encode('utf-8')
print(data)
request.urlopen('http://httpbin.org/post', data=data, context=context)
print(response.read().decode('utf-8'))
# {
#     "args":{},
#     "data":"",
#     "files":{},
#     "form":{
#          'name':'liwenhao'
#          'sex':'1'
#     },
#     "headers":
#     {"Accept-Encoding":"identity",
#     "Connection":"close",
#     "Content-Length":"9",
#     "Content-Type":"application/x-www-form-urlencoded",
#     "Host":"httpbin.org",
#     "User-Agent":"Python-urllib/3.6"
#     },
#     "json":null,
#     "origin":"114.242.248.195",
#     "url":"https://httpbin.org/post"
# }


# timeout: 设置请求的超时时间，一旦超过设置的值，就会报错
#

# cafile：指定CA证书
# capath：设置CA证书路径
# context：可以忽略https的请求协议

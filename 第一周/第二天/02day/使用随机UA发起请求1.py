from urllib import request
import random

USER_AGDNTS = [
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
]

url = 'http://www.baidu.com/'
#携带请求头,需要先创建一个Request对象
# url,:发起请求的url
# data=None, :默认为None,表示一个get请求
# headers={}:设置请求头，对应的是一个字典类型的参数
req_header = {
    'User-Agent':random.choice(USER_AGDNTS)
}
#构建一个request对象
req = request.Request(url,headers=req_header)

#根据Request对象发起请求
response = request.urlopen(req)

req_header1 = {
    'User-Agent':random.choice(USER_AGDNTS)
}

#构建一个request对象
req1 = request.Request(url,headers=req_header1)

#根据Request对象发起请求
response = request.urlopen(req1)

print(response.status)
print(response.read().decode('utf-8'))
print(response.getheaders())
print(response.getheader("Server"))
print(response.reason)
print(response.url)

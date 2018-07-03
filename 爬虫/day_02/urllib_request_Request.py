from urllib.request import Request, urlopen
# import urllib.request as reques
import urllib.parse as parse
import ssl

# urlopen(官方给我们封装的一个简单的发起请求的方法)


# def __init__(self, url, data=None, headers={},
#              origin_req_host=None, unverifiable=False,
#              method=None):
# url:这是我们需要请求的目标地址
# data：我们需要传入的相关参数，如果要传入的话必须是bytes类型
# headers：请求头，（cookis、Uesr-Agent、Referer、Connection)
# origin_req_host:指域名或者是ＩＰ
# method：请求方式(post、get)
# unverifiable：意思是说用户没有足够的权限来访问资源，默认是Ｆａｌｓｅ，表示我们有权限

# 构建一个请求对象
#url = 'https://www.ugirls.com/Models/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
}
# 构造了一个get方式的请求对象，设置了url、headers、请求发起
# req = Request(url, headers=headers, method='GET')

# response = urlopen(req)
# a = response.read().decode('utf-8')
# print(response.read().decode('utf-8'))

# with open('urllib_request_Request.html','w') as f:
#     f.write(a)
# https://www.baidu.com/s?wd=%E7%BE%8E%E5%A5%B3
# https://www.baidu.com/s?wd=美女

data = {
    'wd':'美女',
    'ie':'utf-8'
}
data = parse.urlencode(data)
url = 'https://www.baidu.com/s?'+data
# 转换成编码格式，在转换成字节类型
print(url)

#print(data)

# 忽略未授权的SSL证书
context = ssl._create_unverified_context()

# 调用Request传惨
req = Request(url,headers=headers)

# 打开目标网页
response = urlopen(req,context=context)

# 输出读取的数据 read()读取数据的意思
# print(response.read().decode('utf-8'))

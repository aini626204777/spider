# urllib下使用代理
# http/https代理
# 一定是一个高匿代理
# 隐藏真是IP
from urllib import request,error


# 自定义ProxyHandler的目的是为了设置代理，使用代理发起请求
# proxies:对应的是一个字典
proxies = {
    'HTTP':'183.47.40.35',
    'HTTPS':'118.122.92.252',
}
# req_header = {
#     "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
# }
url = 'https://www.baidu.com/'



handler = request.ProxyHandler(proxies=proxies)

opener = request.build_opener(handler)

response = opener.open(url)
print(response.status)
result = response.read().decode('utf8')
print(result)
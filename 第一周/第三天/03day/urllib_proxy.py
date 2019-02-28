# urllib下使用代理
#　http/https代理
# 一定是一个高匿代理理
# 隐藏真实ip

from urllib import request

#自定义ProxyHandler的目的是为了设置代理,使用代理发起请求
#proxies:对应的是一个字典
# 代理有免费代理（西刺,快代理.....）
# 和收费代理 (西刺,快代理.....,阿布云．．．．)
# proxies = {
#     'http':'118.187.58.34:53281',
#     'https':'124.235.180.121:80',
# }

#独享代理,需要账号密码做验证的
proxies = {
    'http':'http://2295808193:6can7hyh@106.12.23.200:16818',
    'https':'https://2295808193:6can7hyh@106.12.23.200:16818'
}
handler = request.ProxyHandler(proxies=proxies)

#自定义opener
opener = request.build_opener(handler)

#url地址
#https://httpbin.org/get
url = 'http://httpbin.org/get'

response = opener.open(url)

print(response.status)
print(response.read().decode('utf-8'))




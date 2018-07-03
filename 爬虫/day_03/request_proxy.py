import urllib.request
import urllib.parse
import ssl

#使用代理
# 构建一个proxyhandler对象

proxy_handler = urllib.request.ProxyHandler({
    'http':'221.232.233.61:808'
})

context = ssl._create_unverified_context()
opener = urllib.request.build_opener(proxy_handler,urllib.request.HTTPSHandler(context=context))
# 将自定义的opener对象设置为全局的，那系统的urlopen方法就使用你创建的opener方法
# urllib.request.install_opener(opener)

#get请求
# url = 'https://www.baidu.com'
# get_req = urllib.request.Request(url)
# #如果上面使用了install_opener方法，那么这里调用urlopen方法就会使用你创建的opener方法
# #response = urllib.request.urlopen(get_req)
# response = opener.open(get_req)
# #print(response.get_IP)
# print(response.code)
# #print(response.read().decode('utf-8'))
# #print(response.getheaders())

#post请求
url = 'https://httpbin.org/post'
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
    'Host':'httpbin.org'
}
data = {
    'pagenum':'3',
    'password':'woshiniba',
}
data = urllib.parse.urlencode(data).encode('utf-8')
print(data)
post_req = urllib.request.Request(url,headers=headers,data=data,method='POST')
# 如果上面使用了install_opener方法，那么这里调用urlopen方法就会使用你创建的opener方法
# response = urllib.request.urlopen(req,context=context)
response = opener.open(post_req)

print(response.code)
#print(response.read().decode('utf-8'))
#print(response.getheaders())
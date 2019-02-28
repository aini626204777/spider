from urllib import request
import ssl

url = 'http://www.baidu.com/'

# url:发起请求的url
# data:默认为None,表示一个get请求
# timeout:设置请求的超时时间
# context:ssl._create_unverified_context()(忽略ssl证书认证)

response = request.urlopen(url,timeout=10,context=ssl._create_unverified_context())

#携带请求头,需要先创建一个Request对象
# url,:发起请求的url
# data=None, :默认为None,表示一个get请求
# headers={}:设置请求头，对应的是一个字典类型的参数
req_header = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}
#构建一个request对象
req = request.Request(url,headers=req_header)

#根据Request对象发起请求
response = request.urlopen(req)

print(response.status)
print(response.read().decode('utf-8'))
print(response.getheaders())
print(response.getheader("Server"))
print(response.reason)
print(response.url)


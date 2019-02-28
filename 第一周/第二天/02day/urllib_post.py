#测试接口：https://httpbin.org/post
from urllib import parse,request

url = 'https://httpbin.org/post'

#表单数据
fordata = {
    'name':'红红火火',
    'age':18,
    'gender':'男'
}

#先使用urlencode将参数转为url编码格式的字符串,
# 然后在使用encode()方法将字符串转为bytes类型的参数
formdata = parse.urlencode(fordata).encode('utf-8')

#不需要添加请求头
response = request.urlopen(url,data=formdata)
print(response.status)
print(response.read().decode('utf-8'))

#需要设置请求头
red_header = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
req = request.Request(url,headers=red_header,data=formdata)
response = request.urlopen(req)
print(response.status)
print(response.read().decode('utf-8'))





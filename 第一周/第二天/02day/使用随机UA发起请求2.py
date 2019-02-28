#pip3 install fake-useragent
from fake_useragent import UserAgent

#实例化一个UA
user_agent = UserAgent()

#获取google浏览器的ua
print(user_agent.chrome)
#获取火狐浏览器的ua
print(user_agent.firefox)
#获取safar浏览器的ua
print(user_agent.safari)

#随机获取ua
print('-------------')
print(user_agent.random)
print(user_agent.random)
print(user_agent.random)
print(user_agent.random)

from urllib import request
# import ssl
#目标url
url = 'https://github.com/hellysmile/fake-useragent'
#构建请求头
req_header = {
    'User-Agent':user_agent.random
}
#构建一个Request对象
req = request.Request(url,headers=req_header)
#另一种方式添加请求头
req.add_header('Referer','https://github.com/search?q=fake-useragent')
#从请求头中取出一个请求头的参数
print(req.get_header('Referer'))
#发起请求
response = request.urlopen(req,timeout=10)

print(response.status)
print(response.url)



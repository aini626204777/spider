# urllib使用代理
# 服务器吧咱们的ip封掉：请求的次数过于频繁，超过服务器设定的阀值

import urllib.request

# 构建一个代理的ProxyHandler对象
proxy_handler = urllib.request.ProxyHandler({'http':'221.232.233.61:808'})

# 需要用户名和密码的代理(需要验证)
#urllib.request.ProxyHandler({"协议":'用户名:密码@ip+端口号'})

opener = urllib.request.build_opener(proxy_handler)

# 使用opener.open方法去发起请求
response = opener.open('http://www.baidu.com')

# 查看相应的结果
print(response.code)
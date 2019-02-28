from urllib import request  
import ssl

url = 'http://www.baidu.com/'

"""
url:    发起请求的url
data:   默认为None,表示一个get请求
timeout:    设置请求的超时时间
context:    ssl._create_unverified_context()(忽略ssl证书认证)
"""


response = request.urlopen(url,timeout=10,context=ssl._create_unverified_context())
print(response.status)


# pip install request
# http://docs.python-requests.org/zh_CN/latest/
import requests
import urllib.parse as parse

# 使用reuqests发起一个get请求
#response = requests.get('http://docs.python-requests.org/zh_CN/latest/')

# 输出响应状态
#print(response.status_code)
dict = {
    'wd':'美女',
}
# 发起一个请求默认是会验证SSL证书，这里verify设置为False意思就是关闭（忽略）ＳＳＬ验证
# response = requests.get('https://www.baidu.com/s?',params=dict)

# 设置代理
proxy = {
    'https':'121.41.171.223:3128',
}
response = requests.get('https://www.baidu.com/s?',params=dict,proxies=proxy)
print(response.headers)
print(response.url)
print(response.text)
print(response.status_code)
# print(type(response))
# res = response.cookies
# print(res.items())
#
# print(res)
# cookie_str = ''
# for item in res:
#     cookie_str = cookie_str + item.name+'='+item.value
#     print(cookie_str)
#
#


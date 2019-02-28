#requests下使用cookies

import requests
#分析发现
# https://www.douban.com/accounts/login
# 没有验证码的情况
# source: index_nav
# form_email: 18518753265
# form_password: ljh12345678

#有验证码的情况
# source: index_nav
# form_email: 18518753265
# form_password: ljh12345678
# captcha-solution: blade
# captcha-id: 5IBtw5wm2riyrIrnV3utwUPt:en

url = 'https://www.douban.com/accounts/login'

form_data = {
    'source': 'index_nav',
    'form_email': '18518753265',
    'form_password': 'ljh12345678',
    'captcha-solution': 'violent',
    'captcha-id': 'AuKNJ1FIktyrmpljJ6WAzXo3:en'
}

#设置请求头
req_header = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

#发起请求
response = requests.post(url,headers=req_header,data=form_data)

#使用response.cookies获取cookies信息
print('模拟登录后的cookies信息',response.cookies)
print(type(response.cookies))
print(response.headers)

with open('douban.html','w') as file:
    file.write(response.text)

#requests.utils.cookiejar_from_dict():将字典转为cookiejar
#requests.utils.dict_from_cookiejar():将cookiejar转为字典
cookies_dict = requests.utils.dict_from_cookiejar(response.cookies)
print(cookies_dict)
#登录成功后访问个人主页,能够成功获取到个人主页信息,说明确实保存了cookie
#并且在一下次发起请求的时候携带了cookie
url = 'https://www.douban.com/people/175417123/'
#设置cookies参数,模拟用户发起请求
response = requests.get(url,headers=req_header,cookies=cookies_dict)

if response.status_code == 200:

    with open('douban1.html','w') as file:

        file.write(response.text)



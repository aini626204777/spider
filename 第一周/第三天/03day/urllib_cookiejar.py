#使用cookiejar的目的：管理cookie,保存cookie值,
#一旦存储cookie之后,下一次发起请求的时候就会携带cookie
#cookie是保存在内存里面的,最后会进行垃圾回收

from urllib import request,parse
from http.cookiejar import CookieJar

#创建cookiejar对象,目的如上
cookie_jar = CookieJar()

#HTTPCookieProcessor创建handle处理器,管理cookiejar
handler = request.HTTPCookieProcessor(cookie_jar)

#自定义opener
opener = request.build_opener(handler)

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

url = 'https://accounts.douban.com/login'

form_data = {
    'source': 'index_nav',
    'form_email': '18518753265',
    'form_password': 'ljh12345678',
    'captcha-solution': 'science',
    'captcha-id': 'PcPUVYrRWIai40vo7CCdefb2:en'
}

form_data = parse.urlencode(form_data).encode('utf-8')

#设置请求头
req_header = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

#够建一个request对象
req = request.Request(url,headers=req_header,data=form_data)

#发起请求
response = opener.open(req)

#登录成功后访问个人主页,能够成功获取到个人主页信息,说明确实保存了cookie
#并且在一下次发起请求的时候携带了cookie
url = 'https://www.douban.com/people/175417123/'

req = request.Request(url,headers=req_header)

response = opener.open(req)

if response.status == 200:
    with open('douban.html','w') as file:
        file.write(response.read().decode('utf-8'))






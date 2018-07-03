#HTTPCookiesHandler:处理cookies
import urllib.request 
import ssl

# 根据cookies来获取个人主页：
# url = 'https://weibo.com/5920075959/profile?topnav=1&wvr=6&is_all=1'

# headers = {
#     'Host':'weibo.com',
#     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
#     'Cookie':'TC-Ugrow-G0=e66b2e50a7e7f417f6cc12eec600f517; SUB=_2A252EK22DeThGeNH6VIR9yvFzjWIHXVVZ5h-rDV8PUNbmtAKLUHckW9NSsdPGVoExlUofwwt1-4UsXZ6UUEJshER; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFIFiDO8kIDkQ9bBGWfrzWY5JpX5KzhUgL.Fo-4eo57S0-4SK.2dJLoIE5LxK-LBo5L12qLxK.L1-BL1KzLxK-LBo.LBoBcehnf15tt; login_sid_t=800b40406275a6c52f097b0ece65053e; cross_origin_proto=SSL; TC-V5-G0=866fef700b11606a930f0b3297300d95; WBStorage=5548c0baa42e6f3d|undefined; _s_tentry=passport.weibo.com; wb_view_log=800*6001; Apache=2512513009409.145.1528094145478; SINAGLOBAL=2512513009409.145.1528094145478; ULV=1528094145547:1:1:1:2512513009409.145.1528094145478:; WBtopGlobal_register_version=cd58c0d338fe446e; crossidccode=CODE-tc-1FpJ6a-26vTGX-9Ce1Fx2W3GPpCGNbce022; SUHB=02M_NZcrmQYvsK; ALF=1559630180; SSOLoginState=1528094181; wvr=6; TC-Page-G0=07e0932d682fda4e14f38fbcb20fac81; UOR=,,graph.qq.com'
# }
# context = ssl._create_unverified_context()

# req = urllib.request.Request(url,headers=headers)
# response = urllib.request.urlopen(req,context=context)
# with open('person.html','w') as f:
#     f.write(response.read().decode('utf-8'))
# print(response.code)

# cookiejar()
import http.cookiejar as cookiejar
import urllib.request

#构建一个cookies对象，为我们存储cookie值
cookie = cookiejar.CookieJar()
#创建一个handler处理器，来进行cookie的一些操作
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)
#构建一个opener，来让我们想服务器发起请求
opener = urllib.request.build_opener(cookie_handler)
url = 'http://www.baidu.com'
response = opener.open(url)
# print(response.code)
# print(cookie)
# print(type(cookie))
# for item in cookie:
#     print(item.value)
#     print(item.name)

# 使用MozillaCookieJar,它可以直接将
# 我们获取的cookie保存到指定的文件下
cookie_file = 'cookie.txt'

#构建一个使用MozillaCookieJar对象，来保存cookie
mz_cookie = cookiejar.MozillaCookieJar(cookie_file)

mz_cookie.load(cookie_file)

print(mz_cookie)

# #创建一个handler处理器对象，来进行cookie的一些操作
mz_cookie_handler = urllib.request.HTTPCookieProcessor(mz_cookie)
# #创建一个opener对象
opener = urllib.request.build_opener(mz_cookie_handler)
response = opener.open(url)
# #保存cookie到指定的文件
mz_cookie.save() 








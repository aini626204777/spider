import urllib.request
import http.cookiejar

# # 创建一个cookiesjar对象，他用来使用存储cookie的
# cookie = http.cookiejar.CookieJar()

# # 构建一个cookie的处理器对象handler
# cookie_handle = urllib.request.HTTPCookieProcessor(cookie)

# # 作用构建opener
# opener = urllib.request.build_opener(cookie_handle)

# # 使用open方法项服务器发送请求，获取相应
# response = opener.open('http://www.baidu.com')

# print(response.code)
# print(cookie)
# for item in cookie:

#     cookie_str = cookie_str + item.name+'='+item.value+';'
# print(cookie_str)



# mozillaCookieJar():可以直接指定保存的文件，使用save()方法保存
cookie_file = 'cookie.txt'

# 构建一个　mozillaCOokieJar　对象来保存cookie
mz_cookie = http.cookiejar.MozillaCookieJar(cookie_file)

# 构建一个cookie处理器对象
handle = urllib.request.HTTPCookieProcessor(mz_cookie)

# 构建一个opener对象
opener = urllib.request.build_opener(handle)

#　把ｏｐｅｎｅｒ改变成全局的
urllib.request.install_opener(opener)
urllib.request.urlopen
# 发送请求（打开url）
response = opener.open('http://www.baidu.com')

# 保存方法cookie
mz_cookie.save

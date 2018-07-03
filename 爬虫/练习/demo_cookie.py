import urllib.request

url = 'http://www.renren.com'

# 根据刚才的信息来构建一个已经登录过的用户headers信息
headers = {
    'cache-control': 'max-age=0',
    'content-encoding': 'gzip',
    'content-length': '1362',
    'content-security-policy': 'referrer origin; script-src '
                               "self"
                               ' https://hm.baidu.com http://hm.baidu.com *.google-analytics.com http://mat1.gtimg.com https://mat1.gtimg.com http://*.soso.com https://*.soso.com http://*.qq.com https://*.qq.com http://*.qqmail.com  https://*.qqmail.com http://pub.idqqimg.com blob: '
                               "unsafe - inline"
                               ' '
                               "unsafe - eval"
                               '; report-uri https://mail.qq.com/cgi-bin/report_cgi?r_subtype=csp&nocheck=false',
    'content-type': 'text/html;charset=GB18030',
    'date': ' Tue, 05 Jun 2018 12:24:00 GMT',
    'referrer-policy': 'origin',
    'server': 'nginx',
    'status': '200',
}

# 2.通过headers里的报头信息（主要是Ｃｏｏｋｉｅ信息），构建Request对象

request = urllib.request.Request(url, headers=headers)

# 3. 直接访问renren主页，服务器会根据headers报头信息（主要是Cookie信息）
# ，判断这是一个已经登录的用户，并返回相应的页面
response = urllib.request.urlopen(request)

# 4. 打印响应内容
print(type(response.read()))

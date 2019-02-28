#urllib的parse模块主要是实现url的解析,合并,编码,解码

from urllib import  parse

#parse.urlparse实现了url的识别和分段
url = 'https://www.1712B.com/daxuesheng?name=zhangsan#123'
"""
url,：要解析和才分的url
scheme='':设置协议,只有在url没有协议的情况下才会生效
allow_fragments=True:是否忽略锚点,默认为True表示不忽略
"""
result = parse.urlparse(url)
"""
(scheme='https'（协议）, netloc='www.1712B.com'（域）, 
path='/daxuesheng'（路径）, params=''（可选参数）, 
query='name=zhangsan'（查询参数）, fragment='123'（锚点）)
"""
print(result)
#取出才分后的某一个参数
print(result.scheme)

#parse.urlunparse可以实现url的组合
data = [sub_str for sub_str in result]
print('-----',data)
full_url = parse.urlunparse(data)
print(full_url)

#parse.uurlrljoin需要传递一个基类url,根据基类将某一个不完整的url拼接完整
sub_url = '/p/123456'
base_url = 'https://www.1712B.com/daxuesheng?name=zhangsan#123'
full_url = parse.urljoin(base_url,sub_url)
print('urljoin',full_url)

#parse.urlencode将字典类型的参数,序列化为url的编码格式的字符串
parmars = {
    'name':'张三',
    'class':'1712B',
}
result = parse.urlencode(parmars)
print('urlencode',result)

#parse.parse_qs反序列化,将url编码格式的字符串,转为字典类型
result = parse.parse_qs(result)
print('parse_qs',result)

#parse.quote可以将中文字符,转为url编码格式
kw = '摸摸摸'
result = parse.quote(kw)
print('quote',result)

#将url编码进行解码
result = parse.unquote(result)
print('unquote',result)


# 最最常用的urljoin,urlencode两个方法
#urllib.parse:解析url，拼接、编码
import urllib.parse 
#urlparse：拆分一个url连接，分解出各个组成部分
#https://www.baidu.com/s?ie=utf-8&f=8&&tn=baidu&wd=%E7%BE%8E%E5%A5%B3
url = 'https://www.baidu.com/s?&ie=utf-8&f=8&&tn=baidu&wd=%E7%BE%8E%E5%A5%B3#nscks'

result = urllib.parse.urlparse(url)
print(result)
#scheme='https', netloc='www.baidu.com', path='/s', params='',
#query=':uers=a&ie=utf-8&f=8&&tn=baidu&wd=%E7%BE%8E%E5%A5%B3', fragment='nscks'
# scheme:协议
# netloc:域名
# path：路径
# params：参数
# query：查询条件参数，一般用于get请求
# fragment：锚点

#urlunparse 拼接
urls = ('https','www.baidu.com','s','','ie=utf-8','a')
fullurl = urllib.parse.urlunparse(urls)
print(fullurl)

#urlencode:一般用于将字典序列化为url编码的格式
dict = {
    'name':'xknc',
    'password':'lw12354346',
}
# data = urllib.parse.urlencode(dict).encode('UTF-8')
data = bytes(urllib.parse.urlencode(dict),encoding='UTF-8')
print(data)

#parse_qs:将url编码的格式反序列化为字典
result = urllib.parse.parse_qs(data)
print(result)
for k,v in result.items():
    print(k.decode('UTF-8'))
    print(v[0].decode('UTF-8'))

#urljoin:url的拼接
# http://maoyan.com/cinema/25292?poi=171087924
base_url = 'http://maoyan.com/cinemas'
son_url = '/cinema/15331?poi=95489636'
fullurl = urllib.parse.urljoin(base_url,son_url)
#http://maoyan.com/cinema/15331?poi=95489636拼接的结果
print(fullurl)




from urllib import parse
# urllib的parse模块主要是实现url的解析，合并，编码，解码






# 实现了url的识别和分段
url = "https://www.1712B.com/"
"""
url：要解析和拆分的url
scheme：设置协议，只有
"""
result = parse.urlparse(url)

data = [ i for i in result]
full_url = parse.urlunparse(data)
sub_url = '?/daxuesheng/'

result1 = parse.urljoin(url,sub_url)

parmars = {
    'name':'123',
    'class':'1712B',
}
result2 = parse.urlencode(parmars)
print(result2)

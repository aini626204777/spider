from urllib import parse, request
from fake_useragent import UserAgent
import json

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'

formdata = {
    'i': '我的祖国',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION',
    'typoResult': 'false',
}

formdata = parse.urlencode(formdata).encode("utf-8")

req_header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

req = request.Request(url, headers=req_header, data=formdata)
response = request.urlopen(req)
print(response.status)

json_str = response.read().decode('utf-8')
json_str = json.loads(json_str)
print(json_str)

from urllib import parse, request
from fake_useragent import UserAgent
import json

url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

formdata = {
    'first': 'true',
    'pn': '1',
    'kd': 'c++',
}

formdata = parse.urlencode(formdata).encode('utf-8')
req_header = {
    'User-Agent': UserAgent().chrome,
    'Referer': 'https://www.lagou.com/jobs/list_c%2B%2B?labelWords=&fromSearch=true&suginput=',
}

req = request.Request(url, headers=req_header, data=formdata)
response = request.urlopen(req)
print(response.status)
json_str = response.read().decode('utf-8')
json_str = json.loads(json_str)
print(json_str)
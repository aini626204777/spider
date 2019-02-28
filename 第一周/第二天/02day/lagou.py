#https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false
from urllib import parse,request

url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

formdata = {
    'first': 'true',
    'pn': '1',
    'kd': 'c++'
}

formdata = parse.urlencode(formdata).encode('utf-8')

req_header = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Referer':'https://www.lagou.com/jobs/list_c%2B%2B?labelWords=&fromSearch=true&suginput=',
}

req = request.Request(url,headers=req_header,data=formdata)

response = request.urlopen(req)

print(response.status)
print(response.read().decode('utf-8'))


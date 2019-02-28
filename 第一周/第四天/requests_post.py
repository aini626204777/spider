import requests

url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
formdata = {
'first': 'true',
'pn': 1,
'kd': 'python',
}
req_headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
response = requests.post(url=url,data=formdata,headers=req_headers)


# 可以将返回的json字符串转为python数据类型
data = response.json()
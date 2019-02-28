import requests

url = 'https://accounts.douban.com/login'
fromdata = {
    'source':'None',
    'form_email': '18518753265',
    'form_password': 'ljh12345678',
    'captcha-solution': 'scissors',
    'captcha-id': 'SBlWhx634JvSMb2KFyclML9o:en',
}

req_headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
}

response = requests.post(url,headers=req_headers,data=fromdata)



cookie_dict = requests.utils.dict_from_cookiejar(response.cookies)
url1 = 'https://www.douban.com/people/175417123/'
response = requests.get(url=url1,headers=req_headers,cookies=cookie_dict)
if response.status_code == 200:
    with open('douban.html','w') as f:
        f.write(response.text)
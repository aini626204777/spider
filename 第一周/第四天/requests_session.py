# requests.session()维持会话,可以让我们在跨请求时保存某些参数

import requests

# 实例化session
session = requests.session()

# 目标url
url = 'https://www.douban.com/accounts/login'

form_data = {
    'source': 'index_nav',
    'form_email': '18518753265',
    'form_password': 'ljh12345678',
    'captcha-solution': 'harmony',
    'captcha-id': 'CBBUipaibipC6lfsfhWV5wDd:en'
}

req_header = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}


response = session.post(url=url,headers=req_header,data=form_data)
if response.status_code == 200:
    url = 'https://www.douban.com/people/175417123/'
    response = session.get(url=url,headers=req_header)
    if response.status_code == 200:
        with open('douban2.html','w') as f:
            f.write(response.text)
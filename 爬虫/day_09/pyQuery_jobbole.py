# -*- coding:utf-8 -*-
from pyquery import PyQuery
import lxml
import requests




url = 'http://blog.jobbole.com/all-posts/'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
}
response = requests.get(url=url,headers=headers)
print(response.status_code)
with open('jobbole.html','w') as f:
    f.write(response.text)

pq_html = PyQuery(response.text)
# print(type(pq_html))
# print(pq_html.html())

print(pq_html('.post floated-thumb'))
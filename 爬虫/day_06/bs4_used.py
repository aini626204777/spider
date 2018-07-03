from bs4 import BeautifulSoup
import requests
import ssl
url = 'https://hr.tencent.com/position.php?&start=0#a'

content = ssl._create_unverified_context()
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}

response = requests.get(url=url,headers=headers)

html  = response.text

soup = BeautifulSoup(html,'lxml')

tr_result = soup.find_all(class_='even')
#print(tr_result)
for tr in tr_result:
#    title = tr.select('td a').get_text()
    print(tr)
#   print(tr.attrs)
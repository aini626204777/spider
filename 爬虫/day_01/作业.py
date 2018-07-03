from urllib import request,parse

data = {
    'fr': 'homepc_menu_news'
}
data = parse.urlencode(data)
url = 'http://www.1905.com/film/?'+data

request = request.urlopen(url=url)
response = request.read().decode('utf-8')

with open('电影网_1905.html','w') as f:
    f.write(response)
from urllib.request import Request,urlopen
import urllib.parse as parse
import ssl

data = {
    'q':'龙',
    'fr':'wwwsearch_header_search_20150205',
    'ie':'utf-8'
}
header = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
}
data = parse.urlencode(data)
url = 'http://www.1905.com/search/?' + data

req = Request(url,headers=header)
context = ssl._create_unverified_context
response = urlopen(req,context=context)
print(response.read().decode('utf-8'))
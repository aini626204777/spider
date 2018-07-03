from  urllib.request import Request,urlopen
import urllib.parse as parse
import re
import ssl


url = ('https://read.qidian.com/chapter/xgiLUq4wzJZgi2M3GqM4mg2/MXHqbmEjl4zM5j8_3RRvhw2')

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}
data = {
    'ie':'utf-8'
}
req = Request(url,headers=headers)
context = ssl._create_unverified_context()
response = urlopen(req,context=context)
a = response.read().decode('utf-8')
print('获取数据中')

pattern = re.compile('<div.*?read-content.*?>(.*?)</div>',re.S)
f_list = re.findall(pattern,a)
print(f_list)
print('获取数据成功')
with open('起点中文网.text','w') as f:
    f.write(str(f_list))
    f.close()
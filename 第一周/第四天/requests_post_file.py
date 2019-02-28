import requests

# 测试接口
url = 'https://httpbin.org/post'

files = {
    'file':open('cook.txt','r')
}

response = requests.post(url,files=files)
print(response.text)
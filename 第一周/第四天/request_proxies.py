import requests

url = 'https://httpbin.org/get'
proxies = {
    'http':'',
    'https':'',
}

response = requests.get(url=url,proxies=proxies)
print(response.text)
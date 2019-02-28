#
import requests

url = 'https://www.baidu.com/'

#verify:默认为True,表示需要进行CA证书认证,
#如果在请求网站的过程中遇到的ssl证书认证问题
#只需将verify改为False
response = requests.get(url,verify=False)

print(response.status_code)
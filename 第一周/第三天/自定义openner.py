from urllib import request
from fake_useragent import UserAgent

url = 'https://www.baidu.com/'

req_header = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
}
req = request.Request(url,headers=req_header)

def send_request(req,timeout=5,context=None):
    """

    :param req: request请求对象
    :param timeout: 设置请求超时时间
    :param context: 忽略ssl安全证书
    :return:
    """

    if context:
        handler = request.HTTPSHandler(context=context)
        opener = request.build_opener(handler)
        return opener.open(req,timeout=timeout)

    else:
        # debuglevel默认为０，默认为１的时候表示
        handler = request.HTTPSHandler(debuglevel=1)
        opener = request.build_opener(handler)
        return opener.open(req,timeout=timeout)



if __name__ == '__main__':
    response = send_request(req)
    result = response.read().decode('utf8')
    print(result)
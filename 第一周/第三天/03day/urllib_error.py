#　urllib.error:在发起请求的过程中,可能会因为各种情况
# 导致请求出现异常,因而导致代码崩溃,所以我们悬疑处理这些异常的请求

from urllib import error,request

# error.URLError

def check_urlerror():
    """
    1.没有网络
    2.服务器连接失败
    3.找不到指定服务器
    :return:
    """
    url = 'http://www.baidu.com/'
    try:
        response = request.urlopen(url,timeout=0.01)
        print(response.status)
    except error.URLError as err:
        #[Errno -2] Name or service not known(未知服务器)
        #timed out:请求超时
        #[Errno -3] Temporary failure in name resolution(没网)
        print(err.reason)

# check_urlerror()

# error.HTTPError是URLError的子类

def check_httperror():
    url = 'https://www.qidian.com/all/nsacnscn.htm'
    try:
        response = request.urlopen(url)
        print(response.status)
    except error.HTTPError as err:
        #HTTPError的三个属性
        #状态码
        print(err.code)
        #返回错误的原因
        print(err.reason)
        #返回响应头
        print(err.headers)
    except error.URLError as err:
        print(err.reason)

check_httperror()







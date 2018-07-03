from urllib.request import Request, urlopen
import urllib.parse as parse
import ssl


def tiebaSpider(url, beginPage, endPage):

    for page in range(beginPage, endPage + 1):
        pn = (page - 1) * 50

        filename = "第" + str(page) + '页.html'
        fullurl = url + "&pn=" + str(pn)
        html = loadPage(fullurl, filename)

        writeFile(html, filename)


def loadPage(url, filename):
    print('正在下载' + filename)

    # 　忽略SSL未授权证书
    requestContent = ssl._create_unverified_context()
    #
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;'}

    #
    request = Request(url, headers=headers)
    response = urlopen(request, context=requestContent)
    return response.read()


def writeFile(html, filename):
    print('正在存储' + filename)
    with open(filename, 'wb') as f:
        f.write(html)
    print('__' * 20)


if __name__ == '__main__':
    kw = input('请输入需要爬去的贴吧:')

    # 输入起始页和终止页，str转成int类型
    beginPage = int(input('请输入起始页：'))
    endPage = int(input('请输入终止页：'))

    url = 'https://www.baidu.com/s?'
    key = parse.urlencode({'wd': kw})

    # 组合后的url示例：
    url = url + key
    tiebaSpider(url, beginPage, endPage)

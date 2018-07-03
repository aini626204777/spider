from urllib.request import Request, urlopen
import urllib.parse as parse
import ssl
import re


def get_page_data(startpage, endpage, url):
    for i in range(startpage, endpage+1):
        fullurl = (i-1)*12
        url = url+str(fullurl)
        create_request(url)


def create_request(fullurl):
    req = Request(fullurl)
    content = ssl._create_unverified_context()
    response = urlopen(req, context=content)
    a = response.read().decode('utf-8')
    cinema_name = re.compile(
        '<div.*?class="cinema-info">.*?<a\s(.*?)\sclass="cinema-name".*?>(.*?)</a>.*?<p.*?class="cinema-address">(.*?)</p>.*?</div>', re.S)
    cinema = re.findall(cinema_name, a)

    print(cinema)
    for i in cinema:
        with open('maoyan.txt', 'a') as f:
            f.write(str(i)+'\n')


if __name__ == '__main__':

    url = 'http://maoyan.com/cinemas?offset='
    a = int(input('请输入起始页：'))
    b = int(input('请输入结束页：'))
    get_page_data(a, b, url)

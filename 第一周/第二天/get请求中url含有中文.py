from urllib import parse, request
from fake_useragent import UserAgent

def searchSpider(kw, start_page, end_page):
    url = "https://www.baidu.com/s?wd=%E9%A9%AC%E4%BA%91&pn=0"
    # quote,将中文转换为url能够识别的编码格式
    quote_str = parse.quote(kw)
    print(quote_str)
    unquote_str = parse.unquote(quote_str)
    print(unquote_str)

    for page in range(start_page,end_page+1):
        # 将字典类型的参数，转换为url的编码格式
        parmars = {
            "wd": kw,
            "pn": (page-1)*10,
        }
        result = parse.urlencode(parmars)
        print(result)

        full_url = "https://www.baidu.com/s?"+str(result)
        html = load_page(full_url)
        filename = "第"+ str(page) +"页源码.html"
        save_html(html,filename)

def save_html(html,filename):
    """

    :param html: 页面源码
    :param filename: 本地文件名字
    :return:
    """
    
    with open("get请求中url含有中文网页源码/"+filename,'w') as f:
        f.write(html)

def load_page(url):
    req_header = {
        "User-Agent":UserAgent().chrome
    }

    req = request.Request(url,headers=req_header)
    response = request.urlopen(req)
    if response.status == 200:
        print("请求成功！！！")
        return response.read().decode("utf-8")

if __name__ == '__main__':
    # 模拟搜索引擎，根据关键字获取页面信息（ＨＴＭＬ页面源码）
    # 输入搜索关键字
    kw = input("请输入搜索关键字：")
    # 起始页
    start_page = int(input('输入起始页：'))
    # 截止页
    endpage = int(input('输入截止页'))
    searchSpider(kw,start_page,endpage)

"""
https://www.baidu.com/s?wd=%E9%A9%AC%E4%BA%91&rsv_spt=1
&rsv_iqid=0x962113ef0005b240&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8
&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=10&rsv_sug1=5
&rsv_sug7=101&rsv_sug2=0&inputT=3634&rsv_sug4=3635

https://www.baidu.com/s?wd=%E9%A9%AC%E4%BA%91&pn=10
&oq=%E9%A9%AC%E4%BA%91&tn=baiduhome_pg&ie=utf-8&usm=2
&rsv_idx=2&rsv_pq=ffa41cb40006e584
&rsv_t=8f12fcc%2B7V33X1AZGK%2F8rG15hyChSHBEib036c9MrPUoMhDHodySMe5YiBvt%2FYjSXq6r

https://www.baidu.com/s?wd=%E9%A9%AC%E4%BA%91&pn=20
&oq=%E9%A9%AC%E4%BA%91&tn=baiduhome_pg
&ie=utf-8&usm=2&rsv_idx=2
&rsv_pq=a0332c960006ab8b&rsv_t=00a8H9naD%2BndSHikIPyV64OHbv0MDhlgyW8ZT3ejnLRYgCnj3C0R5qSDboOnnELbpXij

https://www.baidu.com/s?wd=%E9%A9%AC%E4%BA%91&pn=30
&oq=%E9%A9%AC%E4%BA%91&tn=baiduhome_pg
&ie=utf-8&usm=2&rsv_idx=2
&rsv_pq=a0332c960006ab8b&rsv_t=00a8H9naD%2BndSHikIPyV64OHbv0MDhlgyW8ZT3ejnLRYgCnj3C0R5qSDboOnnELbpXij

https://www.baidu.com/s?wd=%E9%A9%AC%E4%BA%91&pn=30
&oq=%E9%A9%AC%E4%BA%91&tn=baiduhome_pg
&ie=utf-8&usm=2&rsv_idx=2
&rsv_pq=97faa0350005fc78&rsv_t=3ec0E%2BrXDSShhTxdSamXBhkNv6%2FyuVU2V5BOOh8JoLuRt3iQh9pOtpre%2Flotf358N9rp

"""

"""
https://www.baidu.com/s?wd=%E9%A9%AC%E4%BA%91&pn=0
https://www.baidu.com/s?wd=%E9%A9%AC%E4%BA%91&pn=10
https://www.baidu.com/s?wd=%E9%A9%AC%E4%BA%91&pn=20
https://www.baidu.com/s?wd=%E9%A9%AC%E4%BA%91&pn=30
"""
from urllib import parse,request
from fake_useragent import UserAgent

def searchSpider(kw,start_page,end_page):
    #quote,将中文转为url能够识别的编码格式
    quote_str = parse.quote(kw)
    print(quote_str)
    unquote_str = parse.unquote(quote_str)
    print(unquote_str)

    for page in range(start_page,end_page+1):
        # 将字典类型的参数，转化为url的编码格式的字符串
        parmars = {
            'wd': kw,
            'pn': (page-1)*10,
        }
        result = parse.urlencode(parmars)
        print(result)

        #https://www.baidu.com/s?wd=%E9%A9%AC%E4%BA%91&pn=0
        full_url = 'https://www.baidu.com/s?'+result
        print(full_url)
        html = load_page(full_url)
        filename = '第'+str(page)+'页'+kw+'.html'
        save_page_html(html,filename)

def load_page(url):

    req_header = {
        'User-Agent':user_agent.random
    }

    req = request.Request(url,headers=req_header)

    response = request.urlopen(req)

    if response.status == 200:

        print('请求成功',response.url)

        return response.read().decode('utf-8')

def save_page_html(html,filename):
    """
    保存获取到的页面源码
    :param html:页面源码
    :param filename:文件名
    :return:
    """
    with open('baidusearch/'+filename,'w',encoding='utf-8') as file:
        file.write(html)

if __name__ == '__main__':

    #实例化一个ua对象
    user_agent = UserAgent()

    #模拟搜索引擎，根据关键字获取页面信息（HTML页面源码）
    #输入搜索关键字
    kw = input('请输入搜索关键字')
    #起始页
    start_page = int(input('输入起始页:'))
    #输入截止页
    end_page = int(input('输入截止页:'))

    searchSpider(kw,start_page,end_page)

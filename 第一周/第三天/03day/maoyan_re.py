#step1:分析网站，找到目标url

#https://maoyan.com/board/4?offset=0
#https://maoyan.com/board/4?offset=10
#https://maoyan.com/board/4?offset=20
from urllib import request
import re,pymysql

def maoyanSpider(url):
    """
    根据url发起请求,解析数据,构造下一页请求
    :param url: 分页的url地址
    :return:
    """
    html,current_url = load_page_data(url)
    #解析数据
    movies = parse_page_data(html)
    if len(movies) > 0:
        for movie in movies:
            #print(movie)
            movieData = {}
            #排名
            movieData['rank'] = int(movie[0])
            #封面图片
            movieData['coverImage'] = movie[1]
            #电影名称
            movieData['name'] = movie[2]
            #主演
            movieData['actor'] = movie[3].replace('\n','').replace(' ','')
            #时间
            movieData['publishTime'] = movie[4].replace('上映时间：','')
            #评分数
            movieData['scorenum'] = float(movie[5]+movie[6])

            save_data_to_db(movieData)

        #如何构造下一页的连接,什么时候停
        #https://maoyan.com/board/4?offset=0
        pattern = re.compile('.*?offset=(\d+)')
        current_offset = int(re.findall(pattern,current_url)[0])
        nextpage_offset = current_offset+10
        #next_url = 'https://maoyan.com/board/4?offset='+str(nextpage_offset)
        #方式二：通过正则替换
        pattern = re.compile('offset=\d+')
        next_url = re.sub(pattern,'offset='+str(nextpage_offset),current_url)
        maoyanSpider(next_url)

def load_page_data(url):
    #设置请求头
    req_headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    #构建一个request对象
    req = request.Request(url,headers=req_headers)
    #发起请求
    response = request.urlopen(req)

    if response.status == 200:

        return response.read().decode('utf-8'),response.url

def parse_page_data(html):
    """
    从页面原码中,提取目标数据
    :param html: 页面原码
    :return:
    """
    pattern = re.compile(
        '<dd>.*?<i.*?>(.*?)</i>'+
        '.*?<img.*?data-src="(.*?)"'+
        '.*?<p.*?>.*?<a.*?>(.*?)</a>'+
        '.*?<p.*?>(.*?)</p>'+
        '.*?<p.*?>(.*?)</p>'+
        '.*?<i.*?>(.*?)</i>'+
        '.*?<i.*?>(.*?)</i>.*?</dd>',re.S
    )

    result = re.findall(pattern,html)
    print(result)
    print(len(result))
    return result

def save_data_to_db(movieInfo):
    """
    存储数据
    :param movieInfo:
    :return:
    """

    pass

if __name__ == '__main__':

    #创建数据库连接
    mysql_client = pymysql.Connect(
        '127.0.0.1','root','ljh1314',
        '1712B',3306,charset='utf8'
    )

    #创建游标
    cursor = mysql_client.cursor()

    start_url = 'https://maoyan.com/board/4?offset=0'
    maoyanSpider(start_url)


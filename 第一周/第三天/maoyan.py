from urllib import request, parse
from fake_useragent import UserAgent
import re
import pymysql

url = 'https://maoyan.com/board/4?offset=0'

headers = {
    "User-Agent": UserAgent().chrome
}


def request_url(start_page, end_page):
    for page in range(start_page, end_page + 1):
        parses = {
            'offset': (page - 1) * 10,
        }
        result = parse.urlencode(parses)
        url = "https://maoyan.com/board/4?" + result
        req = request.Request(url, headers=headers)
        response = request.urlopen(url)
        html = response.read().decode("utf-8")
        pipei(html)


def pipei(html):
    pattern = re.compile(
        '<dd>.*?>(.*?)</i>.*?<img.*?<img.*?data-src="(.*?)".*?alt="(.*?)".*?star">(.*?)<.*?releasetime">(.*?)<.*?integer">(.*?)<.*?fraction">(.*?)<',
        re.S)
    data = re.findall(pattern, html)
    for i in data:
        maoyandata = {}
        maoyandata["ranking"] = i[0]
        maoyandata["logo"] = i[1]
        maoyandata["name"] = i[2]
        maoyandata["performer"] = i[3]
        maoyandata["release_time"] = i[4]
        score1 = i[5]
        score2 = i[6]
        maoyandata["score"] = score1+score2
        print(list(maoyandata.values()))
        save_data_to_DB(maoyandata)


def save_data_to_DB(maoyandata):
    # 连接数据库
    '''
    create table maoyan( id int auto_increment primary key,
    ranking varchar(222),
    logo varchar(222),
    name varchar(222),
    performer varchar(222),
    release_time varchar(222),
    score varchar(200));
    Query OK, 0 rows affected (0.29 sec)

    '''
    connect = pymysql.Connect('localhost', "root", "abcd1234", "1712B", 3306, charset="utf8")
    keys = ','.join(maoyandata.keys())
    sql = """INSERT INTO maoyan({columns}) values ({values})""".format(columns=keys,
                                                                      values=(','.join(["%s"] * len(maoyandata))))
    cr = connect.cursor()
    cr.execute(sql, list(maoyandata.values()))
    connect.commit()
    cr.close()
    connect.close()


if __name__ == '__main__':
    start_page = int(input('输入起始页：'))
    end_page = int(input('输入截止页：'))
    request_url(start_page, end_page)

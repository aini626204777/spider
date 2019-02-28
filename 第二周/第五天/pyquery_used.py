import requests
from pyquery import PyQuery


# https://hr.tencent.com/position.php
# https://hr.tencent.com/position.php?&start=10
# https://hr.tencent.com/position.php?&start=20
def tencenJob(offset, sum):
    url = "https://hr.tencent.com/position.php?&start=" + str(offset)
    html = load_data(url=url)
    # with open('a.html','w') as f:
    #     f.write(html)
    next = parse_page_data(html)
    print(next)
    if next != 'javascript:;':
        offset = offset + 10
        sum += 1
        print('这是{}页'.format(sum))
        tencenJob(offset, sum)


def load_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:
        return response.text


def parse_page_data(html):
    # 实例化一个pyquery对象
    html_pq = PyQuery(html)
    # 提取职位列表
    tr_even = html_pq('tr.even')
    tr_odd = html_pq('tr').filter('.odd')
    tr_all = tr_even + tr_odd
    for tr in tr_all.items():
        jobinfo = {}
        # 职位的名称
        jobinfo['title'] = tr('td.l.square a').text()
        # 职位的类型
        jobinfo['type'] = tr('td').eq(1).text()
        # 职位的人数
        jobinfo['number'] = tr('td').eq(2).text()
        # 职位的地点
        jobinfo['addres'] = tr('td').eq(3).text()
        # 职位的发布时间
        jobinfo['date'] = tr('td').eq(4).text()

        url = tr('td.l.square a').attr('href')
        full_url = 'https://hr.tencent.com/' + url
        html = load_data(full_url)
        jobinfo['content'] = parse_detail_data(html)
    next = html_pq('a').filter('#next').attr['href']
    return next

def parse_detail_data(html):
    html_bs = PyQuery(html)

    content_li = html_bs('ul.squareli li').items()

    content = []
    for li in content_li:
        li_text = li.text()
        content.append(li_text)

    return ','.join(content)


if __name__ == '__main__':
    # 设置起始偏移量
    offset = 0
    sum = 1
    tencenJob(offset=offset, sum=sum)

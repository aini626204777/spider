import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


# https://hr.tencent.com/position.php
# https://hr.tencent.com/position.php?&start=10
# https://hr.tencent.com/position.php?&start=20
def tencenJob(offset,sum):
    url = "https://hr.tencent.com/position.php?&start=" + str(offset)
    html = load_data(url=url)
    # with open('a.html','w') as f:
    #     f.write(html)
    next = parse_page_data(html)
    print(next)
    if next != 'javascript:;':
        offset = offset+10
        sum += 1
        print('这是{}页'.format(sum))
        tencenJob(offset,sum)



def load_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:
        return response.text


def parse_page_data(html):
    soup = BeautifulSoup(html, features='lxml')
    tr_even = soup.find_all(name='tr', attrs={'class': 'even'})
    tr_odd = soup.find_all(name='tr', attrs={'class': 'odd'})
    for tr in tr_even + tr_odd:
        jobinfo = {}
        # 职位的名称 .get_text()表示取标签的文本
        jobinfo['title'] = tr.select('td.l.square a')[0].get_text()
        # 职位的类型
        jobinfo['type'] = tr.select('td:nth-of-type(2)')[0].get_text()
        # 职位的人数
        jobinfo['number'] = tr.select('td:nth-of-type(3)')[0].get_text()
        # 职位的地点
        jobinfo['addres'] = tr.select('td:nth-of-type(4)')[0].get_text()
        # 职位的发布时间
        jobinfo['date'] = tr.select('td:nth-of-type(5)')[0].get_text()
        url = tr.select('td.l.square > a')[0].attrs['href']
        full_url = 'https://hr.tencent.com/' + url
        html = load_data(full_url)
        jobinfo['content'] = parse_detail_data(html)

    next = soup.select('#next')[0].attrs['href']
    return next


def parse_detail_data(html):
    html_bs = BeautifulSoup(html, features='lxml')

    content_li = html_bs.select('ul.squareli li')

    content = []
    for li in content_li:
        li_text = li.get_text()
        content.append(li_text)

    return ''.join(content)


if __name__ == '__main__':
    # 设置起始偏移量
    offset = 0
    sum = 1
    tencenJob(offset=offset,sum=sum)

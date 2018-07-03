import requests
from bs4 import BeautifulSoup
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}

url = 'https://www.autohome.com.cn/all/1/'

response = requests.get(url=url, headers=headers)

with open('qichezhijia.html', 'w') as f:
    f.write(response.text)
soup_html = BeautifulSoup(response.text, features='html.parser')

article_list = soup_html.select('.article li')
# print(article_list)
objid_list = []
article_dict = {

}
for item in article_list:
    if len(item.select('a')) != 0:
        title = item.select('h3')[0].get_text()
        href = item.select('a')[0].get('href')
        image_url = item.select('.article-pic img')[0].get('src')
        content = item.select('p')[0].get_text()
        visit_num = item.select('.fn-right em')[0].get_text()
        comment_num = item.select('.fn-right em')[1].get_text()
        # 分析页面之后我们发现要从文章详情的url中获取文章的id
        a = re.compile('.*?.cn/.*?/\d*/(\d+).*?.html')
        objid = re.findall(a, href)[0]
        objid_list.append(objid)
        # print(objid)
        dict = {
            'title':title,
            'href':href,
            'image_url':image_url,
            'content':content,
            'visit_num':visit_num,
            'comment_num':comment_num,
            'objid':objid,
        }
        # print(comment_num)
print(len(objid_list))
print(objid_list)

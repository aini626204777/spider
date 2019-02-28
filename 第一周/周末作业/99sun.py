import requests
import re
import os
from urllib import parse


def loadSpider(url):
    headers = {
        'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
    }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        tage_url(response.text)

def tage_url(html):
    patter = re.compile('<a\starget="_blank"\shref="(.*?)"\stitle="更多">更多</a>.*?<h3>(.*?)</h3>')
    result = re.findall(patter, html)
    for i in result:
        Make(i[1])
        Detail_url(i[0],i[1])


def Make(path):
    floder = os.path.exists(path)
    if not floder:
        os.makedirs(path)
        print(path,'文件夹创建成功')

def Detail_url(url,path):
    headers = {
        'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            html = response.text
            Detail_data(html,path)
    except requests.exceptions.MissingSchema as err:
        base_url = 'https://www.99zuowen.com/xiaoxuezuowen/ynjxieren/'
        full_url = parse.urljoin(base_url, url)
        response = requests.get(full_url, headers=headers)
        if response.status_code == 200:

            html = response.text
            Detail_data_url(html,path)

def Detail_data(html,path):
    patter = re.compile('<h4><a\shref="(.*?)".*?target="_blank">.*?</a></h4>')
    result = re.findall(patter, html)
    Detail(result,path)

def Detail_data_url(html,path):
    # print(html)
    patter = re.compile('<ul\sclass="tlist">(.*?)</ul>')
    result = re.findall(patter, html)
    if len(result)==0:
        patter = re.compile('<a\shref="(.*?)"\sclass="ulink"\starget=_blank>.*?</a>')
        result = re.findall(patter, html)
        Detail(result,path)
    else:
        patter_a = re.compile('<li><a\starget="_blank"\shref="(.*?)"\stitle=".*?">.*?</a></li>')
        result_a = re.findall(patter_a, result[0])
        # print(result_a)
        # for i in result_a:
        #     print(i)
        Detail(result_a,path)

"""--------------------------------提取数据---------------------------------"""
def Detail(result,path):
    for i in result:
        headers = {
            'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
        }
        response = requests.get(i, headers=headers)
        if response.status_code == 200:
            html = response.text
            data_from(html,path)

def data_from(html,path):
    title = re.compile('<h1>(.*?)</h1>.*?<ul>.*?<span>(.*?)<a\shref.*?title.*?>(.*?)</a></span>.*?<span>(.*?)</span>.*?<span>(.*?)</span>.*?</ul>.*?<div\sstyle="padding-left:11px;">.*?<p>(.*)</p>.*?</div>.*?<div\sclass="clearfloat">',re.S)
    result = re.findall(title, html)[0]
    text(path,result)

def text(path,result):
    name = path +'/'+ result[0]+'.txt'
    with open(name,'w+')as f:
        for i in result:
            item = i.replace('<p>','').replace('</p>','').replace('\n','')
            f.write(item+'\n')
        print(name,'写入成功')


if __name__ == '__main__':
    url = 'https://www.99zuowen.com/xiaoxuezuowen/ynjzuowen/'
    loadSpider(url)
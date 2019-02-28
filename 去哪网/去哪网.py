from concurrent.futures import ProcessPoolExecutor
import os, time, json, re
import requests
from lxml.html import etree

headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    }
def download_page_data(url):
    response = requests.get(url,headers=headers)
    if response == 200:
        html = etree.HTML(response.text)
        url = html.xpath('//*[@id="list"]/ul/li[1]/a')
        # url = html.xpath('//*[@id="list"]/ul/li')
        print(url)




if __name__ == '__main__':
    'https://tuan.qunar.com/vc/index.php?category=all_r'  # 周边游
    'https://tuan.qunar.com/vc/index.php?category=all_i'  # 国内游
    'https://tuan.qunar.com/vc/index.php?category=all_o'  # 出境游

    # 创建一个进程池,执行分页任务下载
    # page_pool = ProcessPoolExecutor(3)
    # start_urls = ['https://tuan.qunar.com/vc/index.php?category=all_r&dep=北京&limit=0%2C30'
    # 'https://tuan.qunar.com/vc/index.php?category=all_i&dep=北京&limit=0%2C30'
    # 'https://tuan.qunar.com/vc/index.php?category=all_o&dep=北京&limit=0%2C30']
    # for i in start_urls:
    url = 'https://tuan.qunar.com/vc/index.php?category=all_r&limit=0%2C30&dep=%E5%8C%97%E4%BA%AC'
    download_page_data(url)

from concurrent.futures import ThreadPoolExecutor
import requests,threading
from lxml.html import etree
# 线程池的目的:创建一个线程池,里面有指定数量线程,让线程执行任务
def down_load_data(page):
    print(page)

    print('正在打印第' + str(page) + '页')
    full_url = 'http://blog.jobbole.com/all-posts/page/%s/' % str(page)
    req_header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    }
    response = requests.get(full_url, headers=req_header)

    if response.status_code == 200:
        return response.text,response.status_code

def download_done(futures):
    print(futures.result())
    html = futures.result()[0]
    html_element = etree.HTML(html)
    articles = html_element.xpath('//div[@class="post floated-thumb"]')

    for article in articles:
        articleInfo = {}
        # 标题 老子就是牛逼
        articleInfo['title'] = article.xpath('.//a[@class="archive-title"]/text()')[0]
        # 封面
        img_elenebt = article.xpath('.//div[@class="post-thumb"]/a/img/@src')[0]
        if len(img_elenebt) > 0:
            articleInfo['coverImage'] = img_elenebt.xpath('./@src')
        else:
            articleInfo['coverImage'] = '暂无图片'
        p_as = article.xpath('.//div[@class="post-meta"]/p[1]/a')
        if len(p_as) > 2:
            # tag类型
            articleInfo['tag'] = p_as[1].xpath('./text()')[0]
            # 评论量
            articleInfo['commentNum'] = p_as[2].xpath('./text()')[0]
        else:
            # tag类型
            articleInfo['tag'] = p_as[1].xpath('./text()')
            # 评论量
            articleInfo['commentNum'] = '0'
        # 简介 被逼拔了打了就 der驾
        articleInfo['contment'] = article.xpath('.//span[@class="excerpt"]/p/text()')[0]
        # 时间  哈哈哈哈哈哈哈 哦哦哦哦哦哦哦哦
        articleInfo['publishTime'] = ','.join(article.xpath('.//div[@class="post-meta"]/p[1]/text()')).replace('\n',
                                                                                                               '').replace(
            ' ', '').replace('\r', '').replace('.', '')
        print(articleInfo)


if __name__ == '__main__':
    # 创建线程池
    # max_workers：指定线程池中的线程数量
    pool = ThreadPoolExecutor(max_workers=10)
    for i in range(1,11):
        # 线程池中添加任务
        handler = pool.submit(down_load_data,i)
        # 回调方法
        handler.add_done_callback(download_done)

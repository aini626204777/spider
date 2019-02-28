from concurrent.futures import ProcessPoolExecutor
import os, time,json,re
import requests
from lxml.html import etree


def down_load_page_data(url):
    """
    执行任务的下载
    :param taskQueue:
    :param dataQueue:
    :return:
    """
    response,cur_page = download_page_data(url)
    data_dict = {'data':response.text,'page':cur_page}

    #获取下一页
    if cur_page != 1:
        print('====',cur_page)
        if isinstance(response.json(),list):
            next_page = cur_page+1
            next_url = re.sub('page=\d+','page='+str(next_page),url)
        else:
            print('已获取到'+str(cur_page)+'页','没有数据了',response.json())
            next_url = None
            pass
    elif cur_page == 1:
        next_page = cur_page + 1
        next_url = re.sub('page=\d+', 'page=' + str(next_page), url)

    return data_dict,next_url
def download_page_data(url):
    """
    下载每一个分页的数据
    :param url: 每一个分页的url地址
    :return:
    """
    #http://date.jiayuan.com/eventslist_new.php?
    # page=1&city_id=4201&shop_id=33
    pattern = re.compile('.*?page=(\d+)&city_id=(\d+)&shop_id=(\d+)')
    result = re.findall(pattern,url)[0]
    cur_page = result[0]
    DATE_SHOW_LOC = result[1]
    DATE_SHOW_SHOP = result[2]
    # print(cur_page,DATE_SHOW_SHOP,DATE_SHOW_LOC)
    cookie = """_gscu_1380850711=43812116hs5dyy11; accessID=20181222071935501079; jy_refer=www.baidu.com; _gscbrs_1380850711=1; PHPSESSID=9202a7e752f801a49a5747832520f1da; plat=date_pc; DATE_FROM=daohang; SESSION_HASH=61e963462c6b312ee1ffacf151ffaa028477217d; user_access=1; uv_flag=124.64.18.38; DATE_SHOW_LOC=%s; DATE_SHOW_SHOP=%s""" % (DATE_SHOW_LOC,DATE_SHOW_SHOP)
    # print(cookie)

    req_header = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Cookie':cookie,
        'Referer':'http://date.jiayuan.com/eventslist.php',
    }
    # cookie_dict = {sub_str.split('=')[0]:sub_str.split('=')[1] for sub_str in cookie.split('; ')}
    # print(cookie_dict)
    #cookies(cookiejar object or dict)
    response = requests.get(url,headers=req_header)

    if response.status_code == 200:
        print('第'+cur_page+'页获取成功',DATE_SHOW_SHOP,DATE_SHOW_LOC)
        return response,int(cur_page)

def parse_page_data(futures):
    result = futures.result()
    data = result[0]
    next_page_url = result[1]

    if next_page_url:
        handler = page_pool.submit(down_load_page_data, next_page_url)
        handler.add_done_callback(parse_page_data)

    page = data['page']
    html = data['data']
    # 创建进程池(获取活动详情的页面源码)
    detail_pool = ProcessPoolExecutor(2)

    if page == 1:
        print('解析第一页数据,静态页面')
        html_element = etree.HTML(html)
        hot_active = html_element.xpath('//div[@class="hot_detail fn-clear"]')
        for hot_div in hot_active:
            # 活动详情的url地址
            full_detail_url = 'http://date.jiayuan.com' + hot_div.xpath('.//h2[@class="hot_title"]/a/@href')[0]
            handler = detail_pool.submit(download_detail_data,full_detail_url)
            handler.add_done_callback(parse_detail_data)
        more_active = html_element.xpath('//ul[@class="review_detail fn-clear t-activiUl"]/li')
        for more_li in more_active:
            # 活动详情的url地址
            full_detail_url = 'http://date.jiayuan.com' + more_li.xpath('.//a[@class="review_link"]/@href')[0]
    else:
        print('解析第' + str(page) + '数据', '非静态页面')
        # 使用json.loads()将json字符串转换为python数据类型
        json_obj = json.loads(html)
        if isinstance(data, list):
            # 是列表,说明得到的是正确的数据,
            print('正在解析数据')
            for sub_dict in json_obj:
                id = sub_dict['id']
                # http://date.jiayuan.com/activityreviewdetail.php?id=11706
                full_detail_url = 'http://date.jiayuan.com/activityreviewdetail.php?id=%s' % id
                handler = detail_pool.submit(download_detail_data, full_detail_url)
                handler.add_done_callback(parse_detail_data)
    detail_pool.shutdown()


def download_detail_data(url):
    """
    根据活动详情的url地址发起请求
    :param url:
    :return:
    """
    req_header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Cookie': '_gscu_1380850711=43812116hs5dyy11; accessID=20181222071935501079; jy_refer=www.baidu.com; _gscbrs_1380850711=1; PHPSESSID=9202a7e752f801a49a5747832520f1da; plat=date_pc; DATE_FROM=daohang; SESSION_HASH=61e963462c6b312ee1ffacf151ffaa028477217d; user_access=1; uv_flag=124.64.18.38; DATE_SHOW_LOC=50; DATE_SHOW_SHOP=5',
        'Referer': 'http://date.jiayuan.com/eventslist.php',
    }
    response = requests.get(url, headers=req_header)

    if response.status_code == 200:
        print('详情页面获取成功',response.url)
        return response
def parse_detail_data(futures):
    """
    解析活动详情
    :param response:
    :return:
    """
    response = futures.result()
    html_element = etree.HTML(response.text)
    # 创建一个字典，存放获取的数据
    item = {}
    # 活动标题
    item['title'] = ''.join(html_element.xpath('//h1[@class="detail_title"]/text()')[0])
    # 活动时间
    item['time'] = ','.join(
        html_element.xpath('//div[@class="detail_right fn-left"]/ul[@class="detail_info"]/li[1]//text()')[0])
    # 活动地址
    item['adress'] = html_element.xpath('//ul[@class="detail_info"]/li[2]/text()')[0]
    # 参加人数
    item['joinnum'] = html_element.xpath('//ul[@class="detail_info"]/li[3]/span[1]/text()')[0]
    # 预约人数    item['yuyue'] = html_element.xpath('//ul[@class="detail_info"]/li[3]/span[2]/text()')[0]
    # 介绍
    item['intreduces'] = html_element.xpath('//div[@class="detail_act fn-clear"][1]//p[@class="info_word"]/span[1]/text()')[0]
    # 提示
    item['point'] = html_element.xpath('//div[@class="detail_act fn-clear"][2]//p[@class="info_word"]/text()')[0]
    # 体验店介绍
    item['introductionStore'] = ''.join(
        html_element.xpath('//div[@class="detail_act fn-clear"][3]//p[@class="info_word"]/text()'))
    # 图片连接
    item['coverImage'] = html_element.xpath('//div[@class="detail_left fn-left"]/img/@data-original')[0]

    with open('shijijiyua.json','w') as file:
        json_str = json.dumps(item,ensure_ascii=False)+'\n'
        file.write(json_str)
if __name__ == '__main__':

    # 创建一个进程池,执行分页任务下载
    page_pool = ProcessPoolExecutor(2)
    start_urls = [
        'http://date.jiayuan.com/eventslist_new.php?page=1&city_id=4201&shop_id=33',
        'http://date.jiayuan.com/eventslist_new.php?page=1&city_id=31&shop_id=15',
        'http://date.jiayuan.com/eventslist_new.php?page=1&city_id=3702&shop_id=42',
        'http://date.jiayuan.com/eventslist_new.php?page=1&city_id=50&shop_id=5'
    ]
    for i in start_urls:
        handler = page_pool.submit(down_load_page_data,i)
        handler.add_done_callback(parse_page_data)

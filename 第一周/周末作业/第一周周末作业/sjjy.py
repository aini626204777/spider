# -*- coding: utf-8 -*-
import requests
import re
import json
from lxml import etree

class JiayuanSpider(object):

    def __init__(self):
        #设置起始任务
        self.start_urls = [
            #上海地区的活动url接口
            'http://date.jiayuan.com/eventslist_new.php?page=1&city_id=31&shop_id=15',
            #湖北武汉地区的活动url接口
            'http://date.jiayuan.com/eventslist_new.php?page=1&city_id=4201&shop_id=33',
        ]

    def start_requests(self):
        """
        根据起始任务发起请求
        """
        for url in self.start_urls:
            response = self.download_data(url)
            self.parse(response)

    def download_data(self,req_url,parmas=None):
        """
        下载器，执行任务的下载
        """
        req_header = {
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Cookie':'_gscu_1380850711=43812116hs5dyy11; accessID=20181222071935501079; PHPSESSID=b59c131c44e32d744ab8ad3bb6e27a45; plat=date_pc; uv_flag=223.72.78.37; user_access=1; DATE_SHOW_LOC=4201; DATE_SHOW_SHOP=33',
            'Referer': 'http://date.jiayuan.com/eventslist.php',
        }
        response = requests.get(req_url,headers=req_header,params=parmas)

        if response.status_code == 200:
            print(response.url)
            return response

    def parse(self, response):
        html_element = etree.HTML(response.text)
        hot_active = html_element.xpath('//div[@class="hot_detail fn-clear"]')
        for hot_div in hot_active:
            #活动详情的url地址
            full_detail_url = 'http://date.jiayuan.com'+hot_div.xpath('.//h2[@class="hot_title"]/a/@href')[0]
            detail_response = self.download_data(full_detail_url)
            #解析活动详情的数据
            self.parse_detail_data(detail_response)

        more_active = html_element.xpath('//ul[@class="review_detail fn-clear t-activiUl"]/li')
        for more_li in more_active:
            #活动详情的url地址
            full_detail_url = 'http://date.jiayuan.com'+more_li.xpath('.//a[@class="review_link"]/@href')[0]
            detail_response = self.download_data(full_detail_url)
            #解析活动详情的数据
            self.parse_detail_data(detail_response)

        if 'city_id=31' in response.url:
            print('当前获取的是上海城市的活动')
            #构造第二页的请求,第二页开始数据ajax请求,json数据
            parmas={'page':2,'city_id':'31','shop_id':'15'}
            url = 'http://date.jiayuan.com/eventslist_new.php?'
            self.send_next_page_reuqest(url,parmas)

        if 'city_id=4201' in response.url:
            print('当前获取到的是武汉市的活动')
            # 构造第二页的请求,第二页开始数据ajax请求,json数据
            parmas={'page': 2, 'city_id': '4201', 'shop_id': '33'}
            url = 'http://date.jiayuan.com/eventslist_new.php?'
            self.send_next_page_reuqest(url,parmas)

    def send_next_page_reuqest(self,url,parmas):
        print('正在获取第'+str(parmas['page'])+'页',parmas)
        response = self.download_data(url,parmas=parmas)
        #isStatus判断是否需要发起下一次请求(根据页面返回的数据结果来判断)
        isStatus = self.parse_active_list(response)
        if isStatus:
            parmas['page'] = parmas['page']+1
            self.send_next_page_reuqest(url,parmas)
        
    def parse_active_list(self,response):
        #获取到url中的相关参数（上一次请求的页码,城市id,地区id）
        data = json.loads(response.text)
        if isinstance(data,list):
            #是列表,说明得到的是正确的数据,
            print('正在解析数据')
            for sub_dict in data:
                id = sub_dict['id']
                full_detail_url = 'http://date.jiayuan.com/activityreviewdetail.php?id=%s' % id
                response = self.download_data(full_detail_url)
                self.parse_detail_data(response)
            #　数据可能没取完,继续发起请求
            return True
        else:
            #不是列表，返回的是一个字典说明数据取完了,不需要再发起下一页的请求了
            return False

    def parse_detail_data(self,response):
        html_element = etree.HTML(response.text)

        with open('detail.html','w') as file:
            file.write(response.text)
        #创建一个字典，存放获取的数据
        item = {}
        # 活动标题
        item['title'] = ''.join(html_element.xpath('//h1[@class="detail_title"]/text()')[0])
        # 活动时间
        item['time'] = ','.join(html_element.xpath('//div[@class="detail_right fn-left"]/ul[@class="detail_info"]/li[1]//text()')[0])
        # 活动地址
        item['adress'] = html_element.xpath('//ul[@class="detail_info"]/li[2]/text()')[0]
        # 参加人数
        item['joinnum'] = html_element.xpath('//ul[@class="detail_info"]/li[3]/span[1]/text()')[0]
        # 预约人数
        item['yuyue'] = html_element.xpath('//ul[@class="detail_info"]/li[3]/span[2]/text()')[0]
        # 介绍
        item['intreduces'] = html_element.xpath('//div[@class="detail_act fn-clear"][1]//p[@class="info_word"]/span[1]/text()')[0]
        # 提示
        item['point'] = html_element.xpath('//div[@class="detail_act fn-clear"][2]//p[@class="info_word"]/text()')[0]
        # 体验店介绍
        item['introductionStore'] = ''.join(html_element.xpath('//div[@class="detail_act fn-clear"][3]//p[@class="info_word"]/text()'))
        # 图片连接
        item['coverImage'] = html_element.xpath('//div[@class="detail_left fn-left"]/img/@data-original')[0]

        print(item)


if __name__ == "__main__":

    spider = JiayuanSpider()
    spider.start_requests()

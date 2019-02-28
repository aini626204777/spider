# -*- coding: utf-8 -*-
import scrapy
from wjjlianjia.items import WjjlianjiaershoufangItem, WjjlianjiazufangItem
import re, json


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://bj.lianjia.com/']

    def parse(self, response):
        ershoufang_url = response.xpath('//div[@class="nav typeUserInfo"]/ul/li/a/@href').extract()[0]
        zufang_url = response.xpath('//div[@class="nav typeUserInfo"]/ul/li/a/@href').extract()[2]
        # print(ershoufang_url)
        # print(zufang_url)

        yield scrapy.Request(ershoufang_url + 'pg1', callback=self.ershoufang_parse_data)
        yield scrapy.Request(zufang_url + 'pg1/#contentList', callback=self.zufang_parse_data)

    def ershoufang_parse_data(self, response):
        er_list = response.xpath('//li[@class="clear LOGCLICKDATA"]')
        for data in er_list:
            item = WjjlianjiaershoufangItem()
            # 封面照片
            item['cover'] = data.xpath('.//a/img[2]/@data-original').extract()[0]
            # 名字
            item['title'] = data.xpath('./div/div[1]/a/text()').extract()[0]
            # 地址
            item['adress'] = data.xpath('./div[1]/div[2]/div/a/text()').extract()[0]
            # 厅室
            item['Hall'] = data.xpath('./div[1]/div[2]/div/text()').extract()[0]
            # 平米
            item['SquareMetre'] = data.xpath('./div[1]/div[2]/div/text()').extract()[1]
            # 装修
            item['Renovation'] = data.xpath('./div[1]/div[2]/div/text()').extract()[2:]
            # 楼层
            item['floor'] = data.xpath('./div[1]/div[3]/div/text()').extract()[0]
            # 时间
            item['floorDate'] = data.xpath('./div[1]/div[3]/div/text()').extract()[1]
            # 区域
            item['region'] = data.xpath('./div[1]/div[3]/div/a/text()').extract()[0]
            # 关注
            item['follow'] = data.xpath('./div[1]/div[4]/text()').extract()[0]
            # 参观
            item['visit'] = data.xpath('./div[1]/div[4]/text()').extract()[1]
            # 钱
            item['money'] = data.xpath('./div[1]/div[4]/div[2]/div[1]/span/text()').extract()[0]
            # 单价
            item['UnitPrice'] = data.xpath('./div[1]/div[4]/div[2]/div[2]/span/text()').extract()[0]

            yield item
        print(response.url)
        page_data = response.xpath('//div[@class="page-box house-lst-page-box"]/@page-data').extract()[0]
        next = json.loads(page_data)
        curPage = int(next['curPage'])
        totalPage = int(next['totalPage'])
        print('这是第' + str(curPage) + '页！！！！！！')
        if curPage < totalPage:
            curPage += 1
            url = re.sub('pg(\d+)', 'pg' + str(curPage), response.url)
            yield scrapy.Request(url, callback=self.ershoufang_parse_data)

    def zufang_parse_data(self, response):
        zufang_list = response.xpath('//div[@class="content__list--item"]')
        for data in zufang_list:
            item = WjjlianjiazufangItem()
            # 封面照片
            item['cover'] = data.xpath('./a[@class="content__list--item--aside"]/img/@data-src').extract()[0]
            # 名字
            item['title'] = data.xpath('./div/p[1]/a/text()').extract()[0].strip()
            # 地址
            item['adress'] = data.xpath('./div[1]/p[2]/a/text()').extract()
            # 厅室
            item['Hall'] = ','.join(data.xpath('./div[1]/p[2]/text()').extract()).replace('\n', '').replace(' ',
                                                                                                            '').replace(
                '-', '').replace(',,,', '')
            # 时间
            item['floorDate'] = data.xpath('./div[1]/p[4]/text()').extract()
            # 福利
            item['welfare'] = data.xpath('./div/p[5]/i/text()').extract()
            # 月租
            item['MonthlyRent'] = data.xpath('./div/span/em/text()').extract()[0] + \
                                  data.xpath('./div/span/text()').extract()[0]
            yield item

        data_totalpage = int(response.xpath('//div[@class="content__pg"]/@data-totalpage').extract()[0])
        data_curpage = int(response.xpath('//div[@class="content__pg"]/@data-curpage').extract()[0])
        print(data_totalpage, data_curpage)
        print('这是第' + str(data_curpage) + '页！！！！！！')
        if data_curpage < data_totalpage:
            data_curpage += 1
            url = re.sub('pg(\d+)', 'pg' + str(data_curpage), response.url)
            yield scrapy.Request(url, callback=self.zufang_parse_data)

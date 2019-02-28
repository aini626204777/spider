# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import DangdangwangItem

class DangSpider(scrapy.Spider):
    name = 'Dang'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://book.dangdang.com/']

    def parse(self, response):
        inner_dl = response.xpath('//div[@class="con flq_body"]/div[8]/div/div/div[1]/dl/dd/a/@href').extract()
        for i in inner_dl:
            pattern = re.compile('http://category.dangdang.com/.*?html')
            result = re.findall(pattern, i)
            if result:
                yield scrapy.Request(result[0],callback=self.page_data)

    def page_data(self,response):
        page_list = response.xpath('//div[@class="con shoplist"]/div[1]/ul/li/a/@href').extract()
        for dateil_url in page_list:
            print(dateil_url)
            yield scrapy.Request(dateil_url,callback=self.parse_data)


    def parse_data(self,response):
        
        items = DangdangwangItem()
        # 书名
        items['book_name'] = response.xpath('//div[@class="name_info"]/h1/@title').extract_first('')
        # 简介
        items['introduction'] = response.xpath('//div[@class="name_info"]/h2/span[1]/text()').extract_first('').strip()
        # # 作者
        items['author'] = response.xpath('//div[@class="messbox_info"]/span/a/text()').extract_first('')
        # # 出判社
        items['press'] = response.xpath('//div[@class="messbox_info"]/span[2]/a/text()').extract_first('')
        # # 发布时间
        items['pubdate'] = response.xpath('//div[@class="messbox_info"]/span[3]/text()').extract_first('')
        # 评论数
        items['comment'] = response.xpath('//div[@class="messbox_info"]/div/span[2]/a/text()').extract_first('')
        # 现价钱
        items['price'] = response.xpath('//*[@id="dd-price"]/text()').extract()[1]
        # 收藏人气
        items['Popularity'] = response.xpath('//a[@class="btn_scsp"]/text()').extract_first('')
        # 封面
        items['cover'] = response.xpath('//div[@id="largePicDiv"]/a/img/@src').extract_first('')
        # print(items)
        
        yield items
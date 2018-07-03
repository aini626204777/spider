# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from HongNiang_CrawlSpider.items import HongniangCrawlspiderItem
from scrapy_redis.spiders import RedisCrawlSpider


class HongniangSpider(RedisCrawlSpider):
    name = 'HongNiang'
    allowed_domains = ['hongniang.com']
    # 通过key去redis中获取其实url
    redis_key = 'HongNiang:start_urls'
    # start_urls = [
        # 'http://www.hongniang.com/index/search?sort=0&wh=0&sex=2&starage=1,2,3,4,5,6,7,8,9,10&province=0&city=0&marriage=1&edu=3,2,4,5,6,7&income=1,2,3,4,5,6,7,8&height=0&pro=0&house=0&child=0&xz=0&sx=0&mz=0&hometownprovince=0']

    rules = (
        Rule(LinkExtractor(allow=r'http.*?page=\d+'), callback='parse_item', follow=True),
        # http://www.hongniang.com/user/a/c/10608872.hlstml
        Rule(LinkExtractor(allow=r'.*?user.*?/(\d+)', allow_domains='www.hongniang.com'), callback='parse_details',
             follow=True),
    )

    def parse_item(self, response):
        print(response.url)
        # pass
    def parse_details(self, response):
        items = HongniangCrawlspiderItem()
        # 姓名
        items["name"] = response.xpath('//div[@class="name nickname"]/text()').extract_first().strip()
        # 年龄
        items["age"] = response.xpath('//div[@class="sub1"]//div[@class="info2"]//ul[1]//li[1]/text()').extract_first()
        # 身高
        items["hight"] = response.xpath(
            '//div[@class="sub1"]//div[@class="info2"]//ul[2]//li[1]/text()').extract_first()
        # 工作地点
        items["workLocal"] = response.xpath(
            '//div[@class="sub1"]//div[@class="info2"]//ul[3]//li[2]/text()').extract_first()

        yield items

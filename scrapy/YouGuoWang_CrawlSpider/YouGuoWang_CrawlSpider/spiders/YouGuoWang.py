# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from YouGuoWang_CrawlSpider.items import YouguowangCrawlspiderItem, parse_detailsCrawlspiderItem


class YouguowangSpider(CrawlSpider):
    name = 'YouGuoWang'
    allowed_domains = ['www.ugirls.com']
    start_urls = ['https://www.ugirls.com/']
    rules = (
        Rule(LinkExtractor(allow='https.*?/Magazine-(\d+).html', restrict_xpaths='//ul/li'), callback='parse_item',
             follow=True),
        Rule(LinkExtractor(allow='Magazine-(\d+)-(\d+).html'), callback='parse_page_cover', follow=True),
        Rule(LinkExtractor(allow='https.*?/Product-(\d+).html'), callback='parse_details',
             follow=True),
    )

    def parse_item(self, response):
        # print(response.status)
        pass

    def parse_page_cover(self, response):
        html = response.xpath('//ul[@class="latest_list"]//li')
        for i in html:
            items = YouguowangCrawlspiderItem()
            items['img_path'] = i.xpath('./a/img/@data-original').extract_first()
            items['title'] = i.xpath('./div[2]/a[2]/text()').extract_first()
            items['name'] = i.xpath('./div[2]/h1/a/text()').extract_first()
            yield items

    def parse_details(self, response):
        item = parse_detailsCrawlspiderItem()
        # 头像
        item['head_protrait'] = response.xpath('//div[@class="zhur"]/div/a[1]/@href').extract_first()
        # 姓名
        item['name'] = response.xpath('//div[@class="zhur"]/div/h1/a/text()').extract_first()
        # 身材
        item['stature'] = response.xpath('//div[@class="zhur"]/div/p/text()').extract_first()
        # 人气
        item['popularity'] = response.xpath('//div[@class="ren_info"]/strong/text()').extract_first('0')
        # 粉丝
        item['fans'] = response.xpath('//div[@class="ren_info"]/a[1]/text()').extract_first('0')
        # 专辑
        item['album'] = response.xpath('//div[@class="ren_info"]/a[2]/text()').extract_first('0')
        # 发行时间
        item['issue_date'] = response.xpath('//div[@class="mg-det"]/p[1]/text()').extract_first('0')
        # 专辑介绍
        item['album_introduce'] = response.xpath('//div[@class="mg-det"]/div/p/text()').extract_first('0')
        # 写真
        item['mirror'] = response.xpath('//div[@class="yang auto"]/a/img/@src').extract()
        # print(item)
        yield item

# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from BaiDuLvYou.items import BaidulvyouItem


class LvyouSpider(CrawlSpider):
    name = 'lvyou'
    allowed_domains = ['lvyou.baidu.com']
    start_urls = ['https://lvyou.baidu.com/scene/t-all_s-all_a-all_l-all']

    rules = (
        Rule(LinkExtractor(allow=(r'.*?lvyou.baidu.com/.*?'), restrict_xpaths='//*[@id="body"]/div[3]/span/a'),
            follow=False),
        Rule(LinkExtractor(allow=(r'.*?lvyou.baidu.com/.*?'), restrict_xpaths='//ul[@class="filter-result"]/li'),
             callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        print(response.status)
        item = BaidulvyouItem()
        # 标题
        item['title'] = response.xpath('//*[@id="dest-body"]/div/section/section/div/div[2]/div[2]/span[1]/a/text()').extract_first()
        # 评分
        item['grade'] = response.xpath('//*[@id="dest-body"]/div/section/section/article/div[1]/div[2]/div[1]/text()').extract()[1]
        # 简介
        item['intro'] = response.xpath('//*[@id="dest-body"]/div/section/section/article/div[1]/div[2]/div[2]/p/text()').extract_first()
        # 评论数量
        item['comments'] = response.xpath('//*[@id="dest-body"]/div/section/section/article/div[1]/div[2]/div[1]/a/text()').extract_first(" ")
        yield item


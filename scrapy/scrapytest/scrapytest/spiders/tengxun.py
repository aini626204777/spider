# -*- coding: utf-8 -*-
import scrapy


class TengxunSpider(scrapy.Spider):
    # 爬虫的名称
    name = 'tengxun'
    # 允许爬去的域，可以是多个
    allowed_domains = ['hr.tencent.com']
    # 起始的url，也可以是多个
    start_urls = ['http://hr.tencent.com/']
    # parse解析
    def parse(self, response):
        print()

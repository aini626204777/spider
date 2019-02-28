# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from chinazcrawlspider.items import ChinazcrawlspiderItem

class ChinazSpider(CrawlSpider):
    # 爬虫文件名称
    name = 'chinaz'
    # 允许爬取的域
    allowed_domains = ['chinaz.com']
    # 起始url
    start_urls = ['http://top.chinaz.com/hangyemap.html']
    # rules : 存放定制的获取连接的规则对象（可以是一个列表也可以是一个元祖）
    #    根据规则提取到所有连接，会由crawlspider构建Request对象，并交给引擎处理
    """
    LinkExtractor : 设置提取连接的规则（正则表达式)
    allow=(), : 设置允许提取的目标url 
    deny=(), : 设置不允许提取的url（优先级比allow要高）
    allow_domains=(), : 设置允许提取url的域
    deny_domains=(), : 设置不允许提取url的域（优先级比allow_domains高）
    restrict_xpaths=(),: 根据xpath运发，对位到某一标签下提取链接
    unique=True, : 如果存在多个相同的url,只会保留一个
    restrict_css=(),: 根据css选择器，定位到某一标签下提取目标数据
    strip=True : 默认为True，表示去除url首位的空格
    """
    """
    link_extractor, : LinkExtractor对象
    callback=None, : 设置回调函数
    cb_kwargs=None, : 是否设置跟进
    follow=None, : 可以设置一个回调函数，对所有提取到的url进行拦截
    process_request=identity : 可以设置回调函数，对request对象进行拦截
    """

    rules = (
        Rule(LinkExtractor(allow=r'http://top.chinaz.com/hangye/index.*?.html',restrict_xpaths='//div[@class="Taright"]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        """
        解析分类网页的网站信息
        :param response: 响应结果
        :return:
        """

        Webs = response.xpath('//ul[@class="listCentent"]/li')

        for Web in Webs:
            Web_items = ChinazcrawlspiderItem()
            # 封面图片
            Web_items['CoverImage'] = Web.xpath('./div[1]/a/img/@src').extract()
            # 标题
            Web_items['Title'] = Web.xpath('./div[2]/h3/a/text()').extract_first('')
            # 域名
            Web_items['Domenis'] = Web.xpath('./div[2]/h3/span/text()').extract_first('')
            # 周排行
            Web_items['WeeklyRanking'] = Web.xpath('./div[2]/div[1]/p[1]/a/text()').extract_first('')
            # 反链接
            Web_items['AntiLink'] = Web.xpath('./div[2]/div[1]/p[4]/a/text()').extract_first('')
            # 网站简介
            Web_items['introduction'] = Web.xpath('./div[2]/p/text()').extract_first('')
            # 得分
            Web_items['Score'] = Web.xpath('./div[3]/div/span/text()').extract_first('').split(':')[1]
            # 排名
            Web_items['Ranking'] = Web.xpath('./div[3]/div/strong/text()').extract_first('')

            # yield Web_items
            # print(Web_items)
        # print(response.url)

# -*- coding: utf-8 -*-
import scrapy
from ..items import ChinazTagItem, ChinazWebinfoItem


class ChinazSpider(scrapy.Spider):
    name = 'chinaz'
    allowed_domains = ['chinaz.com']
    start_urls = ['http://top.chinaz.com/hangyemap.html']

    def parse(self, response):
        """
        在parse回调方法中
        step1：提取目标数据
        step2：获取新的目标url
        :param response: 请求的响应结果
        :return:
        """
        print(response.status)
        # response.xpath():使用xpath语法
        # response.css():使用css选择器
        # extract()：将selector 序列化为unicode字符串

        # step1：提取目标数据
        # 实例化一个item,用来存储数据

        # 使用xpath获取分类列表
        Tags = response.xpath('//div[@class="Taright"]/a')
        for Tag in Tags:
            Tag_items = ChinazTagItem()
            # 获取网站分类的名称
            Tag_items['TagName'] = Tag.xpath('./text()')[0].extract()
            # step2：获取新的目标url
            # 获取网站分类的首页url地址
            Tag_items['FirstUrl'] = Tag.xpath('./@href').extract()[0]
            # print(Tag_items)

            # 将获取到的数据交给管道处理
            yield Tag_items

            # 使用css获取分类列表
            # Tags = response.css('.Taright a')
            # for Tag in Tags:
            #     # 获取网站分类的名称
            #     TagName = Tag.css('::text').extract_first('')
            #     # step2：获取新的目标url
            #     # 获取网站分类的首页url地址
            #     FirstUrl = Tag.css('::attr(href)').extract_first('')
            #     print(TagName,FirstUrl)
            yield scrapy.Request(Tag_items['FirstUrl'], callback=self.parser_tags_page)

    def parser_tags_page(self, response):
        """
        解析分类网页的网站信息
        :param response: 响应结果
        :return:
        """

        Webs = response.xpath('//ul[@class="listCentent"]/li')

        for Web in Webs:
            Web_items = ChinazWebinfoItem()
            # 封面图片
            Web_items['CoverImage'] = 'http:' + Web.xpath('./div[1]/a/img/@src')[0].extract()
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

            yield Web_items

        next = response.xpath('//div[@class="ListPageWrap"]/a/@href').extract()[1:]
        for next_url in next:
            next_url = response.urljoin(next_url)
            print(next_url)

            yield scrapy.Request(next_url, callback=self.parser_tags_page)

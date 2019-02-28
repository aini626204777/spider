# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from youGuoWang.items import YouguowangPageItem,YouguowangdetailsItem

class YouguoSpider(CrawlSpider):
    name = 'youguo'
    allowed_domains = ['ugirls.com']
    start_urls = ['https://www.ugirls.com/']
    rules = (
        Rule(LinkExtractor(allow=r'com/.*?',restrict_xpaths='//ul[@class="card"]/li'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'com/.*?', restrict_xpaths='//div[@class="xfenye"]'), callback='parse_data_item',
             follow=True),
        Rule(LinkExtractor(allow=r'com/Shop/Detail/.*?', restrict_xpaths='//ul[@class="latest_list"]/li/a'), callback='parse_details_data_item',
             follow=True),
    )

    def parse_item(self, response):
        """
        获取分类目标url
        :param response:
        :return:
        """
        # print(response.url,response.status)
        # print(response.xpath('//ul[@class="breadcrumb"]/li[3]/text()').extract())
        pass
    def parse_data_item(self,response):
        """
        获取分类数据
        :param response:
        :return:
        """

        latest_list = response.xpath('//ul[@class="latest_list"]/li')
        for latest in latest_list:
            item = YouguowangPageItem()
            # 杂志标签
            item['magazineTag'] = latest.xpath('.//a[@class="magazine_tag"]/text()').extract_first('')
            # 模型名字
            item['modelName'] = latest.xpath('.//h1[@class="magazine_model_name"]/span/text()').extract_first('')
            # 发行时间
            item['issueTime'] = latest.xpath('.//div[@class="magazine_other_info"]/p[1]/span/text()').extract_first('')
            # 订阅量
            item['subscription'] = latest.xpath('.//div[@class="magazine_other_info"]/p[2]/span/text()').extract_first('')
            # 专辑名字
            item['AlbumName'] = latest.xpath('.//h1[@class="magazine_title"]/text()').extract_first('')
            # 名字
            item['name'] = latest.xpath('.//h1[@class="magazine_model_name"]/a/text()').extract_first('')
            # 封面
            item['cover'] = latest.xpath('.//img[@class="magazine_img lazy"]/@data-original').extract_first('')

            yield item


    def parse_details_data_item(self,response):
        """
        获取详情数据
        :param response:
        :return:
        """
        item = YouguowangdetailsItem()
        # 标签
        item['Tag'] = ','.join(response.xpath('//dl[@class="intag"]/dd/a//text()').extract())
        # 专辑名字
        item['AlbumName'] = response.xpath('//div[@class="model_name"]/text()').extract_first('')
        # 名字
        item['name'] = response.xpath('//div[@class="ren"]/h1/a/text()').extract_first('')
        # 发行时间
        item['issueTime'] = response.xpath('//div[@class="mg-det"]/p/text()').extract_first('')
        # 身高
        item['height'] = response.xpath('//div[@class="ren"]/p/text()').extract_first('').split(' ')[0].split('/')[1]
        # 三围
        item['BWH'] = ','.join(response.xpath('//div[@class="ren"]/p/text()').extract_first('').split(' ')[1].split('/')[1:])
        # 人气
        item['Popularity'] = response.xpath('//div[@class="ren_info"]/strong/text()').extract_first('')
        # 粉丝
        item['Fans'] = response.xpath('//div[@class="ren_info"]/a[1]/text()').extract_first('')
        # 专辑数量
        item['AlbumNumber'] = response.xpath('//div[@class="ren_info"]/a[2]/text()').extract_first('')
        # 专辑介绍
        item['AlbumIntroduction'] = ''.join(response.xpath('//div[@class="js"]/p/text()').extract())
        # 头像
        item['headPortrait'] = response.xpath('//a[@class="photo"]/img/@src').extract_first('')

        yield item
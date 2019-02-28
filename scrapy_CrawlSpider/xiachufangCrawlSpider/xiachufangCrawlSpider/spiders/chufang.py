# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
from xiachufangCrawlSpider.items import XiachufangcrawlspiderDataDetailsItem, XiachufangcrawlspiderAuthorDetailsItem
from scrapy_redis.spiders import RedisCrawlSpider

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
}


class ChufangSpider(RedisCrawlSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'chufang'
    allowed_domains = ['xiachufang.com']

    # start_urls = ['http://www.xiachufang.com/']

    redis_key = 'chufang:start_urls'

    rules = (
        Rule(LinkExtractor(allow=r'/category/', restrict_xpaths='//div[@class="left-panel"]/a'), callback='fenlei_data',
             follow=True),
        Rule(LinkExtractor(allow=r'/category/', restrict_xpaths='//div[@class="block-bg p40 font16"]'),
             callback='fenlei_detail',
             follow=True),
        Rule(LinkExtractor(allow=r'/category/', restrict_xpaths='//div[@class="pager"]'), callback='page_fenlei_data',
             follow=True),
        Rule(LinkExtractor(allow=r'/cook/', restrict_xpaths='//div[@class="normal-recipe-list"]'),
             callback='parse_item',
             follow=True),

    )

    def fenlei_data(self, response):
        # print(response.status, response.url)
        pass

    def fenlei_detail(self, response):
        # print(response.status,response.url)
        pass

    def page_fenlei_data(self, response):
        # print(response.status, response.url)
        li_list = response.xpath('//ul[@class="list"]/li')
        for li in li_list:
            detail_url = li.xpath('./div/a/@href').extract()[0]
            result_url = 'http://www.xiachufang.com/' + detail_url
            yield scrapy.Request(result_url, callback=self.parse_data_detail_item)

    def parse_data_detail_item(self, response):
        """
        菜谱详情
        :param response:
        :return:
        """
        print(response.url)
        print('进入到详情页面！！！')
        item = XiachufangcrawlspiderDataDetailsItem()
        item['LevelTitle'] = response.xpath('//ol[@class="breadcrumb plain pl10"]/li[2]/a/text()').extract_first('')
        item['title'] = response.xpath('//h1[@class="page-title"]/text()').extract()[0].replace('\n', '')
        item['cover'] = \
            response.xpath('//div[@class="cover image expandable block-negative-margin"]/img/@src').extract()[0]
        item['score'] = response.xpath('//div[@class="score float-left"]/span[1]/text()').extract_first('0')
        item['number'] = response.xpath('//div[@class="cooked float-left"]/span[1]/text()').extract_first('0')
        item['content'] = ''.join(response.xpath('//div[@class="desc mt30"]//text()').extract()).replace('\n',
                                                                                                         '').replace(
            ' ', '')
        item['material'] = ''.join(response.xpath('//div[@class="ings"]//text()').extract()).replace('\n', '').replace(
            ' ', '')
        item['step'] = ''.join(response.xpath('//div[@class="steps"]//text()').extract()).replace('\n', '').replace(' ',
                                                                                                                    '')
        yield item

    def parse_item(self, response):
        """
        作者详情
        :param response:
        :return:
        """
        item = XiachufangcrawlspiderAuthorDetailsItem()
        # 名字
        item['name'] = response.xpath('//h1[@class="page-title mb10"]/text()').extract_first('').replace('\n',
                                                                                                         '').replace(
            ' ',
            '')
        # 作者唯一标识
        item['UserID'] = re.findall('.*?/(\d+)/', response.url)[0]
        # 性别
        item['sex'] = response.xpath(
            '//div[@class="gray-font"]/div[1]/span[@class="mr10 display-inline-block"][1]/text()').extract_first('')
        if len(item['sex']) == 0:
            item['sex'] = '用户暂无上传性别'
        # 居住地
        item['address'] = response.xpath(
            '//div[@class="gray-font"]/div[1]/span[@class="mr10 display-inline-block"][2]/text()').extract_first('')
        if len(item['address']) == 0:
            item['address'] = '用户暂无上传居住地'
        # 加入时间
        item['shijian'] = response.xpath(
            '//div[@class="gray-font"]/div[1]/span[@class="display-inline-block"]/text()').extract_first('')
        # 关注数
        item['number'] = response.xpath('//div[@class="pure-u-1-2 following-num"]/div[2]/a/text()').extract_first(
            '')
        # 被关注数
        item['number2'] = response.xpath('//div[@class="pure-u-1-2 following-num"]/div[2]/a/text()').extract_first(
            '')
        # 菜谱数量
        item['Menunumber'] = response.xpath('//div[@class="tab-bar pure-g"]/ul/li[2]/a/span/text()').extract_first(
            '')
        # 作品数量
        item['worknumber'] = response.xpath('//div[@class="tab-bar pure-g"]/ul/li[3]/a/span/text()').extract_first(
            '')
        # 个人简介
        item['profile'] = ''.join(
            response.xpath('//div[@class="people-base-desc dark-gray-font mt10"]//text()').extract()).replace('\n',
                                                                                                              '').replace(
            ' ', '').replace('\r', '')
        if len(item['profile']) == 0:
            item['profile'] = '用户暂无上传个人简介'
        print(response.url, response.status)
        yield item

# -*- coding: utf-8 -*-
import scrapy
from BanCiYuan_project.items import BanciyuanProjectItem

class BcySpider(scrapy.Spider):
    name = 'bcy'
    allowed_domains = ['bcy.net']
    start_urls = ['https://bcy.net/illust']

    def parse(self, response):
        print(response.status)
        # 1下载绘画分类的封面图片到本地
        # 2.
        # 将绘画分类下的作者名称、评论量、本地图片路径存入数据库，使用css和Xpath来获取
        # 3
        # 要求二将同样的数据放在mongodb里面
        # 4.
        # 使用的mongodb查询语句实现一个分页查询和一个条件查询
        bcy = BanciyuanProjectItem()
        bcy['image_path'] = response.xpath(
            '//ul[@class="js-illustIndexList l-clearfix gridList smallCards"]/li//img[@class="cardImage"]/@src').extract()
        bcy['name'] = response.xpath(
            '//ul[@class="js-illustIndexList l-clearfix gridList smallCards"]/li//span[@class="fz12 lh18 username cut dib vam"]/text()').extract()
        bcy['comment_nums'] = response.xpath(
            '//ul[@class="js-illustIndexList l-clearfix gridList smallCards"]/li//span[@class="like"]/text()').extract()

        yield bcy


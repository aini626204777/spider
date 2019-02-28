# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangwangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 书名
    book_name = scrapy.Field()
    # 简介
    introduction = scrapy.Field()
    # # 作者
    author = scrapy.Field()
    # # 出判社
    press = scrapy.Field()
    # # 发布时间
    pubdate = scrapy.Field()
    # 评论数
    comment = scrapy.Field()
    # 现价钱
    price = scrapy.Field()
    # 收藏人气
    Popularity = scrapy.Field()
    # 封面
    cover = scrapy.Field()
    # 图片下载路径
    localImagePath = scrapy.Field()

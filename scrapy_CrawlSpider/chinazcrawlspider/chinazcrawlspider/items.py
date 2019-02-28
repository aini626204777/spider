# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChinazcrawlspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 封面图片
    CoverImage = scrapy.Field()
    # 标题
    Title = scrapy.Field()
    # 域名
    Domenis = scrapy.Field()
    # 周排行
    WeeklyRanking = scrapy.Field()
    # 反链接
    AntiLink = scrapy.Field()
    # 网站简介
    introduction = scrapy.Field()
    # 得分
    Score = scrapy.Field()
    # 排名
    Ranking = scrapy.Field()
    # 图片本地存储路径
    localImagePath = scrapy.Field()



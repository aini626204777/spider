# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaidulvyouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 评分
    grade = scrapy.Field()
    # 简介
    intro = scrapy.Field()
    # 评论数量
    comments = scrapy.Field()
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 自定义要爬取网站的字段（类似于一个model容器）
class TestspiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass

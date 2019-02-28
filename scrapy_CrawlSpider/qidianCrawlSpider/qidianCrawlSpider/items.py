# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QidiancrawlspiderBookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 封面图片
    coverImage = scrapy.Field()
    # 标题
    bookName = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 分类
    tags = scrapy.Field()
    # 连载状态
    status = scrapy.Field()
    # 简介
    content = scrapy.Field()


class QidiancrawlspiderChpaterItem(scrapy.Item):
    # 标题
    chpaterName = scrapy.Field()
    # 数据名称
    bookName = scrapy.Field()
    # 字数
    fontsize = scrapy.Field()
    # 发布时间
    publishTime = scrapy.Field()
    # 内容
    content = scrapy.Field()


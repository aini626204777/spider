# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# 目标文件
class JobboleProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 封面
    coverImage = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 发布时间
    publishTime = scrapy.Field()
    # 内容
    content = scrapy.Field()
    # 标签
    tags = scrapy.Field()

    # 文章的详情链接
    url = scrapy.Field()
    # 下载图片
    image_load = scrapy.Field()

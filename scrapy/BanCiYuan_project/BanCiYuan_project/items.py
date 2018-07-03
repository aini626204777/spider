# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BanciyuanProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 图片
    image_path = scrapy.Field()
    # 作者名字
    name = scrapy.Field()
    # 评论量
    comment_nums = scrapy.Field()
    # 本地图片
    load_image = scrapy.Field()
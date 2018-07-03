# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobboleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 创建时间
    create_data = scrapy.Field()
    # 文章地址
    url = scrapy.Field()
    # 文章图片链接
    img_url = scrapy.Field()
    # 点赞数
    praise_nums = scrapy.Field()
    # 收藏数量
    bookmark_nums = scrapy.Field()
    # 评论数量
    comment_nums = scrapy.Field()
    # 文章内容
    content = scrapy.Field()
    # 标签
    tags = scrapy.Field()
    # 图片的本地路径
    coverImageLocalPath = scrapy.Field()




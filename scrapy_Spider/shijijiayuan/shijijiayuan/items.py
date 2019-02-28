# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShijijiayuanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # id
    Uid = scrapy.Field()
    # 头像
    HeaderImage = scrapy.Field()
    # 性别
    Sex = scrapy.Field()
    # 标签
    RandTag = scrapy.Field()
    # 年龄
    Age = scrapy.Field()
    # 身高
    Height = scrapy.Field()
    # 个性签名
    Shortnote = scrapy.Field()
    # 工作地点
    WorkAdress = scrapy.Field()
    # 需求
    MatchCtion = scrapy.Field()
    # 匿名名称
    NickName = scrapy.Field()

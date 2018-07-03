# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YouguowangCrawlspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    name = scrapy.Field()
    img_path = scrapy.Field()
    img_load_path = scrapy.Field()


class parse_detailsCrawlspiderItem(scrapy.Item):
    # 头像
    head_protrait = scrapy.Field()
    # 姓名
    name = scrapy.Field()
    # 身材
    stature = scrapy.Field()
    # 人气
    popularity = scrapy.Field()
    # 粉丝
    fans = scrapy.Field()
    # 专辑
    album = scrapy.Field()
    # 发行时间
    issue_date = scrapy.Field()
    # 专辑介绍
    album_introduce = scrapy.Field()
    # 写真
    mirror = scrapy.Field()

    # def insert(self):
    #     insert_sql = """
    #         INSERT INTO jobs(head_protrait,name,stature,popularity,fans,album,issue_date,album_introduce,mirror)
    #       VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)
    #     """

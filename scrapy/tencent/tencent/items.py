# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 职位名称
    jobName = scrapy.Field()
    # 工作地点
    workLocation = scrapy.Field()
    # 职位类型
    jobType = scrapy.Field()
    # 职位职责
    jobDesc = scrapy.Field()
    # 工作要求
    jobInfo = scrapy.Field()
    pass

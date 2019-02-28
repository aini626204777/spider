# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WjjlianjiaershoufangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 封面照片
    cover = scrapy.Field()
    # 名字
    title = scrapy.Field()
    # 地址
    adress = scrapy.Field()
    # 厅室
    Hall = scrapy.Field()
    # 平米
    SquareMetre = scrapy.Field()
    # 装修
    Renovation = scrapy.Field()
    # 楼层
    floor = scrapy.Field()
    # 时间
    floorDate = scrapy.Field()
    # 区域
    region = scrapy.Field()
    # 关注
    follow = scrapy.Field()
    # 参观
    visit = scrapy.Field()
    # 钱
    money = scrapy.Field()
    # 单价
    UnitPrice = scrapy.Field()

    # mongoDB数据库插入
    def get_mongo_collectionName(self):
        """

        :return:
        """
        return 'ershoufang'

class WjjlianjiazufangItem(scrapy.Item):
    # 封面照片
    cover = scrapy.Field()
    # 名字
    title = scrapy.Field()
    # 地址
    adress = scrapy.Field()
    # 厅室
    Hall = scrapy.Field()
    # 时间
    floorDate = scrapy.Field()
    # 福利
    welfare = scrapy.Field()
    # 月租
    MonthlyRent = scrapy.Field()

    # mongoDB数据库插入
    def get_mongo_collectionName(self):
        """

        :return:
        """
        return 'zufang'

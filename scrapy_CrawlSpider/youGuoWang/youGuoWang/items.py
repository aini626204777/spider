# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YouguowangPageItem(scrapy.Item):
    # 杂志标签
    magazineTag = scrapy.Field()
    # 模型名字
    modelName = scrapy.Field()
    # 专辑名字
    AlbumName = scrapy.Field()
    # 名字
    name = scrapy.Field()
    # 发行时间
    issueTime = scrapy.Field()
    # 订阅量
    subscription = scrapy.Field()
    # 封面
    cover = scrapy.Field()
    # 下载图片路径
    downloadImage = scrapy.Field()

    # mysql数据库插入
    def get_insert_db(self, data_dict):
        keys = ','.join(data_dict.keys())
        sql = """INSERT INTO youguoFL({columns}) VALUES({value})""".format(columns=keys,
                                                                        value=','.join(['%s'] * len(data_dict)))
        data = list(data_dict.values())
        return sql, data


class YouguowangdetailsItem(scrapy.Item):
    # 标签
    Tag = scrapy.Field()
    # 专辑名字
    AlbumName = scrapy.Field()
    # 名字
    name = scrapy.Field()
    # 发行时间
    issueTime = scrapy.Field()
    # 身高
    height = scrapy.Field()
    # 三围
    BWH = scrapy.Field()
    # 人气
    Popularity = scrapy.Field()
    # 粉丝
    Fans = scrapy.Field()
    # 专辑数量
    AlbumNumber = scrapy.Field()
    # 专辑介绍
    AlbumIntroduction = scrapy.Field()
    # 头像
    headPortrait = scrapy.Field()

    # mysql数据库插入
    def get_insert_db(self, data_dict):
        keys = ','.join(data_dict.keys())
        sql = """INSERT INTO youguoDetails({columns}) VALUES({value})""".format(columns=keys,
                                                                        value=','.join(['%s'] * len(data_dict)))
        data = list(data_dict.values())
        return sql, data
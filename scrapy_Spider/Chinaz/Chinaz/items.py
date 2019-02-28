# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChinazTagItem(scrapy.Item):
    """
    存储网站分类信息
    """
    # 分类的名称:
    TagName = scrapy.Field()
    # 分类首页url地址
    FirstUrl = scrapy.Field()

    # mongoDB数据库插入
    def get_mongo_collectionName(self):
        """

        :return:
        """
        return 'tags'
    # mysql数据库插入
    def get_insert_sql_data(self, data_dict):
        """
        step1：创建sql语句
        :param dataDict:
        :return:
        """
        keys = ','.join(data_dict.keys())
        sql = """INSERT INTO tags({columns}) values ({values})""".format(columns=keys,
                                                                         values=(','.join(["%s"] * len(data_dict))))
        data = list(data_dict.values())

        return sql, data


class ChinazWebinfoItem(scrapy.Item):
    # 封面图片
    CoverImage = scrapy.Field()
    # 标题
    Title = scrapy.Field()
    # 域名
    Domenis = scrapy.Field()
    # 周排行
    WeeklyRanking = scrapy.Field()
    # 反链接
    AntiLink = scrapy.Field()
    # 网站简介
    introduction = scrapy.Field()
    # 得分
    Score = scrapy.Field()
    # 排名
    Ranking = scrapy.Field()
    # 图片本地存储路径
    localImagePath = scrapy.Field()


    # mongodb插入
    def get_mongo_collectionName(self):
        """

        :return:
        """
        return 'tags'
    # mysql数据库插入
    def get_insert_sql_data(self, data_dict):
        """
        step1：创建sql语句
        :param dataDict:
        :return:
        """
        keys = ','.join(data_dict.keys())
        sql = """INSERT INTO chianzWeb({columns}) values ({values})""".format(columns=keys,
                                                                         values=(','.join(["%s"] * len(data_dict))))
        data = list(data_dict.values())

        return sql, data

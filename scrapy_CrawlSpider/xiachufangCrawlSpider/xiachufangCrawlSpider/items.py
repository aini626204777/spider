# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiachufangcrawlspiderDataDetailsItem(scrapy.Item):
    # 分类名称
    LevelTitle = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 封面
    cover = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 参考人数
    number = scrapy.Field()
    # 准备内容
    content = scrapy.Field()
    # 原料
    material = scrapy.Field()
    # 步骤
    step = scrapy.Field()

    def get_insert_sql_data(self, data_dict):
        """
        step1：创建sql语句
        :param dataDict:
        :return:
        """
        keys = ','.join(data_dict.keys())
        sql = """INSERT INTO xcfdata({columns}) values ({values})""".format(columns=keys,
                                                                              values=(
                                                                                  ','.join(["%s"] * len(data_dict))))
        data = list(data_dict.values())

        return sql, data



class XiachufangcrawlspiderAuthorDetailsItem(scrapy.Item):
    # 名字
    name = scrapy.Field()
    # 作者唯一标识
    UserID = scrapy.Field()
    # 性别
    sex = scrapy.Field()
    # 居住地
    address = scrapy.Field()
    # 加入时间
    shijian = scrapy.Field()
    # 关注数
    number = scrapy.Field()
    # 被关注数
    number2 = scrapy.Field()
    # 菜谱数量
    Menunumber = scrapy.Field()
    # 作品数量
    worknumber = scrapy.Field()
    # 个人简介
    profile = scrapy.Field()

    def get_insert_sql_data(self, data_dict):
        """
        step1：创建sql语句
        :param dataDict:
        :return:
        """
        keys = ','.join(data_dict.keys())
        sql = """INSERT INTO xcfzuozhe({columns}) values ({values})""".format(columns=keys,
                                                                              values=(
                                                                                  ','.join(["%s"] * len(data_dict))))
        data = list(data_dict.values())

        return sql, data
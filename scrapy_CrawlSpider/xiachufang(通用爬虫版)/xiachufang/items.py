# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class XiachufangTagItem(scrapy.Item):
    # 存储在redis数据库中，取出来处理数据时,可以根据tableName进行判断
    # tableName = scrapy.Field()
    #分类名称
    tagName = scrapy.Field()
    #分类首页地址
    firstUrl = scrapy.Field()
    #标识
    uniqueType = scrapy.Field()

    def insert_data_to_db(self, dataDict):
        return get_sql_and_data(self, dataDict,'tags')


class XiachufangCaiPuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 存储在redis数据库中，取出来处理数据时,可以根据tableName进行判断
    # tableName = scrapy.Field()
    # 分类
    tag = scrapy.Field()
    #菜名
    title = scrapy.Field()
    # 图片链接
    coverImage = scrapy.Field()
    #评分
    score = scrapy.Field()
    #多少人做过
    doitnum = scrapy.Field()
    #发布人（作者）
    author = scrapy.Field()
    #用料
    used = scrapy.Field()
    #做法
    methodway = scrapy.Field()

    def insert_data_to_db(self,dataDict):
        return get_sql_and_data(self, dataDict, 'caipu')


class XiachufangUserInfoItem(scrapy.Item):
    # 存储在redis数据库中，取出来处理数据时,可以根据tableName进行判断
    # tableName = scrapy.Field()
    #用户名
    username = scrapy.Field()
    #用户唯一标识
    uniqueType = scrapy.Field()
    # 性别
    gender = scrapy.Field()
    #居住地
    adress = scrapy.Field()
    #加入时间
    joinTime = scrapy.Field()
    # 关注数
    attentNum = scrapy.Field()
    #被关注数
    fans = scrapy.Field()
    #菜谱数量
    cpNum = scrapy.Field()
    # 作品数量
    zpNum = scrapy.Field()
    # 个人简介
    info = scrapy.Field()

    def insert_data_to_db(self,dataDict):
        return get_sql_and_data(self, dataDict, 'userinfo')


def get_sql_and_data(self,dataDict,tablename):
    sql = """
    INSERT INTO caipu %s (%s)
    VALUES (%s)
    """ % (tablename,','.join(dataDict.keys()),','.join(['%s']*len(dataDict)))

    data = list(dataDict.values())

    return sql,data
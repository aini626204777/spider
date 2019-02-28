# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TianyanchaAndQichachaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class QichachaClassfyItem(scrapy.Item):
    # 分类的字段
    # 哪个网站
    fromdomains = scrapy.Field()
    # 分类名称
    classifyName = scrapy.Field()
    # 分类的表示
    sign = scrapy.Field()
    # 首页列表地址
    firstUrl = scrapy.Field()

    def get_data_save_to_db(self, dict_data):
        '''
        保存数据库语句
        :param dict_data:
        :return:
        '''
        keys = ','.join(dict_data.keys())
        sql = '''INSERT INTO qichachafenlei({keys}) VALUES({value})'''.format(keys=keys, value=','.join(['%s'] * len(dict_data)))

        data = list(dict_data.values())

        return sql, data


class QichachaCompanyItem(scrapy.Item):
    """
    存储公司详情的信息
    """
    # 公司所属的分类
    classifyName = scrapy.Field()
    # 哪个网站
    fromdomains = scrapy.Field()
    # 公司名称
    companyName = scrapy.Field()
    # 是否在业
    tags = scrapy.Field()
    # 电话
    phonenum = scrapy.Field()
    # 官网
    website = scrapy.Field()
    # 邮箱
    email = scrapy.Field()
    # 　浏览量
    watchnum = scrapy.Field()
    # 　更新日期
    updateTime = scrapy.Field()
    # 法人代表
    lagal = scrapy.Field()
    # 注册资本
    capital = scrapy.Field()
    # 实缴资本
    relcapital = scrapy.Field()
    # 　经营状态
    scopeStatus = scrapy.Field()
    # 成立日期
    buildDate = scrapy.Field()
    # 统一社会信用代码
    creditCode = scrapy.Field()
    # 　纳税人识别号
    ratepayerCode = scrapy.Field()
    # 注册号
    registNumber = scrapy.Field()
    # 组织机构代码
    institutionalNumber = scrapy.Field()
    # 公司类型
    companyType = scrapy.Field()
    # 所属行业
    industry = scrapy.Field()
    # 核准日期
    checkTime = scrapy.Field()
    # 登记机关
    registration_authority = scrapy.Field()
    # 英文名
    englishName = scrapy.Field()
    # 曾用名
    oldName = scrapy.Field()
    # 参保人数
    insuredNumber = scrapy.Field()
    # 人员规模
    person_number = scrapy.Field()
    # 营业期限
    business_term = scrapy.Field()
    # 公司地址
    address = scrapy.Field()
    # 经营范围
    scope = scrapy.Field()


    def get_data_save_to_db(self,dict_data):
        """
        保存数据库语句
        :param dict_data:
        :return:
        """
        keys = ','.join(dict_data.keys())
        sql = '''INSERT INTO TABLE({table}) VALUES({value})'''.format(table=keys,value=','.join(['%s']*len(dict_data)))
        data = list(dict_data.values())

        return sql,data
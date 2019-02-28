# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.utils.project import get_project_settings
from youGuoWang.items import YouguowangPageItem
import scrapy
import os

images_store = get_project_settings().get('IMAGES_STORE')


class YouguowangImagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        """
        根据图片url发起请求
        :param item:
        :param info:
        :return:
        """
        if isinstance(item, YouguowangPageItem):
            image_url = item['cover']
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        """
        图片下载
        :param results:
        :param item:
        :param info:
        :return:
        """
        paths = [v['path'] for k, v in results if k]
        if len(paths) > 0:
            os.rename(images_store + '/' + paths[0],
                      images_store + '/full' + '/' + item['magazineTag'] + item['modelName'] + item['name'] + '.jpg')
            image_path = images_store + '/' + paths[0]
            item['downloadImage'] = image_path
        else:
            return item
        return item


# 导入模块实现mysql异步插入
from twisted.enterprise import adbapi


class YouguowangPipeline(object):
    def __init__(self, dbpool):
        """
        初始化参数
        :param dbpool:
        """
        self.dbpool = dbpool

    @classmethod
    def from_crawler(cls, cralwer):
        """
        在settings文件里面数据数据库信息,链接mysql数据库
        :param cralwer:
        :return:
        """
        db_parmars = {
            'host': cralwer.settings['MYSQL_HOST'],
            'user': cralwer.settings['MYSQL_USER'],
            'passwd': cralwer.settings['MYSQL_PASSWD'],
            'db': cralwer.settings['MYSQL_DB'],
            'port': cralwer.settings['MYSQL_PORT'],
            'charset': cralwer.settings['MYSQL_CHARSET'],
        }
        dbpool = adbapi.ConnectionPool('pymysql', **db_parmars)

        return cls(dbpool)

    def process_item(self, item, spider):
        """
        创建队列，存储失败和存储成功
        :param item:
        :param spider:
        :return:
        """
        query = self.dbpool.runInteraction(
            self.insert_data_to_db, item
        )
        query.addErrback(
            self.insert_err, item
        )
        return item

    def insert_data_to_db(self, cursor, item):
        """
        存入数据库
        :param cursor:
        :param item:
        :return:
        """
        data_dict = dict(item)
        sql, data = item.get_insert_db(data_dict)
        cursor.execute(sql, data)
        print('插入成功！！！')

    def insert_err(self, Failure, item):
        """
        存储失败
        :param Failure:
        :param item:
        :return:
        """
        print(Failure, '插入失败', item)

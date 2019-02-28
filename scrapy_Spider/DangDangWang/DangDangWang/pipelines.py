# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.contrib.pipeline.images import ImagesPipeline
import scrapy
import pymysql
from scrapy.pipelines.images import *


class DangdangwangImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image_url = item['cover']
        print('这是要下载的图片', image_url)
        yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        path = [v['path'] for k, v in results if k]
        image_path = path[0]
        item['localImagePath'] = image_path
        return item


class DangdangwangPipeline(object):
    def __init__(self):
        self.connect = pymysql.Connect('127.0.0.1', 'root', 'abcd1234', '1712B', 3306, charset='utf8')
        self.cursor = self.connect.cursor()

    def open_spider(self, spider):
        print('开始爬虫')

    def process_item(self, item, spider):
        data_dict = dict(item)

        keys = ','.join(data_dict.keys())
        sql = """INSERT INTO DDwang({columns}) values ({values})""".format(columns=keys,
                                                                           values=(','.join(["%s"] * len(data_dict))))
        self.cursor.execute(sql, list(data_dict.values()))
        self.connect.commit()

        print('经过管道')

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
        print('结束爬虫！！！')

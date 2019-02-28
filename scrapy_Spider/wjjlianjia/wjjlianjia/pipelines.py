# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class WjjlianjiaPipeline(object):

    def __init__(self, host, port, db):
        # 创建mongodb的数据库链接
        self.mongo_client = pymongo.MongoClient(host=host, port=port)

        self.db = self.mongo_client[db]

    @classmethod
    def from_crawler(cls, crawler):
        """
        MONGO_HOST = '127.0.0.1'
        MONGO_PORT = 27017
        MONGO_DB = 'chinaz'
        :param crawler:
        :return:
        """
        host = crawler.settings['MONGO_HOST']
        port = crawler.settings['MONGO_PORT']
        db = crawler.settings['MONGO_DB']
        return cls(host, port, db)

    def open_spider(self, spider):
        print(spider.name, '：爬虫开始运行！！！')

    def process_item(self, item, spider):
        # 往哪个集合插入数据
        # 往集合下面插入那些数据

        data_dict = dict(item)

        col_name = item.get_mongo_collectionName()
        col = self.db[col_name]
        col.insert(data_dict)

        return item

    def close_spider(self, spider):
        self.mongo_client.close()
        print('爬虫结束')
